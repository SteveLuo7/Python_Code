import threading

local = threading.local

def process_student():
    student_name = local.name
    print('Thread_name {}, Student_name {}'.format(threading.current_thread().getName(),student_name))

def process_thread(name):
    #   name binding local.name
    local.name = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread,args=('luoshibin',),name='THREAD_A')
    t2 = threading.Thread(target=process_thread,args=('zhuliping',),name='THREAD_B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()