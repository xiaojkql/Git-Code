关于numpy
一直在用numpy，但是对numpy的本质不了解，用的很糊涂
numpy是一个包，给我们提供了很多东西，但是要用里面的东西，必须要用python的标准语法，包名.要用的东西
很多，很多的python对象，例如numpy.ndarray, np.int32, np.dtype
即
## array object
在我现有理解水平下，我认为该对象就是用来存储ndarray对象，scla data type 对象，等等，就像一个list一样，但是我们经常使用的确是ndarray，这里面也有很多东西供我们使用

## ndarray object
里面有一个ndarray对象？,反正是一个container,就像C++等语言的数组,用来存放连续数据的,然后我们在基于这个数组建立其他数据结构类型,这个结构包括很多attr和method接口可以获取,是一个存储多维数据的向量，但是它里面的存储的数据类型要一致，即每个item的数据类型要一致，也就是它在底层存放数据时，它是按照一个规则读取每个item的。可以存放，numpy包里面自己定义的数据类型，python内建的类型，我们自己创建的object等等，唯一的要求每一个item的类型必须一致。
这个array类型给我们提供了同样提供了很多attr和method方便我们使用。
我们在创建array对象时，可以直接使用即np.array(),或者我么调用numpy这个包提供给我们的各种创建函数，比如eye,ones,full，arange,可能这些函数在调用array进行创建一个array对象

## data-type-object
这个object的每一个instance都与一个array相关，代表array对象里面存储的数据类型，决定了里面数据的存储方式，我们可以用np.dtype()这个方法创建我们的data-type-object对象的实例
在调用numpy这包的很多函数时，有一个参数dtype要求我们指定数据类型，实际上就是指定这个对象的实例

## array-scalar object
这个就是array内存储的很真实的数据类型了，但我们获得一个array中一个item时在python层面就是这个类型


##
接下来就是各种各样的函数了，用来创建np.ndarray这个数据类型对象，操作这个对象的各种函数接口，还有创建data-type-object这个对象的方法，以及其他很多的numpy里面的对象

我们往往在使用numpy中各种函数时，其实它是操作在一个array这个对象，这个对象就像list一样可以存储很多东西，其实存储很多东西，也就是ndarray，data-type 这些东西，很多内容都是在内部进行操作了，然后给我们返回的就是ndarray这个东西了。

##
我们可以使用numpy做哪些事呢？？
### 1 创建ndarray对象
调用numpy提供的一系列函数接口进行创建
在创建过程中，我们可以用scalar data type指定数据类型，dtype进行创建相应的数据类型

### 2 操作ndarray对象
用一些列库函数，**用indexing**
