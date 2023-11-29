
'''the special use of closure'''
import time


def writeLog(func):
    try:
        file = open('writeLog.txt','a',encoding='utf-8')
        file.write('visit: ')
        file.write(func.__name__)
        file.write('\t')
        file.write(
            'TIME: '
        )
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()

def fun1():
    writeLog(fun1)
    print('Function-1')


def fun2():
    writeLog(fun2)
    print('Function-2')



fun1()
fun2()
