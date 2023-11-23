'''
    multiple process
'''
import multiprocessing
import time
from multiprocessing import Process
from time import sleep
num = 10
def work1():
    global num
    num += 5
    print('num{} when son process work1 is running'.format(num))
def work2():
    global num
    num += 10
    print('num{} when son process work2 is running'.format(num))


if __name__ == '__main__':
    print('MAIN PROGREESS IS RUNNING')
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('global var num{}'.format(num))