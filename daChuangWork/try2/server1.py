import logging
import string
import threading
import socket
import time


"""
服务器端：
实现tcp网络通信，服务器端实现加减法，并将计算结果返回给客户端；
客户端给服务器端传递参数，并打印服务器端的计算结果。
"""


FORMAT = "%(asctime)s %(threadName)s %(thread)d <<- %(message)s ->>"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class SocketMathServer:
    def __init__(self, ip_addr, port_num):
        self.addr = ip_addr, port_num
        self._sock = socket.socket()
        self._event = threading.Event()
        self._lock = threading.Lock()
        self.clients = {}
        # self._data = None
        self._result = None

    def start(self):   # 在主线程之外，启动一个线程接收客户端的连接请求
        self._sock.bind(self.addr)
        self._sock.listen()
        thread_obj = threading.Thread(target=self.accept, name='accept thread')   # accept方法为阻塞式方法
        thread_obj.start()

    def accept(self):   # recv方法也为阻塞式方法，在accept线程之外，启动一个线程接收客户端发送的消息
        while not self._event.is_set():
            try:
                client_sock, client_addr = self._sock.accept()
            except Exception as e:
                logging.info('quit server with {}'.format(e))
                break
            else:
                with self._lock:
                    self.clients[client_addr] = client_sock

                thread_obj = threading.Thread(target=self.recv, args=(client_sock, client_addr), name='recv thread')
                thread_obj.start()

    def recv(self, c_sock: socket.socket, c_addr: tuple):   # 用于接收客户端发送的消息
        while not self._event.is_set():
            try:
                encode_data = c_sock.recv(1024)
            except Exception as e:
                logging.info('quit the server with {}'.format(e))
                break
            else:
                data = encode_data.decode()
                logging.info(data)
                if data == 'quit' or data == 'exit' or data == '':
                    with self._lock:
                        self.clients.pop(c_addr)
                        c_sock.close()
                    logging.info('{} quit'.format(c_addr))
                    break

                if data=='begin':
                    datalist = []

                    file1 = open('E:/new dachuang/daChuangWork/server-data/总电压.txt', 'r')
                    trigger1 = file1.read()
                    print('已传递：总电压数据:'+trigger1)
                    datalist.append(trigger1)
                    file1.close()

                    file2 = open('E:/new dachuang/daChuangWork/server-data/总电流.txt', 'r')
                    trigger2 = file2.read()
                    print('已传递：总电流数据:' + trigger2)
                    datalist.append(trigger2)
                    file2.close()

                    file3 = open('E:/new dachuang/daChuangWork/server-data/氢槽温度.txt', 'r')
                    trigger3 = file3.read()
                    print('已传递：氢槽温度数据:' + trigger3)
                    datalist.append(trigger3)
                    file3.close()

                    file4 = open('E:/new dachuang/daChuangWork/server-data/氧槽温度.txt', 'r')
                    trigger4 = file4.read()
                    print('已传递：氧槽温度数据:' + trigger4)
                    datalist.append(trigger4)
                    file4.close()

                    file5 = open('E:/new dachuang/daChuangWork/server-data/碱液流量.txt', 'r')
                    trigger5 = file5.read()
                    print('已传递：碱液流量数据:' + trigger5)
                    datalist.append(trigger5)
                    file5.close()

                    file6 = open('E:/new dachuang/daChuangWork/server-data/碱液温度.txt', 'r')
                    trigger6 = file6.read()
                    print('已传递：碱液温度数据:' + trigger6)
                    datalist.append(trigger6)
                    file6.close()

                    file7 = open('E:/new dachuang/daChuangWork/server-data/1室电压.txt', 'r')
                    trigger7 = file7.read()
                    print('已传递：1室电压数据:' + trigger7)
                    datalist.append(trigger7)
                    file7.close()

                    file8 = open('E:/new dachuang/daChuangWork/server-data/2室电压.txt', 'r')
                    trigger8 = file8.read()
                    print('已传递：2室电压数据:' + trigger8)
                    datalist.append(trigger8)
                    file8.close()

                    file9 = open('E:/new dachuang/daChuangWork/server-data/3室电压.txt', 'r')
                    trigger9 = file9.read()
                    print('已传递：3室电压数据:' + trigger9)
                    datalist.append(trigger9)
                    file9.close()

                    file10 = open('E:/new dachuang/daChuangWork/server-data/4室电压.txt', 'r')
                    trigger10 = file10.read()
                    print('已传递：4室电压数据:' + trigger10)
                    datalist.append(trigger10)
                    file10.close()

                    file11 = open('E:/new dachuang/daChuangWork/server-data/5室电压.txt', 'r')
                    trigger11 = file11.read()
                    print('已传递：5室电压数据:' + trigger11)
                    datalist.append(trigger11)
                    file11.close()

                    file12 = open('E:/new dachuang/daChuangWork/server-data/6室电压.txt', 'r')
                    trigger12 = file12.read()
                    print('已传递：6室电压数据:' + trigger12)
                    datalist.append(trigger12)
                    file12.close()

                    datastr = '*'.join(datalist)
                    c_sock.send(datastr.encode())
                    time.sleep(10)

    def stop(self):
        self._event.set()
        with self._lock:
            for sock in self.clients.values():
                sock.close()
        self._sock.close()


if __name__ == '__main__':
    addr = '127.0.0.1', 10003
    s1 = SocketMathServer(*addr)
    s1.start()

