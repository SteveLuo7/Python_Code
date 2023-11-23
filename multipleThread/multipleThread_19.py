'''
    thread
'''

import threading
import time

num = 0
def test1():
    global num
    for i in range(1000000):
        num += 1
    print('test1 func num {}'.format(num))

def test2():
    global num
    for i in range(1000000):
        num += 1
    print('test2 fun num {}'.format(num))

if __name__ == '__main__':
    print('MAIN PROCESS IS RUNNING')
    t1 = threading.Thread(test1())
    t2 = threading.Thread(test2())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('MAIN PROCESS IS FINISHED')