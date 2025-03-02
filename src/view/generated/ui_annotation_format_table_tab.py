# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_format_table_tabRTfetN.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_AnnotationFormatTableTab(object):
    def setupUi(self, AnnotationFormatTableTab):
        if not AnnotationFormatTableTab.objectName():
            AnnotationFormatTableTab.setObjectName("AnnotationFormatTableTab")
        AnnotationFormatTableTab.resize(1280, 720)
        AnnotationFormatTableTab.setStyleSheet(
            "QWidget{\n"
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
            "}"
        )
        self.verticalLayout = QVBoxLayout(AnnotationFormatTableTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_annotformat_tablecontainer = QWidget(AnnotationFormatTableTab)
        self.widget_annotformat_tablecontainer.setObjectName(
            "widget_annotformat_tablecontainer"
        )
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_annotformat_tablecontainer.sizePolicy().hasHeightForWidth()
        )
        self.widget_annotformat_tablecontainer.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget_annotformat_tablecontainer)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget = QWidget(self.widget_annotformat_tablecontainer)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_annotformat_heading = QLabel(self.horizontalWidget)
        self.label_annotformat_heading.setObjectName("label_annotformat_heading")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_annotformat_heading.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_annotformat_heading)

        self.btn_help = QPushButton(self.horizontalWidget)
        self.btn_help.setObjectName("btn_help")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_help.setFont(font1)
        self.btn_help.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon = QIcon()
        icon.addFile(":/images/images/Help_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon)
        self.btn_help.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_help)

        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 2, 3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.tableWidget_annotformats = QTableWidget(
            self.widget_annotformat_tablecontainer
        )
        if self.tableWidget_annotformats.columnCount() < 2:
            self.tableWidget_annotformats.setColumnCount(2)
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2)
        self.tableWidget_annotformats.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3)
        self.tableWidget_annotformats.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_annotformats.setObjectName("tableWidget_annotformats")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.tableWidget_annotformats.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget_annotformats.setSizePolicy(sizePolicy2)
        self.tableWidget_annotformats.setMaximumSize(QSize(16777215, 300))
        self.tableWidget_annotformats.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_annotformats.setStyleSheet(
            "QAbstractItemView::indicator{\n"
            "	width: 20px;\n"
            "	height: 20px;\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:checked {\n"
            "    /* Adjust the appearance of the checked indicator */\n"
            "    image: url(:/images/images/checked_icon.png) /* Specify a custom image if desired */\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:unchecked {\n"
            "    /* Adjust the appearance of the unchecked indicator */\n"
            "    image: url(:/images/images/unchecked_icon.png); /* Specify a custom image if desired */\n"
            "}\n"
            "\n"
            "\n"
            "QTableWidget {\n"
            "    font-size: 12pt; /* Set the font size */\n"
            "    font-weight: bold; /* Set the font weight */\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected {\n"
            "    background-color: rgba(50, 50, 225, 0.1); /* Change the background color and opacity */\n"
            "	color:black;\n"
            "}\n"
            "\n"
            "QTableWidget::item:focus {\n"
            "    selection-color: blue; /* Hide the dotted selection border */\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:hover {\n"
            "    /* Adjust the appearance of the hover indicator */\n"
            "    backgrou"
            "nd-color: lightgray; /* Example: change background color when hovering */\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:checked:hover {\n"
            "    /* Adjust the appearance of the checked checkbox when hovering */\n"
            "    background-color: rgb(255, 166, 167); /* Example: change background color of checked checkbox when hovering */\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QAbstractItemView::indicator:unchecked:hover {\n"
            "    /* Adjust the appearance of the unchecked checkbox when hovering */\n"
            "    background-color: lightgreen; /* Example: change background color of unchecked checkbox when hovering */\n"
            "}\n"
            "\n"
            ""
        )
        self.tableWidget_annotformats.setFrameShape(QFrame.Box)
        self.tableWidget_annotformats.setFrameShadow(QFrame.Plain)
        self.tableWidget_annotformats.setLineWidth(2)
        self.tableWidget_annotformats.setMidLineWidth(2)
        self.tableWidget_annotformats.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_annotformats.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.tableWidget_annotformats.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_annotformats.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_annotformats.setDragEnabled(True)
        self.tableWidget_annotformats.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_annotformats.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_annotformats.setShowGrid(True)
        self.tableWidget_annotformats.setSortingEnabled(False)
        self.tableWidget_annotformats.setWordWrap(True)
        self.tableWidget_annotformats.setCornerButtonEnabled(False)
        self.tableWidget_annotformats.setRowCount(0)
        self.tableWidget_annotformats.horizontalHeader().setVisible(True)
        self.tableWidget_annotformats.horizontalHeader().setCascadingSectionResizes(
            False
        )
        self.tableWidget_annotformats.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_annotformats.horizontalHeader().setDefaultSectionSize(600)
        self.tableWidget_annotformats.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_annotformats.verticalHeader().setDefaultSectionSize(40)

        self.gridLayout.addWidget(self.tableWidget_annotformats, 7, 0, 1, 3)

        self.label_annotformat_description = QLabel(
            self.widget_annotformat_tablecontainer
        )
        self.label_annotformat_description.setObjectName(
            "label_annotformat_description"
        )
        font4 = QFont()
        font4.setPointSize(10)
        self.label_annotformat_description.setFont(font4)
        self.label_annotformat_description.setScaledContents(True)
        self.label_annotformat_description.setWordWrap(True)

        self.gridLayout.addWidget(self.label_annotformat_description, 4, 0, 1, 3)

        self.widget_addedit = QWidget(self.widget_annotformat_tablecontainer)
        self.widget_addedit.setObjectName("widget_addedit")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_addedit)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_annotformat_addnew = QPushButton(self.widget_addedit)
        self.btn_annotformat_addnew.setObjectName("btn_annotformat_addnew")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.btn_annotformat_addnew.sizePolicy().hasHeightForWidth()
        )
        self.btn_annotformat_addnew.setSizePolicy(sizePolicy3)
        self.btn_annotformat_addnew.setMinimumSize(QSize(90, 50))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.btn_annotformat_addnew.setFont(font5)
        self.btn_annotformat_addnew.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_annotformat_addnew.setStyleSheet("")
        icon1 = QIcon()
        icon1.addFile(":/images/images/Plus_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_annotformat_addnew.setIcon(icon1)
        self.btn_annotformat_addnew.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_annotformat_addnew)

        self.btn_annotformat_edit = QPushButton(self.widget_addedit)
        self.btn_annotformat_edit.setObjectName("btn_annotformat_edit")
        self.btn_annotformat_edit.setFont(font5)
        self.btn_annotformat_edit.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(
            ":/images/images/edit_icon_white.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_annotformat_edit.setIcon(icon2)
        self.btn_annotformat_edit.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_annotformat_edit)

        self.gridLayout.addWidget(self.widget_addedit, 8, 0, 1, 3)

        self.verticalLayout.addWidget(
            self.widget_annotformat_tablecontainer, 0, Qt.AlignTop
        )

        self.widget_annotformat_buttoncontainer = QWidget(AnnotationFormatTableTab)
        self.widget_annotformat_buttoncontainer.setObjectName(
            "widget_annotformat_buttoncontainer"
        )
        sizePolicy3.setHeightForWidth(
            self.widget_annotformat_buttoncontainer.sizePolicy().hasHeightForWidth()
        )
        self.widget_annotformat_buttoncontainer.setSizePolicy(sizePolicy3)
        self.widget_annotformat_buttoncontainer.setMinimumSize(QSize(0, 80))
        self.horizontalLayout = QHBoxLayout(self.widget_annotformat_buttoncontainer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_annotformat_cancel = QPushButton(
            self.widget_annotformat_buttoncontainer
        )
        self.btn_annotformat_cancel.setObjectName("btn_annotformat_cancel")
        self.btn_annotformat_cancel.setFont(font5)
        self.btn_annotformat_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_annotformat_cancel.setStyleSheet(
            "QPushButton {\n"
            "	color: white;\n"
            "	background-color: lightgrey;\n"
            "	border-width: 2px;\n"
            "	border-radius: 10px;\n"
            "	border-color: grey;\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "	color: black;\n"
            "	background-color: white;\n"
            "	border-style: solid;\n"
            "	border-color: black;\n"
            "	border-width: 2px;\n"
            "	border-radius: 10px;\n"
            "	min-height: 80px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background-color: rgb(120, 120, 120);\n"
            "}\n"
            "\n"
            "QPushButton:disabled{\n"
            "  background-color: rgb(121, 121, 121);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_annotformat_cancel)

        self.btn_annotformat_save = QPushButton(self.widget_annotformat_buttoncontainer)
        self.btn_annotformat_save.setObjectName("btn_annotformat_save")
        self.btn_annotformat_save.setEnabled(True)
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.btn_annotformat_save.sizePolicy().hasHeightForWidth()
        )
        self.btn_annotformat_save.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.btn_annotformat_save.setFont(font6)
        self.btn_annotformat_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_annotformat_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_annotformat_save.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_annotformat_save)

        self.verticalLayout.addWidget(self.widget_annotformat_buttoncontainer)

        self.retranslateUi(AnnotationFormatTableTab)

        QMetaObject.connectSlotsByName(AnnotationFormatTableTab)

    # setupUi

    def retranslateUi(self, AnnotationFormatTableTab):
        self.label_annotformat_heading.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab", "Specify Annotation Fromat", None
            )
        )
        self.btn_help.setText(
            QCoreApplication.translate("AnnotationFormatTableTab", "Help...", None)
        )
        ___qtablewidgetitem = self.tableWidget_annotformats.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab", "Annotation format", None
            )
        )
        ___qtablewidgetitem1 = self.tableWidget_annotformats.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab", "Regular Expression", None
            )
        )
        self.label_annotformat_description.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab",
                "Overview of your specified annotation formats for the current project. Each annotation in your pre-annotated corpus that matches the pattern of one of the specified annotation format will be detected and further processed. In this menu, annotation formats can be added, edited, and deleted so that CorpusCompass can detect all annotations for your individual annotation style.",
                None,
            )
        )
        self.btn_annotformat_addnew.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab", "Add annotation format", None
            )
        )
        self.btn_annotformat_edit.setText(
            QCoreApplication.translate(
                "AnnotationFormatTableTab", "Edit annotation format", None
            )
        )
        self.btn_annotformat_cancel.setText(
            QCoreApplication.translate("AnnotationFormatTableTab", "Cancel", None)
        )
        self.btn_annotformat_save.setText(
            QCoreApplication.translate("AnnotationFormatTableTab", "Save changes", None)
        )
        pass

    # retranslateUi
