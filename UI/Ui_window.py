# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\10139\Documents\SoftwareEngineering\lab1\UI\multi_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        font = QtGui.QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{border-image: url(:/image/010 Winter Neva.png);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(108 ,166 ,205);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.round = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.round.sizePolicy().hasHeightForWidth())
        self.round.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("STXihei")
        font.setPointSize(15)
        font.setBold(False)
        self.round.setFont(font)
        self.round.setStyleSheet("")
        self.round.setText("")
        self.round.setObjectName("round")
        self.horizontalLayout_4.addWidget(self.round)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setStyleSheet("border:none;\n"
"background-color:transparent\n"
"")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/8666820_minus_delete_remove_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setStyleSheet("border:none;\n"
"background-color:transparent")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/8666595_x_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CardWidget_3 = CardWidget(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget_3.sizePolicy().hasHeightForWidth())
        self.CardWidget_3.setSizePolicy(sizePolicy)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.label_2 = QtWidgets.QLabel(self.CardWidget_3)
        self.label_2.setGeometry(QtCore.QRect(55, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.IconWidget_8 = IconWidget(self.CardWidget_3)
        self.IconWidget_8.setGeometry(QtCore.QRect(60, 180, 111, 91))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/7830791_desktop_monitor_upload_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_8.setIcon(icon2)
        self.IconWidget_8.setObjectName("IconWidget_8")
        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget_3)
        self.PrimaryPushButton.setGeometry(QtCore.QRect(45, 120, 153, 32))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.PrimaryPushButton.setFont(font)
        self.PrimaryPushButton.setAutoDefault(False)
        self.PrimaryPushButton.setDefault(False)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.verticalLayout_7.addWidget(self.CardWidget_3)
        self.CardWidget = CardWidget(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setObjectName("CardWidget")
        self.label_4 = QtWidgets.QLabel(self.CardWidget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LineEdit = LineEdit(self.CardWidget)
        self.LineEdit.setGeometry(QtCore.QRect(60, 60, 128, 33))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.LineEdit.setFont(font)
        self.LineEdit.setText("")
        self.LineEdit.setObjectName("LineEdit")
        self.LineEdit_2 = LineEdit(self.CardWidget)
        self.LineEdit_2.setGeometry(QtCore.QRect(60, 100, 128, 33))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.PushButton = PushButton(self.CardWidget)
        self.PushButton.setGeometry(QtCore.QRect(70, 150, 102, 32))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.SimpleCardWidget = SimpleCardWidget(self.CardWidget)
        self.SimpleCardWidget.setGeometry(QtCore.QRect(20, 210, 211, 91))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.CaptionLabel_2 = CaptionLabel(self.SimpleCardWidget)
        self.CaptionLabel_2.setGeometry(QtCore.QRect(10, 10, 191, 71))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.CaptionLabel_2.setFont(font)
        self.CaptionLabel_2.setText("")
        self.CaptionLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_2.setWordWrap(True)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.verticalLayout_7.addWidget(self.CardWidget)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ElevatedCardWidget = ElevatedCardWidget(self.frame_10)
        self.ElevatedCardWidget.setStyleSheet("")
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        self.InfoBadge = InfoBadge(self.ElevatedCardWidget)
        self.InfoBadge.setGeometry(QtCore.QRect(130, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(18)
        font.setBold(False)
        self.InfoBadge.setFont(font)
        self.InfoBadge.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoBadge.setObjectName("InfoBadge")
        self.graphImage = QtWidgets.QFrame(self.ElevatedCardWidget)
        self.graphImage.setGeometry(QtCore.QRect(40, 70, 351, 351))
        self.graphImage.setStyleSheet("")
        self.graphImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphImage.setObjectName("graphImage")
        self.verticalLayout_8.addWidget(self.ElevatedCardWidget)
        self.CardWidget_5 = CardWidget(self.frame_10)
        self.CardWidget_5.setObjectName("CardWidget_5")
        self.label_7 = QtWidgets.QLabel(self.CardWidget_5)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.LineEdit_3 = LineEdit(self.CardWidget_5)
        self.LineEdit_3.setGeometry(QtCore.QRect(30, 60, 301, 33))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.LineEdit_3.setFont(font)
        self.LineEdit_3.setText("")
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.PushButton_3 = PushButton(self.CardWidget_5)
        self.PushButton_3.setGeometry(QtCore.QRect(340, 60, 61, 32))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.PushButton_3.setFont(font)
        self.PushButton_3.setObjectName("PushButton_3")
        self.SimpleCardWidget_2 = SimpleCardWidget(self.CardWidget_5)
        self.SimpleCardWidget_2.setGeometry(QtCore.QRect(40, 110, 331, 61))
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.CaptionLabel = CaptionLabel(self.SimpleCardWidget_2)
        self.CaptionLabel.setGeometry(QtCore.QRect(0, 0, 331, 61))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setText("")
        self.CaptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel.setWordWrap(True)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.verticalLayout_8.addWidget(self.CardWidget_5)
        self.verticalLayout_8.setStretch(0, 7)
        self.verticalLayout_8.setStretch(1, 3)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.CardWidget_4 = CardWidget(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget_4.sizePolicy().hasHeightForWidth())
        self.CardWidget_4.setSizePolicy(sizePolicy)
        self.CardWidget_4.setObjectName("CardWidget_4")
        self.label_6 = QtWidgets.QLabel(self.CardWidget_4)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.PrimaryPushButton_2 = PrimaryPushButton(self.CardWidget_4)
        self.PrimaryPushButton_2.setGeometry(QtCore.QRect(180, 120, 61, 32))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.PrimaryPushButton_2.setFont(font)
        self.PrimaryPushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PrimaryPushButton_2.setObjectName("PrimaryPushButton_2")
        self.LineEdit_4 = LineEdit(self.CardWidget_4)
        self.LineEdit_4.setGeometry(QtCore.QRect(40, 90, 128, 33))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(12)
        font.setBold(False)
        self.LineEdit_4.setFont(font)
        self.LineEdit_4.setInputMask("")
        self.LineEdit_4.setText("")
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.LineEdit_5 = LineEdit(self.CardWidget_4)
        self.LineEdit_5.setGeometry(QtCore.QRect(40, 140, 128, 33))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(12)
        font.setBold(False)
        self.LineEdit_5.setFont(font)
        self.LineEdit_5.setObjectName("LineEdit_5")
        self.CardWidget_6 = CardWidget(self.CardWidget_4)
        self.CardWidget_6.setGeometry(QtCore.QRect(20, 200, 211, 101))
        self.CardWidget_6.setObjectName("CardWidget_6")
        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_4.setGeometry(QtCore.QRect(0, 0, 211, 101))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.CaptionLabel_4.setFont(font)
        self.CaptionLabel_4.setText("")
        self.CaptionLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_4.setWordWrap(True)
        self.CaptionLabel_4.setObjectName("CaptionLabel_4")
        self.verticalLayout_9.addWidget(self.CardWidget_4)
        self.CardWidget_2 = CardWidget(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget_2.sizePolicy().hasHeightForWidth())
        self.CardWidget_2.setSizePolicy(sizePolicy)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.label_5 = QtWidgets.QLabel(self.CardWidget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(15)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.PrimaryPushButton_3 = PrimaryPushButton(self.CardWidget_2)
        self.PrimaryPushButton_3.setGeometry(QtCore.QRect(60, 100, 141, 32))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.PrimaryPushButton_3.setFont(font)
        self.PrimaryPushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PrimaryPushButton_3.setObjectName("PrimaryPushButton_3")
        self.CardWidget_7 = CardWidget(self.CardWidget_2)
        self.CardWidget_7.setGeometry(QtCore.QRect(30, 160, 201, 131))
        self.CardWidget_7.setObjectName("CardWidget_7")
        self.CaptionLabel_3 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_3.setGeometry(QtCore.QRect(0, 0, 201, 131))
        font = QtGui.QFont()
        font.setFamily("YouYuan")
        font.setPointSize(11)
        font.setBold(False)
        self.CaptionLabel_3.setFont(font)
        self.CaptionLabel_3.setText("")
        self.CaptionLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_3.setWordWrap(True)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.verticalLayout_9.addWidget(self.CardWidget_2)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 3)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(MainWindow.showMinimized) # type: ignore
        self.pushButton_7.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.PrimaryPushButton.clicked.connect(self.openFileDialogSlot) # type: ignore
        self.PushButton.clicked.connect(self.queryBridgeWord) # type: ignore
        self.PushButton_3.clicked.connect(self.generateSentence) # type: ignore
        self.PrimaryPushButton_2.clicked.connect(self.calcShortestPath) # type: ignore
        self.PrimaryPushButton_3.clicked.connect(self.randomWalk) # type: ignore
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "结对编程可视化"))
        self.label_2.setText(_translate("MainWindow", "选择文本文件"))
        self.PrimaryPushButton.setText(_translate("MainWindow", "点击此处上传"))
        self.label_4.setText(_translate("MainWindow", "查询桥接词"))
        self.LineEdit.setPlaceholderText(_translate("MainWindow", "word_1"))
        self.LineEdit_2.setPlaceholderText(_translate("MainWindow", "word_2"))
        self.PushButton.setText(_translate("MainWindow", "提交查询"))
        self.InfoBadge.setText(_translate("MainWindow", "文本有向图"))
        self.label_7.setText(_translate("MainWindow", "生成新文本"))
        self.PushButton_3.setText(_translate("MainWindow", "生成"))
        self.label_6.setText(_translate("MainWindow", "计算最短路径"))
        self.PrimaryPushButton_2.setText(_translate("MainWindow", "提交"))
        self.LineEdit_4.setPlaceholderText(_translate("MainWindow", "word_1"))
        self.LineEdit_5.setPlaceholderText(_translate("MainWindow", "word_2"))
        self.label_5.setText(_translate("MainWindow", "随机游走"))
        self.PrimaryPushButton_3.setText(_translate("MainWindow", "开始随机游走"))
from qfluentwidgets import CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget, InfoBadge, LineEdit, PrimaryPushButton, PushButton, SimpleCardWidget
from . import ui_rc