# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 用来做数据清清洗
from scrapy.exceptions import DropItem
from pymongo import MongoClient


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_itme(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem('Missing text, Drop it')


class MongoPipeline(object):

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    # 从全局的setting读取配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                mongo_url=crawler.settings.get('MONGO_URL'),
                mongo_db=crawler.settings.get('MONGO_DB')
            )
    
    # 开启爬虫的时候调用
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item
    
    # 关闭爬虫调用
    def close(self, spider):
        self.client.close()

