'''
    concatenate
'''

import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(5,11).reshape(2,3)
print(a)
print(b)
print('===========================')

#   use hstack
r = np.hstack((a,b))
print(r)
print('=========================')
p = np.vstack((a,b))
print(p)
print('=========================')

x = np.concatenate((a,b),axis=1)
x1 = np.concatenate((a,b))
print(x)
print('=========================')
print(x1)
