'''
    multiple process
'''
import time
from multiprocessing import Process
from time import sleep

def work1(interval):
    print('work1 is ON')
    sleep(interval)
    print('work1 is finished')
def work2(interval):
    print('work2 is ON')
    sleep(interval)
    print('work2 is finished')
def work3(interval):
    print('work3 is ON')
    sleep(interval)
    print('work3 is finished')


if __name__ == "__main__":
    print("MAIN PROCESS IS ON")
    p1 = Process(target=work1,args=(4,))
    p2 = Process(target=work2,args=(2,))
    p3= Process(target=work3,args=(3,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('p1.name:',p1.name)
    print('p2.name:',p2.name)
    print('p3.name:',p3.name)
    print("MAIN PROCESS IS FINISHED")