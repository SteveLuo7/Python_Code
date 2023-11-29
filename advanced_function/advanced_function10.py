'''decorator'''
import time


def fun1():
    print('FUNCTION-1')

def fun2():
    print('FUNCION-2')

def writeLog(func):
    try:
        file=open('log.txt','a',encoding='utf-8')
        file.write('VISIT: ')
        file.write(func,__name__)
        file.write('\t')
        file.write('TIME: ')
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()

def funcOut(func):
    def funcIn():
        writeLog(func)
        func()
    return funcIn
funcOut(fun1)
