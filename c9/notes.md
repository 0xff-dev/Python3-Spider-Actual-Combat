
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

