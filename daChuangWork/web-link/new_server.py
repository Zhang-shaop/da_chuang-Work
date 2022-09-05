# -*- encoding: utf-8 -*-
import socket

IP = 'localhost'  # 服务器端可以写"localhost"，可以为空字符串""，可以为本机IP地址

#创建多个端口号，组成多个套接字，分别可以队友多台客户端。

port1 = 40001 # 端口号
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((IP, port1))
s1.listen(1)
print('listen at port :', port1)
conn1, addr1 = s1.accept()
print('connected by', addr1)

port2 = 40002
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((IP, port2))
s2.listen(1)
print('listen at port :', port2)
conn2, addr2 = s2.accept()
print('connected by', addr2)


while True:
    # 创建数据空数组
    datalist = []

    file1 = open('../data/总电压.txt', 'r')
    trigger1 = file1.read()
    datalist.append(trigger1)
    file1.close()

    file2 = open('../data/总电流.txt', 'r')
    trigger2 = file2.read()
    datalist.append(trigger2)
    file2.close()

    file3 = open('../data/氢槽温度.txt', 'r')
    trigger3= file3.read()
    datalist.append(trigger3)
    file3.close()

    file4 = open('../data/氧槽温度.txt', 'r')
    trigger4 = file4.read()
    datalist.append(trigger4)
    file4.close()

    file5 = open('../data/碱液流量.txt', 'r')
    trigger5 = file5.read()
    datalist.append(trigger5)
    file5.close()

    file6 = open('../data/碱液温度.txt', 'r')
    trigger6 = file6.read()
    datalist.append(trigger6)
    file6.close()

#将数据列表转化为字符串，然后进行编码传输。
    datastr='*'.join(datalist)

#将相同的数据发往多个客户地址。
    conn1.sendall(datastr.encode())
    conn2.sendall(datastr.encode())

#分别将套接字与连接关闭
conn1.close()
s1.close()
conn2.close()
s2.close()
