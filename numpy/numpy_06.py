'''
    use random
'''

import numpy as np

def zeroTest():
    a = np.zeros(5)
    print(a)

    b = np.zeros((5,),dtype=int)
    print(b)

    c = np.zeros((3,4),dtype=int)
    print(c)
zeroTest()


def onesTest():
    a = np.ones(4)
    print(a)

    b = np.ones((4,),dtype=int)
    print(b)

onesTest()

def emptyTest():
    a = np.empty(4)
    print(a)

    b = np.empty((3,4))
    print(b)

emptyTest()

def linespaceTest():
    a = np.linspace(1,10,10)
    print(a)

    b = np.linspace(10,20,5,endpoint=False)
    print(b)

linespaceTest()

def logspaceTest():
    a = np.logspace(1,20,5,base=2)
    print(a)

logspaceTest()