### 1.python 库包的安装

包源：https://www.lfd.uci.edu/~gohlke/pythonlibs/ 可以从这个网站下载whl的python包，然后用pip install 进行安装

安装最新python3.7,有些包才能使用

创建新环境：conda create -n your-env-name python=version

安装新包：conda install pkg

清除包：conda remove pkg

### 2.从kaggle上下载数据集的方法

使用它的python API进行下载

```
pip install kaggle
mkdir .kaggle (in /windows/user/yourname)
从kaggle my account 下载.json文件放入刚创建的文件夹中

以后下载文件都在.kaggle文件中用cmd命令行，下载的问价也在该文件夹中
```

