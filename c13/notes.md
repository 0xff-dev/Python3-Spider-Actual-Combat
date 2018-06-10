
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

## Spider使用
* 用start\_url初始化Request, 请求成功的时候, Response传递给回调函数进行处理
* 在回调函数中进行页面解析, 有两种情况, 解析出item数据, 另一个是解析到url, 重新加入调度队列
* 对解析出的item数据, 可以通过feed exports写入文件, 设置Pipeline写入数据库, 过滤等
* 返回的是Request，执行Request得到Response, 在用回调函数解析


## Spider的分析
### 重要基础属性
* alloww\_domains  允许的爬取域名
* stat\_urls 开始的url列表
* parse Response没有指定回调函数, 调用, 提取数据和下一步的请求, 返回一个Requerst, Item对象

## DOWNLOADER MIDDLERARES
> 想要重新定义DOWNLOADER MIDDLERARES 实现一下三个任意一个方法
* process\_request(request, spider)
    > Request被Scrapy的引擎调度给DownLoader前, 先调用该函数, 返回None, Request, Response
    > 返回None, 将有其他的DownLoader继续执行这个Request
    > 返回Request, Request重新放到调度队列中
    > 返回Response, 每个DOWNLOADER的 process_response()

* process\_response(request, response, spider)
    > 在下载Request后, 在Scrapy将Response传到spider处理之前, 通过process_request处理
    > 返回Request, 送入调度队列中，等待被处理
    > 返回Response 优先级较低的DOWNLOADER处理, 
    > 异常 调errorback()

* process\_exception()
    > 调用类似同上

