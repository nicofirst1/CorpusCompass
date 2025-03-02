# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_information_dialogKjPMrF.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_ProjectInformationDialog(object):
    def setupUi(self, ProjectInformationDialog):
        if not ProjectInformationDialog.objectName():
            ProjectInformationDialog.setObjectName(u"ProjectInformationDialog")
        ProjectInformationDialog.resize(1005, 656)
        self.verticalLayout_2 = QVBoxLayout(ProjectInformationDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_header = QLabel(ProjectInformationDialog)
        self.label_header.setObjectName(u"label_header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_header.sizePolicy().hasHeightForWidth())
        self.label_header.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_2.addWidget(self.label_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(ProjectInformationDialog)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"	color: grey;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: dark grey; \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkgrey;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/edit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(ProjectInformationDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"	color: grey;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: dark grey; \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkgrey;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/export_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_2.setCheckable(False)

        self.horizontalLayout.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_pname = QLabel(ProjectInformationDialog)
        self.label_pname.setObjectName(u"label_pname")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(True)
        self.label_pname.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_pname)

        self.lineEdit_pname = QLineEdit(ProjectInformationDialog)
        self.lineEdit_pname.setObjectName(u"lineEdit_pname")
        self.lineEdit_pname.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(12)
        self.lineEdit_pname.setFont(font3)
        self.lineEdit_pname.setMaxLength(50)

        self.verticalLayout_2.addWidget(self.lineEdit_pname)

        self.label_pdescr = QLabel(ProjectInformationDialog)
        self.label_pdescr.setObjectName(u"label_pdescr")
        self.label_pdescr.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_pdescr)

        self.plainTextEdit_pdescr = QPlainTextEdit(ProjectInformationDialog)
        self.plainTextEdit_pdescr.setObjectName(u"plainTextEdit_pdescr")
        self.plainTextEdit_pdescr.setEnabled(False)
        self.plainTextEdit_pdescr.setFont(font3)

        self.verticalLayout_2.addWidget(self.plainTextEdit_pdescr)

        self.groupBox_annotationstyle = QGroupBox(ProjectInformationDialog)
        self.groupBox_annotationstyle.setObjectName(u"groupBox_annotationstyle")
        self.groupBox_annotationstyle.setFont(font3)
        self.verticalLayout = QVBoxLayout(self.groupBox_annotationstyle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_symbolbased = QRadioButton(self.groupBox_annotationstyle)
        self.radioButton_symbolbased.setObjectName(u"radioButton_symbolbased")
        self.radioButton_symbolbased.setFont(font3)
        self.radioButton_symbolbased.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_symbolbased)

        self.radioButton_colorbased = QRadioButton(self.groupBox_annotationstyle)
        self.radioButton_colorbased.setObjectName(u"radioButton_colorbased")
        self.radioButton_colorbased.setFont(font3)

        self.verticalLayout.addWidget(self.radioButton_colorbased)


        self.verticalLayout_2.addWidget(self.groupBox_annotationstyle)

        self.label_test = QLabel(ProjectInformationDialog)
        self.label_test.setObjectName(u"label_test")

        self.verticalLayout_2.addWidget(self.label_test)

        self.buttonBox = QDialogButtonBox(ProjectInformationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ProjectInformationDialog)
        self.buttonBox.accepted.connect(ProjectInformationDialog.accept)
        self.buttonBox.rejected.connect(ProjectInformationDialog.reject)
        self.pushButton.toggled.connect(self.lineEdit_pname.setEnabled)
        self.pushButton.toggled.connect(self.plainTextEdit_pdescr.setEnabled)

        QMetaObject.connectSlotsByName(ProjectInformationDialog)
    # setupUi

    def retranslateUi(self, ProjectInformationDialog):
        ProjectInformationDialog.setWindowTitle(QCoreApplication.translate("ProjectInformationDialog", u"Dialog", None))
        self.label_header.setText(QCoreApplication.translate("ProjectInformationDialog", u"Project Information", None))
        self.pushButton.setText(QCoreApplication.translate("ProjectInformationDialog", u"Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("ProjectInformationDialog", u"Export Project", None))
        self.label_pname.setText(QCoreApplication.translate("ProjectInformationDialog", u"Project Name:", None))
        self.lineEdit_pname.setText("")
        self.lineEdit_pname.setPlaceholderText(QCoreApplication.translate("ProjectInformationDialog", u"Input Project-Name...", None))
        self.label_pdescr.setText(QCoreApplication.translate("ProjectInformationDialog", u"Project Description:", None))
        self.plainTextEdit_pdescr.setPlainText("")
        self.groupBox_annotationstyle.setTitle(QCoreApplication.translate("ProjectInformationDialog", u"Annotation-Style", None))
        self.radioButton_symbolbased.setText(QCoreApplication.translate("ProjectInformationDialog", u"Symbol-based annotation", None))
        self.radioButton_colorbased.setText(QCoreApplication.translate("ProjectInformationDialog", u"Color-based annotation", None))
        self.label_test.setText(QCoreApplication.translate("ProjectInformationDialog", u"TODO: Only Design Concept, maybe include in general settings menu", None))
    # retranslateUi

