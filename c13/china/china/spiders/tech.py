# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from china.items import NewsItem
from china.loaders import ChinaLoader


class TechSpider(CrawlSpider):
    name = 'tech'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles']

    rules = (
        # 本页里的文章
        Rule(LinkExtractor(allow=r'article\/.*\.html', 
            restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), 
            callback='parse_item'),
        # 下一页的链接
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()

        """
        item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('\
                //div[@id="chan_newsDetail"]//text()').extract()).strip()
        item['datetime'] = response.xpath('\
                //div[@id="chan_newsInfo"]/text()'\
                ).re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
        item['website'] = '中华网'
        yield item
        """

