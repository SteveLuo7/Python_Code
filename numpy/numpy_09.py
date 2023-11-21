'''
    copy range
'''

import numpy as np

#   create a range
a = np.arange(1,13).reshape(3,4)
print(a)

sub_a = a[:2,:2]
print(sub_a)

sub_a[0][0] = 100
print(sub_a)

sub_aa = np.copy(a[:2,:2])
print(sub_aa)
sub_aa[0][0] = 200
print(sub_aa)