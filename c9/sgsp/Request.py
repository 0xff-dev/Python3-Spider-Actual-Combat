#!/usr/bin/env python
# coding=utf-8


from requests import Request
from settings import TIMEOUT


class WeiXinRequest(Request):
    '''
    做一个微信的Request对象，后面直接处理
    '''
    def __init__(self, url=None, callback, method='GET', 
            headers=None, need_proxy=False, fail_times=0, timeout=TIMEOUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_times = fail_times
        self.timeout = timeout

