# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
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
        MainWindow.setObjectName("数据分析") #MainWindow
        MainWindow.resize(2400,600)
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
        #垂直布局问题
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

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        MainWindow.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/saveAs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon5)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon6)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon8)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon9)
        self.actionPaste.setObjectName("actionPaste")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionTile = QtWidgets.QAction(MainWindow)
        self.actionTile.setObjectName("actionTile")
        self.actionCascade = QtWidgets.QAction(MainWindow)
        self.actionCascade.setObjectName("actionCascade")
        self.actionNext = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext.setIcon(icon10)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrevious.setIcon(icon11)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon12)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.menuF.addAction(self.actionNew)
        self.menuF.addAction(self.actionOpen)
        self.menuF.addSeparator()
        self.menuF.addAction(self.actionSave)
        self.menuF.addAction(self.actionSaveAs)
        self.menuF.addSeparator()
        self.menuF.addAction(self.actionExit)
        self.menuE.addAction(self.actionUndo)
        self.menuE.addAction(self.actionRedo)
        self.menuE.addSeparator()
        self.menuE.addAction(self.actionCut)
        self.menuE.addAction(self.actionCopy)
        self.menuE.addAction(self.actionPaste)
        self.menuW.addAction(self.actionClose)
        self.menuW.addAction(self.actionCloseAll)
        self.menuW.addSeparator()
        self.menuW.addAction(self.actionTile)
        self.menuW.addAction(self.actionCascade)
        self.menuW.addSeparator()
        self.menuW.addAction(self.actionNext)
        self.menuW.addAction(self.actionPrevious)
        self.menuH.addAction(self.actionAbout)
        self.menuH.addAction(self.actionAboutQt)
        self.menuBar.addAction(self.menuF.menuAction())
        self.menuBar.addAction(self.menuE.menuAction())
        self.menuBar.addAction(self.menuW.menuAction())
        self.menuBar.addAction(self.menuH.menuAction())
        self.mainToolBar.addAction(self.actionNew)
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionSave)
        self.mainToolBar.addAction(self.actionSaveAs)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionCut)
        self.mainToolBar.addAction(self.actionCopy)
        self.mainToolBar.addAction(self.actionPaste)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionUndo)
        self.mainToolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)
        self.horizontalSlide.valueChanged['int'].connect(self.lcd.display)
        self.horizontalSlide.valueChanged['int'].connect(lambda: cc.update_figure(self.horizontalSlide.value()))
        # x = self.horizontalSlide.value()
        # dc.update_figure()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuF.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menuE.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menuW.setTitle(_translate("MainWindow", "窗口(&W)"))
        self.menuH.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.actionNew.setText(_translate("MainWindow", "新建文件(&N)"))
        self.actionNew.setToolTip(_translate("MainWindow", "新建文件"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "打开文件(&O)..."))
        self.actionOpen.setToolTip(_translate("MainWindow", "打开文件"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "保存(&S)"))
        self.actionSave.setToolTip(_translate("MainWindow", "保存"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存为(&A)..."))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "另存为"))
        self.actionExit.setText(_translate("MainWindow", "退出(&X)"))
        self.actionExit.setToolTip(_translate("MainWindow", "退出"))
        self.actionUndo.setText(_translate("MainWindow", "撤销(&U)"))
        self.actionUndo.setToolTip(_translate("MainWindow", "撤销"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "恢复(&R)"))
        self.actionRedo.setToolTip(_translate("MainWindow", "恢复"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "剪切(&T)"))
        self.actionCut.setToolTip(_translate("MainWindow", "剪切"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "复制(&C)"))
        self.actionCopy.setToolTip(_translate("MainWindow", "复制"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "粘贴(&P)"))
        self.actionPaste.setToolTip(_translate("MainWindow", "粘贴"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionClose.setText(_translate("MainWindow", "关闭(&O)"))
        self.actionClose.setToolTip(_translate("MainWindow", "关闭"))
        self.actionCloseAll.setText(_translate("MainWindow", "关闭所有窗口(&A)"))
        self.actionCloseAll.setToolTip(_translate("MainWindow", "关闭所有窗口"))
        self.actionTile.setText(_translate("MainWindow", "平铺(&T)"))
        self.actionTile.setToolTip(_translate("MainWindow", "平铺"))
        self.actionCascade.setText(_translate("MainWindow", "层叠(&C)"))
        self.actionCascade.setToolTip(_translate("MainWindow", "层叠"))
        self.actionNext.setText(_translate("MainWindow", "下一个(&X)"))
        self.actionNext.setToolTip(_translate("MainWindow", "下一个"))
        self.actionNext.setShortcut(_translate("MainWindow", "Ctrl+Tab"))
        self.actionPrevious.setText(_translate("MainWindow", "前一个(&V)"))
        self.actionPrevious.setToolTip(_translate("MainWindow", "前一个"))
        self.actionPrevious.setShortcut(_translate("MainWindow", "Ctrl+Shift+Backtab"))
        self.actionAbout.setText(_translate("MainWindow", "关于(&A)"))
        self.actionAbout.setToolTip(_translate("MainWindow", "关于"))
        self.actionAboutQt.setText(_translate("MainWindow", "关于Qt(&Q)"))
        self.actionAboutQt.setToolTip(_translate("MainWindow", "关于Qt"))
