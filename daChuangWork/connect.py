# -*- encoding: utf-8 -*-

import socket
import sys
IP = '10.16.65.183' #填写服务器端的IP地址
port = 40005 #端口号必须一致
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((IP,port))
except Exception as e:
    print('server not find or not open')
    sys.exit()
while True:
    trigger = input("send:")
    s.sendall(trigger.encode())
    data = s.recv(1024)
    data = data.decode()
    print('recieved:',data)
    if trigger.lower() == '1':#发送1结束连接
        break
s.close()