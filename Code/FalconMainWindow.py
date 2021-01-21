# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FalconMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 865)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OriginalImglabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OriginalImglabel.sizePolicy().hasHeightForWidth())
        self.OriginalImglabel.setSizePolicy(sizePolicy)
        self.OriginalImglabel.setAcceptDrops(True)
        self.OriginalImglabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100), stop:1\n"
"rgba(158,232,250,100)); \n"
"  border: 2px dashed rgba(205,92,92,255);\n"
"  color: black;\n"
"  padding: 15px 32px;\n"
"  border-radius:20px;\n"
"  text-align: center;\n"
"  font-size: 16px;")
        self.OriginalImglabel.setObjectName("OriginalImglabel")
        self.gridLayout_2.addWidget(self.OriginalImglabel, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.CutImglabel = QtWidgets.QLabel(self.groupBox_3)
        self.CutImglabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100), stop:1\n"
"rgba(251,218,222,100)); \n"
"  border: 2px dashed rgba(205,92,92,255);\n"
"  color: black;\n"
"  padding: 15px 32px;\n"
"  border-radius:20px;\n"
"  text-align: center;\n"
"  font-size: 16px;")
        self.CutImglabel.setObjectName("CutImglabel")
        self.gridLayout_3.addWidget(self.CutImglabel, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.OpenImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImgButton.setObjectName("OpenImgButton")
        self.verticalLayout_2.addWidget(self.OpenImgButton)
        self.CutImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.CutImgButton.setObjectName("CutImgButton")
        self.verticalLayout_2.addWidget(self.CutImgButton)
        self.RecogniteImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecogniteImgButton.setObjectName("RecogniteImgButton")
        self.verticalLayout_2.addWidget(self.RecogniteImgButton)
        self.ClearImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearImgButton.setObjectName("ClearImgButton")
        self.verticalLayout_2.addWidget(self.ClearImgButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ResultImglabel = QtWidgets.QLabel(self.groupBox_2)
        self.ResultImglabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100), stop:1\n"
"rgba(251,218,222,100)); \n"
"  border: 2px dashed rgba(205,92,92,255);\n"
"  color: black;\n"
"  padding: 15px 32px;\n"
"  border-radius:20px;\n"
"  text-align: center;\n"
"  font-size: 16px;")
        self.ResultImglabel.setObjectName("ResultImglabel")
        self.gridLayout_4.addWidget(self.ResultImglabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SaveImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveImgButton.setObjectName("SaveImgButton")
        self.horizontalLayout_2.addWidget(self.SaveImgButton)
        self.ExportExcelButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportExcelButton.setObjectName("ExportExcelButton")
        self.horizontalLayout_2.addWidget(self.ExportExcelButton)
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setObjectName("QuitButton")
        self.horizontalLayout_2.addWidget(self.QuitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionPerferences = QtWidgets.QAction(MainWindow)
        self.actionPerferences.setObjectName("actionPerferences")
        self.actionLanguage = QtWidgets.QAction(MainWindow)
        self.actionLanguage.setObjectName("actionLanguage")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menu.addAction(self.actionPerferences)
        self.menu.addSeparator()
        self.menu.addAction(self.actionLanguage)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.QuitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像识别"))
        self.groupBox.setTitle(_translate("MainWindow", "原始图片"))
        self.OriginalImglabel.setText(_translate("MainWindow", "拖拽到这里显示图片"))
        self.groupBox_3.setTitle(_translate("MainWindow", "裁剪结果"))
        self.CutImglabel.setText(_translate("MainWindow", "点击裁剪按钮，显示裁剪结果"))
        self.OpenImgButton.setText(_translate("MainWindow", "打开"))
        self.CutImgButton.setText(_translate("MainWindow", "裁剪"))
        self.RecogniteImgButton.setText(_translate("MainWindow", "识别"))
        self.ClearImgButton.setText(_translate("MainWindow", "清空"))
        self.groupBox_2.setTitle(_translate("MainWindow", "识别结果"))
        self.ResultImglabel.setText(_translate("MainWindow", "点击识别按钮，显示识别结果"))
        self.SaveImgButton.setText(_translate("MainWindow", "保存结果图片"))
        self.ExportExcelButton.setText(_translate("MainWindow", "导出Excel"))
        self.QuitButton.setText(_translate("MainWindow", "退出"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionPerferences.setText(_translate("MainWindow", "Perferences"))
        self.actionLanguage.setText(_translate("MainWindow", "Language"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        
        
        
        
        
        
