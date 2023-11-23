from threading import Thread
from queue import Queue
import time

class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = 'Produce count {}'.format(count)
                    queue.put(msg)
                    print(msg)
                time.sleep(1)

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(10):
                    msg = 'Consumer Product {}'.format(queue.get())
                    print(msg)
            time.sleep(2)


if __name__ == '__main__':
    queue = Queue()
    p = Producer()
    c = Consumer()
    p.start()
    time.sleep(1)
    c.start()

