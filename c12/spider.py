#!/usr/bin/env python
# coding=utf-8


from pyspider.libs.base_handler import *


class Handler(BaseHandler):

    crawl_config={}

    @every(minutes=24*60)
    def on_start(self):
        sefl.crawl('http://travel.qunar.com/travelbook/list.htm',
                callback=self.inde_page)

    @config(age=10*24*60*60)
    def index_page(self, response):
        for item in response.doc('li > .tit > a').items():
            # 最后的参数由phantomJS驱动js加载图片
            self.crawl(item.attr.href, callback=detail_page, fetch_type='js')
        self.crawl(response.doc('.next').attr.href, callback=self.index_page)
    
    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('#booktitle').text(),
            "data": response.doc('.when .data').text(),
            "day": response.doc('.hoelong .data').text(),
            "text": response.doc('#b_panel_schedule').text(),
            "image": response.doc('.cover_img').text(),
        }

