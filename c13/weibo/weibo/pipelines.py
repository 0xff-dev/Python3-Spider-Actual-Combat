# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from weibo.items import WeiboItem, UserItem, UserRelationItem
from pymongo import MongoClient
import pymongo
import time


class WeiboPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, WeiboItem):
            item['created_at'] = item['created_at'].strip()
            # 时间继进行清洗
            item['created_at'] = self.parse_time(item.get('created_at'))

    def parse_time(self, date):
        if re.match('刚刚', date):
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        if re.match('\d+分钟前', date):
            minutes = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()-float(minutes)*60))
        if re.match('\d+小时前', date):
            hourse = re.match('(\d+)', date).group(1)
            data = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()-float(hourse)*3600))
        if re.match('昨天.*', date):
            date = re.match('昨天(.*)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()-24*3600))+' '+date
        if re.match('\d{2}-\d{2}', date):
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime())+date+'00:00'
        return date


class TimePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, UserItem) or isinstance(item, WeiboItem):
            """用户的item"""
            now = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            item['created_at'] = now
        return item


# 数据存储
class MongoPipeline(object):

    def __init__(self, mongo_uri=None, mongo_db=None):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, cralwer):
        return cls(
            mongo_uri = cralwer.settings.get('MONGO_URI'),
            mongo_db = cralwer.settings.get('MONGO_DB'),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[UserItem.collection].create_index([('id', pymongo.ASCENDING)])
        self.db[WeiboItem.collection].create_index([('id',pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem) or isinstance(item, WeiboItem):
            self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        if isinstance(item, UserRelationItem):
            self.db[item.collection].update(
                    {'id': item.get('id')},
                    {'$addToSet': {
                            'follows': {'$each': item['follows']},
                            'fans': {'$each': item['fans']}
                        }
                    },
                    True)
        return item

