'''
    thread
'''

import threading
import time

def fun1(delay):
    print('THREAD {} is running'.format(threading.current_thread().name))
    time.sleep(delay)
    print('THREAD {} is finished'.format(threading.current_thread().name))
def fun2(delay):
    print('THREAD {} is running'.format(threading.current_thread().name))
    time.sleep(delay)
    print('THREAD {} is finished'.format(threading.current_thread().name))

class MyThread(threading.Thread):
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)

    def run(self):
        self._target(*self._args)

if __name__ == "__main__":
    print('PROCESS IS RUNING ')
    t1 = MyThread(fun1,'THREAD_1',(3,))
    t2 = MyThread(fun2,'THREAD_2',(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('PROCESS IS FINISHED')
