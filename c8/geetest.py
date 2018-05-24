#!/usr/bin/env python
# coding=utf-8

from time import sleep
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


EMAIL = 'cqc@cuiqingcai.com'
PASSWORD = '123456'


#首先geetest这个网站要登录，先有一个点击的验证，然后是拖动的验证
class CrackGeetest(object):

    def __init__(self):
        self.url = 'http://account.geetest.com/login'
        self.brower = webdriver.Firefox()
        self.wait = WebDriverWait(self.brower, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_btn(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            '.geetest_radar_tip')))
        return button

    def get_positon(self):
        '''
        获取验证码的位置
        :return 验证码的位置元组
        '''
        img = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".geetest_canvas_img")))
        sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y']+size['height'],\
                location['x'], location['x']+size['width']
        return top, bottom, left, right

    def get_geetest_image(self, name='captcha.png'):
        top, bottom, left, right = self.get_positon()
        print ('验证码的位置是上{}, 下{}, 左{}, 右{}'.format(top, bottom, left, right))
        # 自己实现
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha
        
    def get_screenshot(self):
        return Image.open(BytesIO(self.brower.get_screenshot_as_png()))
    
    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            ".geetest_slider_button")))
        #点击一下即可 slider.click(), 蓝后用self.get_geetest_image()获取带有缺口的图片
        return slider

    def is_pixel_eq(self, _image1: Image, _image2: Image, x: int, y: int):
        pixel_image1 = _image1.load()[x, y]
        pixel_image2 = _image2.load()[x, y]
        threshold = 60
        if abs(pixel_image1[0]-pixel_image2[0])<threshold and abs(pixel_image1[1]-pixel_image2[1])<threshold and abs(pixel_image1[2]-pixel_image2[2])<threshold:
            return True
        return False

    def get_gap(self, _image1: Image, _image2: Image):
        '''
        获取缺口的偏移量
        :param _image1 不带缺口的图片
        :param _image2 带缺口的图片
        :return
        '''
        left = 60
        for i in range(left, _image1.size[0]):
            for j in range(_image1.size[1]):
                if not self.is_pixel_eq(_image1, _image2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        '''
        根据偏移量获取移动轨迹
        :param distance 偏移量
        :return 移动轨迹
        '''
        track = []
        current = 0
        mid = distance*4/5
        t = 0.5    # 计算间隔? 没有明白m, 调整速度?
        v = 0
        
        while current < distance:
            if current < mid:
                a = 2
            else:
                # 后半部分减速
                a = -3
            v0 = v
            v = v0+a*t
            move = v0*t+1/2*a*t**2
            current += move
            track.append(round(move))
        return track

    def move_to_gap(self, slider, tracks):
        ActionChains(self.brower).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.brower).move_by_offset(xoffset=x, yoffset=0).perform()
        sleep(1)
        # 释放鼠标
        ActionChains(self.brower).release().perform()
    
    def open(self):
        '''
        通过类的url打开
        '''
        self.brower.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def login(self):
        submit = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-btn")))
        submit.click()
        sleep(2)
        print ('Login success')

    def crack(self):
        self.open()
        btn = self.get_geetest_btn()
        btn.click()
        _image1 = self.get_geetest_image('captch1.png')
        slider = self.get_slider()
        slider.click()
        _image2 = self.get_geetest_image('captch2.png')
        gap = self.get_gap(_image1, _image2)
        gap -= 5
        tracks = self.get_track(gap)
        self.move_to_gap(slider, tracks)

        success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "geetest_success_radar_tip_content"), "验证成功"))
        print (success)
        if not success:
            self.crack()
        else:
            self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
