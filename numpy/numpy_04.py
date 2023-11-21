'''
    use random
'''

import numpy as np

#   create range by random
a = np.random.random(size=5)
print(a)
print(type(a))

b = np.random.random(size=(3,4))
print(b)

c = np.random.random(size=(2,3,4))
print(c)
print(type(c))

def randomintTest():
    #   creaete 0-5 random integer
    a = np.random.randint(6,size=10)
    print(a)
    print(type(a))

    b = np.random.randint(5,11,size=(4,3))
    print(b)

    c = np.random.randint(10,16,size=(2,4,3))
    print(c)

    d = np.random.randint(10,size=5)
    print(d)
    print("Default dtype",d.dtype)


randomintTest()
print('=============================================================================================')

#   create rand by random()
def randTest():
    a = np.random.randn(4)
    print(a)

    b = np.random.randn(2,3)
    print(b)

    c = np.random.randn(2,3,4)
    print(c)


randTest()

#   create rand by rand.normal()
print('==============================================================================================================')
def normalTest():
    a = np.random.normal(size=5)    #   default loc = 0.0 scale = 1.0
    print(a)
    print(type(a))
    #   setting loc and scale
    b = np.random.normal(loc=2,scale=3,size=(3,4))
    print(b)


normalTest()