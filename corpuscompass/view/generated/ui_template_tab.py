# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_tab.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_AnnotationFormatTableTab(object):
    def setupUi(self, AnnotationFormatTableTab):
        if not AnnotationFormatTableTab.objectName():
            AnnotationFormatTableTab.setObjectName(u"AnnotationFormatTableTab")
        AnnotationFormatTableTab.resize(1280, 720)
        AnnotationFormatTableTab.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout = QVBoxLayout(AnnotationFormatTableTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AnnotationFormatTableTab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/Plus_Icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.btn_sp_save = QPushButton(self.widget)
        self.btn_sp_save.setObjectName(u"btn_sp_save")
        self.btn_sp_save.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_sp_save.sizePolicy().hasHeightForWidth())
        self.btn_sp_save.setSizePolicy(sizePolicy)
        self.btn_sp_save.setMinimumSize(QSize(254, 104))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.btn_sp_save.setFont(font2)
        self.btn_sp_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sp_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_sp_save.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgb(0, 170, 0);\n"
"    min-width: 250px;\n"
"	min-height: 80px;\n"
"	border-style: solid;\n"
"	border-color: rgb(0, 125, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"   margin-top: 10px; \n"
"   margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 134, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  background-color: rgb(121, 121, 121);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sp_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AnnotationFormatTableTab)

        QMetaObject.connectSlotsByName(AnnotationFormatTableTab)
    # setupUi

    def retranslateUi(self, AnnotationFormatTableTab):
        self.label.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"Specify Annotation Fromat", None))
        self.label_2.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"Overview of annotation formats that will be detected for pre-annotated corpora, as well as what format to use for annotation in CorpusCompass", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"Annotation format", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"Regular Expression", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"[&token.identifier]", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"\\[\\&...", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"DeleteSymbol", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"  Add new annotation format", None))
        self.btn_sp_save.setText(QCoreApplication.translate("AnnotationFormatTableTab", u"Save changes", None))
        pass
    # retranslateUi

