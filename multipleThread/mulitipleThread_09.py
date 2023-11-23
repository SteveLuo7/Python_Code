'''
    multiple process
'''
import multiprocessing
import time
from multiprocessing import Process
from time import sleep

def func(msg):
    print('start:',msg)
    sleep(3)
    print('end',msg)

if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(1,6):
        msg = 'PROCESS{}'.format(i)
        pool.apply_async(func,(msg,))

    pool.close()
    pool.join()