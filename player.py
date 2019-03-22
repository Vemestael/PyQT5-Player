# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 397)
        MainWindow.setMinimumSize(QtCore.QSize(290, 397))
        MainWindow.setMaximumSize(QtCore.QSize(290, 397))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.Add.setObjectName("Add")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(110, 10, 51, 41))
        self.Play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play.setIcon(icon)
        self.Play.setIconSize(QtCore.QSize(50, 35))
        self.Play.setObjectName("Play")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.Back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon1)
        self.Back.setIconSize(QtCore.QSize(35, 35))
        self.Back.setObjectName("Back")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setEnabled(True)
        self.Next.setGeometry(QtCore.QRect(170, 10, 41, 41))
        self.Next.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon2)
        self.Next.setIconSize(QtCore.QSize(35, 35))
        self.Next.setObjectName("Next")
        self.playlistView = QtWidgets.QTableView(self.centralwidget)
        self.playlistView.setGeometry(QtCore.QRect(0, 160, 291, 231))
        self.playlistView.setObjectName("playlistView")
        self.currentTrack = QtWidgets.QLabel(self.centralwidget)
        self.currentTrack.setGeometry(QtCore.QRect(20, 60, 251, 31))
        self.currentTrack.setAutoFillBackground(True)
        self.currentTrack.setText("")
        self.currentTrack.setObjectName("currentTrack")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(220, 30, 20, 20))
        self.Stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon3)
        self.Stop.setIconSize(QtCore.QSize(20, 20))
        self.Stop.setObjectName("Stop")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 271, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.Clear.setObjectName("Clear")
        self.Volume = QtWidgets.QSlider(self.centralwidget)
        self.Volume.setGeometry(QtCore.QRect(170, 131, 111, 21))
        self.Volume.setMaximum(100)
        self.Volume.setProperty("value", 100)
        self.Volume.setTracking(True)
        self.Volume.setOrientation(QtCore.Qt.Horizontal)
        self.Volume.setObjectName("Volume")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Player"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.progressBar.setFormat(_translate("MainWindow", "%v0:%v0"))
        self.Clear.setText(_translate("MainWindow", "Clear"))

