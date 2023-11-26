'''
    send message by udp
'''

from socket import socket,AF_INET,SOCK_DGRAM
#   create UDP
udp_socket = socket(AF_INET,SOCK_DGRAM)

#   create information address
addr = ('192.168.2.247',8080)
data = input(
    'please send your message'
)

#   USE sendto() function to send message   gb2312
udp_socket.sendto(data.encode('gb2312'),addr)
#   close UDP
udp_socket.close()
