背景：python只给出了两种数据类型，即integer type与 floating-point type。这用起来很方便但是这在科学计算时，有时候是不满足应用的。所以numpy库设置了其他数据类型，中国有24种，可以用numpy进行指定类型进而设置数据类型。基于CPython写的，有些type是与python兼容的。
array scalar与numpy的array有同样的操作接口

有一个等级图，np.generic,np.bool,np._object,np.number,np.flexible等等，可以用np.isintance(val,np.generic)来判断是否属于某个等级

flexible 即字符串，np.character:（np.str_, np.unicode), np.void

所有的这些数据类型可以用bit-width的name进行指定

有些数据类型是继承自python本身的内置的数据类型
int_ float_ complex_ bytes_ unicode_
但是bool_ 不是继承自bool，且它不是属于int的子类型，不是一个number,这一点与python是不一样的 --> 可以进行那些操作呢？？？

默认的type是float_
int8 , int16,int32,int64 uint8,uint16,uint32,uint64, float16,float32,float64,float96,float128

有一些attr:
shape,strides,ndim,data,size,itemsize,dtype,base,

dt = np.dtype(np.int32)

numpy的data type是type class的实例
有属性 --> type,itemsize,
