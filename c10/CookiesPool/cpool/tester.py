#!/usr/bin/env python
# coding=utf-8

import json
import requests
from requests.exceptions import ConnectionError
from cpool.RedisClient import RedisClient
from cpool import settings


class Vaildtester(object):

    def __init__(self, website=None):
        self.website = website
        self.cookies_db = RedisClient(settings.REDIS_COOKIE_KEY, self.website)
        self.account_db = RedisClient(settings.REDIS_ACCOUNT_KEY, self.website)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }

    def test(self, username, cookies):
        pass

    def run(self):
        cookies_groups = self.cookies_db.all()
        for cg in cookies_groups:
            self.test(username, cg)


class WeiBoVaildTester(Vaildtester):

    def __init__(self, website="weibo"):
        super(WeiBoVaildTester, self).__init__(website)

    def test(self, username, cookie):
        print ('测试帐号:{}, cookies:{}'.format(username, cookie))
        try:
            cookie = json.loads(cookie)
        except TypeError:
            print ('Cookies 不合法', username)
            self.cookies_db.delete(username)
            print ('删除Cookie: {}'.format(username))
            return
        try:
            test_url = settings.TEST_URL_MAP[self.website]
            resp = requests.get(test_url, cookies=cookies, 
                                headers=self.headers, timeout=5, 
                                allow_redirects=False)
            if resp.status_code == 200:
                print ('{}: cookies{} can use'.format(username, cookie))
            else:
                print ("Cookies test fail")
                self.cookies_db.delete(username)
        except ConnectionError as e:
            print ('ConnectionError {}'.format(e.args))

