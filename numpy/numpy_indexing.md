使用标准的python语法x[obj]
分为三类的indexing
- basic slicing
- advanced indexing
- field access
取决于obj的形式

exp1,exp2,exp3,... = (exp1,exp2,exp3,...)

## Basic Slicing and Indexing

**这种形式的indexing永远是view形式**

Basic slicing when obj is slice object，an integer,tuple of slice object and integers
用(start,stop,step)创建

slice objects,Ellipsis object,newaxis object

standard slicng syntax i:j:k

可以省略：:j:k，i::k, :: == :

Ellipsis ... 扩展为 : 使selection的长度与array的维数一致


np.newaxis 在其位置扩展一维 --> 方便的将一维扩展为二维

an integer i 等效于 i:i+1, 包含几个integer,就减几维x.dims-n所以，差为零时，此时返回的就解释为numpy的scalar对象

如果是 i:j:k此时返回的就是N维的，不会降低维度
包含几个integer就降低几维，但是i:j:K是不会降低维度的

即上面两种混合使用

x[obj] = value，value必须能broadcasting为原来的x[obj]的shape

可以使用slice对象，这样方便表明我们的indexing意义

## Advanced Idexing
**永远返回的是copy**

当obj是一个非tuple的序列时候就会被触发
non-tuple sequence, ndarray(integer or bool),tuple with at least one sequence object or ndarray(integer or bool)

x[(1,2,3),] != x[(1,2,3)] 前者--> ((1,2,3),) 后者 (1,2,3)

[1,2,3] != [1,2,slice(None)]

### integer array indexing
可以copy任意位置的item
#### Purely integer array indexing
result[i_1, ..., i_M] == x[ind_1[i_1, ..., i_M], ind_2[i_1, ..., i_M],.., ind_N[i_1, ..., i_M]]
也就是x[arr1,arr2,arr3,...]里面的arr表示每一维要取的位置，arr1,arr2,arr3 broadcast形成index矩阵，
结果的shape与arr1的shape一致

可以使用便捷函数np.ix_(rows,columns)快捷操作

### combining advanced and basic indexing
slice,ellipsis,newaxis

### Boolean array indexing
返回的是copy
when obj is an array object of Boolean type from comparison operators
多使用z[np.nonzeros(x)] 而不是 z[z>0]
obj.nonzero()

当obj.ndim == x.ndim x[obj]将返回一个一维array,要么用False填充，要么出错


