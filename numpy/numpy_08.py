'''
    slice
'''

import numpy as np

#   create a range
x = np.arange(1,13)
a = x.reshape(4,3)
print(a)
print('Row 2:',a[1])
print(a[1][2])  #   row 2 cloumn 3
print(a[:2])    #   from start to the row 2
print(a[:,:])   #   all row



