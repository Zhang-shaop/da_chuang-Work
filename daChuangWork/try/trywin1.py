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
#由于设置的类型准换问题，文件夹中一定只能是数字！！！不然会闪退。

# 辨别是否为正数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass
    return False


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
        file1 = open('E:/new dachuang/daChuangWork/data/1室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/2室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
         file1 = open('E:/new dachuang/daChuangWork/data/3室电压.txt', 'r')
         self.lineEdit.setText(str(file1.read()))
         file1.close()
         # 设置状态
         file1_data = float(self.lineEdit.text())
         if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
             state = '安全'
         elif file1_data > 50:
             state = '危险'
         else:
             state = '数据异常'
         self.lineEdit_2.setText(state)

     def retranslateUi(self, Form):
         _translate = QtCore.QCoreApplication.translate
         Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/4室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/5室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/6室电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/总电压.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        file1 = open('E:/new dachuang/daChuangWork/data/总电流.txt', 'r')
        self.lineEdit.setText(str(file1.read()))
        file1.close()
        # 设置状态
        file1_data = float(self.lineEdit.text())
        if file1_data < 50 and file1_data > 0 and is_number(file1_data)!=0:
            state = '安全'
        elif file1_data > 50:
            state = '危险'
        else:
            state = '数据异常'
        self.lineEdit_2.setText(state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "数据说明：xxxxxxxxxxx\n"
                                              "xxxxxxxxxxxxxx"))

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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "团队简介："))

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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "返回主页"))
        self.label.setText(_translate("Form", "电解水技术原理："))