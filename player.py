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
        MainWindow.resize(290, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(100, 90, 75, 23))
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
        self.playlistView.setGeometry(QtCore.QRect(0, 121, 291, 171))
        self.playlistView.setObjectName("playlistView")
        self.currentTrack = QtWidgets.QLabel(self.centralwidget)
        self.currentTrack.setGeometry(QtCore.QRect(20, 60, 251, 31))
        self.currentTrack.setAutoFillBackground(True)
        self.currentTrack.setText("")
        self.currentTrack.setObjectName("currentTrack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Player"))
        self.Add.setText(_translate("MainWindow", "Add"))

