import platform
import os
from PyQt5.QtCore import Qt, QEvent, QRect, QPoint
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QSizePolicy)
 
CONST_DRAG_BORDER_SIZE = 3
 
class FlatWidget(QWidget):
    
    def __init__(self, parent = None):
        super(FlatWidget,self).__init__(parent)
        
        self.mousePressed = False
        self.dragTop = False
        self.dragLeft = False
        self.dragRight = False
        self.dragBottom = False
        self.startGeometry = QRect()
        self._drag_track = False
        self._startPos = None
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        #为了在Windows系统下正确处理最小化函数，需要加上最小化标志按钮
        if platform.system() == 'Windows':
            self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
            
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.initUi()
               
        self.setMouseTracking(True)
        
        #监测所有子窗口的鼠标移动事件
        QApplication.instance().installEventFilter(self)
        
    def initUi(self):      
        self.setObjectName('FramelessWindow')
        
        #窗口内容部分 
        self.windowContent = QWidget()
        self.windowContent.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        self.windowFrame = QWidget(self)
        frameLayout = QVBoxLayout()
        frameLayout.setContentsMargins(0, 0, 0, 0)
        frameLayout.setSpacing(0)
        frameLayout.addWidget(self.windowContent)
        self.windowFrame.setLayout(frameLayout)
        
        #设置整个窗口的布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.windowFrame)
        self.setLayout(layout)

        self.closeEvent = self.Close
            
    def Close(self, a0):
        QApplication.instance().quit()
        os._exit(0)

    def onButtonRestoreClicked(self):
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setWindowState(Qt.WindowNoState)
        self.showNormal()
    
    def onButtonMaximizeClicked(self):
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setWindowState(Qt.WindowMaximized)
        self.showMaximized()
            
    def setContent(self, widget):
        self.windowContent.layout().addWidget(widget)                           
   
    def mouseDoubleClickEvent(self, event):
        pass
    
    def checkBorderDragging(self, event):
        if self.isMaximized():
            return
        
        globalMousePos = event.globalPos()
        if self.mousePressed:
            screen = QGuiApplication.primaryScreen()
            #除开任务栏外可用的空间
            availGeometry = screen.availableGeometry()
            h = availGeometry.height()
            w = availGeometry.width()
            screenList = screen.virtualSiblings()
            if screen in screenList:
                sz = QApplication.desktop().size()
                h = sz.height()
                w = sz.width()
            
            #右上角
            if self.dragTop and self.dragRight:
                new_w = globalMousePos.x() - self.startGeometry.x()
                new_y = globalMousePos.y()
                if new_w > 0 and new_y > 0 and new_y < h - 50:
                    new_geom = self.startGeometry
                    new_geom.setWidth(new_w)
                    new_geom.setX(self.startGeometry.x())
                    new_geom.setY(new_y)
                    self.setGeometry(new_geom)      
            #左上角
            elif self.dragTop and self.dragLeft:
                new_x = globalMousePos.x()
                new_y = globalMousePos.y()
                if new_x > 0 and new_y > 0:
                    new_geom = self.startGeometry
                    new_geom.setX(new_x)
                    new_geom.setY(new_y)
                    self.setGeometry(new_geom)                   
            #左下角
            elif self.dragBottom and self.dragLeft:
                new_h = globalMousePos.y() - self.startGeometry.y()
                new_x = globalMousePos.x()
                if new_h > 0 and new_x > 0:
                    new_geom = self.startGeometry
                    new_geom.setX(new_x)
                    new_geom.setHeight(new_h)
                    self.setGeometry(new_geom)                  
            elif self.dragTop:
                new_y = globalMousePos.y()
                if new_y > 0 and new_y < h - 50:
                    new_geom = self.startGeometry
                    new_geom.setY(new_y)
                    self.setGeometry(new_geom)
            elif self.dragLeft:
                new_x = globalMousePos.x()
                if new_x > 0 and new_x < w - 50:
                    new_geom = self.startGeometry
                    new_geom.setX(new_x)
                    self.setGeometry(new_geom)
            elif self.dragRight:
                new_w = globalMousePos.x() - self.startGeometry.x()
                if new_w > 0:
                    new_geom = self.startGeometry
                    new_geom.setWidth(new_w)
                    new_geom.setX(self.startGeometry.x())
                    self.setGeometry(new_geom)
            elif self.dragBottom:
                new_h = globalMousePos.y() - self.startGeometry.y()
                if new_h > 0:
                    new_geom = self.startGeometry
                    new_geom.setHeight(new_h)
                    new_geom.setY(self.startGeometry.y())
                    self.setGeometry(new_geom)
        else:
            #没有鼠标按下
            if self.leftBorderHit(globalMousePos) and self.topBorderHit(globalMousePos):
                self.setCursor(Qt.SizeFDiagCursor)
            elif self.rightBorderHit(globalMousePos) and self.topBorderHit(globalMousePos):
                self.setCursor(Qt.SizeBDiagCursor)
            elif self.leftBorderHit(globalMousePos) and self.bottomBorderHit(globalMousePos):
                self.setCursor(Qt.SizeBDiagCursor)
            else:
                if self.topBorderHit(globalMousePos):
                    self.setCursor(Qt.SizeVerCursor)
                elif self.leftBorderHit(globalMousePos):
                    self.setCursor(Qt.SizeHorCursor)
                elif self.rightBorderHit(globalMousePos):
                    self.setCursor(Qt.SizeHorCursor)
                elif self.bottomBorderHit(globalMousePos):
                    self.setCursor(Qt.SizeVerCursor)
                else:
                    self.dragTop = False
                    self.dragLeft = False
                    self.dragRight = False
                    self.dragBottom = False
                    self.setCursor(Qt.ArrowCursor)
                    
    def leftBorderHit(self, pos):
        rect = self.geometry()
        if pos.x() >= rect.x() and pos.x() <= (rect.x() + CONST_DRAG_BORDER_SIZE):
            return True
        return False
    
    def rightBorderHit(self, pos):
        rect = self.geometry()
        tmp = rect.x() + rect.width()
        if pos.x() <= tmp and pos.x() >= (tmp - CONST_DRAG_BORDER_SIZE):
            return True
        return False
    
    def topBorderHit(self, pos):
        rect = self.geometry()
        if pos.y() >= rect.y() and pos.y() <= (rect.y() + CONST_DRAG_BORDER_SIZE):
            return True
        return False
    
    def bottomBorderHit(self, pos):
        rect = self.geometry()
        tmp = rect.y() + rect.height()
        if pos.y() <= tmp and pos.y() >= (tmp - CONST_DRAG_BORDER_SIZE):
            return True
        return False
    
    def mousePressEvent(self, event):
        globalMousePos = self.mapToGlobal(QPoint(event.x(), event.y()))
        if event.button() == Qt.LeftButton:
            if event.y() < 30:
                self._drag_track = True
                self._startPos = globalMousePos

        self.mousePressed = True
        self.startGeometry = self.geometry()
        
        if self.isMaximized():
            return
        
        if self.leftBorderHit(globalMousePos) and self.topBorderHit(globalMousePos):
            self.dragTop = True
            self.dragLeft = True
            self.setCursor(Qt.SizeFDiagCursor)
        elif self.rightBorderHit(globalMousePos) and self.topBorderHit(globalMousePos):
            self.dragTop = True
            self.dragRight = True
            self.setCursor(Qt.SizeBDiagCursor)
        elif self.leftBorderHit(globalMousePos) and self.bottomBorderHit(globalMousePos):
            self.dragLeft = True
            self.dragBottom = True
            self.setCursor(Qt.SizeBDiagCursor)
        else:
            if self.topBorderHit(globalMousePos):
                self.dragTop = True
                self.setCursor(Qt.SizeVerCursor)
            elif self.leftBorderHit(globalMousePos):
                self.dragLeft = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.rightBorderHit(globalMousePos):
                self.dragRight = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.bottomBorderHit(globalMousePos):
                self.dragBottom = True
                self.setCursor(Qt.SizeVerCursor)
                
    def mouseReleaseEvent(self, event):
        if self.isMaximized():
            return
        
        self.mousePressed = False
        switchBackCursorNeeded = self.dragTop and self.dragLeft and self.dragRight and self.dragBottom
        self.dragTop = False
        self.dragLeft = False
        self.dragRight = False
        self.dragBottom = False
        if switchBackCursorNeeded:
            self.setCursor(Qt.ArrowCursor)

        if event.button() == Qt.LeftButton:
            self._drag_track = False
            self._startPos = None
          
    def mouseMoveEvent(self, event):
        if self._drag_track:
            globalMousePos = self.mapToGlobal(QPoint(event.x(), event.y()))
            self._endPos = globalMousePos - self._startPos
            if self.isMaximized():
                x_ratio = globalMousePos.x() / self.width()
                y_ratio = globalMousePos.y() / self.height()
                self.showNormal()
                new_x, new_y = globalMousePos.x() - x_ratio*self.width(), globalMousePos.y()-self._endPos.y()
                self.move(new_x, new_y)
                return
            self.move(self.pos() + self._endPos)
            self._startPos = globalMousePos

    def eventFilter(self, watched, event):
        # 当鼠标在对象上移动时，检查鼠标移动事件
        if event.type() == QEvent.MouseMove and event:
            self.checkBorderDragging(event)       
        #只有在frame window上时，才触发按下事件
        elif event.type() == QEvent.MouseButtonPress and watched is self:
            if event:
                self.mousePressEvent(event)
        elif event.type() == QEvent.MouseButtonRelease:
            if self.mousePressed and event:
                self.mouseReleaseEvent(event)
                
        return QWidget.eventFilter(self, watched, event)
