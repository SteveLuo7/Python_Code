
#   import queue

from multiprocessing import Queue

q = Queue(3)    #   it can setting size of queue, default is infinity
q.put('msg1')
q.put('msg2')
q.put('msg3')
#   put function have params block=True,timeout=1 if queue is full and wait for 1s , print out error

print('if queue full or not',q.full())
if not q.full():
    q.put('msg4',block=True,timeout=1)

print(q.get())
print(q.get())
print(q.get())
if not q.empty():
    print(q.get(block=True,timeout=1))

#   it can check out the queue's size
print('queue_size',q.qsize())
for i in range(q.qsize()):
    print(q.get())
