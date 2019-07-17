# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/3--17:06

import sys
import Spiders.mainWindow
import requests
from PyQt5.QtWidgets import *
from Spiders.mainWindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    # print('*' * 30 + '欢迎来到音乐下载助手' + '*' * 30)
    # url = input('[请输入歌曲/FM的网址链接]:')
    # main(url)

    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    myWin = MainWindow()

    # 显示在屏幕上
    myWin.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())

#下载
# f = urllib.request.urlopen(url)
# >>> data=f.read()
# >>> if __name__ == '__main__':
# 	with open("F:/tes.mp3", 'wb') as code:
# 		code.write(data)
#command disable
# from subprocess import run
#command2 = 'you-get -o f: url'

#run(command2,shell=True)

#可用：网易云 千千百度 酷我 echo回声 九天音乐 365音乐 一听 5sing 唱吧 qq音乐 荔枝FM
