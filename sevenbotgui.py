# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sevenbot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


import serial
from sevenbot import SevenBot
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 54, 239, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.status0.setObjectName("status0")
        self.horizontalLayout.addWidget(self.status0)
        self.status1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.status1.setObjectName("status1")
        self.horizontalLayout.addWidget(self.status1)
        self.status2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.status2.setObjectName("status2")
        self.horizontalLayout.addWidget(self.status2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(370, 84, 160, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.status = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.status.setObjectName("status")
        self.horizontalLayout_2.addWidget(self.status)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.speedSet = QtWidgets.QSlider(self.centralwidget)
        self.speedSet.setGeometry(QtCore.QRect(650, 100, 22, 160))
        self.speedSet.setMaximum(250)
        self.speedSet.setPageStep(1)
        self.speedSet.setProperty("value", 50)
        self.speedSet.setOrientation(QtCore.Qt.Vertical)
        self.speedSet.setObjectName("speedSet")
        self.speedDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.speedDisplay.setGeometry(QtCore.QRect(630, 50, 64, 23))
        self.speedDisplay.setObjectName("speedDisplay")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 160, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.joint0Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint0Slider.setMaximum(1000)
        self.joint0Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint0Slider.setObjectName("joint0Slider")
        self.verticalLayout.addWidget(self.joint0Slider)
        self.joint1Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint1Slider.setMaximum(1000)
        self.joint1Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint1Slider.setObjectName("joint1Slider")
        self.verticalLayout.addWidget(self.joint1Slider)
        self.joint2Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint2Slider.setMaximum(1000)
        self.joint2Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint2Slider.setObjectName("joint2Slider")
        self.verticalLayout.addWidget(self.joint2Slider)
        self.joint3Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint3Slider.setMaximum(1000)
        self.joint3Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint3Slider.setObjectName("joint3Slider")
        self.verticalLayout.addWidget(self.joint3Slider)
        self.joint4Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint4Slider.setMaximum(1000)
        self.joint4Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint4Slider.setObjectName("joint4Slider")
        self.verticalLayout.addWidget(self.joint4Slider)
        self.joint5Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint5Slider.setMaximum(1000)
        self.joint5Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint5Slider.setObjectName("joint5Slider")
        self.verticalLayout.addWidget(self.joint5Slider)
        self.joint6Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.joint6Slider.setMaximum(1000)
        self.joint6Slider.setOrientation(QtCore.Qt.Horizontal)
        self.joint6Slider.setObjectName("joint6Slider")
        self.verticalLayout.addWidget(self.joint6Slider)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 120, 101, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.joint0Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint0Cmd.setSmallDecimalPoint(True)
        self.joint0Cmd.setObjectName("joint0Cmd")
        self.verticalLayout_2.addWidget(self.joint0Cmd)
        self.joint1Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint1Cmd.setSmallDecimalPoint(True)
        self.joint1Cmd.setObjectName("joint1Cmd")
        self.verticalLayout_2.addWidget(self.joint1Cmd)
        self.joint2Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint2Cmd.setSmallDecimalPoint(True)
        self.joint2Cmd.setObjectName("joint2Cmd")
        self.verticalLayout_2.addWidget(self.joint2Cmd)
        self.joint3Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint3Cmd.setSmallDecimalPoint(True)
        self.joint3Cmd.setObjectName("joint3Cmd")
        self.verticalLayout_2.addWidget(self.joint3Cmd)
        self.joint4Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint4Cmd.setSmallDecimalPoint(True)
        self.joint4Cmd.setObjectName("joint4Cmd")
        self.verticalLayout_2.addWidget(self.joint4Cmd)
        self.joint5Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint5Cmd.setSmallDecimalPoint(True)
        self.joint5Cmd.setObjectName("joint5Cmd")
        self.verticalLayout_2.addWidget(self.joint5Cmd)
        self.joint6Cmd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.joint6Cmd.setSmallDecimalPoint(True)
        self.joint6Cmd.setObjectName("joint6Cmd")
        self.verticalLayout_2.addWidget(self.joint6Cmd)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(290, 120, 61, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 410, 571, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.joint0Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint0Pos.setObjectName("joint0Pos")
        self.horizontalLayout_3.addWidget(self.joint0Pos)
        self.joint1Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint1Pos.setObjectName("joint1Pos")
        self.horizontalLayout_3.addWidget(self.joint1Pos)
        self.joint2Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint2Pos.setObjectName("joint2Pos")
        self.horizontalLayout_3.addWidget(self.joint2Pos)
        self.joint3Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint3Pos.setObjectName("joint3Pos")
        self.horizontalLayout_3.addWidget(self.joint3Pos)
        self.joint4Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint4Pos.setObjectName("joint4Pos")
        self.horizontalLayout_3.addWidget(self.joint4Pos)
        self.joint5Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint5Pos.setObjectName("joint5Pos")
        self.horizontalLayout_3.addWidget(self.joint5Pos)
        self.joint6Pos = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.joint6Pos.setObjectName("joint6Pos")
        self.horizontalLayout_3.addWidget(self.joint6Pos)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 450, 571, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.joint0Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint0Input.setObjectName("joint0Input")
        self.horizontalLayout_4.addWidget(self.joint0Input)
        self.joint1Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint1Input.setObjectName("joint1Input")
        self.horizontalLayout_4.addWidget(self.joint1Input)
        self.joint2Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint2Input.setObjectName("joint2Input")
        self.horizontalLayout_4.addWidget(self.joint2Input)
        self.joint3Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint3Input.setObjectName("joint3Input")
        self.horizontalLayout_4.addWidget(self.joint3Input)
        self.joint4Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint4Input.setObjectName("joint4Input")
        self.horizontalLayout_4.addWidget(self.joint4Input)
        self.joint5Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint5Input.setObjectName("joint5Input")
        self.horizontalLayout_4.addWidget(self.joint5Input)
        self.joint6Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.joint6Input.setObjectName("joint6Input")
        self.horizontalLayout_4.addWidget(self.joint6Input)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(590, 410, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(590, 450, 75, 23))
        self.goButton.setObjectName("goButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 380, 59, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(100, 380, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(190, 380, 59, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(270, 380, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(350, 380, 59, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 380, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(510, 380, 59, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.connectionStatus = QtWidgets.QLabel(self.centralwidget)
        self.connectionStatus.setGeometry(QtCore.QRect(20, 0, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.connectionStatus.setFont(font)
        self.connectionStatus.setObjectName("connectionStatus")
        self.converged = QtWidgets.QLabel(self.centralwidget)
        self.converged.setGeometry(QtCore.QRect(590, 380, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.converged.setFont(font)
        self.converged.setObjectName("converged")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
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
        
        self.joint0Pos.setDecMode()
        self.joint1Pos.setDecMode()
        self.joint2Pos.setDecMode()
        self.joint3Pos.setDecMode()
        self.joint4Pos.setDecMode()
        self.joint5Pos.setDecMode()
        self.joint6Pos.setDecMode()
        
        self.joint0Pos.setSmallDecimalPoint(True)
        self.joint1Pos.setSmallDecimalPoint(True)
        self.joint2Pos.setSmallDecimalPoint(True)
        self.joint3Pos.setSmallDecimalPoint(True)
        self.joint4Pos.setSmallDecimalPoint(True)
        self.joint5Pos.setSmallDecimalPoint(True)
        self.joint6Pos.setSmallDecimalPoint(True)
        
        self.joint0Cmd.setDecMode()
        self.joint1Cmd.setDecMode()
        self.joint2Cmd.setDecMode()
        self.joint3Cmd.setDecMode()
        self.joint4Cmd.setDecMode()
        self.joint5Cmd.setDecMode()
        self.joint6Cmd.setDecMode()
        
        
        self.joint0Slider.valueChanged.connect(self.slider0Update)
        self.joint1Slider.valueChanged.connect(self.slider1Update)
        self.joint2Slider.valueChanged.connect(self.slider2Update)
        self.joint3Slider.valueChanged.connect(self.slider3Update)
        self.joint4Slider.valueChanged.connect(self.slider4Update)
        self.joint5Slider.valueChanged.connect(self.slider5Update)
        self.joint6Slider.valueChanged.connect(self.slider6Update)
        
        self.speedSet.valueChanged.connect(self.speedUpdate)
        
        
        

        
        self.status0.clicked.connect(self.setStatus0)
        self.status1.clicked.connect(self.setStatus1)
        self.status2.clicked.connect(self.setStatus2)
        
        
        self.arm = SevenBot('COM10', 115200)
        
        self.position_cmd = np.array([90,115,65,90,90,90,75],dtype=np.float32)
        self.speed_cmd = np.array([self.speedSet.value()]*7, dtype=np.int);
        self.speedUpdate()
        

            
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(20)
        
        self.update()
        self.sliderPosUpdate()
        
            
        
            
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.status0.setText(_translate("MainWindow", "0 - Forceless"))
        self.status1.setText(_translate("MainWindow", "1 - Normal"))
        self.status2.setText(_translate("MainWindow", "2 - Protected"))
        self.label.setText(_translate("MainWindow", "Current Status: "))
        self.label_2.setText(_translate("MainWindow", "Set Force Status"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.label_8.setText(_translate("MainWindow", "Joint 0"))
        self.label_9.setText(_translate("MainWindow", "Joint 1"))
        self.label_10.setText(_translate("MainWindow", "Joint 2"))
        self.label_11.setText(_translate("MainWindow", "Joint 3"))
        self.label_12.setText(_translate("MainWindow", "Joint 4"))
        self.label_13.setText(_translate("MainWindow", "Joint 5"))
        self.label_14.setText(_translate("MainWindow", "Joint 6"))
        self.label_15.setText(_translate("MainWindow", "Positions"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.label_16.setText(_translate("MainWindow", "Joint 0"))
        self.label_17.setText(_translate("MainWindow", "Joint 1"))
        self.label_18.setText(_translate("MainWindow", "Joint 2"))
        self.label_19.setText(_translate("MainWindow", "Joint 3"))
        self.label_20.setText(_translate("MainWindow", "Joint 4"))
        self.label_21.setText(_translate("MainWindow", "Joint 5"))
        self.label_22.setText(_translate("MainWindow", "Joint 6"))
        self.connectionStatus.setText(_translate("MainWindow", "Status"))
        self.converged.setText(_translate("MainWindow", "Converged"))
        
    #----------------------------------------------------------
    #Methods not generated by QT Designer go below
    #----------------------------------------------------------
    
#    def connect(self):
#        self.arm.connect('COM3')
#        self.position_cmd = self.arm.angle
        
    def disconnect(self):
        self.arm.disconnect()
    
    def setStatus0(self):
        self.arm.setForceStatus(0)
      
    def setStatus1(self):
        self.arm.setForceStatus(1)
        
    def setStatus2(self):
        self.arm.setForceStatus(2)

        
    def update(self):
        
        
        if self.arm.port.is_open:
            self.connectionStatus.setText("Connected")
            
#            self.status.display(self.arm.status)
#            position = self.arm.rangle()
#            
#            if self.arm.status == 0:
#                self.position_cmd = position
#        
#            if self.arm.status == 1:
#                self.arm.setAngle(self.position_cmd)
            
            
        else:
            self.connectionStatus.setText("Not Connected")
            
        self.status.display(self.arm.status)
        position = self.arm.rangle()
        
        self.joint0Pos.display(position[0]/1.0)
        self.joint1Pos.display(position[1]/1.0)
        self.joint2Pos.display(position[2]/1.0)
        self.joint3Pos.display(position[3]/1.0)
        self.joint4Pos.display(position[4]/1.0)
        self.joint5Pos.display(position[5]/1.0)
        self.joint6Pos.display(position[6]/1.0)
        
        
        
        if self.arm.status == 0:
            self.position_cmd = position
    
        if self.arm.status == 1:
            self.arm.setAngle(self.position_cmd)
            
    def sliderPosUpdate(self):
        self.joint0Slider.setValue(self.position_cmd[0]*(50.0/9.0))
        self.joint1Slider.setValue(self.position_cmd[1]*(50.0/9.0))
        self.joint2Slider.setValue(self.position_cmd[2]*(50.0/9.0))
        self.joint3Slider.setValue(self.position_cmd[3]*(50.0/9.0))
        self.joint4Slider.setValue(self.position_cmd[4]*(50.0/9.0))
        self.joint5Slider.setValue(self.position_cmd[5]*(50.0/9.0))
        self.joint6Slider.setValue(self.position_cmd[6]*(50.0/9.0))
        
        self.joint0Cmd.display(self.position_cmd[0]/1.0)
        self.joint1Cmd.display(self.position_cmd[1]/1.0)
        self.joint2Cmd.display(self.position_cmd[2]/1.0)
        self.joint3Cmd.display(self.position_cmd[3]/1.0)
        self.joint4Cmd.display(self.position_cmd[4]/1.0)
        self.joint5Cmd.display(self.position_cmd[5]/1.0)
        self.joint6Cmd.display(self.position_cmd[6]/1.0)
        
        
        
        
    def speedUpdate(self):
        for index,value in np.ndenumerate(self.speed_cmd):
            self.speed_cmd[index] = self.speedSet.value()
            self.arm.setSpeed(self.speed_cmd)
        self.speedDisplay.display(self.speedSet.value())
        
        
    def slider0Update(self):
        self.position_cmd[0] = self.joint0Slider.value()*(9.0/50.0)
        self.joint0Cmd.display(self.position_cmd[0]/1.0)
        
    def slider1Update(self):
        self.position_cmd[1] = self.joint1Slider.value()*(9.0/50.0)
        self.joint1Cmd.display(self.position_cmd[1]/1.0)
        
    def slider2Update(self):
        self.position_cmd[2] = self.joint2Slider.value()*(9.0/50.0)
        self.joint2Cmd.display(self.position_cmd[2]/1.0)
        
    def slider3Update(self):
        self.position_cmd[3] = self.joint3Slider.value()*(9.0/50.0)
        self.joint3Cmd.display(self.position_cmd[3]/1.0)
        
    def slider4Update(self):
        self.position_cmd[4] = self.joint4Slider.value()*(9.0/50.0)
        self.joint4Cmd.display(self.position_cmd[4]/1.0)
        
    def slider5Update(self):
        self.position_cmd[5] = self.joint5Slider.value()*(9.0/50.0)
        self.joint5Cmd.display(self.position_cmd[5]/1.0)
        
    def slider6Update(self):
        self.position_cmd[6] = self.joint6Slider.value()*(9.0/50.0)
        self.joint6Cmd.display(self.position_cmd[6]/1.0)
        
            
        
        
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

