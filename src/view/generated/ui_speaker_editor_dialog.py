# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'speaker_editor_dialoggTtdKn.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_SpeakerEditorDialog(object):
    def setupUi(self, SpeakerEditorDialog):
        if not SpeakerEditorDialog.objectName():
            SpeakerEditorDialog.setObjectName(u"SpeakerEditorDialog")
        SpeakerEditorDialog.resize(530, 506)
        self.gridLayout_2 = QGridLayout(SpeakerEditorDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_colorcontents = QWidget(SpeakerEditorDialog)
        self.widget_colorcontents.setObjectName(u"widget_colorcontents")
        self.horizontalLayout = QHBoxLayout(self.widget_colorcontents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_currentcolor = QLabel(self.widget_colorcontents)
        self.label_currentcolor.setObjectName(u"label_currentcolor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_currentcolor.sizePolicy().hasHeightForWidth())
        self.label_currentcolor.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_currentcolor.setFont(font)

        self.horizontalLayout.addWidget(self.label_currentcolor)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_colorsquare = QLabel(self.widget_colorcontents)
        self.label_colorsquare.setObjectName(u"label_colorsquare")
        self.label_colorsquare.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 3px solid black; /* Change border properties as needed */\n"
"	max-height: 20px;\n"
"	max-width: 20px;\n"
"	min-height: 20px;\n"
"	min-width: 20px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_colorsquare)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_changecolor = QPushButton(self.widget_colorcontents)
        self.btn_changecolor.setObjectName(u"btn_changecolor")
        self.btn_changecolor.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_changecolor.sizePolicy().hasHeightForWidth())
        self.btn_changecolor.setSizePolicy(sizePolicy1)
        self.btn_changecolor.setMinimumSize(QSize(25, 25))
        self.btn_changecolor.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_changecolor)


        self.gridLayout_2.addWidget(self.widget_colorcontents, 8, 0, 1, 1)

        self.groupBox_ivs = QGroupBox(SpeakerEditorDialog)
        self.groupBox_ivs.setObjectName(u"groupBox_ivs")
        self.groupBox_ivs.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_ivs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_ivs = QScrollArea(self.groupBox_ivs)
        self.scrollArea_ivs.setObjectName(u"scrollArea_ivs")
        self.scrollArea_ivs.setEnabled(True)
        self.scrollArea_ivs.setWidgetResizable(True)
        self.scrollArea_ivscontents = QWidget()
        self.scrollArea_ivscontents.setObjectName(u"scrollArea_ivscontents")
        self.scrollArea_ivscontents.setEnabled(False)
        self.scrollArea_ivscontents.setGeometry(QRect(0, 0, 453, 194))
        self.gridLayout = QGridLayout(self.scrollArea_ivscontents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea_ivs.setWidget(self.scrollArea_ivscontents)

        self.verticalLayout.addWidget(self.scrollArea_ivs)


        self.gridLayout_2.addWidget(self.groupBox_ivs, 11, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_speakername = QLabel(SpeakerEditorDialog)
        self.label_speakername.setObjectName(u"label_speakername")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_speakername.sizePolicy().hasHeightForWidth())
        self.label_speakername.setSizePolicy(sizePolicy2)
        self.label_speakername.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_speakername)

        self.label_variableinputwarning = QLabel(SpeakerEditorDialog)
        self.label_variableinputwarning.setObjectName(u"label_variableinputwarning")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_variableinputwarning.setFont(font1)
        self.label_variableinputwarning.setStyleSheet(u"QLabel{color:red;}")

        self.horizontalLayout_2.addWidget(self.label_variableinputwarning, 0, Qt.AlignRight)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.comboBox_selectspeaker = QComboBox(SpeakerEditorDialog)
        self.comboBox_selectspeaker.setObjectName(u"comboBox_selectspeaker")
        self.comboBox_selectspeaker.setMinimumSize(QSize(119, 25))
        self.comboBox_selectspeaker.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"}\n"
"")
        self.comboBox_selectspeaker.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_2.addWidget(self.comboBox_selectspeaker, 2, 0, 1, 1)

        self.btn_delete_speaker = QPushButton(SpeakerEditorDialog)
        self.btn_delete_speaker.setObjectName(u"btn_delete_speaker")
        self.btn_delete_speaker.setEnabled(False)
        self.btn_delete_speaker.setMinimumSize(QSize(25, 25))
        self.btn_delete_speaker.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgrey;\n"
"    border: 1px solid white;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightgrey;\n"
"    color: dark grey; \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_speaker.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_delete_speaker, 2, 1, 1, 1)

        self.label_speakerselect = QLabel(SpeakerEditorDialog)
        self.label_speakerselect.setObjectName(u"label_speakerselect")
        self.label_speakerselect.setFont(font)

        self.gridLayout_2.addWidget(self.label_speakerselect, 1, 0, 1, 1)

        self.lineEdit_nameinput = QLineEdit(SpeakerEditorDialog)
        self.lineEdit_nameinput.setObjectName(u"lineEdit_nameinput")
        self.lineEdit_nameinput.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_nameinput.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameinput.setSizePolicy(sizePolicy3)
        self.lineEdit_nameinput.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.lineEdit_nameinput, 6, 0, 1, 1)

        self.label_header = QLabel(SpeakerEditorDialog)
        self.label_header.setObjectName(u"label_header")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_header.setFont(font2)

        self.gridLayout_2.addWidget(self.label_header, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(SpeakerEditorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout_2.addWidget(self.buttonBox, 12, 0, 1, 3)

        self.label_duplicate_color = QLabel(SpeakerEditorDialog)
        self.label_duplicate_color.setObjectName(u"label_duplicate_color")
        self.label_duplicate_color.setFont(font1)
        self.label_duplicate_color.setStyleSheet(u"QLabel{color: red;}")

        self.gridLayout_2.addWidget(self.label_duplicate_color, 9, 0, 1, 1)


        self.retranslateUi(SpeakerEditorDialog)
        self.buttonBox.rejected.connect(SpeakerEditorDialog.reject)
        self.buttonBox.accepted.connect(SpeakerEditorDialog.accept)

        QMetaObject.connectSlotsByName(SpeakerEditorDialog)
    # setupUi

    def retranslateUi(self, SpeakerEditorDialog):
        SpeakerEditorDialog.setWindowTitle(QCoreApplication.translate("SpeakerEditorDialog", u"Dialog", None))
        self.label_currentcolor.setText(QCoreApplication.translate("SpeakerEditorDialog", u"Color:", None))
        self.btn_changecolor.setText(QCoreApplication.translate("SpeakerEditorDialog", u"Change Color", None))
        self.groupBox_ivs.setTitle(QCoreApplication.translate("SpeakerEditorDialog", u"Set Speaker-Attributes (based on IVs)", None))
        self.label_speakername.setText(QCoreApplication.translate("SpeakerEditorDialog", u"Speaker-Names cannot be changed:", None))
        self.label_variableinputwarning.setText("")
        self.comboBox_selectspeaker.setCurrentText("")
        self.comboBox_selectspeaker.setPlaceholderText(QCoreApplication.translate("SpeakerEditorDialog", u"Select Speaker...", None))
        self.btn_delete_speaker.setText("")
        self.label_speakerselect.setText(QCoreApplication.translate("SpeakerEditorDialog", u"Select Speaker to edit:", None))
        self.lineEdit_nameinput.setPlaceholderText(QCoreApplication.translate("SpeakerEditorDialog", u"Input Speaker-Name", None))
        self.label_header.setText(QCoreApplication.translate("SpeakerEditorDialog", u"Speaker - Edit", None))
        self.label_duplicate_color.setText(QCoreApplication.translate("SpeakerEditorDialog", u"The selected color is a duplicate! Please select a different color!", None))
    # retranslateUi

