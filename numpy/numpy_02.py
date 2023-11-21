import numpy as np

a = np.array([1,2,3,4])
print(a)
print(type(a))

#   二维数组
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))

c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(type(c))

d = np.array([3,4,5],dtype=float)
print(d)
print(type(d))

e = np.array([5,6,7],dtype=float,ndmin=3)
print(e)
print(type(e))