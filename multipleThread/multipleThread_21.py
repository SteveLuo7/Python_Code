from threading import Thread,Lock
import time

#   create 3 lock
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()

#   acquire lock2 and 3
lock2.acquire()
lock3.acquire()

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('task1 is on...')
                time.sleep(1)
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('task2 is on .....')
                time.sleep(1)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('task3 is on.....')
                time.sleep(1)
                lock1.release()


if __name__ == '__main__':
    print('MAIN PROCESS IS RUNNING...')
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()

    t1.start()
    t2.start()
    t3.start()
