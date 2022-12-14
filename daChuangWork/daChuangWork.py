# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daChuangWork.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 120, 250, 350))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

#氢槽温度
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        file1=open('data/氢槽温度.txt', 'r')
        self.lineEdit.setText(file1.read())
        file1.close()

#氧槽温度
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 250, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        file2 = open('data/氧槽温度.txt', 'r')
        self.lineEdit_2.setText(file2.read())
        file2.close()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

#碱液温度
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 340, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        file3 = open('data/碱液温度.txt', 'r')
        self.lineEdit_3.setText(file3.read())
        file3.close()

#碱液流量
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 430, 113, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        file4 = open('data/碱液流量.txt', 'r')
        self.lineEdit_4.setText(file4.read())
        file4.close()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 130, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 180, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 230, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 230, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 300, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(620, 350, 141, 28))
        self.pushButton_8.setObjectName("pushButton_8")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(440, 490, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 490, 141, 20))
        self.label_6.setObjectName("label_6")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(600, 520, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")

        self.menu_3 = QtWidgets.QMenu(self.menubar) #####新增部分
        self.menu_3.setObjectName("menu_3") #####

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionguan = QtWidgets.QAction(MainWindow)
        self.actionguan.setObjectName("actionguan")
        self.actionjiemian = QtWidgets.QAction(MainWindow)
        self.actionjiemian.setObjectName("actionjiemian")
        self.action1shi = QtWidgets.QAction(MainWindow)
        self.action1shi.setObjectName("action1shi")
        self.action2shi = QtWidgets.QAction(MainWindow)
        self.action2shi.setObjectName("action2shi")
        self.action3shi = QtWidgets.QAction(MainWindow)
        self.action3shi.setObjectName("action3shi")
        self.action4shi = QtWidgets.QAction(MainWindow)
        self.action4shi.setObjectName("action4shi")
        self.action5shi = QtWidgets.QAction(MainWindow)
        self.action5shi.setObjectName("action5shi")
        self.action6shi = QtWidgets.QAction(MainWindow)
        self.action6shi.setObjectName("action6shi")
        self.actionzong = QtWidgets.QAction(MainWindow)
        self.actionzong.setObjectName("actionzong")
        self.actiondianliu = QtWidgets.QAction(MainWindow)
        self.actiondianliu.setObjectName("actiondianliu")
        self.actionshowdata = QtWidgets.QAction(MainWindow)  #####
        self.actionshowdata.setObjectName("actionshowdata")     #####


        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionguan)
        self.menu.addAction(self.actionjiemian)
        self.menu_2.addAction(self.action1shi)
        self.menu_2.addAction(self.action2shi)
        self.menu_2.addAction(self.action3shi)
        self.menu_2.addAction(self.action4shi)
        self.menu_2.addAction(self.action5shi)
        self.menu_2.addAction(self.action6shi)
        self.menu_2.addAction(self.actionzong)
        self.menu_2.addAction(self.actiondianliu)
        self.menu_3.addAction(self.actionshowdata) #####

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction()) #####

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "电解水孪生数据检测系统"))
        self.label.setText(_translate("MainWindow", "电解水孪生数据检测系统"))
        self.label_2.setText(_translate("MainWindow", "氢槽温度："))
        self.label_3.setText(_translate("MainWindow", "氧槽温度："))
        self.label_4.setText(_translate("MainWindow", "碱液温度："))
        self.label_5.setText(_translate("MainWindow", "碱液流量："))
        self.pushButton.setText(_translate("MainWindow", "1室电压"))
        self.pushButton_2.setText(_translate("MainWindow", "2室电压"))
        self.pushButton_3.setText(_translate("MainWindow", "3室电压"))
        self.pushButton_4.setText(_translate("MainWindow", "4室电压"))
        self.pushButton_5.setText(_translate("MainWindow", "5室电压"))
        self.pushButton_6.setText(_translate("MainWindow", "6室电压"))
        self.pushButton_7.setText(_translate("MainWindow", "总电压"))
        self.pushButton_8.setText(_translate("MainWindow", "总电流"))
        self.label_6.setText(_translate("MainWindow", "电解水完成度："))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "数据查询"))
        self.menu_3.setTitle(_translate("MainWindow", "数据分析")) #####
        self.actionHelp.setText(_translate("MainWindow", "数据说明"))
        self.actionguan.setText(_translate("MainWindow", "关于团队"))
        self.actionjiemian.setText(_translate("MainWindow", "电解水技术原理"))
        self.action1shi.setText(_translate("MainWindow", "1室电压"))
        self.action2shi.setText(_translate("MainWindow", "2室电压"))
        self.action3shi.setText(_translate("MainWindow", "3室电压"))
        self.action4shi.setText(_translate("MainWindow", "4室电压"))
        self.action5shi.setText(_translate("MainWindow", "5室项目"))
        self.action6shi.setText(_translate("MainWindow", "6室电压"))
        self.actionzong.setText(_translate("MainWindow", "总电压"))
        self.actiondianliu.setText(_translate("MainWindow", "总电流"))
        self.actionshowdata.setText(_translate("MainWindow", "理论模拟值"))  #####


        self.textBrowser.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Arial Black\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"logo\pic1.jpg\" alt=\"电解水示意图\" /></p></body></html>"))
    def printf(self, mypstr):
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

