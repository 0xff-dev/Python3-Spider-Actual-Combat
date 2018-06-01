#!/usr/bin/env python
# coding=utf-8


import json
from flask import Flask, g
from RedisClient import RedisClient
import settings


__all__ = ['app']


app = Flask(__name__)
GENERATOR_MAP = {
    'weibo': 'WeiBoCookiesGenerator',
}


def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            # eval 及其草但，不要脸，唉我去
            setattr(g, website+':cookies', 
                    eval('RedisClient'+'("cookies", "'+website+'")'))
            setattr(g, website+':account', 
                    eval('RedisClient'+'("account", "'+website+'")'))
            # 这里的eavl直接创建一个RedisCient对象，也就是
        return g


@app.route('/')
def index():
    return '<h1>Cookies Pool</h1>'


@app.route('/<website>/random')
def random(website):
    g = get_conn()
    cookies = getattr(g, website+':cookies').random()
    return cookies

@app.route('/<website>/add/<username>/<password>')
def add(website, username, password):
    """
    添加用户，
    :param website
    :param username
    :param password
    :return:
    """
    g = get_conn()
    print (username, password)
    # 拿到RedisClient的set方法
    getattr(g, website+':account').set(username, password)
    return json.dumps({'status': '1'})

@app.route('/<website>/count')
def count(website):
    g = get_conn()
    count = getattr(g, website+':cookies').count()
    return json.dumps({'status': '1', 'count': count})

if __name__ == '__main__':
    app.run(debug=True)

