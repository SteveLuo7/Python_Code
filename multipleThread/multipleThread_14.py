'''
    thread
'''

import _thread

import time
def fun1():
    print("fun1 is running")
    time.sleep(4)
    print('fun1 is finished')
def fun2():
    print("fun2 is running")
    time.sleep(2)
    print('fun2 is finished')


if __name__ == '__main__':
    print('MAIN PROCESS IS RUNING')
    _thread.start_new_thread(fun1,())
    _thread.start_new_thread(fun2,())
    time.sleep(7)
    print('MAIN PROCESS IS FINISHED')