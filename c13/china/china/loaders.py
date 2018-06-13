#!/usr/bin/env python
# coding=utf-8

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):

    default_out_processor = TakeFirst()


class ChinaLoader(NewsLoader):

    """input processor 以_in结尾, 前面是item的字段名字, output 类似, _out结尾"""
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())

