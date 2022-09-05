import logging
import threading
import socket
import time

"""
客户端：
实现tcp网络通信，服务器端实现加减法，并将计算结果返回给客户端；
客户端给服务器端传递参数，并打印服务器端的计算结果。
"""

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s)'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class SocketMathClient:
    def __init__(self, ip_addr, port_num):
        self.addr = ip_addr, port_num
        self._sock = socket.socket()
        self._event = threading.Event()

    def start(self):
        self._sock.connect(self.addr)
        # my_addr, my_port = self._sock.getsockname()
        # self._sock.send('{} is ready'.format((my_addr, my_port)).encode())
        #msg = input()
        #encode_msg = msg
        #self.send(encode_msg)
        thread_obj = threading.Thread(target=self.recv, name='recv')
        thread_obj.start()

    def recv(self):
        while not self._event.is_set():
            try:
                data = self._sock.recv(1024)
            except Exception as e:
                logging.info('client receive error with << {} >>'.format(e))
                break
            else:
                data = data.decode()  # 汉字字符才需要解码
                if not data:
                    print('no data!!!')
                datalist = data.split('*')

                print('recieved message data[0]:', datalist[0])
                file1 = open('E:/new dachuang/daChuangWork2/data/总电压.txt', 'w')
                file1.write(datalist[0])
                file1.close()

                print('recieved message data[1]:', datalist[1])
                file2 = open('E:/new dachuang/daChuangWork2/data/总电流.txt', 'w')
                file2.write(datalist[1])
                file2.close()

                print('recieved message data[2]:', datalist[2])
                file3 = open('E:/new dachuang/daChuangWork2/data/氢槽温度.txt', 'w')
                file3.write(datalist[2])
                file3.close()

                print('recieved message data[3]:', datalist[3])
                file4 = open('E:/new dachuang/daChuangWork2/data/氧槽温度.txt', 'w')
                file4.write(datalist[3])
                file4.close()

                print('recieved message data[4]:', datalist[4])
                file5 = open('E:/new dachuang/daChuangWork2/data/碱液流量.txt', 'w')
                file5.write(datalist[4])
                file5.close()

                print('recieved message data[5]:', datalist[5])
                file6 = open('E:/new dachuang/daChuangWork2/data/碱液温度.txt', 'w')
                file6.write(datalist[5])
                file6.close()

    def send(self):
        encode_data = 'begin'.encode()
        self._sock.send(encode_data)

    def stop(self):
        client_ip, client_port = self._sock.getsockname()
        self.send('{} is quit'.format((client_ip, client_port)))
        self._sock.close()
        self._event.wait(3)
        self._event.set()
        logging.info('Client is over')


while True:
    server_ip, server_port = '127.0.0.1', 10001
    sc = SocketMathClient(server_ip, server_port)
    sc.start()
    sc.send()
    time.sleep(5)