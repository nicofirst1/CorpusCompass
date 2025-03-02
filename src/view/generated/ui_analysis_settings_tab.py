# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_settings_tabpuohzU.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_AnalysisSettingsTab(object):
    def setupUi(self, AnalysisSettingsTab):
        if not AnalysisSettingsTab.objectName():
            AnalysisSettingsTab.setObjectName(u"AnalysisSettingsTab")
        AnalysisSettingsTab.resize(1280, 720)
        AnalysisSettingsTab.setStyleSheet(u"QWidget{\n"
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
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.gridLayout_3 = QGridLayout(AnalysisSettingsTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_analysisscope = QWidget(AnalysisSettingsTab)
        self.widget_analysisscope.setObjectName(u"widget_analysisscope")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_analysisscope.sizePolicy().hasHeightForWidth())
        self.widget_analysisscope.setSizePolicy(sizePolicy)
        self.widget_analysisscope.setMinimumSize(QSize(300, 0))
        self.gridLayout_2 = QGridLayout(self.widget_analysisscope)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget_analysisscope)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4, Qt.AlignHCenter)

        self.label_29 = QLabel(self.widget_analysisscope)
        self.label_29.setObjectName(u"label_29")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_29.setFont(font1)

        self.gridLayout_2.addWidget(self.label_29, 5, 0, 1, 1)

        self.checkBox_selectall_dvs = QCheckBox(self.widget_analysisscope)
        self.checkBox_selectall_dvs.setObjectName(u"checkBox_selectall_dvs")
        self.checkBox_selectall_dvs.setMaximumSize(QSize(33, 16777215))
        self.checkBox_selectall_dvs.setStyleSheet(u"QCheckBox {\n"
"    /* Increase the size of the checkbox */\n"
"    width: 30px; /* Adjust width as needed */\n"
"    height: 30px; /* Adjust height as needed */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    /* Adjust the size and position of the check indicator */\n"
"    width: 28px; /* Adjust width as needed */\n"
"    height: 28px; /* Adjust height as needed */\n"
"    margin: 2px; /* Adjust margin to center the indicator within the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    /* Adjust the appearance of the checked indicator */\n"
"    image: url(:/images/images/checked_icon.png) /* Specify a custom image if desired */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    /* Adjust the appearance of the unchecked indicator */\n"
"    image: url(:/images/images/unchecked_icon.png); /* Specify a custom image if desired */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    /* Adjust the appearance of the hover indicator */\n"
"    background-color: lightgray; /* Example: change backgr"
                        "ound color when hovering */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    /* Adjust the appearance of the checked checkbox when hovering */\n"
"    background-color: rgb(255, 166, 167); /* Example: change background color of checked checkbox when hovering */\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    /* Adjust the appearance of the unchecked checkbox when hovering */\n"
"    background-color: lightgreen; /* Example: change background color of unchecked checkbox when hovering */\n"
"}\n"
"\n"
"")
        self.checkBox_selectall_dvs.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_selectall_dvs, 1, 3, 1, 1)

        self.scrollArea_speakers = QScrollArea(self.widget_analysisscope)
        self.scrollArea_speakers.setObjectName(u"scrollArea_speakers")
        self.scrollArea_speakers.setMinimumSize(QSize(0, 250))
        self.scrollArea_speakers.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_speakers.setWidgetResizable(True)
        self.scrollArea_speakercontents = QWidget()
        self.scrollArea_speakercontents.setObjectName(u"scrollArea_speakercontents")
        self.scrollArea_speakercontents.setGeometry(QRect(0, 0, 280, 248))
        self.gridLayout_5 = QGridLayout(self.scrollArea_speakercontents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_speakers.setWidget(self.scrollArea_speakercontents)

        self.gridLayout_2.addWidget(self.scrollArea_speakers, 6, 0, 1, 4)

        self.line = QFrame(self.widget_analysisscope)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 4)

        self.scrollArea_dvs = QScrollArea(self.widget_analysisscope)
        self.scrollArea_dvs.setObjectName(u"scrollArea_dvs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_dvs.sizePolicy().hasHeightForWidth())
        self.scrollArea_dvs.setSizePolicy(sizePolicy2)
        self.scrollArea_dvs.setMinimumSize(QSize(0, 250))
        self.scrollArea_dvs.setWidgetResizable(True)
        self.scrollArea_dvcontents = QWidget()
        self.scrollArea_dvcontents.setObjectName(u"scrollArea_dvcontents")
        self.scrollArea_dvcontents.setGeometry(QRect(0, 0, 280, 248))
        self.gridLayout_4 = QGridLayout(self.scrollArea_dvcontents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_dvs.setWidget(self.scrollArea_dvcontents)

        self.gridLayout_2.addWidget(self.scrollArea_dvs, 2, 0, 1, 4, Qt.AlignTop)

        self.label_51 = QLabel(self.widget_analysisscope)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.gridLayout_2.addWidget(self.label_51, 1, 0, 1, 1)

        self.checkBox_selectall_speakers = QCheckBox(self.widget_analysisscope)
        self.checkBox_selectall_speakers.setObjectName(u"checkBox_selectall_speakers")
        self.checkBox_selectall_speakers.setMaximumSize(QSize(33, 16777215))
        self.checkBox_selectall_speakers.setStyleSheet(u"QCheckBox {\n"
"    /* Increase the size of the checkbox */\n"
"    width: 30px; /* Adjust width as needed */\n"
"    height: 30px; /* Adjust height as needed */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    /* Adjust the size and position of the check indicator */\n"
"    width: 28px; /* Adjust width as needed */\n"
"    height: 28px; /* Adjust height as needed */\n"
"    margin: 2px; /* Adjust margin to center the indicator within the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    /* Adjust the appearance of the checked indicator */\n"
"    image: url(:/images/images/checked_icon.png) /* Specify a custom image if desired */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    /* Adjust the appearance of the unchecked indicator */\n"
"    image: url(:/images/images/unchecked_icon.png); /* Specify a custom image if desired */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    /* Adjust the appearance of the hover indicator */\n"
"    background-color: lightgray; /* Example: change backgr"
                        "ound color when hovering */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    /* Adjust the appearance of the checked checkbox when hovering */\n"
"    background-color: rgb(255, 166, 167); /* Example: change background color of checked checkbox when hovering */\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    /* Adjust the appearance of the unchecked checkbox when hovering */\n"
"    background-color: lightgreen; /* Example: change background color of unchecked checkbox when hovering */\n"
"}\n"
"\n"
"")
        self.checkBox_selectall_speakers.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_selectall_speakers, 5, 3, 1, 1)


        self.gridLayout_3.addWidget(self.widget_analysisscope, 0, 0, 1, 1)

        self.widget_contents = QWidget(AnalysisSettingsTab)
        self.widget_contents.setObjectName(u"widget_contents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_contents.sizePolicy().hasHeightForWidth())
        self.widget_contents.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.widget_contents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_contentdisplay = QScrollArea(self.widget_contents)
        self.scrollArea_contentdisplay.setObjectName(u"scrollArea_contentdisplay")
        self.scrollArea_contentdisplay.setFrameShadow(QFrame.Plain)
        self.scrollArea_contentdisplay.setWidgetResizable(True)
        self.scrollAreaWidgetContents_contentdisplay = QWidget()
        self.scrollAreaWidgetContents_contentdisplay.setObjectName(u"scrollAreaWidgetContents_contentdisplay")
        self.scrollAreaWidgetContents_contentdisplay.setGeometry(QRect(0, 0, 708, 682))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_contentdisplay)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.scrollArea_contentdisplay.setWidget(self.scrollAreaWidgetContents_contentdisplay)

        self.verticalLayout_3.addWidget(self.scrollArea_contentdisplay)


        self.gridLayout_3.addWidget(self.widget_contents, 0, 1, 1, 1)

        self.widget_settings = QWidget(AnalysisSettingsTab)
        self.widget_settings.setObjectName(u"widget_settings")
        sizePolicy.setHeightForWidth(self.widget_settings.sizePolicy().hasHeightForWidth())
        self.widget_settings.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget_settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_highlights = QLabel(self.widget_settings)
        self.label_highlights.setObjectName(u"label_highlights")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_highlights.sizePolicy().hasHeightForWidth())
        self.label_highlights.setSizePolicy(sizePolicy4)
        self.label_highlights.setFont(font1)
        self.label_highlights.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_highlights)

        self.checkBox_showfileindicators = QCheckBox(self.widget_settings)
        self.checkBox_showfileindicators.setObjectName(u"checkBox_showfileindicators")
        self.checkBox_showfileindicators.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox_showfileindicators)

        self.checkBox_showannotations = QCheckBox(self.widget_settings)
        self.checkBox_showannotations.setObjectName(u"checkBox_showannotations")

        self.verticalLayout_6.addWidget(self.checkBox_showannotations)

        self.checkBox_showspeakers = QCheckBox(self.widget_settings)
        self.checkBox_showspeakers.setObjectName(u"checkBox_showspeakers")

        self.verticalLayout_6.addWidget(self.checkBox_showspeakers)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.widget_searchwords = QWidget(self.widget_settings)
        self.widget_searchwords.setObjectName(u"widget_searchwords")
        self.widget_searchwords.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.widget_searchwords)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.widget_searchwords)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignTop)

        self.lineEdit = QLineEdit(self.widget_searchwords)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_8.addWidget(self.lineEdit)

        self.checkBox_multiplewordsearch = QCheckBox(self.widget_searchwords)
        self.checkBox_multiplewordsearch.setObjectName(u"checkBox_multiplewordsearch")

        self.verticalLayout_8.addWidget(self.checkBox_multiplewordsearch)


        self.verticalLayout_4.addWidget(self.widget_searchwords, 0, Qt.AlignTop)

        self.widget_searchvars = QWidget(self.widget_settings)
        self.widget_searchvars.setObjectName(u"widget_searchvars")
        self.widget_searchvars.setEnabled(False)
        self.verticalLayout_7 = QVBoxLayout(self.widget_searchvars)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.widget_searchvars)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.comboBox = QComboBox(self.widget_searchvars)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_7.addWidget(self.comboBox)


        self.verticalLayout_4.addWidget(self.widget_searchvars, 0, Qt.AlignTop)

        self.widget_buttons = QWidget(self.widget_settings)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.horizontalLayout = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_close_overview = QPushButton(self.widget_buttons)
        self.btn_close_overview.setObjectName(u"btn_close_overview")
        self.btn_close_overview.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_close_overview)

        self.btn_save_settings = QPushButton(self.widget_buttons)
        self.btn_save_settings.setObjectName(u"btn_save_settings")
        self.btn_save_settings.setFont(font1)
        self.btn_save_settings.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-color: rgb(0, 170, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 140, 0);\n"
"	border-color: rgb(0, 140, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  background-color: rgb(121, 121, 121);\n"
"  border-color: rgb(121, 121, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_save_settings)


        self.verticalLayout_4.addWidget(self.widget_buttons, 0, Qt.AlignBottom)


        self.gridLayout_3.addWidget(self.widget_settings, 0, 2, 1, 1)


        self.retranslateUi(AnalysisSettingsTab)

        QMetaObject.connectSlotsByName(AnalysisSettingsTab)
    # setupUi

    def retranslateUi(self, AnalysisSettingsTab):
        self.label.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Choose analysis scope", None))
        self.label_29.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Speakers", None))
        self.checkBox_selectall_dvs.setText("")
        self.label_51.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Dependent Variables", None))
        self.checkBox_selectall_speakers.setText("")
        self.label_highlights.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Highlights", None))
        self.checkBox_showfileindicators.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Show file indicators", None))
        self.checkBox_showannotations.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Show annotations", None))
        self.checkBox_showspeakers.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Show speakers", None))
        self.label_5.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Search words", None))
        self.checkBox_multiplewordsearch.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Multiple word search", None))
        self.label_4.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Search variables", None))
        self.btn_close_overview.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Close\n"
"Overview", None))
        self.btn_save_settings.setText(QCoreApplication.translate("AnalysisSettingsTab", u"Save\n"
"Settings", None))
        pass
    # retranslateUi

