# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\workspace\FlatWidget\python\ui\MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 535)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMouseTracking(True)
        Form.setStyleSheet("background-color: rgb(7, 7, 7);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MenuWidget = QtWidgets.QWidget(Form)
        self.MenuWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.MenuWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.MenuWidget.setMouseTracking(True)
        self.MenuWidget.setAutoFillBackground(False)
        self.MenuWidget.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"border: 1px solid white;\n"
"border-color: rgb(60, 60, 60);")
        self.MenuWidget.setObjectName("MenuWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MenuWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IconPushButton = QtWidgets.QPushButton(self.MenuWidget)
        self.IconPushButton.setEnabled(True)
        self.IconPushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.IconPushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.IconPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.IconPushButton.setAutoFillBackground(False)
        self.IconPushButton.setStyleSheet("border:0px;")
        self.IconPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../assets/pictures/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconPushButton.setIcon(icon)
        self.IconPushButton.setIconSize(QtCore.QSize(32, 32))
        self.IconPushButton.setFlat(True)
        self.IconPushButton.setObjectName("IconPushButton")
        self.horizontalLayout.addWidget(self.IconPushButton)
        self.TitlePushButton = QtWidgets.QPushButton(self.MenuWidget)
        self.TitlePushButton.setEnabled(True)
        self.TitlePushButton.setMinimumSize(QtCore.QSize(152, 40))
        self.TitlePushButton.setMaximumSize(QtCore.QSize(152, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TitlePushButton.setFont(font)
        self.TitlePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TitlePushButton.setAutoFillBackground(False)
        self.TitlePushButton.setStyleSheet("border:0px;\n"
"color: rgb(111, 72, 65);")
        self.TitlePushButton.setFlat(True)
        self.TitlePushButton.setObjectName("TitlePushButton")
        self.horizontalLayout.addWidget(self.TitlePushButton)
        self.TitleLabel = QtWidgets.QLabel(self.MenuWidget)
        self.TitleLabel.setStyleSheet("border: 0px;")
        self.TitleLabel.setText("")
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.ControlWidget = QtWidgets.QWidget(self.MenuWidget)
        self.ControlWidget.setMinimumSize(QtCore.QSize(160, 40))
        self.ControlWidget.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ControlWidget.setStyleSheet("border: 0px;")
        self.ControlWidget.setObjectName("ControlWidget")
        self.CloseButton = QtWidgets.QPushButton(self.ControlWidget)
        self.CloseButton.setGeometry(QtCore.QRect(114, 0, 38, 38))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CloseButton.setFont(font)
        self.CloseButton.setMouseTracking(False)
        self.CloseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CloseButton.setStyleSheet("QPushButton::hover\n"
"{\n"
"    background-color: rgb(232, 17, 35);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: rgb(160, 160, 160);\n"
"}")
        self.CloseButton.setFlat(True)
        self.CloseButton.setObjectName("CloseButton")
        self.MaxButton = QtWidgets.QPushButton(self.ControlWidget)
        self.MaxButton.setGeometry(QtCore.QRect(76, 0, 38, 38))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MaxButton.setFont(font)
        self.MaxButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MaxButton.setStyleSheet("QPushButton::hover\n"
"{\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: rgb(160, 160, 160);\n"
"}")
        self.MaxButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../assets/pictures/maximize1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MaxButton.setIcon(icon1)
        self.MaxButton.setIconSize(QtCore.QSize(12, 12))
        self.MaxButton.setFlat(True)
        self.MaxButton.setObjectName("MaxButton")
        self.MinButton = QtWidgets.QPushButton(self.ControlWidget)
        self.MinButton.setGeometry(QtCore.QRect(38, 0, 38, 38))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MinButton.setFont(font)
        self.MinButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MinButton.setStyleSheet("QPushButton::hover\n"
"{\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: rgb(160, 160, 160);\n"
"}")
        self.MinButton.setFlat(True)
        self.MinButton.setObjectName("MinButton")
        self.SettingButton = QtWidgets.QPushButton(self.ControlWidget)
        self.SettingButton.setGeometry(QtCore.QRect(1, 1, 37, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SettingButton.setFont(font)
        self.SettingButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SettingButton.setStyleSheet("QPushButton::hover\n"
"{\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: rgb(160, 160, 160);\n"
"}")
        self.SettingButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../assets/pictures/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingButton.setIcon(icon2)
        self.SettingButton.setIconSize(QtCore.QSize(25, 25))
        self.SettingButton.setFlat(True)
        self.SettingButton.setObjectName("SettingButton")
        self.horizontalLayout.addWidget(self.ControlWidget)
        self.verticalLayout.addWidget(self.MenuWidget)
        self.DisplayStackedWidget = QtWidgets.QStackedWidget(Form)
        self.DisplayStackedWidget.setStyleSheet("background-color: rgb(7, 7, 7);")
        self.DisplayStackedWidget.setObjectName("DisplayStackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.LineWidget = QtWidgets.QWidget(self.main_page)
        self.LineWidget.setObjectName("LineWidget")
        self.horizontalLayout_7.addWidget(self.LineWidget)
        self.DisplayStackedWidget.addWidget(self.main_page)
        self.verticalLayout.addWidget(self.DisplayStackedWidget)
        self.StatusWidget = QtWidgets.QWidget(Form)
        self.StatusWidget.setMinimumSize(QtCore.QSize(0, 24))
        self.StatusWidget.setMaximumSize(QtCore.QSize(16777215, 24))
        self.StatusWidget.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"border: 1px solid white;\n"
"border-color: rgb(60, 60, 60);")
        self.StatusWidget.setObjectName("StatusWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.StatusWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NewsLabel = QtWidgets.QLabel(self.StatusWidget)
        self.NewsLabel.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NewsLabel.setFont(font)
        self.NewsLabel.setStyleSheet("color: rgb(160, 160, 160);\n"
"border:0px;")
        self.NewsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NewsLabel.setObjectName("NewsLabel")
        self.horizontalLayout_2.addWidget(self.NewsLabel)
        self.StatusSpaceLabel = QtWidgets.QLabel(self.StatusWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StatusSpaceLabel.setFont(font)
        self.StatusSpaceLabel.setStyleSheet("color: rgb(160, 160, 160);\n"
"border:0px;")
        self.StatusSpaceLabel.setText("")
        self.StatusSpaceLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StatusSpaceLabel.setObjectName("StatusSpaceLabel")
        self.horizontalLayout_2.addWidget(self.StatusSpaceLabel)
        self.TimesLabel = QtWidgets.QLabel(self.StatusWidget)
        self.TimesLabel.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TimesLabel.setFont(font)
        self.TimesLabel.setStyleSheet("color: rgb(160, 160, 160);\n"
"border:0px;")
        self.TimesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimesLabel.setObjectName("TimesLabel")
        self.horizontalLayout_2.addWidget(self.TimesLabel)
        self.verticalLayout.addWidget(self.StatusWidget)

        self.retranslateUi(Form)
        self.DisplayStackedWidget.setCurrentIndex(0)
        self.MinButton.clicked.connect(Form.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitlePushButton.setText(_translate("Form", "亦梦云烟"))
        self.CloseButton.setText(_translate("Form", "×"))
        self.MinButton.setText(_translate("Form", "-"))
        self.NewsLabel.setText(_translate("Form", "状态"))
        self.TimesLabel.setText(_translate("Form", "CN 07/18  17:28:30"))

