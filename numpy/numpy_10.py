'''
    copy range
'''

import numpy as np

a = np.arange(1,25)
print(a)
print('============================================================')
b = a.reshape(3,8)
print(b)
print('============================================================')
c = a.reshape(2,3,4)
print(c)
print('============================================================')

#   use np.reshape

x = np.reshape(a,(4,3,2))
print(x)
print('============================================================')

y = np.reshape(a,(4,6))
print(y)
y1 = y.reshape(24)
print(y1)
