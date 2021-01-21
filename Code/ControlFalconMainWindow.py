# author:Hongkun Xu 
# datetime:2020/03/11 16:14
# software: PyCharm
"""
説明： 界面控制逻辑
"""
import os
import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from FalconMainWindow import Ui_MainWindow
from Falcon import CropPicture
import webbrowser

class ControlFalconMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ControlFalconMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.file = None
        self.filePath = None

        self.actionOpen.triggered.connect(self.OpenImg)
        self.actionClose.triggered.connect(self.ClearImgs)

        self.OpenImgButton.clicked.connect(self.OpenImg)     # 打开图片
        self.ClearImgButton.clicked.connect(self.ClearImgs)  # 清空图片
        self.CutImgButton.clicked.connect(self.CutImg)       # 裁剪图片

        self.actionAbout.triggered.connect(self.Goto)        # 跳转到我的Github首页

    def OpenImg(self):
        """载入图片"""
        file, ok = QFileDialog.getOpenFileName(self, "打开", "./", "Image Files(*.jpg *.jpeg *.png)")
        self.file = file     # 保存图片
        if ok:
            pixmap = QPixmap(file)
            # Label高度
            width = self.OriginalImglabel.geometry().width()
            height = self.OriginalImglabel.geometry().height()
            scaredPixmap = pixmap.scaled(width, height, aspectRatioMode=Qt.KeepAspectRatio)  # 等比例缩放
            self.OriginalImglabel.setPixmap(scaredPixmap)
            # self.pushButton_Start1.setEnabled(True)   # 开始检测按钮1
            # 自适应Label大小
            # self.OriginalImglabel.setScaledContents(True)
            self.statusbar.showMessage(file)
            self.filePath = file
        else:
            self.statusbar.showMessage("获取图片地址信息失败")

    def ClearImgs(self):
        self.OriginalImglabel.setText("拖拽到这里显示图片")
        self.CutImglabel.setText("点击裁剪按钮，显示裁剪结果")
        self.ResultImglabel.setText("点击识别按钮，显示识别结果")
        self.statusbar.showMessage(" ")

    def dragEnterEvent(self, event):
        event.accept()
        print('dragEnterEvent')
        self.OriginalImglabel.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
            "rgba(251, 218, 222, 100), stop:1\n"
            "rgba(204, 44, 55, 100)); \n"
            "  border: 2px dashed rgba(205,92,92,255);\n"
            "  color: red;\n"
            "  padding: 15px 32px;\n"
            "  border-radius:20px;\n"
            "  text-align: center;\n"
            "  font-size: 16px;")

    def dropEvent(self, event):
        event.accept()
        mimeData = event.mimeData()
        print('dropEvent')
        # for mimetype in mimeData.formats():
        #     print('MIMEType:', mimetype)
        #     print('Data:', mimeData.data(mimetype))
        #     print()
        filePath = str(mimeData.data("text/uri-list"), encoding="utf-8")[8:-2]
        if os.path.exists(filePath):
            pixmap = QPixmap(filePath)
            # Label高度
            width = self.OriginalImglabel.geometry().width()
            height = self.OriginalImglabel.geometry().height()
            scaredPixmap = pixmap.scaled(self.OriginalImglabel.size(), aspectRatioMode=Qt.KeepAspectRatio)  # 等比例缩放
            self.OriginalImglabel.setPixmap(scaredPixmap)
            # 自适应Label大小
            # self.OriginalImglabel.setScaledContents(True)
            self.statusbar.showMessage(filePath)
            self.filePath = filePath
        else:
            self.statusbar.showMessage("获取图片地址信息失败")
            print(filePath)

        self.OriginalImglabel.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
            "rgba(214,249,255,100), stop:1\n"
            "rgba(158,232,250,100)); \n"
            "  border: 2px dashed rgba(205,92,92,255);\n"
            "  color: black;\n"
            "  padding: 15px 32px;\n"
            "  border-radius:20px;\n"
            "  text-align: center;\n"
            "  font-size: 16px;")

        # MIMEType: text / uri - list
        # Data: b'file:///C:/Users/jc-Xu-h/Desktop/test/test5.jpg\r\n'

    def CutImg(self):
        if self.filePath:
            ResultImg = CropPicture(self.filePath)
            show = cv2.cvtColor(ResultImg, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            showFin = QPixmap.fromImage(showImage)
            # Label高度
            width = self.OriginalImglabel.geometry().width()
            height = self.OriginalImglabel.geometry().height()
            scaredPixmap = showFin.scaled(width, height, aspectRatioMode=Qt.KeepAspectRatio)  # 等比例缩放
            self.CutImglabel.setPixmap(scaredPixmap)

    def jump(self, URL):
        return webbrowser.open(URL)

    def Goto(self):
        URL = "https://github.com/birdtianyu"
        if self.jump(URL):
            print("Success!")

    


def MyMain():
    MyApp = QApplication(sys.argv)
    MainWin = ControlFalconMainWindow()
    MainWin.show()
    sys.exit(MyApp.exec_())


if __name__ == "__main__":
    MyMain()
