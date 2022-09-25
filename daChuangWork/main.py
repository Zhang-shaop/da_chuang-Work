#引入对应文件中的类
from daChuangWork import *
from win1 import *

#引入对应的库
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import PyQt5.QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import math
from PyQt5.Qt import *
import sys
import socket
import try_canvas1

#进入主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)

#菜单界面
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

#显示主菜单界面
    MainWindow.show()

# 1室电压
    MainWindow1 = QMainWindow()
    ui1 = Ui_Form()
    ui1.setupUi(MainWindow1)
    ui1.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui1.pushButton.clicked.connect(partial(MainWindow1.close, ))

# 2室电压
    MainWindow2 = QMainWindow()
    ui2 = Ui_Form2()
    ui2.setupUi(MainWindow2)
    ui2.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui2.pushButton.clicked.connect(partial(MainWindow2.close, ))

# 3室电压
    MainWindow3 = QMainWindow()
    ui3 = Ui_Form3()
    ui3.setupUi(MainWindow3)
    ui3.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui3.pushButton.clicked.connect(partial(MainWindow3.close, ))

# 4室电压
    MainWindow4 = QMainWindow()
    ui4 = Ui_Form4()
    ui4.setupUi(MainWindow4)
    ui4.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui4.pushButton.clicked.connect(partial(MainWindow4.close, ))

 # 5室电压
    MainWindow5 = QMainWindow()
    ui5 = Ui_Form5()
    ui5.setupUi(MainWindow5)
    ui5.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui5.pushButton.clicked.connect(partial(MainWindow5.close, ))

 # 6室电压
    MainWindow6= QMainWindow()
    ui6 = Ui_Form6()
    ui6.setupUi(MainWindow6)
    ui6.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui6.pushButton.clicked.connect(partial(MainWindow6.close, ))

 # 总电压
    MainWindow7 = QMainWindow()
    ui7 = Ui_Form7()
    ui7.setupUi(MainWindow7)
    ui7.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui7.pushButton.clicked.connect(partial(MainWindow7.close, ))

# 总电流
    MainWindow8 = QMainWindow()
    ui8 = Ui_Form8()
    ui8.setupUi(MainWindow8)
    ui8.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui8.pushButton.clicked.connect(partial(MainWindow8.close, ))

    MainWindow9 = QMainWindow()
    ui9 = Ui_Form9()
    ui9.setupUi(MainWindow9)
    ui9.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui9.pushButton.clicked.connect(partial(MainWindow9.close, ))

    MainWindow10 = QMainWindow()
    ui10 = Ui_Form10()
    ui10.setupUi(MainWindow10)
    ui10.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui10.pushButton.clicked.connect(partial(MainWindow10.close, ))

    MainWindow11 = QMainWindow()
    ui11 = Ui_Form11()
    ui11.setupUi(MainWindow11)
    ui11.pushButton.clicked.connect(partial(MainWindow.show, ))
    ui11.pushButton.clicked.connect(partial(MainWindow11.close, ))

    MainWindow12 = QtWidgets.QMainWindow()  #####
    ex = try_canvas1.Ui_MainWindow()
    ex.setupUi(MainWindow12)
    ex.pushButton.clicked.connect(partial(MainWindow.show, ))
    ex.pushButton.clicked.connect(partial(MainWindow12.close, ))

    #主菜单的槽与信号
    ui.pushButton.clicked.connect(partial(MainWindow1.show, ))
    ui.pushButton.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_2.clicked.connect(partial(MainWindow2.show, ))
    ui.pushButton_2.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_3.clicked.connect(partial(MainWindow3.show, ))
    ui.pushButton_3.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_4.clicked.connect(partial(MainWindow4.show, ))
    ui.pushButton_4.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_5.clicked.connect(partial(MainWindow5.show, ))
    ui.pushButton_5.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_6.clicked.connect(partial(MainWindow6.show, ))
    ui.pushButton_6.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_7.clicked.connect(partial(MainWindow7.show, ))
    ui.pushButton_7.clicked.connect(partial(MainWindow.close, ))
    ui.pushButton_8.clicked.connect(partial(MainWindow8.show, ))
    ui.pushButton_8.clicked.connect(partial(MainWindow.close, ))

    ui.action1shi.triggered.connect(partial(MainWindow1.show, ))
    ui.action1shi.triggered.connect(partial(MainWindow.close, ))
    ui.action2shi.triggered.connect(partial(MainWindow2.show, ))
    ui.action2shi.triggered.connect(partial(MainWindow.close, ))
    ui.action3shi.triggered.connect(partial(MainWindow3.show, ))
    ui.action3shi.triggered.connect(partial(MainWindow.close, ))
    ui.action4shi.triggered.connect(partial(MainWindow4.show, ))
    ui.action4shi.triggered.connect(partial(MainWindow.close, ))
    ui.action5shi.triggered.connect(partial(MainWindow5.show, ))
    ui.action5shi.triggered.connect(partial(MainWindow.close, ))
    ui.action6shi.triggered.connect(partial(MainWindow6.show, ))
    ui.action6shi.triggered.connect(partial(MainWindow.close, ))
    ui.actionzong.triggered.connect(partial(MainWindow7.show, ))
    ui.actionzong.triggered.connect(partial(MainWindow.close, ))
    ui.actiondianliu.triggered.connect(partial(MainWindow8.show, ))
    ui.actiondianliu.triggered.connect(partial(MainWindow.close, ))
    ui.actionHelp.triggered.connect(partial(MainWindow9.show, ))
    ui.actionHelp.triggered.connect(partial(MainWindow.close, ))
    ui.actionguan.triggered.connect(partial(MainWindow10.show, ))
    ui.actionguan.triggered.connect(partial(MainWindow.close, ))
    ui.actionjiemian.triggered.connect(partial(MainWindow11.show, ))
    ui.actionjiemian.triggered.connect(partial(MainWindow.close, ))

    ui.actionshowdata.triggered.connect(partial(MainWindow12.show, )) #####
    ui.actionshowdata.triggered.connect(partial(MainWindow.close, ))   #####
#退出程序
    sys.exit(app.exec_())
