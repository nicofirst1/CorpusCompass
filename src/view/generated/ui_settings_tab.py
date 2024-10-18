# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_tabivFlpi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_SettingsTab(object):
    def setupUi(self, SettingsTab):
        if not SettingsTab.objectName():
            SettingsTab.setObjectName(u"SettingsTab")
        SettingsTab.resize(1280, 729)
        SettingsTab.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
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
"}")
        self.gridLayout_2 = QGridLayout(SettingsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widge_settingscontents = QWidget(SettingsTab)
        self.widge_settingscontents.setObjectName(u"widge_settingscontents")
        self.verticalLayout = QVBoxLayout(self.widge_settingscontents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_back = QPushButton(self.widge_settingscontents)
        self.btn_back.setObjectName(u"btn_back")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"	color: black;\n"
"	min-height: 40px;\n"
"	max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: dark grey; \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid grey;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: none;\n"
"}")

        self.verticalLayout.addWidget(self.btn_back, 0, Qt.AlignLeft)

        self.label_settingstitle = QLabel(self.widge_settingscontents)
        self.label_settingstitle.setObjectName(u"label_settingstitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_settingstitle.sizePolicy().hasHeightForWidth())
        self.label_settingstitle.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_settingstitle.setFont(font1)

        self.verticalLayout.addWidget(self.label_settingstitle)

        self.label = QLabel(self.widge_settingscontents)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(self.widge_settingscontents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_8 = QCheckBox(self.groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_2.addWidget(self.checkBox_7)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widge_settingscontents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.gridLayout_2.addWidget(self.widge_settingscontents, 0, 0, 1, 1, Qt.AlignTop)


        self.retranslateUi(SettingsTab)

        QMetaObject.connectSlotsByName(SettingsTab)
    # setupUi

    def retranslateUi(self, SettingsTab):
        self.btn_back.setText(QCoreApplication.translate("SettingsTab", u"<-- Back to home", None))
        self.label_settingstitle.setText(QCoreApplication.translate("SettingsTab", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsTab", u"TODO: Specify all settings after implementation is mostly finished (otherwise exact settings are unclear as data/structure/... is unclear)", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsTab", u"Settings1", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsTab", u"Settings2", None))
        self.checkBox_2.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("SettingsTab", u"CheckBox", None))
        pass
    # retranslateUi

