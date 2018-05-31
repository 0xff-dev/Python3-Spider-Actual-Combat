#!/usr/bin/env python
# coding=utf-8

from random import choice


import redis
from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisClient(object):

    def __init__(self, type, website: str, host=REDIS_HOST, port=REDIS_PORT, 
            password=REDIS_PASSWORD):
        """初始化Redis链接"""
        self.db = redis.StrictRedis(host=host, port=port, password=password)
        self.type = type
        self.website = website

    def name(self):
        """
        返回Hash的名称, 做Hash的key
        :return: {}:{}
        """
        return '{}:{}'.format(self.type, self.website)

    def set(self, username, value: str):
        """
        设置键值对
        hset(key, field, value)
        :return:
        """
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        #print (str(self.db.hget(self.name(), username), encoding='utf-8'))
        return str(self.db.hget(self.name(), username), encoding='utf-8')

    def delete(self, username):
        """删除过期的Cookie?帐号"""
        return self.db.hdel(self.name(), username)

    def count(self):
        """返回有多少数据"""
        return self.db.hlen(self.name())

    def random(self):
        """返回随机的Cookies"""
        return choice(self.db.hvals(self.name()))

    def usernames(self):
        return self.db.hkeys(self.name())

    def all(self):
        """获取所有的键值对"""
        return self.db.hgetall(self.name())

