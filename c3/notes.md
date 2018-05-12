
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
