import time


def writeLog(fun):
    print('VISIT: ',fun.__name__,'\tTIME: ',time.asctime())

def funOut(fun):
    def funIn(x,y):
        writeLog(fun)
        return fun(x,y)
    return funIn

def funOut2(fun):
    def funIn(x,y,z):
        writeLog(fun)
        return fun(x,y,z)
    return funIn



@funOut
def sum(a,b):
    return a + b

@funOut2
def total(a,b,c):
    return a * b * c


result = sum(10,20)
print('TOTAL: ',result)

sum2 = total(1,3,5)
print('function-2_TOTAL: ',sum2)