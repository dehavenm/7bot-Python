# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ikgui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import serial
from serialports import list_ports
from sevenbot import SevenBot
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 461, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.xSlider.setMinimum(-500)
        self.xSlider.setMaximum(500)
        self.xSlider.setOrientation(QtCore.Qt.Horizontal)
        self.xSlider.setObjectName("xSlider")
        self.horizontalLayout.addWidget(self.xSlider)
        self.xDisplay = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.xDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.xDisplay.setObjectName("xDisplay")
        self.horizontalLayout.addWidget(self.xDisplay)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ySlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.ySlider.setMinimum(-500)
        self.ySlider.setMaximum(500)
        self.ySlider.setProperty("value", 200)
        self.ySlider.setOrientation(QtCore.Qt.Horizontal)
        self.ySlider.setObjectName("ySlider")
        self.horizontalLayout_2.addWidget(self.ySlider)
        self.yDisplay = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.yDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.yDisplay.setObjectName("yDisplay")
        self.horizontalLayout_2.addWidget(self.yDisplay)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.zSlider.setMinimum(-500)
        self.zSlider.setMaximum(500)
        self.zSlider.setProperty("value", 50)
        self.zSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zSlider.setObjectName("zSlider")
        self.horizontalLayout_3.addWidget(self.zSlider)
        self.zDisplay = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.zDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.zDisplay.setObjectName("zDisplay")
        self.horizontalLayout_3.addWidget(self.zDisplay)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget.raise_()
        self.xSlider.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #----------------------------------------------------------
        #Everything not generated by QT Designer goes below
        #----------------------------------------------------------
        
        self.xSlider.valueChanged.connect(self.xUpdate)
        self.ySlider.valueChanged.connect(self.yUpdate)
        self.zSlider.valueChanged.connect(self.zUpdate)
        
        self.arm = SevenBot('COM10', 115200)
        
        self.vec56 = [0, 0, -1]
        self.vec67 = [1, 0, 0]
        self.joints = [90, 90]
        
        self.arm.setIK6([self.xSlider.value(), self.ySlider.value(), self.zSlider.value()], self.vec56, self.vec67, 90)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Z"))
        
    def xUpdate(self):
        self.xDisplay.display(self.xSlider.value())
        self.arm.setIK6([self.xSlider.value(), self.ySlider.value(), self.zSlider.value()], self.vec56, self.vec67, 90)
        
    def yUpdate(self):
        self.yDisplay.display(self.ySlider.value())
        self.arm.setIK6([self.xSlider.value(), self.ySlider.value(), self.zSlider.value()], self.vec56, self.vec67, 90)
        
    def zUpdate(self):
        self.zDisplay.display(self.zSlider.value())
        self.arm.setIK6([self.xSlider.value(), self.ySlider.value(), self.zSlider.value()], self.vec56, self.vec67, 90)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

