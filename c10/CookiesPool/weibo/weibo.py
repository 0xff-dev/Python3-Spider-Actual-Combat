#!/usr/bin/env python
# coding=utf-8


import time
from os import listdir
from multiprocessing import Pool
from io import BytesIO


from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


WEIBO_USERNAME = '13050901105'
WEIBO_PASSWORD = '123456'
TEMPLATE_FOLDER = 'templates/'


class CrackWeiboSlide(object):

    def __init__(self, username, password, brower):
        self.url = 'https://passport.weibo.cn/signin/login'
        self.brower = brower
        self.wait = WebDriverWait(self.brower, 30)
        self.username = username
        self.password = password

    def __del__(self):
        self.brower.close()

    def open(self):
        '''
        输入网址，打开网页，并进行登录
        '''
        self.brower.get(self.url)
        username = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()


    def get_position(self):
        '''
        获取验证码的位置
        :return: 验证码的四个位置
        '''
        try:
            img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
        except TE:
            print ('为出现验证码')
            self.open()
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom = location['y'], location['y']+size['height']
        left, right = location['x'], location['x']+size['width']
        return (top, bottom, left, right)
        
    def get_screenshot(self):
        '''
        获取屏幕截图
        '''
        screenshot = self.brower.get_screenshot_as_png()
        return Image.open(BytesIO(screenshot))

    def get_image(self, name='{}/captcha.png'.format(TEMPLATE_FOLDER)):
        '''
        获取验证码的图片
        '''
        top, bottom, left, right = self.get_position()
        print ('验证码的位置top[{}], bottom[{}], left[{}], right[{}]'.
                format(top, bottom, left, right))
        screenshot = self.get_screenshot()
        screenshot = screenshot.crop((left, top, right, bottom))
        screenshot.save(name)
        return screenshot
    
    def get_cookies(self):
        return self.brower.get_cookies()

    def do(self):
        '''
        批量获取验证码
        '''
        count = 1
        while count < 100000:
            self.open()
            self.get_image('{}/{}.png'.format(TEMPLATE_FOLDER, str(count)))
            count +=1
    
    def is_pixel_eq(self, image1, image2, x, y):
        '''
        通过像素比较两张图片的不同
        '''
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 20
        if abs(piexl1[0]-pixel2[2])<threshold and abs(piexl1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
            return True
        return False

    def same_image(self, image1, template_image):
        '''
        相似度为0.99即可
        '''
        threshold = 0.99
        count = 0
        for x in range(image1.width):
            for y in range(image1.height):
                if self.is_pixel_eq(image1, template_image, x, y):
                    count += 1
        result = float(count)/(image1.width*image1.height)
        if result > threshold:
            return True
        return False

    def move(self, numbers):
        '''
        param: numbers list
        :return:
        '''
        circles = self.brower.find_elements_by_css_selector('.patt-wrap .patt-circ')
        dx = dy = 0
        for index in range(4):
            circle = circles[numbers[index]-1]
            if index == 0:
                # 第一次出现
                ActionChains(self.brower).move_to_element_with_offset(
                        circle, circle.size['width']/2, 
                        circle.size['height']/2).click().perform()
            else:
                times = 30
                for i in range(times):
                    ActionChains(self.brower).move_by_offset(dx/times, dy/times).perform()
                    time.sleep(1/times)
            if index == 3:
                # 最后一 松开鼠标
                ActionChains(self.brower).release().perform()
            else:
                dx = circles[numbers[index+1]-1].location['x'] - circle.location['x']
                dy = circles[numbers[index+1]-1].location['y'] - circle.location['y']

    def detect_image(self, image):
        for pic in listdir(TEMPLATE_FOLDER):
            print ('匹配{}'.format(pic))
            template = Image.open(TEMPLATE_FOLDER+pic)
            if self.same_image(image, template):
                # 匹配到了图片
                numbers = [int(number) for number in pic.split('.')[0]]
                # 根据文件的名字提供提动的方向
                return numbers
    
    def password_error(self):
        """判断密码错误"""
        try:
            WebDriverWait(self.brower, 4).until(EC.text_to_be_present_in_element((By.ID, "errorMsg"), "用户名或密码错误"))
        except TE as e:
            return False

    def login_successfully(self):
        """无验证码直接登录"""
        try:
            return bool(
                    WebDriverWait(self.brower, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "drop-title"))))
        except TE as e:
            return False


    def crack(self):
        self.open()
        if self.password_error():
            return {
                    'status': 2,
                    'content': '用户名或者密码错误',
                    }
        if self.login_successfully():
            # 无需验证直接登录
            return {
                    'status': 1,
                    'content': self.get_cookies(),
                    }

        image = self.get_image()
        numbers = self.detect_image(image)
        self.move(numbers)
        if self.login_successfully():
            return {
                'status': 1,
                'content': self.get_cookies(),
            }
        else:
            return {
                'status': 3,
                'content': '验证码错误或者帐号密码错误',
            }

