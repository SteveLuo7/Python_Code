'''
    slice
'''

import numpy as np

#   create a range
a = np.arange(10)
print(a)

print('索引0处元素:',a[0])
print('索引5处元素:',a[5])
print('索引倒数第一处元素:',a[-1])
print('索引倒数第三处元素:',a[-3])

print(a[:])     #   from start to the end
print(a[3:])    #   from 3 to the end
print(a[3:5])   #   from 3 to the 4
print(a[3:10:2])   #   from 3 to the 9 and step = 2
