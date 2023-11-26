import struct
from socket import *
filename = 'face.jpg'
server_ip = '127.0.0.1'
send_data = struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'octet'.encode(),0)
s = socket(AF_INET,SOCK_DGRAM)
s.sendto(send_data,(server_ip,69))
f = open(filename,'ab')
while True:
    recv_data = s.recvfrom(1024)
    caozuoma,ack_num = struct.unpack('!HH',recv_data[0][:4])
    rand_port = recv_data[1][1]

    if int(caozuoma) == 5:
        print('File is no exist...')
        break

    f.write(recv_data[0][:4])
    if len(recv_data[0]) < 516:
        break

    ack_data = struct.pack("!HH",4,ack_num)
    s.sendto(ack_data,(server_ip,rand_port))

