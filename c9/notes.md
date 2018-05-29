
# 代理使用

## urllib使用代理socks5
* socks安装 pip install PySocks

```python
import socks, socket
from urllib import request
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


# http, https类型的代理
proxy = ProxyHandler({
    'http': '',
    'https': '',
})

opener = build_opener(proxy)
try:
    opener.open(url)
except URLError as e:
    print (e)


# socks 代理
socks.set_default_proxy(socks.SOCKS5, ip, port)
socket.socket = socks.socksocket
try:
    resp = request.urlopen(url)
    do
except URLError as e:
    pass
```

## requests代理
* pip install 'requests[socks]'
```python
import requests

# http, https类型的代理
proxiex = {
    'http': 'http://ip:port',
    'https': 'https://ip:port',
}

resp = request.get(url, proxies=proxies)

# socks5 代理
proxies = {
    'http': 'socks5://ip:port',
    'https': 'socks5://ip:port',
}

resp = requests.get(url, proxies=proxies)

```

## 说明
> 在搜狗微信爬虫中，没有设置cookies，使用代理需要设置一下，同时参考我的[ProxyPool](https://github.com/stevenshuang/ProxyPool)使用代理池
> 我设置的池子貌似只有15条左右的ip可以使用，可以在自己增加一些其他的免费ip, 后面会增加付费代理, 以及ADSL拨号代理

## 感谢
> 感谢支持!以及崔大大

