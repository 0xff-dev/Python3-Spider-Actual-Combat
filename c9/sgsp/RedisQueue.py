#!/usr/bin/env python
# coding=utf-8

from pickle import dumps, loads
from Request import WeiXinRequest
from settings imprt REDIS_HSOT, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
import redis


class RedisQueue(object):
    '''
    抓取队列
    '''

    def __init__(self):
        self.db = redis.StrictRedis(host=REDIS_HSOT, 
                port=REDIS_PORT, password=REDIS_PASSWORD)
    
    def pusp(self, request):
        if isinstance(request, WeiXinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False
    
    def pop(self):
        if not self.db.llen(REDIS_KEY) == 0:
            return self.db.lpop(REDIS_KEY)
        return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0

