
# pyspider框架

## 安装
> * pipenv install pyspider
>可能会遇到错误  
```bash
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-qyfvpmey/pycurl/

sudo apt-get install python python-dev python-distribute python-pip libcurl4-openssl-dev libxml2-dev libxslt1-dev python-lxml
```

## 使用
```bash
pyspider all启动pyspider
```
* 点击创建, 新建一个爬虫, 写好名称和爬去的url
* 在crawl函数总配置自己需要抓取的目标css选择路径
* 在detail\_page函数中拿到自己需要数据
* 回到主界面, status=debug or running, 点击run, 启动爬虫.

## pyspier参数详解
* 配置webUI的认证
```bash
新建pyspider.json
{
    "webui":{
        "username": "root",
        "password": "root",
        "need-auth": true,
        //下面的配置
        "port": 5001,
    }
}

pyspider -c pyspider.json all
```

* --port port改变运行端口或者在json文件中
* crawl函数, 主要的参数
    > 1. url, 抓取的url
    > 2. callback，回调函数
    > 3. age, 任务的有效时间
    > 4. priority 任务的优先级
    > 5. data 表单数据
    > 6. files 上传文件
    > 7. fetch_type='js' 开启phantomJS的渲染

* @every来设置周期性的爬取. @evecy(mintims=24\*60)
* 项目的状态
    > 1. TOIO 刚创建, 还未实现的状态
    > 2. STOP 停止项目的抓取
    > 3. DEBUG/RUNNING 项目可以运行
    > 4. CHECKING 项目被修改的状态
    > 5. PAUS 抓取暂停

