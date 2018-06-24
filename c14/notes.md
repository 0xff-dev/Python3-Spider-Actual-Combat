
# 分布式爬虫


## 分布式爬虫的原理

## Scrapy 去重
> 使用hashlib的计算URL, Method, URL, Body, Headers的hash值(使用sha1加密算法)

## 防止中断
> 每次中断爬虫在启动都要多做好多重复的爬取, 可以通过保存爬取队列, 进行中断防止
```bash
scrapy crawl spider -s JOB_DIR=crawls/spider
```

## Scrapy-Redia剖析

