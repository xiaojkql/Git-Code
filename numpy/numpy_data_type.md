data_type_object
# 概述
是numpy包内定义的一个python class
它描述了
- 数据类型，整数，浮点数等等
- 数据的大小，16位，32位等等
- 存放的方式，大端，小端，
- 数据结构-->有这个类型的原因，因为用户可以自己创建自己要指定的类型，而不仅仅限定于一些很简单的数据类型，当指定这种时，我们获得是item是np.void类型
- subarray

scalar type 不是 dtype object，但是当需要dtype这个参数时我们可以直接使用scalar type进行简单的指定

# 创建方法
其他类型可以自动转换为dtype
可以显示用constructor的创建，
可以用其他转换而来，scalar data type, python built in type, object,但是都与sclar data type中的一个相联系，复杂的用np.void表示

# 属性
type-->array scalar type
shape
itemsize

