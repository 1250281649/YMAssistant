import sys, os
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
import threading
import time, datetime
sys.path.append(os.getcwd() + os.path.sep + "thirdparty")
from netron.server import start
from ui.FlatWidget import FlatWidget
import ui.Ui_MainFrame
from functools import partial

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
        self.MainWindow_.NetronToolButton.setIcon(QIcon("assets/pictures/netron.png"))
        self.MainWindow_.TernimalToolButton.setIcon(QIcon("assets/pictures/ternimal.png"))
        self.MainWindow_.MaxButton.clicked.connect(self.Maximized)
        self.MainWindow_.MinButton.clicked.connect(self.Minimized)
        self.MainWindow_.TitleLabel.mouseDoubleClickEvent = self.TitleDClicked

        self.ToolMenuButtonSetupEvent()

        # time
        update_time_thread = threading.Thread(target=self.UpdateTime)
        update_time_thread.start()

        self.FlatWidget_.resizeEvent = self.WindowReiszeEvent
        self.view_layout = QVBoxLayout(self.MainWindow_.ViewWidget)
        self.view_layout.setContentsMargins(0, 0, 0, 0)
        self.browser = QWebEngineView()
        self.view_layout.addWidget(self.browser)
        
        self.address = start(None, None, browse=False)
        url_address = "http://{}:{}".format(self.address[0], self.address[1])
        self.browser.load(QUrl(url_address))

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
        self.FlatWidget_.Close(None)

    def ToolMenuButtonSetupEvent(self):
        self.MenuToolButtons = [
            self.MainWindow_.NetronToolButton,
            self.MainWindow_.TernimalToolButton,
        ]
        for i in range(len(self.MenuToolButtons)):
            self.MenuToolButtons[i].clicked.connect(partial(self.MenuToolButtonEvent, i))
        self.MenuToolButtonEvent(0)

    def MenuToolButtonEvent(self, index):
        self.MainWindow_.DisplayStackedWidget.setCurrentIndex(index)
        menu_style_str = '''
            QToolButton::hover { color: rgb(220, 220, 220); background-color: rgb(38, 38, 38);}
            QToolButton { color: rgb(160, 160, 160); border: 0px; background-color: rgb(20, 20, 20);}'''
        menu_clicked_style_str = '''
            QToolButton { color: rgb(234, 85, 4);border: 0px; background-color: rgb(0, 0, 0);}'''
        for i in range(len(self.MenuToolButtons)):
            if i==index:
                self.MenuToolButtons[i].setStyleSheet(menu_clicked_style_str)
            else:
                self.MenuToolButtons[i].setStyleSheet(menu_style_str)

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
    app = QApplication(sys.argv + ["--no-sandbox"])
    MainWindow = FlatWidget()
    ui=ui.Ui_MainFrame.Ui_Form()
    ui.setupUi(MainWindow.windowContent)
    mainFrame = MainFrame(ui, MainWindow)
    mainFrame.Init()
    MainWindow.show()
    sys.exit(app.exec_())