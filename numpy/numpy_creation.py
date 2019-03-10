# creation
import numpy as np

# ones and zeros

""" 1 empty(shape,dtype,order='C'or'F') """
z = np.empty((4, 5))
print(z)
z = np.empty_like(np.arange(1, 5, 1))

""" 2 eye(N,M,k,dtype,order) M==N default k 表示对角线的偏移量 """
z = np.eye(4, 5)
print(z)
z = np.eye(4, 5, -1)

""" 3 identiy(n,dtype) 只能指明一个n，创建nxn的单位对角阵"""
z = np.identity(5)
print(z)

""" 4 ones(shape,dtype,order) --> 全部元素都为1，可以指明shape"""
z = np.ones((4, 5))
print(z)
z = np.ones_like(z)

""" 5 zeros(shape,dtype,order) --> 全部元素为零的shape的矩阵 """
z = np.zeros((7, 8))
print(z)
z = np.zeros_like(z)

""" 6 full(shape,fill_value,dtype,order) --> 全部元素的值为fill_value"""
z = np.full((2, 3), 10)
print(z)
z = np.full_like(z, 1)


# from existing data

""" 1 array(object,dtype) 返回的是复制过后的不是view """
z = np.array([7, 8, 9])
print(z)
x = np.array(z)
x[0] = 10
print(z)  # 不变

""" 2 asarray(array,dtype,order) 在类型匹配的情况下不同于array，不会复制 """
ls = [1, 2, 3]
z = np.asarray(ls)
z[1] = 100
print(ls)
y = np.asarray(z)
y[1] = 1000
print(z)  # z 改变了

""" 3 copy(a,order) """
z = np.ones((4, 5))
x = np.copy(z)
print(x)


# 3 numerical ranges

""" 1 arrange(start,stop,step=1,dtype) """
print(np.arange(1, 5))
print(np.arange(4, 8, 2))

# 上面指明步长
# 下面指明个数
""" 2 linspace(start,stop,num,endpoint) """
print(np.linspace(4, 5, 20))


""" 3 logspace(start,stop,num,base=10) """
# 将[start,stop] 分成 num个数，然后base**[...]
print(np.logspace(1, 10, 10))
print(np.logspace(1, 10, 10, base=2))

""" 4 meshgrid(x1,x2,x3...,indexing='ij' or 'xy) """
x = np.arange(4, 6)
y = np.arange(12, 15)
xx, yy = np.meshgrid(x, y)
# 返回的是网格点的坐标，x,y分别存在两个ndarray中
print(xx)
print(yy)


# 4 buildding matrices
""" 1 diag(a,k) """
# 创建对角阵，并指明对角线的偏移 a为一个一维向量
print(np.diag(np.arange(1, 8), k=1))
# 提取对角元素 a为一个二维矩阵
print(np.diag(np.eye(4, 5), k=-1))


""" 2 tril(matrix,k) 提取下三角阵"""
print(np.tril(np.full((4, 6), 8)))


""" 3 triu(matrix,k) 提取上三角阵 """
print(np.triu(np.ones((7, 8)), k=-1))


""" 4 vander(1-D,N,increasing=False) """
