
# 5.3
## Mongo
<table>
    <tr>
        <th>符号</th>
        <th>含义</th>
        <th>示列</th>
    </tr>
    <tr>
        <td>$lt</td>
        <td>小于</td>
        <td>{'age': {"%lt": 20}}</td>
    </tr>
    <tr>
        <td>$gt</td>
        <td>大于</td>
        <td>{'age': {"$gt": 20}}</td>
    </tr>
    <tr>
        <td>$lte</td>
        <td>小于等于</td>
        <td>{"age": {"$lte": 20}}</td>
    </tr>
    <tr>
        <td>$gte</td>
        <td>大于等于</td>
        <td>{"age": {"$gte": 20}}</td>
    </tr>
    <tr>
        <td>$ne</td>
        <td>等于</td>
        <td>{"age": {"$ne": 20}}</td>
    </tr>
    <tr>
        <td>$in</td>
        <td>在范围</td>
        <td>{"age": {"$in": [20, 30, 40]}}</td>
    </tr>
    <tr>
        <td>$nin</td>
        <td>不再范围</td>
        <td>{"age": {"$nin": [1, 2, 3]}}</td>
    </tr>
    <tr>
        <td>$regex</td>
        <td>正则表达式</td>
        <td>{"age": {"$regex": "\d+"}}</td>
    </tr>
    <tr>
        <td>$exists</td>
        <td>属性存在</td>
        <td>{"name": {"exists": True}}</td>
    </tr>
    <tr>
        <td>$type</td>
        <td>类型判断</td>
        <td>{"age": {"$type": "int"}} 判断age是否是int</td>
    </tr>
    <tr>
        <td>$mod</td>
        <td>取模运算</td>
        <td>{"age": {"$mod": [5, 0]}} 年龄%5=0</td>
    </tr>
    <tr>
        <td>$text</td>
        <td>文本查询</td>
        <td>{"$text": {"$search": "like"}} text串中包含like的</td>
    </tr>
    <tr>
        <td>$were</td>
        <td>高级条件查询</td>
        <td>{"$where": obj.fans_count == obj.follows_count} 粉丝数=关注数</td>
    </tr>
</table>


