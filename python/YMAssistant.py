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