
#   import queue

from multiprocessing import *
from time import sleep


def write(q):
    for i in ['l','u','o']:
        print('the elements is {}'.format(i))
        q.put(i)
        sleep(1)


def read(q):
    for i in range(q.qsize()):
        print('the reading elements {}'.format(q.get()))
        sleep(1)

if __name__ == '__main__':
    print('MAIN PROCESS IS RUNNING')
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write,(q,))
    pool.apply(read,(q,))
    pool.close
    pool.join

    print('MAIN PROGRESS IS FINISHED')
