'''
    receive message by using udp
'''
from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)
#   bind a port
udp_socket.bind(('',8989))
#   send message
data = input('plesae send your message')
#   input address
addr = ('192.168.2.247',8080)

udp_socket.sendto(data.encode('gb2312'),addr)
#   this connection can transfer 1024 byte max
recv_data = udp_socket.recvfrom(1024)
print('the message%s receive %s'%(recv_data[1],recv_data[0].decode('gb2312')))
#   close the udp socket
udp_socket.close()