import numpy as np

#   new array
a = np.arange(10)
print(a)

print(type(a))

#   square the elements in list
import math
b = [3,4,9]
#   save in a list
result = []
for i in b:
    result.append(math.sqrt(i))

print(result)

print(np.sqrt(a))