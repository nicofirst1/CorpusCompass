# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_project_dialogbzETdR.ui'
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
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CreateProjectDialog(object):
    def setupUi(self, CreateProjectDialog):
        if not CreateProjectDialog.objectName():
            CreateProjectDialog.setObjectName(u"CreateProjectDialog")
        CreateProjectDialog.resize(400, 357)
        icon = QIcon()
        icon.addFile(u":/images/images/cc_logo_sd.png", QSize(), QIcon.Normal, QIcon.Off)
        CreateProjectDialog.setWindowIcon(icon)
        CreateProjectDialog.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:white ;\n"
"	color: black;\n"
"    min-width: 80px;\n"
"	min-height: 30px;\n"
"	border-style: solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(244, 244, 244) ;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.verticalLayout = QVBoxLayout(CreateProjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.proj_name_lineedit = QLineEdit(CreateProjectDialog)
        self.proj_name_lineedit.setObjectName(u"proj_name_lineedit")

        self.gridLayout.addWidget(self.proj_name_lineedit, 1, 1, 1, 1)

        self.label_description = QLabel(CreateProjectDialog)
        self.label_description.setObjectName(u"label_description")

        self.gridLayout.addWidget(self.label_description, 3, 0, 1, 1)

        self.label_name = QLabel(CreateProjectDialog)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)

        self.textEdit_createproject_description = QTextEdit(CreateProjectDialog)
        self.textEdit_createproject_description.setObjectName(u"textEdit_createproject_description")

        self.gridLayout.addWidget(self.textEdit_createproject_description, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.groupBox_preannotated = QGroupBox(CreateProjectDialog)
        self.groupBox_preannotated.setObjectName(u"groupBox_preannotated")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_preannotated)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton_corpuspreannot = QRadioButton(self.groupBox_preannotated)
        self.radioButton_corpuspreannot.setObjectName(u"radioButton_corpuspreannot")
        self.radioButton_corpuspreannot.setChecked(True)

        self.verticalLayout_5.addWidget(self.radioButton_corpuspreannot)

        self.radioButton_corpusnotannot = QRadioButton(self.groupBox_preannotated)
        self.radioButton_corpusnotannot.setObjectName(u"radioButton_corpusnotannot")
        self.radioButton_corpusnotannot.setEnabled(False)

        self.verticalLayout_5.addWidget(self.radioButton_corpusnotannot)


        self.verticalLayout.addWidget(self.groupBox_preannotated)

        self.groupBox_annottechnique = QGroupBox(CreateProjectDialog)
        self.groupBox_annottechnique.setObjectName(u"groupBox_annottechnique")
        self.groupBox_annottechnique.setEnabled(True)
        self.groupBox_annottechnique.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_annottechnique)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_symbolbasedannot = QRadioButton(self.groupBox_annottechnique)
        self.radioButton_symbolbasedannot.setObjectName(u"radioButton_symbolbasedannot")
        self.radioButton_symbolbasedannot.setEnabled(True)
        self.radioButton_symbolbasedannot.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_symbolbasedannot)

        self.radioButton_colorbasedannot = QRadioButton(self.groupBox_annottechnique)
        self.radioButton_colorbasedannot.setObjectName(u"radioButton_colorbasedannot")
        self.radioButton_colorbasedannot.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioButton_colorbasedannot)


        self.verticalLayout.addWidget(self.groupBox_annottechnique)

        self.error_message_label = QLabel(CreateProjectDialog)
        self.error_message_label.setObjectName(u"error_message_label")
        self.error_message_label.setStyleSheet(u"QLabel { color : red; }")

        self.verticalLayout.addWidget(self.error_message_label)

        self.buttonBox = QDialogButtonBox(CreateProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.proj_name_lineedit, self.textEdit_createproject_description)
        QWidget.setTabOrder(self.textEdit_createproject_description, self.radioButton_corpuspreannot)
        QWidget.setTabOrder(self.radioButton_corpuspreannot, self.radioButton_symbolbasedannot)
        QWidget.setTabOrder(self.radioButton_symbolbasedannot, self.radioButton_colorbasedannot)
        QWidget.setTabOrder(self.radioButton_colorbasedannot, self.radioButton_corpusnotannot)

        self.retranslateUi(CreateProjectDialog)
        self.buttonBox.accepted.connect(CreateProjectDialog.accept)
        self.buttonBox.rejected.connect(CreateProjectDialog.reject)
        self.radioButton_corpuspreannot.toggled.connect(self.groupBox_annottechnique.setEnabled)
        self.radioButton_corpusnotannot.clicked["bool"].connect(self.groupBox_annottechnique.setDisabled)

        QMetaObject.connectSlotsByName(CreateProjectDialog)
    # setupUi

    def retranslateUi(self, CreateProjectDialog):
        CreateProjectDialog.setWindowTitle(QCoreApplication.translate("CreateProjectDialog", u"Create new Project", None))
        self.label_description.setText(QCoreApplication.translate("CreateProjectDialog", u"Description", None))
        self.label_name.setText(QCoreApplication.translate("CreateProjectDialog", u"Name", None))
        self.groupBox_preannotated.setTitle(QCoreApplication.translate("CreateProjectDialog", u"Corpus settings", None))
        self.radioButton_corpuspreannot.setText(QCoreApplication.translate("CreateProjectDialog", u"Corpus already fully annotated", None))
        self.radioButton_corpusnotannot.setText(QCoreApplication.translate("CreateProjectDialog", u"Corpus not yet annotated", None))
        self.groupBox_annottechnique.setTitle(QCoreApplication.translate("CreateProjectDialog", u"Used annotation-technique", None))
        self.radioButton_symbolbasedannot.setText(QCoreApplication.translate("CreateProjectDialog", u"Symbol-Based", None))
        self.radioButton_colorbasedannot.setText(QCoreApplication.translate("CreateProjectDialog", u"Color/Highlighting-Based", None))
    # retranslateUi

