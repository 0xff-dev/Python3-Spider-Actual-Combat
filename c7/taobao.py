#!/usr/bin/env python
# coding=utf-8


from time import sleep
from urllib.parse import quote    # 用于便于url识别


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq


from pymongo import MongoClient


brower = webdriver.PhantomJS()
KEYWORD='iPad'
wait = WebDriverWait(brower, 10)

# Mongo setting
MONGO_HOST = 'localhost'
MONGO_DB = 'taobao_ipad'
MONGO_COLLECTION = 'product'
client = MongoClient(MONGO_HOST, 27017)
db = client[MONGO_DB]


def save_product(product):
    try:
        db[MONGO_COLLECTION].insert_one(product)
        print ('Insert Success')
    except Exception as e:
        print ('Insert Error')


def get_product():
    html = brower.page_source    #$ 网页源代码
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr("data-src"),    # src, data-src图片大小不同
            'title': item.find('.title').text(),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        # 发现抓到一些奇怪的数据
        if product['title'] and product['shop'] is not None:
            print (product)
            save_product(product)


def get_index(page):
    '''
    抓取索引页面
    :param page: 页码
    '''
    print ('抓取第{}页'.format(page))
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        brower.get(url)
        if page > 1:
            # 等待页面跳转和确定按钮出现
            _input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager div.form > input")))
            _submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager div.form span.btn.J_Submit")))
            _input.clear()
            _input.send_keys(page)
            _submit.click()
        # 判断页面是否加载完成
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager li.item.active > span"), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".m-itemlist .items .item")))
        get_product()
    except TimeoutException as e:
        print ('Timeout, 3秒后重新连接')
        sleep(3)
        print ('重新连接')
        get_index(page)


if __name__ == '__main__':
    for i in range(1, 3):
        get_index(i)

