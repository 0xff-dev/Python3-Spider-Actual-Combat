# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode, quote
from scrapy import Request
from ssp.items import SspItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']
    base_url = 'https://s.taobao.com/search?q='


    def start_requests(self):
        for key in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_url + quote(key)
                # 在spider启动一个Request
                yield Request(url, self.parse, 
                        meta={'page': page}, dont_filter=True)

    def parse(self, response):
        
        products = response.xpath('\
                //div[@id="mainsrp-itemlist"]//div[@class="items"][1]\
                //div[contains(@class, "item")]')
        for key in products:
            item = SspItem()
            item['price'] = ''.join(key.xpath('\
                    .//div[contains(@class, "price")]//text()').extract()).strip()
            item['title'] = ''.join(key.xpath('\
                    .//div[contains(@class, "title")]//text()').extract()).strip()
            item['shop'] = ''.join(key.xpath('\
                    .//div[contains(@class, "shop")]//text()').extract()).strip()
            item['image'] = ''.join(key.xpath('\
                    .//div[@class="pic"]//img[contains(@class, "img")]\
                    /@data-src').extract()).strip()
            item['deal'] = key.xpath('\
                    .//div[contains(@class, "deal-cnt")]//text()').extract_first()
            item['location'] = key.xpath('\
                    .//div[contains(@class, "location")]//text()').extract_first()
            yield item

