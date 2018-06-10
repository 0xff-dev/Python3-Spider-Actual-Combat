# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        # 日志
        self.logger.debug(response.text)
        self.logger.debug('Status Code: {}'.format(response.status))
        
