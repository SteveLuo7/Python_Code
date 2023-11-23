'''
    multiple process
'''
import time
from multiprocessing import Process
from time import sleep

class ClockProcess(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval


    def run(self):
        print('子进程开始执行的时间：{}'.format(time.ctime()))
        sleep(self.interval)
        print('子进程结束的时间：{}'.format(time.ctime()))

if __name__ == "__main__":
    print("MAIN PROCESS IS ON")
    p = ClockProcess(3)
    p.start()
    p.join()
    print("MAIN PROCESS IS FINISHED")