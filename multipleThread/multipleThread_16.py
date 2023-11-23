'''
    thread
'''

import threading
import time

def fun1(thread_name,delay):
    print('my name is luoshibin, thread_name {}'.format(thread_name))
    time.sleep(delay)
    print('{} is finished'.format(thread_name))


def fun2(thread_name,delay):
    print('my wifes name is zhuliping thread_name {}'.format(thread_name))
    time.sleep(delay)
    print('{} is finished'.format(thread_name))


if __name__ == "__main__":
    print('MAIN PROCESS IS RUNING')
    t1 = threading.Thread(target=fun1,args=('Thread-Luo',3))
    t2 = threading.Thread(target=fun2,args=('Thread-Zhu',3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('MAIN PROCESS IS FINISHED')

