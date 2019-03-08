# 1 change array shape

import numpy as np
""" 1 np.reshape(a,newshape,order) == ndarray.reshape(newshape) --> 返回一个新的array """
z = np.arange(0, 10)
a = z.reshape(5, 2)  # 返回的是view
a[1, 1] = 100
# print(a)
# print(z)
z = np.arange(0, 10)
a = np.reshape(z, (5, 2))  # 返回的是复制
a[1, 1] = 100
print(a)
print(z)

""" 2 np.ravel(array,order)-->view --> 返回一个扁平化的array C-order or F-order"""
""" ndarray.flatten() --> copy """
""" ndarray.reshape(-1) --> view """
""" ndarray.flat() --> iterator """
z = np.arange(0, 10).reshape(2, 5)
a = np.ravel(z)  # 返回的是view
print(a)
z[1] = 100
print(a)
z = np.arange(0, 10).reshape(2, 5)
a = z.flatten()  # 返回的是复制
z[1] = 100
print(a)
print(z)


# 2 transpose
""" 1 np.transpose(array,[axes: eg. 1,0,2,3])--> view  改变轴的大小"""
z = np.arange(0, 10).reshape(2, 5)
a = z.transpose()  # 返回view
z[1, 2] = 200
print(a)

# 3 joining arrays
# sequence_arrays --> tuple,list
""" 1 np.concatenate((arr1,arr2),axis=0)-->copy """
z = np.arange(6).reshape(2, 3)
z2 = np.arange(3).reshape(1, 3)
z3 = np.concatenate((z, z2))
z[1, 1] = 102
print(z3)

# 上面要在所在axis先打开括号，连接后加括号
# 下面不打开括号直接先联，然后也加括号
""" 2 np.stack(arr_seqs,axis=0) --> copy """
# 看时看成一个[[[1],[2],[3]]]进行解释
z = np.array([[1, 2], [3, 4]])
z1 = np.copy(z)
z2 = np.copy(z)
z3 = np.stack((z, z1, z2), axis=2)
z2[1, 1] = 100
print(z3)

""" 3 np.column_stack(1-D-arr-tuple)-->copy """
# 将一维或者2维按照列合并进行输出
z = np.arange(6)
z1 = np.arange(6, 12)
z3 = np.column_stack((z, z1))
print(z3)
z = np.array([[1, 2], [3, 4]])
z1 = np.copy(z)
z3 = np.column_stack((z, z1))
print(z3)

""" 4 np.hstack(tup)-->copy second_axis"""
# 输入一系列一维向量时，按照一维进行合拼 [n,1]
# 输入一系列二维矩阵时，按照第二维进行合并
# 可以将多个 --> contenate的特殊形式
z = np.arange(6)
z1 = np.arange(6, 13)
z2 = np.hstack((z, z1))
print(z2)
z = np.array([[1, 2], [3, 4]])
z1 = np.copy(z)
z2 = np.hstack((z, z1))
print(z2)

""" 5 np.vstack(tup) --> first_axis"""
# 所有arrays必须在除了first_axis的其他轴相等，
# array-->是1维时，看成2维[1,N]
z = np.arange(6)
z1 = np.random.random((4, 6))
z2 = np.vstack((z, z1))
print(z2)


# 4 splitting arrays
""" 1 np.split(array,indices_or_sections) --> copy @return list(arrays) """
# indices_or_sections 为int时 会按照axis分成N分如果不可以将报错
# indices_or_sections 为1-Darray时 将会按照给定的位置进行划分，没有时返回空
# axis --> 指定轴
z = np.random.random((7, 8))
z = np.split(z, indices_or_sections=[1, 5, 2], axis=0)
print(z)


""" 2 np.hsplit(ary,inces_or_sections) """
# 按照columns进行划分
z = np.random.random((2, 8))
z = np.hsplit(z, indices_or_sections=4)
print(z)


""" 3 np.vsplit(ary,indices_or_sections) """
# 按照行进行划分
z = np.random.random((2, 8))
z = np.vsplit(z, indices_or_sections=2)
print(z)


# Tiling arrays --> 重复数组形成新的数组
""" 1 np.tile(A,repos) """
# 当模型不匹配时会进行匹配
z = np.arange(12).reshape(3, 4)
z = np.tile(z, [2])
print(z)

""" 2 np.repeat(A,repeats,axis) """


# Adding and removing elements
""" 1 np.delete(arr,obj=(int or slice or arrayofints),axis=None) """
# obj 指定要删除的行或者多个行
# axis 指定要删除的所在轴,如果没有指定，则是flatten后再进行删除
z = np.random.random((7, 8))
z = np.delete(z, obj=slice(2, 5), axis=0)
print(z)

""" 2 np.insert(arr,obj,values,axis=None) """
# 未指出axis将按照flatten后进行插入
# obj Int,slice,or sequenceofint 指出要插入的位置
# values 指出要从插入的值，可以是单个值，可以是一个序列
# 在二维数组上插入上指定axis,在一维数组上操作无需指定轴即可

""" 3 np.append(arr,values,axis=None) --> copy"""
# axis=None,未指定时，会将arr进行flatten，然后再进行扩张
# values 指定要进行插入的数组，除了指定轴外，其他一定要一样的shape
z = np.random.random((1, 2))
z1 = np.random.random((3, 2))
print(np.append(z, z1))

""" 4 np.resize(a,new_shape)-->copy """
# 如果new_shape的dim大于a的dim那么将会剩余的复制a的元素进行填充
# 而ndarray.resize(new_shape)则会将不够的填充为零


""" 5 np.trim_zeros(filt,trim='fb') """
# 'fb' 去除前面的零，还是后面的零
# 针对的是一维数组

""" 6 np.unique(ar,) """


""" Rearranging elements """
""" 1 flip """
""" 2 np.fliplr """
""" 3 np.flipud """
""" 4 np.roll """
""" 5 np.rot90 """
