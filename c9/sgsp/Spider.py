#!/usr/bin/env python
# coding=utf-8


import requests
from requests import Session
from requests import ReadTimeout, ConnectionError
from pyquery import PyQuery as pq


from RedisQueue import RedisQueue
from Request import WeiXinRequest
from urllib.parse import uelencode

# 明天完成mysql的链接
MAX_FAIL_TIME = 10


class Spider(object):

    def __init__(self, url='http://weixin.sogou.com/weixin', key_word=None):
        self.url = url
        self.key_word = key_word
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml.application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en,q-0.6,ja;q=0.4,zs-TW;q=0.2,mt;q=0.2',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'weixin.sogou.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        self.session = Session()
        self.queue = RedisQueue()
    
    def start(self):
        '''
        初始化工作
        '''
        self.session.headers.update(self.headers)
        start_url = self.url+'?'+urlencode({'query': self.key_word, 'type':2})
        weixin_request = WeiXinRequest(url=start_url, 
                callback=self.parse_index, need_proxy=True)
        self.queue.pusp(weixin_request)

    def parse_index(self, response):
        '''
        页面解析
        '''
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = WeiXinRequest(url=url, 
                    callback=self.parse_index, headers=self.headers)
            yield weixin_request
        # 下一页链接
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.url+str(next)
            weixin_request = WeiXinRequest(url=url, 
                    callback=self.parse_index, headers=self.headers)
            yield weixin_request

    def parse_detail(self, response):
        '''
        解析详情
        '''
        doc(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('rich_medai_content').text(),
            'data': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text(),
        }
        yield data
    
    def error(self, weixin_request: WeiXinRequest):
        weixin_request.fail_times += 1
        print ('Request Faile: {}, Url is{}'.format(weixin_request.fail_times, 
            weixin_request.url))
        if weixin_request.fail_times < MAX_FAIL_TIME:
            self.queue.pusp(weixin_request)

    def get_proxy(self, url='localhsot:5000/random'):
        '''
        在自己的ip池中获取可用的代理ip
        '''
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp.text
            return None
        except Exception as e:
            return None

    def schedule(self):
        '''
        调度策略
        '''
        while not self.queue.empty():
            # 队列不为空
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print ('Schedule: {}'.format(weixin_request.url))
            response = self.request(weixin_request)
            if response and response.status_code == 200:
                results = list(callback(response))    # gererator
                if results:
                    for result in results:
                        if isinstance(weixin_request, WeiXinRequest):
                            self.queue.pusp(weixin_request)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def request(self, weixin_request: WeiXinRequest):
        '''
        执行请求
        '''
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                            'http': proxy,
                            'https': proxy,
                    }
                    return self.session.send(weixin_request.prepare(),
                            timeout=weixin_request.timeout, allow_redirects=False,
                            proxies=proxies)
            return self.session.send(weixin_request.prepare(), 
                    timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout):
            return False

    def run(self):
        self.start()
        self.schedule()

