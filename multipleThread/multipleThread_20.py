'''
    thread
'''

from threading import Thread, Lock
import time

num = 0
lock = Lock()


def test1():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print('test1 function num {}'.format(num))


def test2():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print('test2 function num {}'.format(num))


if __name__ == '__main__':
    print('MAIN PROCESS IS RUNNING')
    t1 = Thread(test1())
    t2 = Thread(test2())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('MAIN PROCESS IS FINISHED')
