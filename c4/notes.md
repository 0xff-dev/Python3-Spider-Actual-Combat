
# 4.1
# XPath
<table>
    <tr>
        <th>表&nbsp;&nbsp;&nbsp;达&nbsp;&nbsp;&nbsp式</th>
        <th>描&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;述</th>
    </tr>
    <tr>
        <td text-align="left">nodename</td>
        <td text-align="center">选取此节点的所有子节点</td>
    </tr>
    <tr>
        <td text-align="left">/</td>
        <td text-align="center">从当前节点选取直接子节点</td>
    </tr>
    <tr>
        <td text-align="left">//</td>
        <td text-align="center">从当前节点选取子孙节点</td>
    </tr>
    <tr>
        <td text-align="left">.</td>
        <td text-align="center">选取当前节点</td>
    </tr>
    <tr>
        <td text-align="left">..</td>
        <td text-align="center">选取当前节点的父节点</td>
    </tr>
    <tr>
        <td text-align="left">@</td>
        <td text-align="center">选取属性</td>
    </tr>
</table>

## 所有节点
```
html = etree.parse(file, etree.HTMLParse())
html.xpath('//*')
```

## 子节点
```
html.xpath('//li/a')
```

## 父节点
```
html.xpath('//a["href=link"]/../@class')
html.xpath('//a["href=link"]/parent::*/@class')
```

## 属性匹配
```
html.xpath('//li[@class="link"]')
```

## 文本获取
```
text = html.xpath('//li/a["href=link3.html"]/text()')
html.xpath('//li[@class="item-0"]//text()')    选取子孙的节点的内容
```

## 属性获取
```
html.xpath('//li/a/@href')
```

## 属性多值匹配
```
html.xpath('//li[contains(@class, 'li')]')
```

## 多属性匹配
```
html.xpath('//li[contains(@class, "li") and @name="zs"]')
选取class包含li,同时含有name=zs的li
```

## 排序选择
```
html.xpath('//li[1]/a/text()')
html.xpath('//li[last()]/a/text()')
html.xpath('//li[position()<3]/a/text()')
html.xpath('//li[last()-1]/a/text()')
```

## 节点轴选择
```
html.xpath('//li[1]/ancestor::*')    选取所有的祖先节点
html.xpath('//li[1]/ancestor::div')  选取祖先div节点
html.xpath('//li[1]/attribute::*')   获取li的所有属性值
html.xpath('//li[1]/child::a["href="xxx]') 选取所有的直接子节点,
html.xpath('//li[1]/descendant::span') 选取子孙节点 span
html.xpath('//li[1]/following::*[2]')  选取当前节点的全部后续节点，在这里选择第二个
html.xpath('//li[1]/following-sibling::*')  选取兄弟节点
```

# BeautifulSoup
* 选择元素
```
soup = BeautlfulSoup(markup, 'lxml')
soup.title, soup.title.p, soup.title.string(获取title的文本内容)
```
* 提取信息
```
soup.title.name(打印节点的名称), soup.title.attrs['class'](获取属性的值)
soup.p['class'](获取属性)
```
* 嵌套选择
```
soup.head.title.string
```
* 关联选择
```
soup.p.contents(获取p节点的直接节点, 并且以list的形式返回)
soup.p.children(返回p节点的直接子节点, generator)
soup.p.descendants(p的所有子孙节点,generator)
soup.a.paretn(寻找父亲节点, generator)
soup.a.parents(寻找祖先节点, generator)
soup.a.next_sbiling?s(寻找下一个兄弟节点, )
soup.a.previous_sibling?s(寻找前一个兄弟节点)
获取关联节点的信息，同上面一样
```

* 方法选择器
```
soup.find_all(name="tag")    # 查找所有的tag标签
for ul in soup.find_all(name="ul"):
    for li in ul.find_all("li"):
        # 嵌套的查询
soup.find_all(attrs={})    #通过属性来查找 对于属性id, class直接用 id=xxx, class_(与python的class关键字冲突, 所以添加_)
soup.find_all(text=re.compile(r'pattern'))    # 通过text来匹配文本
find()返回一个符合条件的tag
find_parents(), find_parent()   返回父亲节点s/父亲节点
find_next_siblings(), find_next_sibling()   返回后面兄弟节点s/兄弟节点
find_previous_sibling(), find_previous_siblings()   返回前面的兄弟节点s/兄弟节点
find_next(), find_all_next()    返回符合条件的后面的节点/全部节点
find_previous(), find_all_previous()    返回符合条件的前面的节点/全部节点
```

* css选择器
```
soup.select(".panel .panel-head")    # 选择class=panel下的class=panel-heading的标签
soup.select("ul")
soup.slect("#list-2 .element")    # 选取id=list-2下的class=element的所有标签
获取文本 string, get_text()
```
