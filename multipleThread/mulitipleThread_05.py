'''
    timeout
'''

from multiprocessing import Process
from time import sleep

def woker(interval):
    print('work start')
    sleep(interval)
    print('work finished')

if __name__ == '__main__':
    print('MAIN PROCESS IS ON')
    p = Process(target=woker,args=(5,))
    p.start()
    # sleep(4)
    #   use join() Main Process wait untill son process finished
    p.join(3)
    print('MAIN PROCESS IS FINISHED')