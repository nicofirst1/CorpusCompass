# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowncyNQp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1298, 781)
        icon = QIcon()
        icon.addFile(u":/images/images/cc_logo_sd.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}\n"
"\n"
"/*QPushButton {\n"
"    background-color:rgb(154, 217, 234) ;\n"
"	color: white;\n"
"    min-width: 80px;\n"
"	min-height: 40px;\n"
"	border-style: solid;\n"
"	border-color: rgb(154, 217, 234);\n"
"	border-width: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(134, 189, 203) ;\n"
"	border-color: rgb(134, 189, 203);\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button \n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent \n"
"}\n"
"*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1298, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Corpus Compass", None))
    # retranslateUi

