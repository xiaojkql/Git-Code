# Markdown  Guide

## 标题的使用

### 格式使用

段落格式Ctrl+0

#一阶标题 快捷键Ctrl+1

##一阶标题 快捷键Ctrl+2

###一阶标题 快捷键Ctrl+3

......

### 显示形式

![1标题显示格式](https://github.com/xiaojkql/Handy-Command-Code/blob/master/Markdown/Pic/1%E6%A0%87%E9%A2%98%E6%98%BE%E7%A4%BA%E6%A0%BC%E5%BC%8F.png)

## 文本居中

### 使用格式

  .<center>这是要居中的文本内容</center>

### 显示格式

<center>这是要居中的文本内容</center>

## 下划线

### 使用格式

</u>下划线内容</u>(去掉第一个斜杆/)  或者 快捷键Ctrl+U

### 显示格式

<u>下划线文本</u>

## 删除线

### 使用格式

\~~删除的内容~~  或者alt+shift+5

### 显示格式

~~删除的内容~~

## 字体加粗

### 使用格式

\**加粗的内容**  或者  Ctrl+B

### 显示格式

**加粗的内容**  **哈哈哈**

## 字体倾斜

### 使用格式

\*倾斜的内容*或者Ctrl+I

### 显示格式

*倾斜的内容* 

## 加入图片

直接从文件夹里面拉进

## 超链接

第一种：\http://www.baidu.com\

第二种：Ctrl + K

\[自定义内容](超链接地址) 

## 代码区域

Typora支持对多种语言的代码区域进行语法高亮。这些语言可以说是涵盖了绝大部分经常使用的编程语言，包括C++，Python，MATLAB，甚至包含spreadsheet（也就是Excel电子表格）。用Typora记编程笔记，看起来一清二楚。如果设置代码语言为flow，那么可以直接画出一个流程图；还可以使用相应的方法画出时序图等图表。

### 使用格式

\```+编程语言```C++

### 显示格式

``````c++
#include<iostream>

int main()
{
    using namespace std;
	int a = 0;
    cout<<a<<endl;
    return 0;
}
``````

## 表格的使用

第一种：Ctrl+T

![插入表格](C:\Users\xiaojkql\Desktop\Handy-Command-Code\Markdown\Pic\插入表格.png)

|  1   |  2   |  3   |
| :--: | :--: | :--: |
|  1   |  2   |  3   |
|      |      |      |

第二种：\|1|2|3|

| 中国 | 俄罗斯 | 美国 |
| ---- | ------ | ---- |
|      |        |      |

## 引注的使用

格式：>开头，空格+文字，按换行键换行，双按换行键跳出

显示：

> hahahhahahhha
>
> hfsdhfjsdfksa
>
> ashdfkasdfh
>
> sdfhjksd

## 序列的使用

格式; 开头*/+/-，空格+文字，可以创建无序序列，换行键换行，删除键+shift+tab跳出

开头1.，空格+后接文字，可以创建有序序列

*   Red
+   Green
-   Blue

1.  Red
2.  Green
3.  Blue

## 可选序列

开头序列+空格+[ ]+空格+文字，换行键换行，删除键+shift+tab跳出

- [ ] a
+ [ ] b
* [ ] c
- [ ] completed

## 高亮

==Hightlights==

