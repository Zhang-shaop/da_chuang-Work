import sys
import random
import numpy as np
from time import sleep
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WorkThread(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread, self).__init__()
    #线程运行函数
    def run(self):
        while True:
            global T_value
            global P_value
            T_value = random.randint(200,225)
            P_value = random.randint(150,200)
            print(T_value, P_value)
            sleep(3)

class plotwindows(QtWidgets.QWidget):
    def __init__(self):
        super(plotwindows,self).__init__()
        layout = QFormLayout()
        self.edita3 = QLineEdit()
        self.edita4 = QLineEdit()
        self.edita5 = QLineEdit()
        layout.addRow("A数值", self.edita3)
        layout.addRow("B数值", self.edita4)
        layout.addRow("C数值", self.edita5)
        self.setLayout(layout)
        self.Mytimer()

    def Mytimer(self):
      timer = QTimer(self)
      timer.timeout.connect(self.update)
      timer.start(100)

    def update(self):
      self.edita3.setText(str(T_value))
      self.edita4.setText(str(P_value))
      global SUM_value
      SUM_value = T_value + P_value
      self.edita5.setText(str(SUM_value))

def mainwindows():
    app =QtWidgets.QApplication(sys.argv)
    new = plotwindows()
    new.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    workThread = WorkThread()
    workThread.start()
    mainwindows()
