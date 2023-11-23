from multiprocessing import Process
from time import sleep

def run_test(name,age,**kwargs):
    print("子进程正在运行 name的值为:%s"%name)
    print('age:',age)
    print("dic kwargs:",kwargs)

if __name__ == '__main__':
    print("MAIN PROCESS IS ON")
    p = Process(target=run_test,args=('Luoshibin',25),kwargs={'key':7})
    p.start()
