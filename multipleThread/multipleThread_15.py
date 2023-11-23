'''
    thread
'''

import _thread

import time
def fun1(thread_name,delay):
    print("fun1 is running,name: {}".format(thread_name))
    time.sleep(delay)
    print('fun1 is finished')
def fun2(thread_name,delay):
    print("fun2 is running,threadname: {}".format(thread_name))
    time.sleep(delay)
    print('fun2 is finished')


if __name__ == '__main__':
    print('MAIN PROCESS IS RUNING')
    _thread.start_new_thread(fun1,('therad-1',3))
    _thread.start_new_thread(fun2,('thread-2',4))
    time.sleep(7)
    print('MAIN PROCESS IS FINISHED')