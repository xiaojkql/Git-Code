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
# print((np.logical_or(z1, z2)))
# print((z1 > 0) & (z2 > 1))
# print(max(z1))
z2 = np.arange(27).reshape(3, 3, 3)
z1 = np.array([1, 2, 3])
print(z1)
z2 = z1[:, np.newaxis]
print(z2)
z2[1, 0] = 100
print(z1)

z1 = np.array([[[1], [2]]])
print(z1.shape)

z2 = np.arange(27).reshape(3, 3, 3)
print(z2[z2 > 3])
z3 = z2[z2 > 3]
z3[1] = 100
print(z3)
z1 = np.arange(9).reshape(3, 3)
z2 = np.arange(27).reshape(3, 3, 3)
print(z2[z1 > 4, :])

z1 = np.array([[1, 2, 3], [np.nan, 1, np.nan]])
print(np.nonzero(np.isnan(z1)))
print(np.isnan(z1))

z1[np.isnan(z1)] = 100
print(z1)

z = np.arange(6)
z1 = np.arange(6, 13)
z2 = np.hstack((z, z1))
print(z2)

z = np.arange(6)
z1 = np.random.random((4, 6))
z2 = np.vstack((z, z1))
print(z2)
