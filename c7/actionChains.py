#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains


brower = webdriver.Firefox()    # 模拟火狐浏览器
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
brower.get(url)
brower.switch_to.frame("iframeResult")
source = brower.find_element_by_css_selector('#draggable')
target = brower.find_element_by_css_selector("#droppable")
action = ActionChains(brower)
action.drag_and_drop(source, target)
action.perform()

