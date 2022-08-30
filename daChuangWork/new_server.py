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
datalist=[]

while True:
    file1 = open('总电压.txt', 'r')
    trigger1 = float(file1.read())
    datalist.append(trigger1)
    file1.close()

    file2 = open('总电流.txt', 'r')
    trigger2 = float(file2.read())
    datalist.append(trigger2)
    file2.close()

    file3 = open('氢槽温度.txt', 'r')
    trigger3= float(file3.read())
    datalist.append(trigger3)
    file3.close()

    file4 = open('氧槽温度.txt', 'r')
    trigger4 = float(file4.read())
    datalist.append(trigger4)
    file4.close()

    conn.sendall(datalist.encode())
conn.close()
s.close()

'''
    conn.sendall(trigger1.encode())
    data1 = s.recv(1024)
    data1 = data1.decode()
    print('recieved:', data1)

    file2 = open('总电流.txt', 'r')
    trigger2 = file2.read()
    file2.close()
    conn.sendall(trigger2.encode())
    data2 = s.recv(1024)
    data2 = data1.decode()
    print('recieved:', data2)

    file3 = open('氢槽温度.txt', 'r')
    trigger3 = file3.read()
    file3.close()
    conn.sendall(trigger3.encode())
    data3 = s.recv(1024)
    data3 = data3.decode()
    print('recieved:', data3)

    file4 = open('氧槽温度.txt', 'r')
    trigger4 = file4.read()
    file4.close()
    conn.sendall(trigger4.encode())
    data4 = s.recv(1024)
    data4 = data1.decode()
    print('recieved:', data4)

    file5 = open('碱液流量.txt', 'r')
    trigger5 = file5.read()
    file5.close()
    conn.sendall(trigger5.encode())
    data5 = s.recv(1024)
    data5 = data5.decode()
    print('recieved:', data5)

    file6 = open('碱液温度.txt', 'r')
    trigger6 = file6.read()
    file6.close()
    conn.sendall(trigger6.encode())
    data6 = s.recv(1024)
    data6 = data6.decode()
    print('recieved:', data6)
'''
