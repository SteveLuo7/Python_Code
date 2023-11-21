'''
    use random
'''

import numpy as np

#   create array
a = np.array([1,2,3,4])
print(a)
print(type(a))

b = np.arange(4,10)
print(b)

c = np.random.randint(4,10,size=(2,3))
print(c)

d = list(range(10))
print(d)
print(type(d))

e = np.random.randn(2,3,4)
print(e)


print("ndim:",a.ndim,b.ndim,c.ndim,e.ndim)

print("shape:",a.shape,b.shape,c.shape,e.shape)

print("dtype:",a.dtype,b.dtype,c.dtype,e.dtype)

print("itemsize:",a.itemsize,b.itemsize,c.itemsize,e.itemsize)
