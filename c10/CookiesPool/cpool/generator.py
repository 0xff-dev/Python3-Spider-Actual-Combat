#!/usr/bin/env python
# coding=utf-8


import sys
import os

sys.path.append(os.path.dirname(os.path.relpath(__file__))+'../')

import json
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from cpool import settings
from cpool.RedisClient import RedisClient
from weibo.weibo import CrackWeiboSlide


class CookiesGenerator(object):

    def __init__(self, website=None):
        self.website = website
        self.cookies_db=  RedisClient(settings.REDIS_COOKIE_KEY, website=website)
        self.account_db = RedisClient(settings.REDIS_ACCOUNT_KEY, website=website)
        self.init_brower()

    def __del__(self):
        self.close()

    def init_brower(self):
        """
        通过brower初始化全局的浏览器模拟登录
        """
        if settings.BROWER_TYPE == 'PhantomJS':
            caps = DesiredCapabilities.PHANTOMJS
            caps["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            self.brower = webdriver.PhantomJS(desired_capabilities=caps)
            self.brower.set_window_size(1400, 500)
        elif settings.BROWER_TYPE == 'Firefox':
            self.brower = webdriver.Firefox()

    def new_cookies(self, usernam, password):
        """
        新生成Cookies, 子类重写
        """
        pass

    def process_cookies(self, cookies):
        """
        处理cookies
        :param cookies
        :return
        """
        dict = {}
        for cookie in cookies:
            dict[cookie['name']] = cookie['value']
        return dict

    def run(self):
        """的到所有的帐号, 顺次模拟登录"""
        account_usernames = self.account_db.usernames()
        cookies_usernames = self.cookies_db.usernames()
        for username in account_usernames:
            if not username in cookies_usernames:
                # 该用户还没有拿到cookies
                username = str(username, encoding='utf-8')
                print ('收集用户{} Cookies'.format(username))
                password = self.account_db.get(username)
                # result: dict
                result = self.new_cookies(username, password) 
                if result.get('status') == 1:
                    print ('捕获Cookies')
                    if self.cookies_db.set(username, result.get('content')):
                        print ('Cookies 保存成功')
                elif result.get('status') == 2:
                    print ('你的帐号或者密码错误')
                    if self.account_db.delete(username):
                        print ('密码错误，帐号移除')
            else:
                print ('用户Cookies存在')

    def close(self):
        try:
            print ('Closeing Brower')
            self.brower.close()
            del self.brower
        except TypeError:
            print ('Brower not open')


class WeiBoCookiesGenerator(CookiesGenerator):

    def __init__(self, website=None):
        super(WeiBoCookiesGenerator, self).__init__(website)

    def new_cookies(self, username, password):
        """成成Cookies"""
        return CrackWeiboSlide(str(username), password.strip(), self.brower).crack()

if __name__ == '__main__':
    WeiBoCookiesGenerator('weibo').run()

