#### 1 加快对github的访问速度

```linux
nslookup github.global.ssl.fastly.Net
nslookup github.com 
vim /etc/hosts
增加以下内容 
151.101.77.149 http://global-ssl.fastly.net
13.229.188.59 http://github.com
sudo /etc/init.d/networking restart
```

使用TI等
https://gitee.com/wszqkzqk/deepin-wine-for-ubuntu

ubuntu更新源在
/etc/apt/source.list中