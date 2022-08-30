import socket
import sys
IP = '10.16.65.183'    #填写服务器端的IP地址!!!
port = 40005 #端口号必须一致!!!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#判断是否连接成功
try:
    s.connect((IP,port))
except Exception as e:
    print('server not find or not open')
    sys.exit()

while True:
    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[0])
    file1 = open('总电压.txt', 'w')
    file1.write(data[0])
    file1.close()

    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[1])
    file2 = open('总电流.txt', 'w')
    file2.write(data[1])
    file2.close()

    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[2])
    file3 = open('氢槽温度.txt', 'w')
    file3.write(data[2])
    file3.close()

    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[3])
    file4 = open('氧槽温度.txt', 'w')
    file4.write(data[3])
    file4.close()

s.close()
'''
    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[5])
    file5 = open('碱液流量', 'w')
    file5.write(data[5])
    send = '碱液流量ok'  # python27要写raw_input,python3.X可写input
    s.sendall(send.encode())  # 再编码发送

    data = s.recv(1024)
    data = data.decode()  # 解码
    if not data:
        break
    print('recieved message:', data[6])
    file6 = open('碱液温度.txt', 'w')
    file6.write(data[6])
    file6.close()
    send = '碱液温度ok'  # python27要写raw_input,python3.X可写input
    s.sendall(send.encode())  # 再编码发送
'''
