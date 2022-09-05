
# !/usr/bin/python
# coding: utf-8
from ftplib import FTP
import time
import tarfile

from ftplib import FTP

host='10.21.22.56'
port=12344
def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, port)  # 连接
    ftp.login()  # 登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024  # 设置缓冲块大小
    fp = open(localpath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR'+remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()  # 关闭文件


if __name__ == "__main__":
    ftp = ftpconnect(host,None,None)
    downloadfile(ftp, "E:/new dachuang/daChuangWork/try/voltage.txt", "E:/new dachuang/daChuangWork/try/总电压new.txt")

    ftp.quit()
