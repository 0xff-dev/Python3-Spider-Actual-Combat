#!/usr/bin/env python
# coding=utf-8

import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep
from settings import *


class Moments(object):

    def __init__(self):
        """
        初始化
        """
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient('localhost')
        self.db = self.client[DB_DB]
        self.collection = self.db[DB_COLLECTIONS]

    def login(self):
        """
        微信登录
        """
        login = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/cjk")))
        login.click()
        phone = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/h2")))
        phone.set_text(USERNAME)
        next = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/adj")))
        next.click()
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/h2"]')))
        password.set_text(PASSWORD)
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/adj")))
        submit.click()

    def enter(self):
        """
        进入朋友圈
        """
        tab = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/bw3"][3]')))
        tab.click()
        monents = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/atz')))
        monents.click()

    def crawl(self):
        """
        爬去
        """
        while True:
            items = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/cve"]//android.widget.FrameLayout')))
            self.driver.swipe(FLICK_START_X, FLICK_STAT_Y+FLICK_DISTANCE, FLICK_STAT_X, FLICK_STAT_Y)
            for item in items:
                try:
                    nickname = item.find_element_by_id('com.tencent.mm:id/aig').get_attribute('text')
                    content = item.find_element_by_id('com.tencent.mm:id/cwm').get_attribute('text')
                    data = {
                        'nickname': nickname,
                        'content': content,
                    }
                    self.collection.update({'nickname': nickname, 'content': content}, 
                            {'$set': data}, True)
                except NoSuchElementException as e:
                    pass

    def main(self):
        """
        住函数入口
        """
        self.login()
        self.enter()
        self.crawl()

