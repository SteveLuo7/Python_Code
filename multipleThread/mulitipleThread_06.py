'''
    timeout
'''
import time
from multiprocessing import Process
from time import sleep

def clock(interval):
    for i in range(3):
        print('TIME NOW:{}'.format(time.ctime()))
        time.sleep(interval)

if __name__ == '__main__':
    print('MAIN PROCESS IS ON')
    p = Process(target=clock,args=(5,))
    p.start()
    p.join()
    print('p.pid:',p.pid)
    print('p.name',p.name)
    print('p.is_alive',p.is_alive())
    print('MAIN PROCESS IS FINISHED')
