import numpy as np

""" 1 np.concatenate((arr1,arr2),axis=0)-->copy """
z = np.arange(6).reshape(2, 3)
z2 = np.arange(6, 12).reshape(2, 3)
z3 = np.concatenate((z, z2), axis=1)  # 连接元素时合并的
z4 = np.stack((z, z2), axis=2)  # 连接元素是分开的
print(z3)
print(z4)
