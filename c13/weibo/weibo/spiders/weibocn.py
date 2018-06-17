# -*- coding: utf-8 -*-

from scrapy import Request, Spider
from weibo.items import UserItem, UserRelationItem, WeiboItem
import json
import re
import time


class WeibocnSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}'
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107630{uid}'
    start_users = ['3217179555', '1742566624', '2282991915']

    def start_requests(self):
        for user in self.start_users:
            yield Request(self.user_url.format(uid=user), callback=self.parse_user)

    def parse_user(self, response):
        self.logger.debug(response)
        result = json.loads(response.text)
        if result.get('data').get('userInfo'):
            user_info = result.get('data').get('userInfo')
            user_item = UserItem()
            field_map = {
                    'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'cover': 'cover_image_phone',
                    'gender': 'gener', 'description': 'description', 'fans_count': 'followers_count',
                    'follows_count': 'follow_count', 'weibos_count': 'statuses_count', 'verified': 'verified',
                    'verified_reason': 'verified_reason', 'verified_type': 'verified_type',
                }
            for field, attr in field_map.items():
                user_item[field] = user_info.get(attr)
            yield user_item
            uid = user_info.get('id')
            # 关注
            yield Request(self.follow_url.format(uid=uid, page=1), 
                    callback=self.parse_follows, meta={'page': 1, 'uid': uid})
            # 粉丝
            yield Request(self.fans_url.format(uid=uid, page=1), 
                    callback=self.parse_fans, meta={'page': 1, 'uid': uid})
            # 微薄
            yield Request(self.weibo_url.format(uid=uid, page=1), 
                    callback=self.parse_weibos, meta={'page': 1, 'uid': uid})

    def parse_follows(self, response):
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') \
            and len(result.get('data').get('cards')) \
            and result.get('data').get('cards')[-1].get('card_group'):
            follows = result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid = follow.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_user)
            # 当前用户的uid, 最relation
            uid = response.meta.get('uid')
            user_relation = UserRelationItem()
            follows = [{'id': follow.get('user').get('id'), 'name': follow.get('user').get('screen_name')} 
                    for follow in follows]
            user_relation['id'] = uid
            user_relation['follows'] = follows
            user_relation['fans'] = []
            yield user_relation
            page = response.meta.get('page')+1
            yield Request(self.follow_url.format(uid=uid, page=page), 
                    callback=self.parse_follows, meta={'uid': uid, 'page': page})
    
    def parse_fans(self, response):
        pass

    def parse_weibos(self, response):
        """抓取用户的微波信息"""
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos = result.get('data').get('cards')
            for weibo in weibos:
                mblog = weibo.get('mblog')
                if mblog:
                    weibo_item = WeiboItem()
                    field_map = {
                        'id': 'id', 'attitudes_count': 'attitudes_count', 'comments_count': 'comments_count',
                        'created_at': 'created-at', 'reposts_count': 'reposts_count', 'picture': 'original_pic',
                        'pictures': 'pics', 'source': 'source', 'text': 'text', 'raw_text': 'raw_text',
                        'thumbnail': 'thumbnail_pic'
                    }
                    for field, attr in field_map.items():
                        weibo_item[field] = mblog.get(attr)
                        weibo_item['user'] = response.meta.get('uid')
                        yield weibo_item
                uid = response.meta.get('uid')
                page = response.meta.get('page')+1
                yield Request(self.weibo_url.format(uid, page), 
                        callback=self.parase_weibos, meta={'uid': uid, 'page': page})

