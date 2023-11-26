'''
    receive message by using udp
'''
from socket import *
from threading import Thread

udp_socket = socket(AF_INET,SOCK_DGRAM)

udp_socket.bind(('',8989))

def recv_fun():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('>>%s:%s'%(recv_data[1],recv_data[0].decode('gb2312')))


def send_fun():
    while True:
        addr = ('192.168.2.247',8080)
        data = input('<<:')
        udp_socket.sendto(data.encode('gb2312'),addr)

if __name__ == '__main__':
    t1 = Thread(target=send_fun)
    t2 = Thread(target=recv_fun)
    t1.start()
    t2.start()
    t1.join()
    t2.join()