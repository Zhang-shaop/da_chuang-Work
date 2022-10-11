from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
import numpy as np
from time import sleep
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#加入了实时刷新的功能
#可视化页面

#1室电压
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()

        # 调用页面的刷新
    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/1室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 6.0 and file1_data > 2.0:
            state = '安全'
        elif file1_data > 6.0:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "1室电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "1室电压："))
        self.label_2.setText(_translate("Form", "安全状态："))

#2室电压
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()

        # 调用页面的刷新
    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/2室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 6.0 and file1_data > 2.0:
            state = '安全'
        elif file1_data > 6.0:
            state = '危险'
        else:
               state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "2室电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "2室电压："))
        self.label_2.setText(_translate("Form", "安全状态："))

class Ui_Form3(object):
     def setupUi(self, Form):
         Form.setObjectName("Form")
         Form.resize(629, 422)
         self.pushButton = QtWidgets.QPushButton(Form)
         self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
         font = QtGui.QFont()
         font.setFamily("Arial")
         font.setPointSize(10)
         font.setBold(True)
         font.setItalic(True)
         font.setWeight(75)
         self.pushButton.setFont(font)
         self.pushButton.setObjectName("pushButton")
         self.label = QtWidgets.QLabel(Form)
         self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
         font = QtGui.QFont()
         font.setFamily("Arial")
         font.setPointSize(12)
         font.setBold(True)
         font.setWeight(75)
         self.label.setFont(font)
         self.label.setObjectName("label")

         self.lineEdit = QtWidgets.QLineEdit(Form)
         self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
         self.lineEdit.setObjectName("lineEdit")


         self.label_2 = QtWidgets.QLabel(Form)
         self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
         font = QtGui.QFont()
         font.setFamily("Arial")
         font.setPointSize(12)
         font.setBold(True)
         font.setWeight(75)
         self.label_2.setFont(font)
         self.label_2.setObjectName("label_2")

         self.lineEdit_2 = QtWidgets.QLineEdit(Form)
         self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
         self.lineEdit_2.setObjectName("lineEdit_2")

         self.retranslateUi(Form)
         QtCore.QMetaObject.connectSlotsByName(Form)

         self.Mytimer()

     def Mytimer(self):
         timer = QTimer(self.lineEdit)
         timer.timeout.connect(self.update)
         timer.start(100)

     def update(self):
         # 读入文本
         file1 = open('E:/new dachuang/daChuangWork2/data/3室电压.txt', 'r')
         self.lineEdit.setText(str(file1.read()))
         file1.close()
         # 设置状态
         file1_data = float(self.lineEdit.text())
         if file1_data < 6.0 and file1_data > 2.0:
             state = '安全'
         elif file1_data > 6.0:
             state = '危险'
         else:
             state = '数据异常'
         self.lineEdit_2.setText(state)

     def retranslateUi(self, Form):
         _translate = QtCore.QCoreApplication.translate
         Form.setWindowTitle(_translate("Form", "3室电压"))
         self.pushButton.setText(_translate("Form", "返回主页"))
         self.label.setText(_translate("Form", "3室电压："))
         self.label_2.setText(_translate("Form", "安全状态："))

#4室电压
class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()

    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/4室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 6.0 and file1_data > 2.0:
            state = '安全'
        elif file1_data > 6.0:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "4室电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "4室电压："))
        self.label_2.setText(_translate("Form", "安全状态："))

    # 5室电压
class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()
    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/5室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 6.0 and file1_data > 2.0:
            state = '安全'
        elif file1_data > 6.0:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "5室电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "5室电压："))
        self.label_2.setText(_translate("Form", "安全状态："))

    # 6室电压
class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()

    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/6室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 6.0 and file1_data > 2.0:
            state = '安全'
        elif file1_data > 6.0:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "6室电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "6室电压："))
        self.label_2.setText(_translate("Form", "安全状态："))
#总电压
class Ui_Form7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()

    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/总电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 60 and file1_data > 0:
            state = '安全'
        elif file1_data > 60:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "总电压"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "总电压："))
        self.label_2.setText(_translate("Form", "安全状态："))
#总电流
class Ui_Form8(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 113, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Mytimer()
    def Mytimer(self):
        timer = QTimer(self.lineEdit)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        # 读入文本
        file1 = open('E:/new dachuang/daChuangWork2/data/总电流.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 2 and file1_data > 0:
            state = '安全'
        elif file1_data > 2:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "总电流"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "总电流："))
        self.label_2.setText(_translate("Form", "安全状态："))

class Ui_Form9(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, -150, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据说明"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "\n\n\n\n\n\n数据说明：\n氢槽温度：氢槽热平衡后温度。\n氧槽温度：氧槽热平衡后温度。\n"
                                              "碱液流量：持续输入输出的交换碱液流量。\n碱液温度:   碱液预热后流入的温度。\n"
                                              "n槽室电压：串联的第n个电解槽的电解电压。\n总电压：加载在主电极两端的电压。\n"
                                              "总电流：电解装置工作时的主极电流。"
                                      ))

class Ui_Form10(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, -150, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "团队介绍"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "\n\n\n\n团队简介：\n"
                                              "队长：曹瑜，负责组织开发进度，文献阅读整理，路线规划。\n"
                                              "图像识别技术开发：刘建胜，王敬修\n"
                                              "展示页面设计及部分功能设计：张劭鹏，孙钰昊"))

class Ui_Form11(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 422)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, -150, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "技术说明"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "\n\n\n\n电解水技术原理：\n"
                                              "碱性电解水技术是以KOH、NaOH水溶液为电解质，如采用石棉布\n"
                                              "等作为隔膜，在直流电的作用下，将水电解成氢气和氧气。在阴\n"
                                              "极，水分子被分解为氢离子和氢氧根离子，氢离子得到电子生成\n"
                                              "氢原子，并进一步生成氢分子；氢氧根离子则在阴、阳极之间的\n"
                                              "电场力作用下穿过多孔的横膈膜，到达阳极，在阳极失去电子生\n"
                                              "成水分子和氧分子。"))