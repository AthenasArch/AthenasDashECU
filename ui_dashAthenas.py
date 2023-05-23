# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashAthenasaGjeJL.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

from analoggaugewidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 750)
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
        self.stackedWidget.setGeometry(QRect(-10, -20, 950, 750))
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
        font2.setFamilies([u"Verdana"])
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
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
        self.btnPage1.setFont(font2)
        self.btnPage1.setMouseTracking(True)
        self.btnPage1.setTabletTracking(False)
        self.btnPage1.setAutoFillBackground(False)
        self.btnPage1.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
        self.label_6.setGeometry(QRect(40, 30, 731, 61))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(25)
        self.label_6.setFont(font3)
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
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
        self.label_7 = QLabel(self.page_0_main)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 460, 391, 61))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(18)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.labelComStatus = QLabel(self.page_0_main)
        self.labelComStatus.setObjectName(u"labelComStatus")
        self.labelComStatus.setGeometry(QRect(440, 460, 101, 61))
        self.labelComStatus.setFont(font4)
        self.labelComStatus.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(182, 0, 0);")
        self.labelComStatus.setAlignment(Qt.AlignCenter)
        self.labelComCnt = QLabel(self.page_0_main)
        self.labelComCnt.setObjectName(u"labelComCnt")
        self.labelComCnt.setGeometry(QRect(550, 460, 101, 61))
        self.labelComCnt.setFont(font4)
        self.labelComCnt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelComCnt.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_0_main)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 30, 551, 61))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(25)
        font5.setBold(True)
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: #c586c0;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.bntReturn_1 = QPushButton(self.page_1)
        self.bntReturn_1.setObjectName(u"bntReturn_1")
        self.bntReturn_1.setGeometry(QRect(630, 30, 231, 61))
        self.bntReturn_1.setFont(font2)
        self.bntReturn_1.setAutoFillBackground(False)
        self.bntReturn_1.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
        self.comboBoxPortaCom = QComboBox(self.page_1)
        self.comboBoxPortaCom.addItem("")
        self.comboBoxPortaCom.setObjectName(u"comboBoxPortaCom")
        self.comboBoxPortaCom.setGeometry(QRect(70, 150, 121, 51))
        self.comboBoxPortaCom.setLayoutDirection(Qt.RightToLeft)
        self.comboBoxPortaCom.setStyleSheet(u"QComboBox {\n"
"	gridline-color: rgb(255, 255, 255);\n"
"    background-color: #282a36;\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 8px;\n"
"    color: #f8f8f2;\n"
"    font-family: Verdana;\n"
"    font-size: 18px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: #44475a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:on { /* quando selecionado */\n"
"    border-color: #f1fa8c;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #6272a4;\n"
"    border-left-style: solid; /* estilo de linha da esquerda - pode ser qualquer um dos seguintes: solid, dashed, dot-dash, dot-dot-dash, none */"
                        "\n"
"    border-top-right-radius: 3px; /* raio superior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"    border-bottom-right-radius: 3px; /* raio inferior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/path/to/your/image.png); /* substitua '/path/to/your/image.png' pelo caminho correto para sua imagem */\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* mude a cor do bot\u00e3o para laranja quando a caixa est\u00e1 focada */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #f8f8f2; /* cor do texto dos itens */\n"
"    background-color: #3c0a8c; /* cor de fundo dos itens */\n"
"}\n"
"\n"
"\n"
"")
        self.bntCheckPorts = QPushButton(self.page_1)
        self.bntCheckPorts.setObjectName(u"bntCheckPorts")
        self.bntCheckPorts.setGeometry(QRect(210, 150, 231, 51))
        self.bntCheckPorts.setFont(font2)
        self.bntCheckPorts.setAutoFillBackground(False)
        self.bntCheckPorts.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 18px;\n"
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
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 110, 371, 31))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"color: #c586c0;\n"
"background-color: rgb(40, 42, 54);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.bntConnect = QPushButton(self.page_1)
        self.bntConnect.setObjectName(u"bntConnect")
        self.bntConnect.setGeometry(QRect(70, 210, 371, 61))
        self.bntConnect.setFont(font2)
        self.bntConnect.setAutoFillBackground(False)
        self.bntConnect.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 18px;\n"
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
        self.debugTextTermina = QPlainTextEdit(self.page_1)
        self.debugTextTermina.setObjectName(u"debugTextTermina")
        self.debugTextTermina.setGeometry(QRect(80, 350, 781, 291))
        self.debugTextTermina.setStyleSheet(u"font: 12pt \"Consolas\";\n"
"border-color: rgb(85, 0, 127);\n"
"background-color: rgb(230, 230, 230);")
        self.debugTextTermina.setTabChangesFocus(False)
        self.comboBoxPortaCom_2 = QComboBox(self.page_1)
        self.comboBoxPortaCom_2.addItem("")
        self.comboBoxPortaCom_2.setObjectName(u"comboBoxPortaCom_2")
        self.comboBoxPortaCom_2.setGeometry(QRect(470, 230, 381, 41))
        self.comboBoxPortaCom_2.setLayoutDirection(Qt.RightToLeft)
        self.comboBoxPortaCom_2.setStyleSheet(u"QComboBox {\n"
"	gridline-color: rgb(255, 255, 255);\n"
"    background-color: #282a36;\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 8px;\n"
"    color: #f8f8f2;\n"
"    font-family: Verdana;\n"
"    font-size: 18px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: #44475a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:on { /* quando selecionado */\n"
"    border-color: #f1fa8c;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #6272a4;\n"
"    border-left-style: solid; /* estilo de linha da esquerda - pode ser qualquer um dos seguintes: solid, dashed, dot-dash, dot-dot-dash, none */"
                        "\n"
"    border-top-right-radius: 3px; /* raio superior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"    border-bottom-right-radius: 3px; /* raio inferior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/path/to/your/image.png); /* substitua '/path/to/your/image.png' pelo caminho correto para sua imagem */\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* mude a cor do bot\u00e3o para laranja quando a caixa est\u00e1 focada */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #f8f8f2; /* cor do texto dos itens */\n"
"    background-color: #3c0a8c; /* cor de fundo dos itens */\n"
"}\n"
"\n"
"\n"
"")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(470, 200, 371, 31))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"color: #c586c0;\n"
"background-color: rgb(40, 42, 54);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.page_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(480, 110, 371, 31))
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: #c586c0;\n"
"background-color: rgb(40, 42, 54);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.comboBoxPortaCom_3 = QComboBox(self.page_1)
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.addItem("")
        self.comboBoxPortaCom_3.setObjectName(u"comboBoxPortaCom_3")
        self.comboBoxPortaCom_3.setGeometry(QRect(470, 150, 151, 41))
        self.comboBoxPortaCom_3.setLayoutDirection(Qt.RightToLeft)
        self.comboBoxPortaCom_3.setStyleSheet(u"QComboBox {\n"
"	gridline-color: rgb(255, 255, 255);\n"
"    background-color: #282a36;\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 8px;\n"
"    color: #f8f8f2;\n"
"    font-family: Verdana;\n"
"    font-size: 18px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: #44475a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #282a36;\n"
"}\n"
"\n"
"QComboBox:on { /* quando selecionado */\n"
"    border-color: #f1fa8c;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #6272a4;\n"
"    border-left-style: solid; /* estilo de linha da esquerda - pode ser qualquer um dos seguintes: solid, dashed, dot-dash, dot-dot-dash, none */"
                        "\n"
"    border-top-right-radius: 3px; /* raio superior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"    border-bottom-right-radius: 3px; /* raio inferior direito da borda quando a caixa n\u00e3o est\u00e1 focada */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/path/to/your/image.png); /* substitua '/path/to/your/image.png' pelo caminho correto para sua imagem */\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* mude a cor do bot\u00e3o para laranja quando a caixa est\u00e1 focada */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #f8f8f2; /* cor do texto dos itens */\n"
"    background-color: #3c0a8c; /* cor de fundo dos itens */\n"
"}\n"
"\n"
"\n"
"")
        self.label_12 = QLabel(self.page_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(630, 150, 221, 31))
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: #c586c0;\n"
"background-color: rgb(40, 42, 54);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.bntReturn_2 = QPushButton(self.page_2)
        self.bntReturn_2.setObjectName(u"bntReturn_2")
        self.bntReturn_2.setGeometry(QRect(250, 260, 250, 150))
        font7 = QFont()
        font7.setFamilies([u"DS-Digital"])
        font7.setBold(True)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.bntReturn_2.setFont(font7)
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
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.bntReturn_3 = QPushButton(self.page_3)
        self.bntReturn_3.setObjectName(u"bntReturn_3")
        self.bntReturn_3.setGeometry(QRect(660, 20, 231, 61))
        self.bntReturn_3.setFont(font2)
        self.bntReturn_3.setAutoFillBackground(False)
        self.bntReturn_3.setStyleSheet(u"        QPushButton {\n"
"            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0.05 #630303, stop: 1 #4cc7c9);\n"
"            border-radius: 8px;\n"
"            color: #ffffff;\n"
"            font-family: Verdana;\n"
"            font-size: 30px;\n"
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
        self.label_28.setGeometry(QRect(70, 20, 541, 54))
        font8 = QFont()
        font8.setFamilies([u"Verdana"])
        font8.setPointSize(32)
        font8.setBold(False)
        self.label_28.setFont(font8)
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
        self.menubar.setGeometry(QRect(0, 0, 994, 22))
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
        self.btnPage3.setText(QCoreApplication.translate("MainWindow", u"MEDIDOR", None))
        self.btnPage1.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ATHENAS DASH SPEEDUINO - V1.1.15", None))
        self.btnPage5.setText(QCoreApplication.translate("MainWindow", u"PAGE 5", None))
        self.btnPage6.setText(QCoreApplication.translate("MainWindow", u"PAGE 6", None))
        self.btnPage4.setText(QCoreApplication.translate("MainWindow", u"PAGE 4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COMUNICA\u00c7\u00c3O COM A PLACA:", None))
        self.labelComStatus.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.labelComCnt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES E CONEX\u00c3O", None))
        self.bntReturn_1.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.comboBoxPortaCom.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.comboBoxPortaCom.setCurrentText(QCoreApplication.translate("MainWindow", u"-", None))
        self.bntCheckPorts.setText(QCoreApplication.translate("MainWindow", u"CHECK PORTS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1 - SELECIONE A PORTA SERIAL", None))
        self.bntConnect.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.debugTextTermina.setPlainText(QCoreApplication.translate("MainWindow", u"DESCONECTADO.\n"
"\n"
"1 - Primeiro pressione o bot\u00e3o \"Check ports\" \n"
"para verificar em qual porta o Speeduino est\u00e1 conectado.\n"
"\n"
"2 - Depois selecione a porta para conectar.\n"
"\n"
"3 - Pressione o bot\u00e3o de conectar\n"
"", None))
        self.comboBoxPortaCom_2.setItemText(0, QCoreApplication.translate("MainWindow", u"     -", None))

        self.comboBoxPortaCom_2.setCurrentText(QCoreApplication.translate("MainWindow", u"     -", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"3 - SELECIONE UM COMANDO:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"2 - PERIODO DE REQUISI\u00c7\u00c3O", None))
        self.comboBoxPortaCom_3.setItemText(0, QCoreApplication.translate("MainWindow", u"0.25", None))
        self.comboBoxPortaCom_3.setItemText(1, QCoreApplication.translate("MainWindow", u"0.50", None))
        self.comboBoxPortaCom_3.setItemText(2, QCoreApplication.translate("MainWindow", u"0.75", None))
        self.comboBoxPortaCom_3.setItemText(3, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBoxPortaCom_3.setItemText(4, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBoxPortaCom_3.setItemText(5, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBoxPortaCom_3.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBoxPortaCom_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBoxPortaCom_3.setItemText(8, QCoreApplication.translate("MainWindow", u"10", None))

        self.comboBoxPortaCom_3.setCurrentText(QCoreApplication.translate("MainWindow", u"0.25", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SEGUNDOS", None))
        self.bntReturn_2.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.bntReturn_3.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ATHENAS DASH ECU", None))
    # retranslateUi

