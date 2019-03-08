import numpy as np

# 1 Generating index arrays

""" 1 np.c_[arr1,arr2] --> column stack"""
# 相似于column_stack
# 列堆积
# arr1 arr2 看成（n,1）是一维向量的时候就把对应元素相连接，返回一个二维
# arr1 arr2 是二维向量，列相链接
z = np.arange(6).reshape(2, 3)
z1 = np.arange(6, 12).reshape(2, 3)
z3 = np.c_[z, z1]
print(z3)


""" 2 np.r_[arr1,arr2] """
# 对于一维（n，1） [[1],[2],[3]],行相连接，最后在去掉中括号
# 按行相加
z = np.arange(6)
z1 = np.arange(6, 12)
z4 = np.r_[z1, z]
print(z4)


""" 3 np.s_[start:stop:step] --> slice(start,stop,step) """
# 创建slice
z1 = np.arange(0, 12).reshape(6, 2)
print(z1[:,np.s_[::2]])


""" 4 np.index_exp[::]-->上面一样 """


""" 5 np.nonzero(array) --> (arr1,arr2,arr3)"""
# 返回非零的索引，len(arr1)==非零的个数，每个arr1对应非零元素的每一维的索引
# 可以用np.transpose(return_value) --> 2-D arr element --> index of nonzero
z = np.array([[0,2,0],[4,5,6],[0,0,2]])
z1 = np.nonzero(z)
print(z1)
print(np.transpose(z1))
# 用在筛选功能
a = np.nonzero(z>3)
print(z[a])
print(z[z>3]) #比此要好
