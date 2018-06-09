
# Scrapy 框架的使用

## 安装
```bash
pipenv install scrapy
```

## 创建项目
```bash
scrapy startproject p_name
```

## 创建爬虫, 使用item, 以及pipeline
```python
scrapy genspider spider_name spider_url
修改 sipder_name的parser方法

在编写item类, 用来存储数据的, 需要使用scrapy.Field，类似django的感觉呢

pipeline多用来做数据清洗, 操作数据库
定义from_crawler()从配置文件导入配置
open_spier(), 在爬虫开启的时候，调用
close_spider() 关闭爬虫调用
process_item()  对结果item进行过滤
```

## Scrapy Xpath
```python3

from scrapy import Selector

selector = Selector(text=html)
result = selector.xpath('//a[@href="xx"]')

# 提取, 使用extract_first可以避免数组越界的问题, 还可以传默认参数, 得不到数据的时候返回
first_result = result.extract_frist()
results = result.extract()

```
