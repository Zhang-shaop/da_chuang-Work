# -*- encoding: utf-8 -*-
import socket

IP = "10.16.65.183"  # 服务器端可以写"localhost"，可以为空字符串""，可以为本机IP地址
port = 40005  # 端口号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, port))
s.listen(1)
print('listen at port :', port)
conn, addr = s.accept()
print('connected by', addr)


while True:
    data = conn.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data)
    file1 = open('总电压.txt', 'w')
    file1.write(data)
    send = 'ok'  # python27要写raw_input,python3.X可写input
    conn.sendall(send.encode())  # 再编码发送

conn.close()
s.close()