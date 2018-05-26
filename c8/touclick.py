#!/usr/bin/env python
# coding=utf-8

# note 那个网站访问不到，一下代码全是自己跟着写的，没有做验证

from time import sleep
from hashlib import md5
from io import BytesIO


from PIL import Image


import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


EMAIL = 'stevenshuang@gmail.com'
PASSWORD = '123456'
CHAOJIYING_USERNAME = 'stevenshuang'
CHAOJIYING_PASSWORD = ''
CHAOJIYING_SOFT_ID = '8888'
CHAIJIYING_KIND = '8888'    # 这是什么码?


class Chaojiying(object):
    '''
    超级鹰是一个是识别点击汉字进行验证的网站，90%准确率
    自己注册一下，搞几个题分就ojbk了
    '''
    
    def __init__(self, username, password, soft_id):
        self.username = username
        self.passwrod = passwrod
        self.soft_id = soft_id
        self.proces_url = 'http://upload.chaojiying.net/Upload/Processing.php'
        self.error_url = 'http://upload.chaojiying.net/Upload/ReportError.php'
        self.base_params = {
            'user': self.username,
            'pass2': self.passwrod
            'softid': self.soft_id
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }

    def post_pic(self, im, codetype):
        '''
        im: 图片的字节数据
        codetype: 看超级鹰的价格页面，没种类型的价格，以及类型
        '''
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('xxx.jpg', im)}
        r = requests.post(self.proces_url, data=params, files=files, 
                headers=self.headers)
        return r.json()

    def report_error(self, im_id):
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(self.error_url, data=params, headers=self.headers)
        return r.json()


class ClickCaptcha(object):

    def __init__(self):
        self.url = 'https://www.touclick.com/login.html'
        self.brower = webdriver.Firefox()
        self.wait = WebDriverWait(self.brower, 30)
        self.email = EMAIL
        self.password = PASSWROD
        self.cjy = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, 
                CHAOJIYING_SOFT_ID)

    def open(self):
        '''
        请求登录
        '''
        self.brower.get(self.url)
        email = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touclick_button(self):
        '''
        获取验证图片的对象
        '''
        button = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'touclick-hod-wrap')))
        return button

    def get_touclick_element(self):
        element = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'touclick-pub-content')))
        return element

    def get_position(self):
        element = self.get_touclick_element()
        sleep(1)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y']+size['height'],\
                location['x'], location[x]+size['width']
        return top, bottom, left, right

    def get_screenshot(self):
        screentshot = self.brower.get_screenshot_as_png()
        return Image.open(BytesIO(screentshot))
    
    def get_touclick_image(self, name='captcha.png'):
        '''
        获取到验证码的位置，截屏，扣出验证码
        '''
        top, bottom, left, right = self.get_touclick_element()
        print ('验证码的位置: top[{}]-bottom[{}]-left[{}]-right[{}]'.
                format(top, bottom, left, right))
        screentshot = self.get_screenshot()
        return screentshot.crop((left, top, right, bottom))
    
    def cjy_deal(self):
        captcha = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        result  = self.cjy.post_pic(bytes_array.getvalue, CHAIJIYING_KIND)
        print (result)
        return result

    def get_points(self, captcha_result): 
        groups = captcha_result.get('pic_str').spilt('|')
        locations = [[int(number) for number in group] for group in groups]
        return locations

    def touch_click(self, locations):
        for location in locations:
            print (location)
            ActionChains(self.brower).move_to_element_with_offset(
                    self.get_touclick_element, xoffset=location[0], 
                    yoffset=location[1]).click().perform()
            sleep(2)


if __name__ == '__main__':
    obj = ClickCaptcha()
    obj.touch_click()

