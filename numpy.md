# 1 creation
## 1.1 ones and zeros
empty(shape,dtype,order='C'or'F')
eye(N,M,k,dtype,order) M==N default k 表示对角线的偏移量
identiy(n,dtype) 只能指明一个n，创建nxn的单位对角阵
ones(shape,dtype,order) --> 全部元素都为1，可以指明shape
zeros(shape,dtype,order) --> 全部元素为零的shape的矩阵
full(shape,fill_value,dtype,order) --> 全部元素的值为fill_value

## 1.2 from existing data
array(object,dtype) 返回的是复制过后的不是view 
asarray(array,dtype,order) 在类型匹配的情况下不同于array，不会复制
copy(a,order)

## 1.3 numerical ranges
arrange(start,stop,step=1,dtype)
linspace(start,stop,num,endpoint)
logspace(start,stop,num,base=10)
meshgrid(x1,x2,x3...,indexing='ij' or 'xy)

## 1.4 buildding matrices
diag(a,k)
tril(matrix,k) 提取下三角阵
triu(matrix,k) 提取上三角阵
vander(1-D,N,increasing=False)



