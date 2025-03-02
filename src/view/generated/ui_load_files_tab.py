# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_files_tabNGLaQt.ui'
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
    QApplication,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSplitter,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_LoadFilesTab(object):
    def setupUi(self, LoadFilesTab):
        if not LoadFilesTab.objectName():
            LoadFilesTab.setObjectName("LoadFilesTab")
        LoadFilesTab.resize(1280, 720)
        LoadFilesTab.setStyleSheet(
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
        self.verticalLayout_4 = QVBoxLayout(LoadFilesTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QSplitter(LoadFilesTab)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.verticalWidget = QWidget(self.splitter)
        self.verticalWidget.setObjectName("verticalWidget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.verticalWidget.sizePolicy().hasHeightForWidth()
        )
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.verticalWidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 599))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_loaded_filenames = QTableWidget(self.scrollAreaWidgetContents)
        if self.list_loaded_filenames.columnCount() < 2:
            self.list_loaded_filenames.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_loaded_filenames.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_loaded_filenames.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.list_loaded_filenames.setObjectName("list_loaded_filenames")
        self.list_loaded_filenames.setStyleSheet(
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
            "    border: 1px solid white;\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:hover {\n"
            "    /* Adjust the appearance of the ho"
            "ver indicator */\n"
            "    background-color: lightgray; /* Example: change background color when hovering */\n"
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
        self.list_loaded_filenames.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_loaded_filenames.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_loaded_filenames.setSelectionMode(QAbstractItemView.NoSelection)
        self.list_loaded_filenames.setShowGrid(False)
        self.list_loaded_filenames.horizontalHeader().setVisible(False)
        self.list_loaded_filenames.horizontalHeader().setMinimumSectionSize(28)
        self.list_loaded_filenames.horizontalHeader().setDefaultSectionSize(28)
        self.list_loaded_filenames.horizontalHeader().setStretchLastSection(True)
        self.list_loaded_filenames.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.list_loaded_filenames)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_file = QPushButton(self.verticalWidget)
        self.btn_add_file.setObjectName("btn_add_file")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btn_add_file.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_add_file)

        self.btn_remove_file = QPushButton(self.verticalWidget)
        self.btn_remove_file.setObjectName("btn_remove_file")
        self.btn_remove_file.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_remove_file)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalWidget)
        self.verticalWidget_2 = QWidget(self.splitter)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.verticalWidget_2.sizePolicy().hasHeightForWidth()
        )
        self.verticalWidget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab_file_preview = QTabWidget(self.verticalWidget_2)
        self.tab_file_preview.setObjectName("tab_file_preview")
        self.tab_file_preview.setTabsClosable(True)
        self.tab_file_preview.setMovable(True)

        self.verticalLayout_3.addWidget(self.tab_file_preview)

        self.btn_finished = QPushButton(self.verticalWidget_2)
        self.btn_finished.setObjectName("btn_finished")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.btn_finished.sizePolicy().hasHeightForWidth()
        )
        self.btn_finished.setSizePolicy(sizePolicy2)
        self.btn_finished.setMinimumSize(QSize(84, 44))
        self.btn_finished.setFont(font)
        self.btn_finished.setStyleSheet(
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

        self.verticalLayout_3.addWidget(self.btn_finished)

        self.splitter.addWidget(self.verticalWidget_2)

        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(LoadFilesTab)

        self.tab_file_preview.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(LoadFilesTab)

    # setupUi

    def retranslateUi(self, LoadFilesTab):
        self.label.setText(
            QCoreApplication.translate("LoadFilesTab", "Loaded Files", None)
        )
        ___qtablewidgetitem = self.list_loaded_filenames.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("LoadFilesTab", "Neue Spalte", None)
        )
        ___qtablewidgetitem1 = self.list_loaded_filenames.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("LoadFilesTab", "File-Name", None)
        )
        self.btn_add_file.setText(
            QCoreApplication.translate("LoadFilesTab", "Add File", None)
        )
        self.btn_remove_file.setText(
            QCoreApplication.translate("LoadFilesTab", "Remove selected\nFiles", None)
        )
        self.btn_finished.setText(
            QCoreApplication.translate("LoadFilesTab", "Save", None)
        )
        pass

    # retranslateUi
