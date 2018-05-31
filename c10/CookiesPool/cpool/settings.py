#!/usr/bin/env python
# coding=utf-8


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

# 两个hash表
REDIS_COOKIE_KEY = 'cookies'
REDIS_ACCOUNT_KEY = 'account'


# test_url_map
TEST_URL_MAP={
    'weibo': 'https://m.weibo.cn/',
}

BROWER_TYPE = 'Firefox'
GERERATOR_MAP = {
    'weibo': 'WeiBoCookiesGenerator',
}

TESTER_MAP = {
    'weibo': 'WeiBoVaildTester',
}


CYCLE = 120
API_HOST = 'localhost'
API_PORT = 5000


GENERATOR_PROCESS = False
VALID_PROCESS = False
API_PROCESS = True

