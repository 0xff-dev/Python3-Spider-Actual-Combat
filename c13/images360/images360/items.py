# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collections = table = 'Images'
    id = Field()
    url = Field()
    title = Field()
    # 缩略图
    thumb = Field()

