'''
    TCP Coding
    more reliable
'''
from socket import *
#   create socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#   binding server socket port
serverSocket.bind(('',8989))
#   listen
serverSocket.listen()
#   receive client connection
client_socket,client_info = serverSocket.accept()
#   receive clients message
recv_data = client_socket.recv(1024)

print('the message receive from%s -- %s'%(client_info,recv_data.decode('gb2312')))

client_socket.close()
serverSocket.close()

