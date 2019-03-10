import numpy as np

a = np.arange(6).reshape(2, 3)[::-1]
b = np.sort(a, axis=0)
b[0, 0] = 100
print(a)
print(b)

z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.stack(z))
print(z[(1,2),])
