
# App抓包工具

#Charles
> 这里并没有安装Charles，他需要付费, 我目前支付不起.
> [Charles官方下载链接](https://www.charlesproxy.com/download)


# Fiddler
> 本机之前就有Fiddler, 配置一下抓包手机app即可

## Fiddler安装
> [fiddler下载地址](https://www.telerik.com/download/fiddler)
> 需要mono环境
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list
sudo apt-get update

sudo apt-get install mono-complete
```

## 配置Fiddler
1. 重要的一点是保证Fiddler和你的手机处在同一个网络下
2. 打开Fiddler, tools - options - connections 将allow remote computers connect选中
3. 重启Fiddler
4. 手机配置以iphone为例
    * 点击wifi右边的反向叹号, 在最下边看到配置代理
    * 选择手动会要求你配置服务器(电脑的IP)，端口(如果你的Fiddler的默认端口没有修改就是8888), 和Fiddler的监听端口是一样的
    * 保存，大功告成, 启动Fiddler, 在开启你的app会发现好多请求，找自己需要的

