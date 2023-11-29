import time

def funOut(func):
    def funIn(*args,**kwargs):
        writeLog(func)
        return func(*args,**kwargs)
    return funIn

def writeLog(func):
    print('VISIT FUNC_NAME: ',func.__name__,'\tTIME: ',time.asctime())
@funOut
def sum(a,b):
    return a+b

@funOut
def add(a,b,c):
    return a+b+c

result = sum(10,20)
print(result)
result = add(10,20,30)
print(result)