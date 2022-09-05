
import socket
import sys
IP = 'localhost'   #填写服务器端的IP地址!!!
port = 40002 #端口号必须一致!!!
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#判断是否连接成功
try:
    s.connect((IP,port))
    print('have found socket')
except Exception as e:
    print('server not find or not open')

#while True:
data = s.recv(1024)
data = data.decode()  # 汉字字符才需要解码
if not data:
   # break
   print('no data!!!')
datalist = data.split('*')

print('recieved message data[0]:', datalist[0])
file1 = open('../data/总电压.txt', 'w')
file1.write(datalist[0])
file1.close()

print('recieved message data[1]:', datalist[1])
file2 = open('../data/总电流.txt', 'w')
file2.write(datalist[1])
file2.close()

print('recieved message data[2]:', datalist[2])
file3 = open('../data/氢槽温度.txt', 'w')
file3.write(datalist[2])
file3.close()


print('recieved message data[3]:', datalist[3])
file4 = open('../data/氧槽温度.txt', 'w')
file4.write(datalist[3])
file4.close()

print('recieved message data[4]:', datalist[4])
file5 = open('../data/碱液流量.txt', 'w')
file5.write(datalist[4])
file5.close()


print('recieved message data[5]:', datalist[5])
file6 = open('../data/碱液温度.txt', 'w')
file6.write(datalist[5])
file6.close()

s.close()