'''
    create list by range
'''

import numpy as np

a = list(range(1,10))
print(a)

b = list(range(10))
print(b)    #   default from 0 step = 1

c = list(range(1,10,3))
print(c)    #   step = 3


#   create range by arange
d = np.arange(1,11)
print(d)

#   setting step = 3
e = np.arange(1,11,2)
print(e)

f = np.arange(10,20,2,dtype=float)
print(f)