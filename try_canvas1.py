# WARNING! All changes made in this file will be lost!
import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):  # 单个画布
    """静态画布：一条正弦线"""

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(4 * pi * t)
        self.axes.plot(t, s)


class MyControlMplCanvas(MyMplCanvas):  # 单个画布
    """动态画布：每秒自动更新，更换一条折线。"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 0, 0, 0], [1, 2, 3, 4], 'r')

    def update_figure(self, x=1):
        self.axes.cla()
        # 构建4个随机整数，位于闭区间[0, 10]
        t = arange(0.0, 3.0, 0.01)
        print (x)
        s = sin(2 * pi * t + x / 100. * 2 * pi)
        self.axes.plot(t, s, 'r')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.draw()


class MyDynamicMplCanvas(MyMplCanvas):  # 单个画布
    """动态画布：每秒自动更新，更换一条折线。"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # 构建4个随机整数，位于闭区间[0, 10]
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.cla()  ##清除上一次的绘制数据
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.draw()

class Ui_MainWindow(object):

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
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticallayout.addLayout(self.horizontalLayout)
        # 把垂直布局增加到网格线布局
        self.gridLayout.addLayout(self.verticallayout, 1, 1, 1, 1)
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