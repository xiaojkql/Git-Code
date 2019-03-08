#### 1 pip更换源

mkdir ~/.pip

vim .pip/pip.conf

[global]

index-url = https://pypi.tuna.tsinghua.edu.cn/simple

trusted-host =  pypi.tuna.tsinghua.edu.cn

源地址：

清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

阿里云 http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

豆瓣(douban) http://pypi.douban.com/simple/

中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

#### 2 pip 常用命令


python 
autoPep8 --> 格式化的东西，在vscode由python.format.provider进行更改
pep8 / flake8 就是检查错误的，即linting，vscode中用python 选择lingting进行选择插件

关于缩进
tab与space不能共存，可以用notepad++显示空格与tab来查看是否同时存在，视图-->

linux 上解压的文件不能再windows上使用





