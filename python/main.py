from asyncio.windows_events import NULL
import sys, os
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import threading
import time, datetime

from ui.FlatWidget import FlatWidget
import ui.Ui_MainFrame

def timestr(d):
    if len(str(d))==1:
        return '0'+str(d)
    else:
        return str(d)

class MainFrame(QObject):
    FreshUI = QtCore.pyqtSignal(str)
    def __init__(self, MainWindow, FlatWidget):
        super(MainFrame, self).__init__()
        self.MainWindow_ = MainWindow
        self.FlatWidget_ = FlatWidget

    def Init(self):
        self.MainWindow_.CloseButton.clicked.connect(self.Close)
        self.MainWindow_.IconPushButton.setIcon(QIcon("assets/pictures/icon.png"))
        self.MainWindow_.MaxButton.setIcon(QIcon("assets/pictures/maximize1.png"))
        self.MainWindow_.SettingButton.setIcon(QIcon("assets/pictures/setting.png"))
        self.MainWindow_.MaxButton.clicked.connect(self.Maximized)
        self.MainWindow_.MinButton.clicked.connect(self.Minimized)
        self.MainWindow_.TitleLabel.mouseDoubleClickEvent = self.TitleDClicked

        # time
        update_time_thread = threading.Thread(target=self.UpdateTime)
        update_time_thread.start()

        # K线图
        self.klines_ts_codes = None
        self.FlatWidget_.resizeEvent = self.WindowReiszeEvent


    # ----------------------------------------- UI -----------------------------------------
    def Maximized(self):
        if self.FlatWidget_.isMaximized():
            self.MainWindow_.MaxButton.setIcon(QIcon("assets/pictures/maximize.png"))
            self.FlatWidget_.showNormal()
        else:
            self.MainWindow_.MaxButton.setIcon(QIcon("assets/pictures/maximize1.png"))
            self.FlatWidget_.showMaximized()

    def Minimized(self):
        self.FlatWidget_.showMinimized()

    def WindowReiszeEvent(self, event):
        if self.FlatWidget_.isMaximized():
            self.MainWindow_.MaxButton.setIcon(QIcon("assets/pictures/maximize.png"))
        else:
            self.MainWindow_.MaxButton.setIcon(QIcon("assets/pictures/maximize1.png"))

    def TitleDClicked(self, event):
        self.Maximized()


    def Close(self):
        self.FlatWidget_.Close(NULL)

    # ----------------------------------------- UI end ----------------------------------------
    def SetCurrentTime(self):
        ts = datetime.datetime.now()
        ts_str = 'CN ' + timestr(ts.month)+"/"+timestr(ts.day)+"  "+timestr(ts.hour)+":"+timestr(ts.minute)+":"+timestr(ts.second)
        self.MainWindow_.TimesLabel.setText(ts_str)

    def UpdateTime(self):
        while True:
            self.SetCurrentTime()
            time.sleep(1)

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_UseSoftwareOpenGL,True)
    app = QApplication(sys.argv)
    MainWindow = FlatWidget()
    ui=ui.Ui_MainFrame.Ui_Form()
    ui.setupUi(MainWindow.windowContent)
    mainFrame = MainFrame(ui, MainWindow)
    mainFrame.Init()
    MainWindow.show()
    sys.exit(app.exec_())