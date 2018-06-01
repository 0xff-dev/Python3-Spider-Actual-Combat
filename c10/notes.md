
# Github模拟登录，维护cookies池

## Github登录
> 首先抓包分析，登录需要提交的信息
> 维持session, 进行登录
### Bug
> github更新了，个人动态部分抓取不到，*网页源代码可以获取到

## Cookies池
> Cookie池和之前的ProxyPool池是类似的实现，分别包括
* 获取模块 (用与获取帐号的Cookies)
* 存储模块 (将username, password, cookie 存储在Redis中)
* 检测模块 (用于检测Cookie是否过期, 过期的删掉)
* 接口模块 (用户计算总的cookies数量，和随机返回可用的Cookies)



