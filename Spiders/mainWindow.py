# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon ,QCursor
from Spiders.UrlConfirm import *
from Spiders.Downloader import downloadfile
import urllib
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 410)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景设置为透明
        self.setWindowFlag(Qt.FramelessWindowHint)  # 设置为无边框
        MainWindow.setStyleSheet("background-image: url(../Pic/back.png);border-radius:12px")

        self.setWindowIcon(QIcon('../Pic/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)


        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(580, 25, 30, 30))
        self.closeButton.setObjectName("closeButton")

        self.showMiniButton = QtWidgets.QPushButton(self.centralwidget)
        self.showMiniButton.setGeometry(QtCore.QRect(545, 25, 30, 30))
        self.showMiniButton.setObjectName("showMiniButton")

        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 282, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 150, 54, 31))
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 210, 54, 15))
        self.label_2.setAttribute(Qt.WA_TranslucentBackground)
        self.label_2.setObjectName("label_2")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 210, 210, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 282, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 150, 210, 20))
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "多平台音乐下载器"))

        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.pushButton.clicked.connect(self.download)

        self.label.setText(_translate("MainWindow", "音频链接"))
        self.label_2.setText(_translate("MainWindow", "保存地址"))



        self.pushButton_2.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setIcon(QIcon("../Pic/folder.png"))
        self.pushButton_2.clicked.connect(self.setDownloadPath)

        self.closeButton.setIcon(QIcon("../Pic/close.png"))
        self.closeButton.clicked.connect(self.closeButton_clicked)

        self.showMiniButton.setIcon(QIcon("../Pic/mini.png"))
        self.showMiniButton.clicked.connect(self.showMinipushButton_clicked)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def setDownloadPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,"浏览")
        self.lineEdit_2.setText(download_path)
    def getDownload_path(self):
        download_path = self.lineEdit_2.text()
        return download_path

    def getUrl(self):
         url = self.lineEdit.text()
         return url
    def download(self):
        url = self.getUrl()
        download_path = self.getDownload_path()
        message=''
        confirm = 1
        song = Songinfo(url)

        if(url==''):
            message+='请输入链接 '
            confirm = 0
        if(url!='' and song.getSongUrl()==0):
            message+=' 链接不可用 '
            confirm = 0
        if(download_path==''):
            message+=' 请选择下载地址 '
            confirm = 0
        if(confirm==0):
            self.messageBox(message)
        else:
            download_url=song.getSongUrl()
            #下载
            downloadfile(download_path,download_url)
            return
    def messageBox(self,message):
        reply = QMessageBox.information(self, 'Message', message, QMessageBox.Yes  |  QMessageBox.No, QMessageBox.No)
    def closeButton_clicked(self):
        """
        关闭窗口
        """
        self.close()

    def showMinipushButton_clicked(self):
        """
        最小化窗口
        """
        self.showMinimized()