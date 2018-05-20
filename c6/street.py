#!/usr/bin/env python
# coding=utf-8

import os
import json
import requests
from hashlib import md5
from multiprocessing import Pool
from urllib.parse import urlencode    # 编辑get请求参数


BASE_URL = 'http://www.toutiao.com/'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest',
    }

# 分线程爬取
GROUP_START = 1
GROUP_END = 10


def get_page(offset):
    '''
    请求的url的参数
    offset=offset, format=json, keyword=, autoload=true, count=20, cur_tab=search_tab
    '''
    print (offset)
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }

    url = BASE_URL + 'search_content/?'+ urlencode(params)
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
    except requests.ConnectionError as e:
        print ('Error: {}'.format(e.args))
        return None



def get_images(json):
    '''
    将拿到的json数据，存储
    '''
    items = json.get('data')
    if items:
        for item in items:
            title = item.get('title')
            images = item.get('image_list')
            if images is not None:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title,
                        }



def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        resp = requests.get('http:'+item.get('image'))
        if resp.status_code == 200:
            # 图片请求成功
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                    md5(resp.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as fp:
                    fp.write(resp.content)
            else:
                print ('Image already exits')
    except requests.ConnectionError as e:
        print ('Image request Error{}'.format(e.args))


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print (item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    # 制造offset
    groups = [x* 20 for x in range(GROUP_START, GROUP_END)]
    pool.map(main, groups)
    pool.close()
    pool.join()

