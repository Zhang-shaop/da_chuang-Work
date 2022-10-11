#需要的python函数库的引用关系
import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from PyQt5.QtCore import *
from numpy import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pylab import mpl
import os

list0=[]

#最基本的画布结构定义，所有的画布的原型。具体的修改在def compute_initial_figure(self)中修改
class MyMplCanvas(FigureCanvas):  # 画布基类
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""

    def __init__(self, parent=None, width=50, height=50, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        #self.axes.set_xlabel('x')
        #self.axes.set_ylabel('y')
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

#电解槽等效阻抗与电解槽温度的关系，界面静态曲线
class MyStaticMplCanvas(MyMplCanvas):
    """静态画布"""

    def compute_initial_figure(self):
        self.axes.set_xlabel('工作槽温T(摄氏度)',fontproperties='SimHei')
        self.axes.set_ylabel('等效阻抗R（欧姆）',fontproperties='SimHei')
        self.axes.set_title('电解槽等效阻抗随槽温变化局部曲线', fontproperties='SimHei')
        t = arange(50.0, 80.0, 0.01)
        s = 1.1763*0.000001*t*t-2.32*0.0001*t+0.0172
        self.axes.plot(t, s)

#每秒自动刷新的图像
class MyControlMplCanvas(MyMplCanvas):  # 单个画布
    """动态画布：每秒自动更新，更换一条折线。"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)  #设置成每一秒更新的模式

    def compute_initial_figure(self):
        self.axes.plot([0, 0, 0, 0], [1, 2, 3, 4], 'r')

    def update_figure(self, x=1):
        self.axes.cla()  #每次清空一次画布
        t = arange(0.0, 3.0, 0.01)
        print (x)
        s = sin(2 * pi * t + x / 100. * 2 * pi)
        self.axes.plot(t, s, 'r')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.draw()

#自己尝试绘制动态画布的函数，关键在于数组list0
class MyDynamicMplCanvas(MyMplCanvas):  # 单个画布
    """动态画布：每秒自动更新，更换一条折线。"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000) #单位是毫秒

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

   #def update_figure(self):
        # 构建4个随机整数，位于闭区间[0, 10]
       # l = [random.randint(0, 10) for i in range(4)]
       # self.axes.cla()  ##清除上一次的绘制数据
       # self.axes.plot([0, 1, 2, 3], l, 'r')
       # self.axes.set_xlabel('x')
       # self.axes.set_ylabel('y')
       # self.draw()

#自己写一个动态绘制曲线的数组：
    def update_figure(self):
        self.axes.cla()  ##清除上一次的绘制数据
        t = arange(0.0, 1000.0, 10)

        #file1 = open('/daChuangWork/data/总电压.txt', 'r')
        #listmem=file1.read()
        #list0.append(listmem)
        #file1.close()
        #list0.popleft()
#这里需要的就是，将硬件的数据传到list0，然后就是要要动态更新这个数组。
        self.axes.plot(t,list0, 'r')
        self.axes.set_xlabel('时间（s）',fontproperties='SimHei')
        self.axes.set_ylabel('1室电压（V）',fontproperties='SimHei')
        self.draw()



#############开始正式界面定义
#定义数据模拟界面的第一个页面：槽阻抗随槽温度的变化曲线绘制
class Ui_MainWindow0(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #MainWindow
        MainWindow.resize(1200,600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        #网格线布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        #垂直布局0
        self.verticallayout = QtWidgets.QVBoxLayout()
        self.verticallayout.setContentsMargins(11, 11, 11, 11)
        self.verticallayout.setSpacing(6)
        self.verticallayout.setObjectName("verticallayout")
        #水平线布局0
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 垂直布局1
        self.verticallayout1 = QtWidgets.QVBoxLayout()
        self.verticallayout1.setContentsMargins(11, 11, 11, 11)
        self.verticallayout1.setSpacing(6)
        self.verticallayout1.setObjectName("verticallayout")
        # 水平线布局1
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout1.setSpacing(6)
        self.horizontalLayout1.setObjectName("horizontalLayout")

        # 垂直布局2
        self.verticallayout2 = QtWidgets.QVBoxLayout()
        self.verticallayout2.setContentsMargins(11, 11, 11, 11)
        self.verticallayout2.setSpacing(6)
        self.verticallayout2.setObjectName("verticallayout")
        # 水平线布局2
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout2.setSpacing(6)
        self.horizontalLayout2.setObjectName("horizontalLayout")

        #增加数据显示部分
        self.main_widget2 = QWidget()
        self.label1 = QtWidgets.QLabel(self.main_widget2)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.main_widget2)
        self.label2 = QtWidgets.QLabel(self.main_widget2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.main_widget2)
        self.horizontalLayout1.addWidget(self.label1)
        self.horizontalLayout1.addWidget(self.lineEdit_1)
        self.horizontalLayout1.addWidget(self.label2)
        self.horizontalLayout1.addWidget(self.lineEdit_2)
        self.verticallayout1.addLayout(self.horizontalLayout1)
        self.gridLayout.addLayout(self.verticallayout1,0,0,1,3)

        #将表格绘制出来！！！！这是一个重要的部分。
        self.main_widget = QWidget()
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.horizontalLayout.addWidget(sc)
        #在垂直布局基础上增加这个水平布局。
        self.verticallayout.addLayout(self.horizontalLayout)
        #把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.verticallayout, 1, 0, 3, 3)
        MainWindow.setCentralWidget(self.centralWidget)

        self.main_widget1 = QWidget()
        self.pushButton = QtWidgets.QPushButton(self.main_widget1)
       # self.horizontalLayout.addWidget(self.pushButton)
       #self.verticallayout.addLayout(self.horizontalLayout)
        self.verticallayout2.addWidget(self.pushButton)
        self.horizontalLayout2.addLayout(self.verticallayout2)
        # 把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.horizontalLayout2, 4, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)
        #设置字体
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        #对于按键设置字体
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
####
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Mytimer()
    def Mytimer(self):
        timer = QTimer(self.centralWidget)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        file1 = open('E:/new dachuang/daChuangWork/data/氢槽温度.txt', 'r')
        tt=float(file1.read())  #时刻注意数据类型的问题
        ss = format(1.1763 * 0.000001 * tt * tt - 2.32 * 0.0001 * tt + 0.0172, '.4f')
        self.lineEdit_1.setText(str(tt))
        self.lineEdit_2.setText(str(ss))
        #为什么只能运行第一个？不能显示第二个？？？第二个不能填任何值？文件读取问题。
        file1.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "理论数值模拟"))
        self.pushButton.setText(_translate("pushButton", "返回主页"))
        self.label1.setText(_translate("label1", "槽室温度（摄氏度）:"))
        self.label2.setText(_translate("label2", "电解槽等效阻抗（欧姆）:"))

#自己定义的第2个界面，有限元模型展示界面。
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #MainWindow
        MainWindow.resize(1000,800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 网格线布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        # 垂直布局1
        self.verticallayout1 = QtWidgets.QVBoxLayout()
        self.verticallayout1.setContentsMargins(11, 11, 11, 11)
        self.verticallayout1.setSpacing(6)
        self.verticallayout1.setObjectName("verticallayout")

       #把图片加入界面
        self.main_widget = QWidget()
        self.label0 = QtWidgets.QLabel(self.main_widget)
        self.label1 = QtWidgets.QLabel(self.main_widget)
        self.label2 = QtWidgets.QLabel(self.main_widget)
        self.label3 = QtWidgets.QLabel(self.main_widget)

        self.label1.setObjectName("label")

        self.main_widget1 = QWidget()
        self.pushButton = QtWidgets.QPushButton(self.main_widget1)

        self.verticallayout1.addWidget(self.label0)
        self.verticallayout1.addWidget(self.label1)
        self.verticallayout1.addWidget(self.label2)
        self.verticallayout1.addWidget(self.label3)
        self.verticallayout1.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticallayout1,0,0,0,0)

        MainWindow.setCentralWidget(self.centralWidget)
        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        # 对于按键设置字体
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "有限元模型展示"))
        self.pushButton.setText(_translate("pushButton", "返回主页"))
        self.label0.setText(_translate("pushButton", "有限元模型展示:"))
        self.label2.setText(_translate("pushButton", "装配实物展示:"))

        #插入图片2
        self.cover_img = os.path.abspath('E:/new dachuang/daChuangWork2/logo/pic2.png')
        self.image0 = QtGui.QPixmap(self.cover_img).scaled(600, 400)
        self.label1.setPixmap(self.image0)
        self.label1.setScaledContents(True)

        # 插入图片3
        self.cover_img1 = os.path.abspath('E:/new dachuang/daChuangWork2/logo/pic3.jpg')
        self.image1 = QtGui.QPixmap(self.cover_img1).scaled(600, 400)
        self.label3.setPixmap(self.image1)
        self.label3.setScaledContents(True)

#自己定义的第三个界面：寿命预测技术
class Ui_MainWindow2(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #MainWindow
        MainWindow.resize(1200,600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        #网格线布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        #垂直布局0
        self.verticallayout = QtWidgets.QVBoxLayout()
        self.verticallayout.setContentsMargins(11, 11, 11, 11)
        self.verticallayout.setSpacing(6)
        self.verticallayout.setObjectName("verticallayout")
        #水平线布局0
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 垂直布局1
        self.verticallayout1 = QtWidgets.QVBoxLayout()
        self.verticallayout1.setContentsMargins(11, 11, 11, 11)
        self.verticallayout1.setSpacing(6)
        self.verticallayout1.setObjectName("verticallayout")
        # 水平线布局1
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout1.setSpacing(6)
        self.horizontalLayout1.setObjectName("horizontalLayout")

        # 垂直布局2
        self.verticallayout2 = QtWidgets.QVBoxLayout()
        self.verticallayout2.setContentsMargins(11, 11, 11, 11)
        self.verticallayout2.setSpacing(6)
        self.verticallayout2.setObjectName("verticallayout")
        # 水平线布局2
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout2.setSpacing(6)
        self.horizontalLayout2.setObjectName("horizontalLayout")

        # 垂直布局3
        self.verticallayout3 = QtWidgets.QVBoxLayout()
        self.verticallayout3.setContentsMargins(11, 11, 11, 11)
        self.verticallayout3.setSpacing(6)
        self.verticallayout3.setObjectName("verticallayout")
        # 水平线布局3
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout3.setSpacing(6)
        self.horizontalLayout3.setObjectName("horizontalLayout")

        #增加数据显示部分
        self.main_widget2 = QWidget()
        self.label1 = QtWidgets.QLabel(self.main_widget2)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.main_widget2)
        self.label2 = QtWidgets.QLabel(self.main_widget2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.main_widget2)
        self.horizontalLayout1.addWidget(self.label1)
        self.horizontalLayout1.addWidget(self.lineEdit_1)
        self.horizontalLayout1.addWidget(self.label2)
        self.horizontalLayout1.addWidget(self.lineEdit_2)
        self.verticallayout1.addLayout(self.horizontalLayout1)
        self.gridLayout.addLayout(self.verticallayout1,0,0,1,3)

        #增加数据显示部分2
        self.main_widget3 = QWidget()
        self.label3 = QtWidgets.QLabel(self.main_widget3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.main_widget3)
        self.label4 = QtWidgets.QLabel(self.main_widget3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.main_widget3)
        self.horizontalLayout3.addWidget(self.label3)
        self.horizontalLayout3.addWidget(self.lineEdit_3)
        self.horizontalLayout3.addWidget(self.label4)
        self.horizontalLayout3.addWidget(self.lineEdit_4)
        self.verticallayout3.addLayout(self.horizontalLayout3)
        self.gridLayout.addLayout(self.verticallayout3,1,0,1,3)

        #将表格绘制出来！！！！这是一个重要的部分。
        self.main_widget = QWidget()
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.horizontalLayout.addWidget(sc)
        #在垂直布局基础上增加这个水平布局。
        self.verticallayout.addLayout(self.horizontalLayout)
        #把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.verticallayout, 2, 0, 4, 3)
        MainWindow.setCentralWidget(self.centralWidget)

        self.main_widget1 = QWidget()
        self.pushButton1 = QtWidgets.QPushButton(self.main_widget1)
        self.pushButton = QtWidgets.QPushButton(self.main_widget1)

       # self.horizontalLayout.addWidget(self.pushButton)
       #self.verticallayout.addLayout(self.horizontalLayout)
        self.verticallayout2.addWidget(self.pushButton1)
        self.verticallayout2.addWidget(self.pushButton)
        self.horizontalLayout2.addLayout(self.verticallayout2)
        # 把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.horizontalLayout2, 6, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)
        #设置字体
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        #对于按键设置字体
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4.setFont(font)
        self.label4.setObjectName("label4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Mytimer()
    def Mytimer(self):
        timer = QTimer(self.centralWidget)
        timer.timeout.connect(self.update)
        timer.start(100)

    def update(self):
        file1 = open('E:/new dachuang/daChuangWork/data/总电压.txt', 'r')
        tt=float(file1.read())  #时刻注意数据类型的问题
        tt=tt/6
        #关于计算预期寿命的函数部分？？？
        ####把这个补充起来，就好了！！！

        ss = format(1.1763 * 0.000001 * tt * tt - 2.32 * 0.0001 * tt + 0.0172, '.4f')
        self.lineEdit_3.setText(str(tt))
        self.lineEdit_4.setText(str(ss))
        #为什么只能运行第一个？不能显示第二个？？？第二个不能填任何值？文件读取问题。
        file1.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "电气寿命预测"))
        self.pushButton1.setText(_translate("pushButton1", "绘制曲线"))
        self.pushButton.setText(_translate("pushButton", "返回主页"))
        self.label1.setText(_translate("label1", "产氢速率（产氢电流）（安培）:"))
        self.label2.setText(_translate("label2", "额定电压（伏）:"))
        self.label3.setText(_translate("label3", "实际槽总电压（伏）:"))
        self.label4.setText(_translate("label4", "预期电气寿命（hour）:"))


#自己定义的第四个界面：实时数据刷新界面
class Ui_MainWindow3(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #MainWindow
        MainWindow.resize(1500,600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        #网格线布局
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        #垂直布局
        self.verticallayout = QtWidgets.QVBoxLayout()
        self.verticallayout.setContentsMargins(11, 11, 11, 11)
        self.verticallayout.setSpacing(6)
        self.verticallayout.setObjectName("verticallayout")
        #水平线布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #水平滑标
        self.lcd = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd.setObjectName("lcd1")
        self.verticallayout.addWidget(self.lcd)
        self.horizontalSlide = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlide.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlide.setObjectName("horizontalSlide")
        self.verticallayout.addWidget(self.horizontalSlide)
        #将三个表格绘制出来！！！！这是一个重要的部分。
        self.main_widget = QWidget()
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        cc = MyControlMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.horizontalLayout.addWidget(sc)
        self.horizontalLayout.addWidget(dc)
        self.horizontalLayout.addWidget(cc)
        #在垂直布局基础上增加这个水平布局。
        self.verticallayout.addLayout(self.horizontalLayout)
        #把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.verticallayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        #设置水平菜单栏
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 519, 23))
        self.menuBar.setObjectName("menuBar")
        #菜单栏里面的选项卡
        self.menuF = QtWidgets.QMenu(self.menuBar)
        self.menuF.setObjectName("menuF")
        self.menuE = QtWidgets.QMenu(self.menuBar)
        self.menuE.setObjectName("menuE")
        self.menuW = QtWidgets.QMenu(self.menuBar)
        self.menuW.setObjectName("menuW")
        self.menuH = QtWidgets.QMenu(self.menuBar)
        self.menuH.setObjectName("menuH")
        MainWindow.setMenuBar(self.menuBar)
####
        self.main_widget1 = QWidget()
        self.pushButton = QtWidgets.QPushButton(self.main_widget1)
       # self.horizontalLayout.addWidget(self.pushButton)
       #self.verticallayout.addLayout(self.horizontalLayout)
        self.verticallayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticallayout)
        # 把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
####
        self.retranslateUi(MainWindow)
        self.horizontalSlide.valueChanged['int'].connect(self.lcd.display)
        self.horizontalSlide.valueChanged['int'].connect(lambda: cc.update_figure(self.horizontalSlide.value()))
        # x = self.horizontalSlide.value()
        # dc.update_figure()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "理论数值模拟"))
        self.pushButton.setText(_translate("pushButton", "返回主页"))