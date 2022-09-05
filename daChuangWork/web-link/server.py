# -*- encoding: utf-8 -*-

import socket
import sys
IP = '10.21.20.155'    #填写服务器端的IP地址!!!\客户端的ip
port = 40002 #端口号必须一致!!!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((IP,port))
    print('have found server')
except Exception as e:
    print('server not find or not open')
    sys.exit()



while True:
    file1=open('../data/总电流.txt', 'r')
    trigger = file1.read()
    s.sendall(trigger.encode())
    data = s.recv(1024)
    data = data.decode()
    print('recieved:',data)
    if trigger.lower() == '1':#发送1结束连接
        break




s.close()