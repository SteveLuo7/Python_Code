'''
    split
'''

import numpy as np

a = np.arange(1,13)
#   use split func
a1 = np.split(a,4)
print(a1)

a2 = np.split(a,[4,6])
print(a2)
print('==============================')


b = np.arange(1,13).reshape(3,4)
print(b)
print('==============================')

r,w = np.split(b,2,axis=1)
print(r)
print(w)
print('==============================')

# x,y,z = np.split()
