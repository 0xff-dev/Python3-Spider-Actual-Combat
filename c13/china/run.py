#!/usr/bin/env python
# coding=utf-8

import sys
from scrapy.utils.project import get_project_settings
from china.spiders.universal import UniversalSpider
from china.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():

    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 设置用户的User-Agent
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()

