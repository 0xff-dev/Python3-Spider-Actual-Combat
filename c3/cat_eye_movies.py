#!/usr/bin/env python
# coding=utf-8

import re
import json
import time
import requests
from requests.exceptions import RequestException


# 后面拼接&offset=(page-1)*10
BASE_URL = 'http://maoyan.com/board/4'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}


def get_one_page(url, offset=1):
    """
    url: aim url
    offset: page offset
    """
    if offset != 1:
        url += ('?offset='+str((offset-1)*10))
    print (url)
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException as e:
        return None


def parse_one_page(html):
    """
    解析获取到的html代码
    """
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
                '排名': item[0].strip(),
                '图片': item[1].split('@')[0].strip(),
                '电影名': item[2].strip(),
                '演员': item[3].strip()[3:] if len(item[3]) > 3 else '',
                '上映时间': item[4][5:].strip(),
                '评分': item[5]+item[6].strip(),
            }


if __name__ == '__main__':

    for page in range(1, 11):
        html = get_one_page(BASE_URL, page)
        for item in parse_one_page(html):
            with open('./cat_movies_index.txt', 'a') as fp:
                fp.write(json.dumps(item, ensure_ascii=False)+'\n')
