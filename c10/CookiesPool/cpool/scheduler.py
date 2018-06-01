#!/usr/bin/env python
# coding=utf-8

import time
import os, sys
# 增加搜索路径
sys.path.append(os.path.dirname(os.path.relpath(__file__))+'../')
from multiprocessing import Process
from cpool.app import app
from cpool import settings
from cpool.tester import *
from cpool.generator import *


class Scheduler(object):
    """调度策略"""

    @staticmethod
    def valid_cookie(cycle=settings.CYCLE):
        while True:
            print ('Cookies检测进程开始')
            try:
                for website, cls in settings.TESTER_MAP.items():
                    tester = eval(cls+'(website="' + website + '")')
                    tester.run()
                    print ('Cookie 检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print (e.args)

    @staticmethod
    def generate_cookie(cycle=settings.CYCLE):
        while True:
            print ('Cookie 生成开始')
            try:
                for website, cls in settings.GERERATOR_MAP.items():
                    generator = eval(cls+'(website="'+website+'")')
                    generator.run()
                    generator.close()
                    time.sleep(cycle)
            except Exception as e:
                print (e.args)

    @staticmethod
    def api():
        print ('API start')
        app.run(host=settings.API_HOST, port=settings.API_PORT)

    def run(self):
        if settings.API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()

        if settings.GENERATOR_PROCESS:
            generator_process = Process(target=Scheduler.generate_cookie)
            generator_process.start()

        if settings.VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()

if __name__ == '__main__':
    sc = Scheduler()
    sc.run()
