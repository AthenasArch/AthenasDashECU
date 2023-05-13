# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashAthenasyYdmNr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

from analoggaugewidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMaximumSize(QSize(1200, 1000))
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1199, 1000))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, -10, 950, 750))
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(1200, 1000))
        font1 = QFont()
        font1.setFamilies([u"DS-Digital"])
        font1.setPointSize(12)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.page_0_main = QWidget()
        self.page_0_main.setObjectName(u"page_0_main")
        self.btnPage2 = QPushButton(self.page_0_main)
        self.btnPage2.setObjectName(u"btnPage2")
        self.btnPage2.setGeometry(QRect(280, 120, 250, 150))
        font2 = QFont()
        font2.setFamilies([u"DS-Digital"])
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.btnPage2.setFont(font2)
        self.btnPage2.setAutoFillBackground(False)
        self.btnPage2.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.btnPage3 = QPushButton(self.page_0_main)
        self.btnPage3.setObjectName(u"btnPage3")
        self.btnPage3.setGeometry(QRect(540, 120, 250, 150))
        self.btnPage3.setFont(font2)
        self.btnPage3.setAutoFillBackground(False)
        self.btnPage3.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.btnPage1 = QPushButton(self.page_0_main)
        self.btnPage1.setObjectName(u"btnPage1")
        self.btnPage1.setGeometry(QRect(20, 120, 250, 150))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.btnPage1.setFont(font3)
        self.btnPage1.setMouseTracking(True)
        self.btnPage1.setTabletTracking(False)
        self.btnPage1.setAutoFillBackground(False)
        self.btnPage1.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 25px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.label_6 = QLabel(self.page_0_main)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 10, 561, 61))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(25)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.btnPage5 = QPushButton(self.page_0_main)
        self.btnPage5.setObjectName(u"btnPage5")
        self.btnPage5.setGeometry(QRect(280, 290, 250, 150))
        self.btnPage5.setFont(font2)
        self.btnPage5.setAutoFillBackground(False)
        self.btnPage5.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.btnPage6 = QPushButton(self.page_0_main)
        self.btnPage6.setObjectName(u"btnPage6")
        self.btnPage6.setGeometry(QRect(540, 290, 250, 150))
        self.btnPage6.setFont(font2)
        self.btnPage6.setAutoFillBackground(False)
        self.btnPage6.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.btnPage4 = QPushButton(self.page_0_main)
        self.btnPage4.setObjectName(u"btnPage4")
        self.btnPage4.setGeometry(QRect(20, 290, 250, 150))
        self.btnPage4.setFont(font2)
        self.btnPage4.setMouseTracking(True)
        self.btnPage4.setTabletTracking(False)
        self.btnPage4.setAutoFillBackground(False)
        self.btnPage4.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.stackedWidget.addWidget(self.page_0_main)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.bntReturn_1 = QPushButton(self.page_1)
        self.bntReturn_1.setObjectName(u"bntReturn_1")
        self.bntReturn_1.setGeometry(QRect(210, 310, 250, 150))
        self.bntReturn_1.setFont(font2)
        self.bntReturn_1.setAutoFillBackground(False)
        self.bntReturn_1.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 180, 351, 61))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(18)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.bntReturn_2 = QPushButton(self.page_2)
        self.bntReturn_2.setObjectName(u"bntReturn_2")
        self.bntReturn_2.setGeometry(QRect(250, 260, 250, 150))
        self.bntReturn_2.setFont(font2)
        self.bntReturn_2.setAutoFillBackground(False)
        self.bntReturn_2.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 140, 351, 61))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.bntReturn_3 = QPushButton(self.page_3)
        self.bntReturn_3.setObjectName(u"bntReturn_3")
        self.bntReturn_3.setGeometry(QRect(570, 20, 211, 51))
        self.bntReturn_3.setFont(font2)
        self.bntReturn_3.setAutoFillBackground(False)
        self.bntReturn_3.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: DS-Digital;\n"
"            font-size: 45px;\n"
"            font-weight: bold;\n"
"            padding: 13px 32px;\n"
"            text-decoration: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #4cc7c9, stop: 1 #630303);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.label_28 = QLabel(self.page_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(250, 30, 281, 54))
        font6 = QFont()
        font6.setFamilies([u"DS-Digital"])
        font6.setPointSize(45)
        font6.setBold(True)
        self.label_28.setFont(font6)
        self.label_28.setLayoutDirection(Qt.LeftToRight)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28.setAlignment(Qt.AlignCenter)
        self.widgetSpeed = AnalogGaugeWidget(self.page_3)
        self.widgetSpeed.setObjectName(u"widgetSpeed")
        self.widgetSpeed.setGeometry(QRect(10, 90, 300, 300))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widgetSpeed.sizePolicy().hasHeightForWidth())
        self.widgetSpeed.setSizePolicy(sizePolicy1)
        self.widgetSpeed.setMinimumSize(QSize(300, 300))
        self.widgetSpeed.setMaximumSize(QSize(600, 600))
        self.widgetSpeed.setBaseSize(QSize(300, 300))
        self.widgetSpeed.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout = QHBoxLayout(self.widgetSpeed)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetRPM = AnalogGaugeWidget(self.page_3)
        self.widgetRPM.setObjectName(u"widgetRPM")
        self.widgetRPM.setGeometry(QRect(330, 90, 300, 300))
        sizePolicy1.setHeightForWidth(self.widgetRPM.sizePolicy().hasHeightForWidth())
        self.widgetRPM.setSizePolicy(sizePolicy1)
        self.widgetRPM.setMinimumSize(QSize(300, 300))
        self.widgetRPM.setMaximumSize(QSize(600, 600))
        self.widgetRPM.setBaseSize(QSize(300, 300))
        self.widgetRPM.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetRPM)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetTPS = AnalogGaugeWidget(self.page_3)
        self.widgetTPS.setObjectName(u"widgetTPS")
        self.widgetTPS.setGeometry(QRect(650, 90, 300, 300))
        sizePolicy1.setHeightForWidth(self.widgetTPS.sizePolicy().hasHeightForWidth())
        self.widgetTPS.setSizePolicy(sizePolicy1)
        self.widgetTPS.setMinimumSize(QSize(300, 300))
        self.widgetTPS.setMaximumSize(QSize(600, 600))
        self.widgetTPS.setBaseSize(QSize(300, 300))
        self.widgetTPS.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout_3 = QHBoxLayout(self.widgetTPS)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widgetPW = AnalogGaugeWidget(self.page_3)
        self.widgetPW.setObjectName(u"widgetPW")
        self.widgetPW.setGeometry(QRect(10, 410, 300, 300))
        sizePolicy1.setHeightForWidth(self.widgetPW.sizePolicy().hasHeightForWidth())
        self.widgetPW.setSizePolicy(sizePolicy1)
        self.widgetPW.setMinimumSize(QSize(300, 300))
        self.widgetPW.setMaximumSize(QSize(600, 600))
        self.widgetPW.setBaseSize(QSize(300, 300))
        self.widgetPW.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout_4 = QHBoxLayout(self.widgetPW)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widgetDuty = AnalogGaugeWidget(self.page_3)
        self.widgetDuty.setObjectName(u"widgetDuty")
        self.widgetDuty.setGeometry(QRect(330, 410, 300, 300))
        sizePolicy1.setHeightForWidth(self.widgetDuty.sizePolicy().hasHeightForWidth())
        self.widgetDuty.setSizePolicy(sizePolicy1)
        self.widgetDuty.setMinimumSize(QSize(300, 300))
        self.widgetDuty.setMaximumSize(QSize(600, 600))
        self.widgetDuty.setBaseSize(QSize(300, 300))
        self.widgetDuty.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout_5 = QHBoxLayout(self.widgetDuty)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widgetMAP = AnalogGaugeWidget(self.page_3)
        self.widgetMAP.setObjectName(u"widgetMAP")
        self.widgetMAP.setGeometry(QRect(650, 410, 300, 300))
        sizePolicy1.setHeightForWidth(self.widgetMAP.sizePolicy().hasHeightForWidth())
        self.widgetMAP.setSizePolicy(sizePolicy1)
        self.widgetMAP.setMinimumSize(QSize(300, 300))
        self.widgetMAP.setMaximumSize(QSize(600, 600))
        self.widgetMAP.setBaseSize(QSize(300, 300))
        self.widgetMAP.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetMAP)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Athenas Dash ECU", None))
        self.btnPage2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.btnPage3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.btnPage1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ATHENAS DASH ECU - V0.1.12", None))
        self.btnPage5.setText(QCoreApplication.translate("MainWindow", u"PAGE 5", None))
        self.btnPage6.setText(QCoreApplication.translate("MainWindow", u"PAGE 6", None))
        self.btnPage4.setText(QCoreApplication.translate("MainWindow", u"PAGE 4", None))
        self.bntReturn_1.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.bntReturn_2.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.bntReturn_3.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"MEDIDORES", None))
    # retranslateUi

