# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variable_management_tabWFpduJ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_VariableManagementTab(object):
    def setupUi(self, VariableManagementTab):
        if not VariableManagementTab.objectName():
            VariableManagementTab.setObjectName(u"VariableManagementTab")
        VariableManagementTab.resize(1280, 720)
        VariableManagementTab.setStyleSheet(u"QWidget{\n"
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
"   background-color:rgb(134, 189, 203) ;\n"
"	border-color: rgb(134, 189, 203);\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"   background-color:rgb(134, 189, 203) ;\n"
"	border-color: rgb(134, 189, 203);\n"
"	color: rgb(245, 245, 245);\n"
"	\n"
"	font: 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.horizontalLayout = QHBoxLayout(VariableManagementTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(VariableManagementTab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalWidget = QWidget(self.widget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_allvarialbes_header = QLabel(self.verticalWidget)
        self.label_allvarialbes_header.setObjectName(u"label_allvarialbes_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_allvarialbes_header.sizePolicy().hasHeightForWidth())
        self.label_allvarialbes_header.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_allvarialbes_header.setFont(font)

        self.verticalLayout_7.addWidget(self.label_allvarialbes_header, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.verticalWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_2)

        self.btn_open_iv = QPushButton(self.verticalWidget)
        self.btn_open_iv.setObjectName(u"btn_open_iv")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_open_iv.sizePolicy().hasHeightForWidth())
        self.btn_open_iv.setSizePolicy(sizePolicy2)
        self.btn_open_iv.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"	color: grey;\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
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
"}\n"
"QPushButton:checked {\n"
"	color: black;\n"
"	text-decoration: underline;\n"
"}")
        self.btn_open_iv.setCheckable(True)
        self.btn_open_iv.setChecked(True)

        self.verticalLayout_7.addWidget(self.btn_open_iv, 0, Qt.AlignTop)

        self.btn_open_dv = QPushButton(self.verticalWidget)
        self.btn_open_dv.setObjectName(u"btn_open_dv")
        sizePolicy2.setHeightForWidth(self.btn_open_dv.sizePolicy().hasHeightForWidth())
        self.btn_open_dv.setSizePolicy(sizePolicy2)
        self.btn_open_dv.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"	color: grey;\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
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
"}\n"
"QPushButton:checked {\n"
"	color: black;\n"
"	text-decoration: underline;\n"
"}")
        self.btn_open_dv.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_open_dv, 0, Qt.AlignTop)

        self.btn_open_speakers = QPushButton(self.verticalWidget)
        self.btn_open_speakers.setObjectName(u"btn_open_speakers")
        sizePolicy2.setHeightForWidth(self.btn_open_speakers.sizePolicy().hasHeightForWidth())
        self.btn_open_speakers.setSizePolicy(sizePolicy2)
        self.btn_open_speakers.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"	color: grey;\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
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
"}\n"
"QPushButton:checked {\n"
"	color: black;\n"
"	text-decoration: underline;\n"
"}")
        self.btn_open_speakers.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_open_speakers, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.verticalWidget, 0, Qt.AlignTop)

        self.verticalWidget1 = QWidget(self.widget)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_import_metadata = QPushButton(self.verticalWidget1)
        self.btn_import_metadata.setObjectName(u"btn_import_metadata")
        self.btn_import_metadata.setFont(font)

        self.verticalLayout_8.addWidget(self.btn_import_metadata)

        self.btn_export_metadata = QPushButton(self.verticalWidget1)
        self.btn_export_metadata.setObjectName(u"btn_export_metadata")
        self.btn_export_metadata.setFont(font)

        self.verticalLayout_8.addWidget(self.btn_export_metadata)


        self.verticalLayout_2.addWidget(self.verticalWidget1, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(VariableManagementTab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.IV_page = QWidget()
        self.IV_page.setObjectName(u"IV_page")
        self.verticalLayout_3 = QVBoxLayout(self.IV_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeWidget_ivs = QTreeWidget(self.IV_page)
        self.treeWidget_ivs.setObjectName(u"treeWidget_ivs")
        self.treeWidget_ivs.setStyleSheet(u"QTreeWidget { \n"
"	font-size: 14pt; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"	font-size: 24px;\n"
"	font: bold\n"
"}")

        self.verticalLayout_3.addWidget(self.treeWidget_ivs)

        self.widget_iv_addedit_container = QWidget(self.IV_page)
        self.widget_iv_addedit_container.setObjectName(u"widget_iv_addedit_container")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_iv_addedit_container)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_add_iv = QPushButton(self.widget_iv_addedit_container)
        self.btn_add_iv.setObjectName(u"btn_add_iv")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_add_iv.sizePolicy().hasHeightForWidth())
        self.btn_add_iv.setSizePolicy(sizePolicy3)
        self.btn_add_iv.setFont(font)
        self.btn_add_iv.setStyleSheet(u"QPushButton {\n"
"	min-height: 50px;\n"
"	max-height:50px;\n"
"	min-width: 150px;\n"
"	max-width: 150px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/Plus_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_iv.setIcon(icon)
        self.btn_add_iv.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.btn_add_iv)

        self.btn_edit_ivs = QPushButton(self.widget_iv_addedit_container)
        self.btn_edit_ivs.setObjectName(u"btn_edit_ivs")
        sizePolicy3.setHeightForWidth(self.btn_edit_ivs.sizePolicy().hasHeightForWidth())
        self.btn_edit_ivs.setSizePolicy(sizePolicy3)
        self.btn_edit_ivs.setFont(font)
        self.btn_edit_ivs.setStyleSheet(u"QPushButton {\n"
"	min-height: 50px;\n"
"	max-height:50px;\n"
"	min-width: 150px;\n"
"	max-width: 150px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/edit_icon_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_ivs.setIcon(icon1)
        self.btn_edit_ivs.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_edit_ivs)


        self.verticalLayout_3.addWidget(self.widget_iv_addedit_container, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.IV_page)
        self.DV_page = QWidget()
        self.DV_page.setObjectName(u"DV_page")
        self.gridLayout = QGridLayout(self.DV_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_dvgroup_addnewdvs = QWidget(self.DV_page)
        self.widget_dvgroup_addnewdvs.setObjectName(u"widget_dvgroup_addnewdvs")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_dvgroup_addnewdvs.sizePolicy().hasHeightForWidth())
        self.widget_dvgroup_addnewdvs.setSizePolicy(sizePolicy4)
        self.verticalLayout_9 = QVBoxLayout(self.widget_dvgroup_addnewdvs)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.treeWidget_dvs = QTreeWidget(self.widget_dvgroup_addnewdvs)
        self.treeWidget_dvs.setObjectName(u"treeWidget_dvs")
        self.treeWidget_dvs.setMinimumSize(QSize(320, 0))
        self.treeWidget_dvs.setStyleSheet(u"QTreeWidget { \n"
"	font-size: 14pt; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"	font-size: 24px;\n"
"	font: bold\n"
"}")
        self.treeWidget_dvs.header().setDefaultSectionSize(175)

        self.verticalLayout_9.addWidget(self.treeWidget_dvs)

        self.widget_dv_addedit_container = QWidget(self.widget_dvgroup_addnewdvs)
        self.widget_dv_addedit_container.setObjectName(u"widget_dv_addedit_container")
        self.gridLayout_2 = QGridLayout(self.widget_dv_addedit_container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_add_dv = QPushButton(self.widget_dv_addedit_container)
        self.btn_add_dv.setObjectName(u"btn_add_dv")
        sizePolicy1.setHeightForWidth(self.btn_add_dv.sizePolicy().hasHeightForWidth())
        self.btn_add_dv.setSizePolicy(sizePolicy1)
        self.btn_add_dv.setMinimumSize(QSize(90, 50))
        self.btn_add_dv.setFont(font)
        self.btn_add_dv.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_add_dv, 1, 0, 1, 1)

        self.btn_edit_dvs = QPushButton(self.widget_dv_addedit_container)
        self.btn_edit_dvs.setObjectName(u"btn_edit_dvs")
        self.btn_edit_dvs.setFont(font)
        self.btn_edit_dvs.setIcon(icon1)
        self.btn_edit_dvs.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_edit_dvs, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_dv_addedit_container)


        self.gridLayout.addWidget(self.widget_dvgroup_addnewdvs, 0, 0, 5, 2)

        self.widget_dvgroup_table = QWidget(self.DV_page)
        self.widget_dvgroup_table.setObjectName(u"widget_dvgroup_table")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_dvgroup_table.sizePolicy().hasHeightForWidth())
        self.widget_dvgroup_table.setSizePolicy(sizePolicy5)
        self.verticalLayout_6 = QVBoxLayout(self.widget_dvgroup_table)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_dvdetectionheadercontainer = QWidget(self.widget_dvgroup_table)
        self.widget_dvdetectionheadercontainer.setObjectName(u"widget_dvdetectionheadercontainer")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_dvdetectionheadercontainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_detectedvariants = QLabel(self.widget_dvdetectionheadercontainer)
        self.label_detectedvariants.setObjectName(u"label_detectedvariants")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_detectedvariants.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_detectedvariants)

        self.btn_help = QPushButton(self.widget_dvdetectionheadercontainer)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setPointSize(11)
        self.btn_help.setFont(font2)
        self.btn_help.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"	color: grey;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/images/Help_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_help)


        self.verticalLayout_6.addWidget(self.widget_dvdetectionheadercontainer)

        self.checkBox_unassociated_dvs = QCheckBox(self.widget_dvgroup_table)
        self.checkBox_unassociated_dvs.setObjectName(u"checkBox_unassociated_dvs")
        self.checkBox_unassociated_dvs.setEnabled(False)

        self.verticalLayout_6.addWidget(self.checkBox_unassociated_dvs)

        self.tableWidget_detectedinformation = QTableWidget(self.widget_dvgroup_table)
        if (self.tableWidget_detectedinformation.columnCount() < 4):
            self.tableWidget_detectedinformation.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_detectedinformation.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget_detectedinformation.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget_detectedinformation.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget_detectedinformation.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_detectedinformation.setObjectName(u"tableWidget_detectedinformation")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableWidget_detectedinformation.sizePolicy().hasHeightForWidth())
        self.tableWidget_detectedinformation.setSizePolicy(sizePolicy7)
        self.tableWidget_detectedinformation.setMinimumSize(QSize(625, 0))
        self.tableWidget_detectedinformation.setStyleSheet(u"")
        self.tableWidget_detectedinformation.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_detectedinformation.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_detectedinformation.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_detectedinformation.setRowCount(0)
        self.tableWidget_detectedinformation.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_detectedinformation.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tableWidget_detectedinformation)

        self.label_corpuswaschanged = QLabel(self.widget_dvgroup_table)
        self.label_corpuswaschanged.setObjectName(u"label_corpuswaschanged")
        self.label_corpuswaschanged.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_corpuswaschanged)

        self.btn_detectvariants = QPushButton(self.widget_dvgroup_table)
        self.btn_detectvariants.setObjectName(u"btn_detectvariants")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_detectvariants.sizePolicy().hasHeightForWidth())
        self.btn_detectvariants.setSizePolicy(sizePolicy8)
        self.btn_detectvariants.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_detectvariants)

        self.label_detectednewvariants = QLabel(self.widget_dvgroup_table)
        self.label_detectednewvariants.setObjectName(u"label_detectednewvariants")

        self.verticalLayout_6.addWidget(self.label_detectednewvariants)


        self.gridLayout.addWidget(self.widget_dvgroup_table, 0, 3, 5, 1)

        self.line = QFrame(self.DV_page)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 0, 2, 5, 1)

        self.stackedWidget.addWidget(self.DV_page)
        self.Speaker_page = QWidget()
        self.Speaker_page.setObjectName(u"Speaker_page")
        self.verticalLayout_5 = QVBoxLayout(self.Speaker_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.treeWidget_speakers = QTreeWidget(self.Speaker_page)
        self.treeWidget_speakers.setObjectName(u"treeWidget_speakers")
        self.treeWidget_speakers.setStyleSheet(u"QTreeWidget { \n"
"	font-size: 14pt; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #616161, stop: 0.5 #505050,\n"
"                                      stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"	font-size: 24px;\n"
"	font: bold\n"
"}")

        self.verticalLayout_5.addWidget(self.treeWidget_speakers)

        self.widget_sp_addedit_container = QWidget(self.Speaker_page)
        self.widget_sp_addedit_container.setObjectName(u"widget_sp_addedit_container")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_sp_addedit_container)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_add_speaker = QPushButton(self.widget_sp_addedit_container)
        self.btn_add_speaker.setObjectName(u"btn_add_speaker")
        self.btn_add_speaker.setFont(font)
        self.btn_add_speaker.setStyleSheet(u"QPushButton {\n"
"	min-height: 50px;\n"
"	max-height:50px;\n"
"	min-width: 150px;\n"
"	max-width: 150px;\n"
"}")
        self.btn_add_speaker.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.btn_add_speaker)

        self.btn_edit_speakers = QPushButton(self.widget_sp_addedit_container)
        self.btn_edit_speakers.setObjectName(u"btn_edit_speakers")
        self.btn_edit_speakers.setFont(font)
        self.btn_edit_speakers.setStyleSheet(u"QPushButton {\n"
"	min-height: 50px;\n"
"	max-height:50px;\n"
"	min-width: 150px;\n"
"	max-width: 150px;\n"
"}")
        self.btn_edit_speakers.setIcon(icon1)
        self.btn_edit_speakers.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_speakers)


        self.verticalLayout_5.addWidget(self.widget_sp_addedit_container, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.Speaker_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.widget_metadatamanag_savecancel = QWidget(VariableManagementTab)
        self.widget_metadatamanag_savecancel.setObjectName(u"widget_metadatamanag_savecancel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_metadatamanag_savecancel.sizePolicy().hasHeightForWidth())
        self.widget_metadatamanag_savecancel.setSizePolicy(sizePolicy9)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_metadatamanag_savecancel)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_save_changes = QPushButton(self.widget_metadatamanag_savecancel)
        self.btn_save_changes.setObjectName(u"btn_save_changes")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.btn_save_changes.setFont(font3)
        self.btn_save_changes.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-style: solid;\n"
"	border-color: rgb(0, 125, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 134, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  background-color: rgb(121, 121, 121);\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_save_changes)


        self.verticalLayout.addWidget(self.widget_metadatamanag_savecancel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(VariableManagementTab)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VariableManagementTab)
    # setupUi

    def retranslateUi(self, VariableManagementTab):
        self.label_allvarialbes_header.setText(QCoreApplication.translate("VariableManagementTab", u"All Variables", None))
        self.btn_open_iv.setText(QCoreApplication.translate("VariableManagementTab", u"Independent Variables (IV)", None))
        self.btn_open_dv.setText(QCoreApplication.translate("VariableManagementTab", u"Dependent Variables (DV)", None))
        self.btn_open_speakers.setText(QCoreApplication.translate("VariableManagementTab", u"Speakers", None))
        self.btn_import_metadata.setText(QCoreApplication.translate("VariableManagementTab", u"Import Metadata\n"
" from file", None))
        self.btn_export_metadata.setText(QCoreApplication.translate("VariableManagementTab", u"Export Metadata\n"
" from file", None))
        ___qtreewidgetitem = self.treeWidget_ivs.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("VariableManagementTab", u"Independent Variables(IV)", None));
        self.btn_add_iv.setText(QCoreApplication.translate("VariableManagementTab", u"Add IV", None))
        self.btn_edit_ivs.setText(QCoreApplication.translate("VariableManagementTab", u"Edit IVs", None))
        ___qtreewidgetitem1 = self.treeWidget_dvs.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("VariableManagementTab", u"Dependent Variables(DV)", None));
        self.btn_add_dv.setText(QCoreApplication.translate("VariableManagementTab", u"Add DVs", None))
        self.btn_edit_dvs.setText(QCoreApplication.translate("VariableManagementTab", u"Edit DVs", None))
        self.label_detectedvariants.setText(QCoreApplication.translate("VariableManagementTab", u"Detected DV-Variants", None))
        self.btn_help.setText(QCoreApplication.translate("VariableManagementTab", u"Help...", None))
        self.checkBox_unassociated_dvs.setText(QCoreApplication.translate("VariableManagementTab", u"Only show Variants that are not associated to a DV yet?", None))
        ___qtablewidgetitem = self.tableWidget_detectedinformation.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VariableManagementTab", u"Detected Variant", None));
        ___qtablewidgetitem1 = self.tableWidget_detectedinformation.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VariableManagementTab", u"Occurences", None));
        ___qtablewidgetitem2 = self.tableWidget_detectedinformation.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VariableManagementTab", u"Associated DV", None));
        ___qtablewidgetitem3 = self.tableWidget_detectedinformation.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VariableManagementTab", u"Color", None));
        self.label_corpuswaschanged.setText(QCoreApplication.translate("VariableManagementTab", u"The corpus was changed since the last detection of DV-Variants! Do you wish to automatically detect and extract them again?", None))
        self.btn_detectvariants.setText(QCoreApplication.translate("VariableManagementTab", u"Extract DV-Variants from corpus annotations", None))
        self.label_detectednewvariants.setText(QCoreApplication.translate("VariableManagementTab", u"Detected XY new variables!", None))
        ___qtreewidgetitem2 = self.treeWidget_speakers.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("VariableManagementTab", u"Speakers", None));
        self.btn_add_speaker.setText(QCoreApplication.translate("VariableManagementTab", u"Add Speakers", None))
        self.btn_edit_speakers.setText(QCoreApplication.translate("VariableManagementTab", u"Edit Speakers", None))
        self.btn_save_changes.setText(QCoreApplication.translate("VariableManagementTab", u"Save", None))
        pass
    # retranslateUi

