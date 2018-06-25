
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
* 爬取队列
> 在这个文件中实现了基于Redis的数据结构的FifoQueue, LifoQueue, PeiorityQueue(SortedSet)分布式队列
```python
class FifoQueue(Base):
    """Per-spider FIFO queue"""

    def __len__(self):
        """返回队列数据的多少"""
        return self.server.llen(self.key)
    
    def push(self, request):
        """
        push request into redis
        使用父类的_encode_request, 将request对象序列化, 
        """
        self.server.lpush(self.key, self._encode_request(request))
    
    def pop(self, timeout=0):
        """Pop a request Obj"""
        
        if timeout > 0:
            # BRPOP 是列表的阻塞式(blocking)弹出原语。
            # 它是 RPOP 命令的阻塞版本，当给定列表内没有任何元素可供弹出的时候，
            # 连接将被 BRPOP 命令阻塞，直到等待超时或发现可弹出元素为止。
            data = self.server.brpop(self.key, timeout)
            if isinstance(data, tuple):
                data = data[1]
        else:
             data = self.server.rpop(self.key)
        if data:
            return self._decode_request(data)
```

* 过滤去重
> 主要实现了request\_see()用来判断request是否在redis中, 
> 以及使用request\_fingerprint()使用scrapy的request\_fingerprint()用来生成request的指纹

```python
def request_see(self, request):
    fp = self.request._fingerprint(request)
    added = self.server.sadd(self.key, fp)
    return added == 0

def request_fingerprint(self, request):
    """使用scrapy的request_fingerprint返回指纹"""

    return request_fingerprint(request)
```

* 调度器
> 
