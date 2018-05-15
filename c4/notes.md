
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

