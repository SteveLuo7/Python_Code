'''
    function
'''

import numpy as np
a = np.arange(9,dtype=float).reshape(3,3)
b = np.array([10,10,10])

print(a)
print(b)

print('2 range add:',np.add(a,b))
print('=============')
print(a+b)
print('=============')
print('2range substact:',np.subtract(b,a))
print('=============')
print(b-a)


x = np.array([0,30,60,90])
print(np.sin(x))

y = np.array([1.3214234,2234.32515151,2432.3214123412])
y1 = np.around(y)
print(y1)
y2 = np.ceil(y)
print(y2)

r = np.arange(1,13).reshape(3,4)
print(a)
print('power:',np.power(a,2))
print('---------------------------------')

#   median()

a = np.arange(1,10)
print('median:',np.median(a))
print('max:',np.max(a))
print('max:',np.min(a))
print('max:',np.sum(a))


