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



# 2 Indexing
## 2.1 Basic indexing
slice,integer,ellips,np.newaxis
always view
arr[:] == x[::] -> all
arr[i:j:k,...] 不会降维auto expand
arr[i,j,k,:,np.newaxis...] 会降维
arr[:,np.newaxis]
arr[[1,2,3,..]]是将1,2,3找第一维的1,2,3行
arr[(1,2,3),] 与上面一样
arr[(1,2,3)]会对应到相应的维上
备注：会不会映射到相应的维度上，还是取一个维度上的内容

## 2.2 advanced indexing
### Purely integer
always copy
arr[arr1,arr2,arr3] --> shape(arr1)
arr[np.ix(arr_1D_0,arr_1D_1,arr_1D_2)] # 使用了broadcasting
### Boolean indexing
arr[obj] --> one dimension
arr[np.ix_(arr_bool_row,col)] # 使用了broadcasting
arr[ind_1,bool_arr,ind2] = arr[ind_1+bool_arr.nonzeros()+ind_2]
ind_1+bool_arr.nonzeros()+ind_2 -> tuple add，注意会降维也就是advace与basic的联合使用的方法

## 2.3 Generating index arrays
np.c_[arr1,arr2] --> column stack for 1-D arr, first convert to [n,1] then stack
np.r_[arr1,arr2] --> row stack, for 1-D arr, first convert to [n,1] then stack
np.s_[start:stop:step] --> slice(start,stop,step)
np.index_exp[::]-->上面一样
np.nonzero(array) --> tuple(arr1,arr2,arr3)"""
no.nonzero(bool_array) bool_array = arr>value,np.isnan(zrr)...
z1[np.nonzero(np.isnan(z1))] = value 
z1[np.isnan(z1)] = 100
np.where(condition,x,y)
np.indices(dimensions) 
np.x_(row,col) -> tuple(arr1,arr2) --> meshgrid with given indices

np.ravel_multi_index(multi_index,shape) e.g. np.ravel_multi_index([[4,5],[5,6]],(10,11))，将一个index转换成一个flatten的位置， multi_index : tuple(arr1,arr2,arr3)
np.unravel_index(indices, shape[, order]) 将一个flatten的index转换成对应的shape的index



## 2.4 indexing-like operation



# 3 manipulation
## 3.1 Changing array shape
np.reshape(a,newshape,order) == ndarray.reshape(newshape) --> copy
ndarray.reshape(newshape) --> view
np.ravel(array,order)-->view --> 返回一个扁平化的array C-order or F-order
ndarray.flatten() --> copy
ndarray.reshape(-1) --> view
ndarray.flat() --> iterator
## 3.2 Transpose like operation
np.transpose(array,[axes: eg. 1,0,2,3])--> view  改变轴的大小
## 3.3 joining arrays 可以将seq,array进行stack
np.concatenate((arr1,arr2),axis=0)-->copy # 打开括号相联，然后加[]
np.stack(arr_seqs,axis=0) --> copy # 不打开[]直接join，然后加[]
np.column_stack(1-D-arr-tuple)-->copy # 将一维或者2维按照列合并进行输出
np.hstack(tup)-->copy second_axis # 一维[1,n]，然后进行水平连接
np.vstack(tup) --> first_axis # 一维[1,n],然后进行垂直连接
## 3.4 splitting arrays
np.split(array,indices_or_sections，axis) --> copy @return list(arrays)
np.hsplit(ary,indices_or_sections)
np.vsplit(ary,indices_or_sections)


# 4 sort,search
## 4.1 sort

np.sort(arr,axis=-1)--> copy，when axis == None first flatten

np.argsort(arr,axis=-1) return the orginal indices of sorted element [3,2,1] return [2,1,0]indixces, when axis=0 sorted by column, when axis=1, sorted by row

ndarray.sort(axis=-1,kind=quicksort) in-place sort

np.msort(arr) = np.sort(arr,axis=0)

np.partition(arr,kth,axis,kind)
np.argpartition(arr,kth,axis,kind)两个与快排有关的函数


## 4.2 search
np.argmax(arr,axis=None) first flatten then return the index after fallten when axis=None, otherwise,return the index array element-wise argmax(arr([[1,2,3],[4,5,6]]),axis=0) --> arr[1,1,1]，when axis=0, select by col, when axis=1,select by row

np.argmin(arr,axis=None) # return the index occurred first time

ndarray.argmin()

ndarray.argmax() when find the index of min in flatten we can use to find the indices in original array

np.unravel_index([flatten-index],a.shape) can be converted to N-dim indices in arr a, return(a,b) or (arr1,arr2) 

np.nanargmin(arr,axis=None) neglect the nan when compare, with comparison to argmin, raise error when all is nan
np.nanargmax(arr,axis=None)


np.nonzero(a) return the indices of non-zero

np.argwhere(a) == np.transpose(np.nonzero(a)) is not suitable for indexing, so please using np.nonzero

np.flatnonzero(arr) return the indices of non-zero element in the flatten of a

np.where(condition,arr1,arr2) return the arr1-element when arr1 is True else return arr2-element when False

np.extract(condition,arr1) return the 1-D array containing the element satisfy the condition
