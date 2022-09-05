import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        data = conn.recv(1000)  # Should be ready
    except:
        print('closing 1', conn)
        sel.unregister(conn)
        conn.close()
    else:
        if data:
            print('echoing', repr(data), 'to', conn)
            conn.send(data)  # Hope it won't block
        else:
            print('closing 2', conn)
            sel.unregister(conn)
            conn.close()


sock = socket.socket()
sock.bind((socket.gethostname(), 12344))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    '''
    第一次: 会阻塞在select()这里, 
    解除阻塞: 当客户端调用connect方法时,解除阻塞,此时callback是本代码中的accept方法, 执行完之后,又阻塞在select
    第二次: 当客户端调用send发消息时, 解除阻塞, 此时callback是本代码中的read方法
    '''
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
    trigger3 = file3.read()
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

    # 将数据列表转化为字符串，然后进行编码传输。
    datastr = '*'.join(datalist)

    sel.select()
