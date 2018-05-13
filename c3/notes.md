
# 3.1
## urllib
* request: 用来模拟发送请求
* error: 异常处理, 可以捕获这些异常, 避免程序意外终止
* parse: 一个工具模块, 一共了许多URL的处理方法, 拆分, 解析, 合并
* robotparser: 识别网站的robots文件

## Request对象
```python
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```
* data, 如果传参数必须是bytes(字节流)类型的, 是字典, 先用urllib.parse.urlencode编码
* origin\_req\_host: 请方的地址或者IP

## Handler(在urllib.request)
>用handler构建opener
* HTTPDefaultErrorHandler: 用于处理HTTP响应错误,
* HTTPRedirectHandler: 重定向
* HTTPCookieProcessor: 用于处理cookies
* ProxyHandler: 代理
* HTTPPasswordMgr: 用于维护用户名和密码的表
* HTTPBasicAuthHandler: 打开链接需要认证, 用这个Handler处理
```python
from urllib.request import HTTPPasswordMgsWithDefaultRealm, HTTPBasicAuthHandler, ProxyHandler, build_opener
HTTPCookieProcessor
from urllib.error import URLError
import http.cookiejar

# auth
BASE_URL = "https://www.example.com"
auth_name = "username"
auth_password = "password"
auth_obj = HTTPPasswordMgrWithDefaultRealm()
auth_obj.add_password(None, url, auth_name, auth_password)
auth_handler = HTTPBasicAuthHandler(auth_obj)
opener = build_opener(auth_handler)
# Proxy
proxy_handler = ProxyHandler({"http": "http://IP:PORT"})

# Cookies

cookie = http.cookiejar.CookieJar() 
# MozillaCookieJar(filename)将cookie保存到文件中, 是Mozilla形式
# LWPCookieJar() 
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
```
## Error
* URLError: 
* HTTPError:

## Parse
* urlparse(urlstring, scheme="", allow+_fagmetns="")    # 用于解析url
* urlunparse([])     # 用于合成url
* urlsplit(urlstring) 与parse相似, 将params去掉
* urlunspilt([]) urlsplit反过来
* urljoin()
* urlencode()将get的请求参数传到url中. base_\_url + urlencode(data\_dict)
* parse\_qs(query)    # 将query进行拆分
* parse\_qsl(query)   # 将数据解析为[(), ()]
* quote(key)   # 将key转换成url可以识别的格式

## Robots协议
* User-Agent: spider-name, \*(全部的爬虫)
* Disallow: xxxxx, Allow: xxxx
```python3
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print (rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
```

# 3.2
## requests
* get()    get请求方法
* post()    post请求方法


## 高级用法
* file\_upload   加在post的files参数上, 下面有例子
* Cookies: 放在headers {'Cookie': 'balabala'}
* 会话维持, 使用会话, 相当于新开了浏览器的选项卡, 而不是新打开浏览器，当然可以选择使用cookies
* SSL验证, verify参数控制SSL验证, 
* 代理
* 身份认证 requests.auth.HTTPBasicAuth requests.get(urlm auth=HTTPBasicAuth(name, pwd))
    或者其他第三方认证 requests_oauthlib(pip)
* Prepared Request对象


```python3
import requests
import logging
from requests import Request, Session


files = {'file': open(path_to_filem, 'rb')}
data = {'name': 'vvyx', 'mail': 'stevenshuang521@gmail.com'}
headers = {'User-Agent': xxxxx}


# 上传文件
response = requests.post(url, data=data, files=files, headers=headers)


# Cookies
cookies = 'balabala';   # 在浏览器登录后拿到的cookies一个字符串, 可以将该cookies放到headers, 或者封装RequestCookieJar()对象

headers = {
    'Cookie': 'balabala',
}

jar = requests.cookie.Requests.CookieJar()
for cookie in cookies.split(;):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
res = requests.post(url, cookies=jar, headers=headers)    # cookies包含一次就可以这里只是做演示


# 会话维持
session = requests.Seesion()
session.get('http://httpbin.org/cookies/set/number/123')
res = session.get('http://httpbin.org/cookies')
print (res.json())  # json.loads(res.text)


# SSL
res = requests.get('https://www.12306.cn', verify=False)    # verify默认是True, 这样, 证书验证出错的时候，会抛出错误
# 指定一个本地的证书用作客户端证书, 需要有crt, key文件， 同时key必须是解密状态
res = requests.get('https://www.12306.cn', cert('path/to/server.crt', '/path/key'))


# 代理
proxies = {
    'http': 'ip:port',
}
# 5连接的超时时间, 11是read的超时时间, 30总的超时时间
res = requests.get(url, proxies=proxies, timeout=(5, 11, 30))


# Prepared Request
s = Session()
req = Request('POST', url ,data, headers)
prepped = s.prepare_request(req)
r = s.send(prepped)

```

