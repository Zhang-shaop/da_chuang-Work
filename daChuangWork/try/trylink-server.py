#!/usr/bin/python3.7
# coding=utf-8
from socket import *
import threading
address='10.21.22.56'    #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12330            #监听自己的哪个端口
buffsize=1024           #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(5)     #最大连接数

def tcplink(sock,addr):
    while True:
        # 创建数据空数组
        datalist = []

        file1 = open('E:/new dachuang/daChuangWork/data/总电压.txt', 'r')
        trigger1 = file1.read()
        datalist.append(trigger1)
        file1.close()

        file2 = open('E:/new dachuang/daChuangWork/data/总电流.txt', 'r')
        trigger2 = file2.read()
        datalist.append(trigger2)
        file2.close()

        file3 = open('E:/new dachuang/daChuangWork/data/氢槽温度.txt', 'r')
        trigger3 = file3.read()
        datalist.append(trigger3)
        file3.close()

        file4 = open('E:/new dachuang/daChuangWork/data/氧槽温度.txt', 'r')
        trigger4 = file4.read()
        datalist.append(trigger4)
        file4.close()

        file5 = open('E:/new dachuang/daChuangWork/data/碱液流量.txt', 'r')
        trigger5 = file5.read()
        datalist.append(trigger5)
        file5.close()

        file6 = open('E:/new dachuang/daChuangWork/data/碱液温度.txt', 'r')
        trigger6 = file6.read()
        datalist.append(trigger6)
        file6.close()

        # 将数据列表转化为字符串，然后进行编码传输。
        datastr = '*'.join(datalist)

        clientsock.send(datastr.encode())
    clientsock.close()

while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #t为新创建的线程
    t.start()
