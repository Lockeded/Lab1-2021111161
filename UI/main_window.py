import time,math,json,sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QGraphicsView, QGraphicsScene, 
                             QGraphicsItem, QGraphicsTextItem,QMainWindow,QDesktopWidget,QStyle,QFileDialog)
from PyQt5.QtCore import QTimer, Qt, QRectF,qAbs, QLineF, QPointF, qrand, QRectF, QSizeF, qsrand,Qt, QTime
from PyQt5.QtGui import QPen, QBrush, QColor, QFont,QMouseEvent,QRadialGradient,QPainter,QBrush, QColor, QLinearGradient, QPainter,QPainterPath, QPen, QPolygonF, QRadialGradient
from qfluentwidgets import *
from .Ui_window import Ui_MainWindow
#from window_ui import Ui_MainWindow
from PyQt5 import QtCore
from qframelesswindow import FramelessMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
# 定义节点类，继承自QGraphicsItem
import threading
# 定义主窗口类，继承自QWidget
class MainWindow(FramelessMainWindow,Ui_MainWindow):
    def __init__(self,graph):
        super().__init__()
        self.setupUi(self)
        self.setCenter()
        self.graph = graph

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.offset)
            
    def setCenter(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
    
    def openFileDialogSlot(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*);;文本文件 (*.txt);;图片文件 (*.jpg *.png)")    
        if file_path:
            print(f"选定的文件路径: {file_path}")
            self.graph.read_txt(file_path)
            self.graph.print_graph()
            self.graphImage.setStyleSheet(f"border-image: url('graph.png');")
    def queryBridgeWord(self):
        start = self.LineEdit.text()
        end = self.LineEdit_2.text()
        bridge = self.graph.query(start, end)
        print(bridge)
        self.CaptionLabel_2.setText(bridge)
    def generateSentence(self):
        words = self.LineEdit_3.text()
        sentence = self.graph.generate_sentence(words)
        self.CaptionLabel.setText(sentence)
    def calcShortestPath(self):
        start = self.LineEdit_4.text()
        end = self.LineEdit_5.text()
        if(start == ''):
            (distances,paths) = self.graph.shortest_path(end)
            if isinstance(paths,str):
                self.CaptionLabel_4.setText(paths)
                return
            s = ("到达所有节点的最短路径如下:\n")
            for key in paths.keys():
                if end!=key:
                    s = s+key+':'+'->'.join(paths[key])+'\n'
            self.CaptionLabel_4.setText(s)
        elif(end == ''):
            (distances,paths) = self.graph.shortest_path(start)
            if isinstance(paths,str):
                self.CaptionLabel_4.setText(paths)
                return
            s = ("到达所有节点的最短路径如下:\n")
            for key in paths.keys():
                if start!=key:
                    s = s+key+':'+'->'.join(paths[key])+'\n'
            self.CaptionLabel_4.setText(s)
        else:
            s = self.graph.shortest_path(start, end)
            if isinstance(s,tuple):
                self.CaptionLabel_4.setText(s[1])
                return
            self.CaptionLabel_4.setText(s)
            self.graphImage.setStyleSheet(f"border-image: url('graph.png');")
            print(s)
            
    def randomWalk(self):
        if self.PrimaryPushButton_3.isChecked():
            self.PrimaryPushButton_3.setText('结束随机游走')
            print('random walk on')
            self.graph.stop = False
            t1 = threading.Thread(target=self.graph.random_walk)
            t2 = threading.Thread(target=self.setRandomWalk)
            t1.start()
            t2.start()
        else:
            self.PrimaryPushButton_3.setText('开始随机游走')
            print('random walk off')
            self.graph.stop = True

    def setRandomWalk(self):
        while True:
            time.sleep(0.1)
            if self.graph.done:
                self.PrimaryPushButton_3.setChecked(False)
                self.PrimaryPushButton_3.setText('开始随机游走')
                with open('traversal_path.txt','r') as f:
                    s = f.read()
                self.CaptionLabel_3.setText(s)
                return

def qt_start(graph):
    # 创建应用对象
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 创建主窗口对象
    window = MainWindow(graph)
    qsrand(QTime(0,0,0).secsTo(QTime.currentTime()))
    # 显示主窗口
    window.show()
    # 进入应用的事件循环
    sys.exit(app.exec_())