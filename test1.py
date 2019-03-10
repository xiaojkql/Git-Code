import numpy as np

""" 1 np.concatenate((arr1,arr2),axis=0)-->copy """
z = np.arange(6).reshape(2, 3)
z2 = np.arange(6, 12).reshape(2, 3)
z3 = np.concatenate((z, z2), axis=1)  # 连接元素时合并的
z4 = np.stack((z, z2), axis=2)  # 连接元素是分开的
# print(z3[1][1].size)
# print(z4)

z = np.array([1, 2, 3])
# print(np.geterr())
z1 = np.array([1, 2, 3])
z2 = np.array([4, 5, 5])
print((np.logical_or(z1, z2)))
print((z1 > 0) & (z2 > 1))
print(max(z1))
