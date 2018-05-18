#!/usr/bin/env python
# coding=utf-8

import requests
from time import sleep
from urllib.parse import urlencode
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq


# 模拟ajax请求, 打开开发者模式，查看xhr类型的请求, 就是ajax的, 
#然后分析, 用正常的请求方式即可
# 程序说明，当page=1的情况下，cards的第二条返回的是本人follow的用户以及其他的信息


BASE_URL = 'https://m.weibo.cn/api/container/getIndex?'
#type=uid&value=2830678474&containerid=1076032830678474&page=1
HEADERS = {
        'Host': 'm.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'X-Requested-With': 'XMLHttpRequest',
    }


def get_page(page=1):

    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': str(page),
    }
    url = BASE_URL+urlencode(params)
    try:
        resp = requests.get(url, headers=HEADERS)
        sleep(1)
        if resp.status_code == 200:
            return resp.json(), page
    except requests.ConnectionError as e:
        print ('Error: {}'.format(e.args))


def parse_page(json, page):
    '''
    用request请求德 json数据
    '''
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')
                weibo_data = {}
                weibo_data['id'] = item.get('id')
                weibo_data['text'] = pq(item.get('text')).text()
                weibo_data['attitudes'] = item.get('attitudes_count')
                weibo_data['comments'] = item.get('comments_count')
                weibo_data['reposts'] = item.get('reposts_count')
                yield weibo_data


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print (result)

