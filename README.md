
# Python3-Spider-Actual-Combat

# Python3网络爬虫开发实战

## 服务器的响应代码
<table>
    <tr>
        <th text-align="center">状&nbsp;&nbsp;&nbsp;态&nbsp;&nbsp;&nbsp;码</th>
        <th text-align="center">说&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;明</th>
        <th text-align="center">详&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;情</th>
    </tr>
    <tr>
        <td text-align="left">100</td>
        <td text-align="left">继续</td>
        <td text-align="left">请求者应该继续提出请求, 服务器已经收到请求的一部分, 正在等待其他的部分</td>
    </tr>
    <tr>
        <td text-align="left">101</td>
        <td text-align="left">切换协议</td>
        <td text-align="left">请求这要求服务器切换协议, 并且服务器已经确认准备切换</td>
    </tr>
    <tr>
        <td text-align="left">200</td>
        <td text-align="left">成功</td>
        <td text-align="left">服务器成功的处理了请求</td>
    </tr>
    <tr>
        <td text-align="left">201</td>
        <td text-align="left">已创建</td>
        <td text-align="left">请求成功并且服务器创建了新的资源</td>
    </tr>
    <tr>
        <td text-align="left">202</td>
        <td text-align="left">已接受</td>
        <td text-align="left">服务器接受请求, 尚未处理</td>
    </tr>
    <tr>
        <td text-align="left">203</td>
        <td text-align="left">非授权信息</td>
        <td text-align="left">服务器成功的处理了请求，但返回的信息可能来自另一个源</td>
    </tr>
    <tr>
        <td text-align="left">204</td>
        <td text-align="left">无内容</td>
        <td text-align="left">服务器成功的处理了请求, 但未返回任何信息</td>
    </tr>
    <tr>
        <td text-align="left">205</td>
        <td text-align="left">重置内容</td>
        <td text-align="left">服务器成功的处理了请求，但请求被重置</td>
    </tr>
    <tr>
        <td text-align="left">206</td>
        <td text-align="left">部分内容</td>
        <td text-align="left">服务器处理了部分请求</td>
    </tr>
    <tr>
        <td text-align="left">300</td>
        <td text-align="left">多种选择</td>
        <td text-align="left">针对请求，服务器执行多种操作</td>
    </tr>
    <tr>
        <td text-align="left">301</td>
        <td text-align="left">永久移动</td>
        <td text-align="left">请求的网页被移动到新的位置，永久重定向</td>
    </tr>
    <tr>
        <td text-align="left">302</td>
        <td text-align="left">临时移动</td>
        <td text-align="left">请求的网页暂时跳转到其他页面，暂时重定向</td>
    </tr>
    <tr>
        <td text-align="left">303</td>
        <td text-align="left">查看其他位置</td>
        <td text-align="left">如果原来的请求是POST请求，重定向目标文档应该是通过GET提取</td>
    </tr>
    <tr>
        <td text-align="left">304</td>
        <td text-align="left">未修改</td>
        <td text-align="left">此次请求的网页修改，继续使用上次的资源</td>
    </tr>
    <tr>
        <td text-align="left">305</td>
        <td text-align="left">使用代理</td>
        <td text-align="left">请求这使用代理请求网页</td>
    </tr>
    <tr>
        <td text-align="left">307</td>
        <td text-align="left">临时重定向</td>
        <td text-align="left">请求的资源临时从其他位置响应</td>
    </tr>
    <tr>
        <td text-align="left">400</td>
        <td text-align="left">错误请求</td>
        <td text-align="left">服务器无法解析该请求</td>
    </tr>
    <tr>
        <td text-align="left">401</td>
        <td text-align="left">未授权</td>
        <td text-align="left">请求没有进行身份验证或者未通过验证</td>
    </tr>
    <tr>
        <td text-align="left">403</td>
        <td text-align="left">禁止访问</td>
        <td text-align="left">服务器拒绝此请求</td>
    </tr>
    <tr>
        <td text-align="left">404</td>
        <td text-align="left">未找到</td>
        <td text-align="left">服务器找不到请求的网页</td>
    </tr>
    <tr>
        <td text-align="left">405</td>
        <td text-align="left">方法禁用</td>
        <td text-align="left">服务器禁用了请求中的指定的方法</td>
    </tr>
    <tr>
        <td text-align="left">406</td>
        <td text-align="left">不接受</td>
        <td text-align="left">无法使用请求的内容响应请求的网页</td>
    </tr>
    <tr>
        <td text-align="left">407</td>
        <td text-align="left">需要代理请求</td>
        <td text-align="left">请求者需要使用代理的授权</td>
    </tr>
    <tr>
        <td text-align="left">408</td>
        <td text-align="left">请求超时</td>
        <td text-align="left">服务器请求超时</td>
    </tr>
    <tr>
        <td text-align="left">409</td>
        <td text-align="left">请求冲突</td>
        <td text-align="left">服务器请求冲突</td>
    </tr>
    <tr>
        <td text-align="left">410</td>
        <td text-align="left">已删除</td>
        <td text-align="left">请求的资源被永久的删除</td>
    </tr>
    <tr>
        <td text-align="left">411</td>
        <td text-align="left">需要有效的长度</td>
        <td text-align="left">服务器不接受不含有效内容长度标头字段的请求</td>
    </tr>
    <tr>
        <td text-align="left">412</td>
        <td text-align="left">未满足前提条件</td>
        <td text-align="left">服务器未满足请求者在请求中设置的一个前提条件</td>
    </tr>
    <tr>
        <td text-align="left">413</td>
        <td text-align="left">请求实体过大</td>
        <td text-align="left">请求实体过大，超出了服务器的处理能力</td>
    </tr>
    <tr>
        <td text-align="left">414</td>
        <td text-align="left">请求URI过长</td>
        <td text-align="left">请求的URI过长，服务器无法处理</td>
    </tr>
    <tr>
        <td text-align="left">415</td>
        <td text-align="left">不支持类型</td>
        <td text-align="left">请求的格式不被请求页面支持</td>
    </tr>
    <tr>
        <td text-align="left">416</td>
        <td text-align="left">请求不在范围</td>
        <td text-align="left">页面无法提供请求的范围</td>
    </tr>
    <tr>
        <td text-align="left">417</td>
        <td text-align="left">未满足期望值</td>
        <td text-align="left">服务器未满足期望请求标头的要求</td>
    </tr>
    <tr>
        <td text-align="left">500</td>
        <td text-align="left">服务器内部错误</td>
        <td text-align="left">服务器遇到错误，无法完成请求</td>
    </tr>
    <tr>
        <td text-align="left">501</td>
        <td text-align="left">未实现</td>
        <td text-align="left">服务器不具备完整的请求功能</td>
    </tr>
    <tr>
        <td text-align="left">502</td>
        <td text-align="left">错误网关</td>
        <td text-align="left">服务器作为网关或者代理，从上游服务器收到无效响应</td>
    </tr>
    <tr>
        <td text-align="left">503</td>
        <td text-align="left">服务不可用</td>
        <td text-align="left">服务器目前无法使用</td>
    </tr>
    <tr>
        <td text-align="left">504</td>
        <td text-align="left">网关超时</td>
        <td text-align="left">服务器作为网关或者代理，但是没有及时的从上游服务器收到请求</td>
    </tr>
    <tr>
        <td text-align="left">505</td>
        <td text-align="left">HTTP版本不支持</td>
        <td text-align="left">服务器不支持请求使用HTTP协议版本</td>
    </tr>
</table>
