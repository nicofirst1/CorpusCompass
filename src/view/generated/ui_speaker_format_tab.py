# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'speaker_format_tabwOvqeN.ui'
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
    QGridLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resources_rc
import resources_rc
import resources_rc


class Ui_SpeakerIdTab(object):
    def setupUi(self, SpeakerIdTab):
        if not SpeakerIdTab.objectName():
            SpeakerIdTab.setObjectName("SpeakerIdTab")
        SpeakerIdTab.resize(1280, 720)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpeakerIdTab.sizePolicy().hasHeightForWidth())
        SpeakerIdTab.setSizePolicy(sizePolicy)
        SpeakerIdTab.setStyleSheet(
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
        self.gridLayout_7 = QGridLayout(SpeakerIdTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_3 = QWidget(SpeakerIdTab)
        self.widget_3.setObjectName("widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sp_h = QLabel(self.widget_2)
        self.label_sp_h.setObjectName("label_sp_h")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_sp_h.sizePolicy().hasHeightForWidth())
        self.label_sp_h.setSizePolicy(sizePolicy2)
        self.label_sp_h.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_sp_h.setFont(font)
        self.label_sp_h.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_sp_h, 0, Qt.AlignTop)

        self.label_sp_description_2 = QLabel(self.widget_2)
        self.label_sp_description_2.setObjectName("label_sp_description_2")
        self.label_sp_description_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_sp_description_2)

        self.label_sp_subheader = QLabel(self.widget_2)
        self.label_sp_subheader.setObjectName("label_sp_subheader")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_sp_subheader.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_subheader.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_sp_subheader.setFont(font1)
        self.label_sp_subheader.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_sp_subheader)

        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(60, -1, -1, -1)
        self.radbtn_sp_flex = QRadioButton(self.widget_4)
        self.radbtn_sp_flex.setObjectName("radbtn_sp_flex")
        self.radbtn_sp_flex.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.radbtn_sp_flex.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_sp_flex.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setItalic(False)
        self.radbtn_sp_flex.setFont(font2)
        self.radbtn_sp_flex.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.radbtn_sp_flex, 5, 0, 1, 1)

        self.label_sp_helppraat = QLabel(self.widget_4)
        self.label_sp_helppraat.setObjectName("label_sp_helppraat")
        self.label_sp_helppraat.setEnabled(False)
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.label_sp_helppraat.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_helppraat.setSizePolicy(sizePolicy5)
        self.label_sp_helppraat.setPixmap(QPixmap(":/images/images/Help_Icon.svg"))

        self.gridLayout.addWidget(self.label_sp_helppraat, 3, 2, 1, 1)

        self.radbtn_sp_elan = QRadioButton(self.widget_4)
        self.radbtn_sp_elan.setObjectName("radbtn_sp_elan")
        self.radbtn_sp_elan.setEnabled(False)
        sizePolicy4.setHeightForWidth(
            self.radbtn_sp_elan.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_sp_elan.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        self.radbtn_sp_elan.setFont(font3)
        self.radbtn_sp_elan.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.radbtn_sp_elan, 4, 0, 1, 1)

        self.label_sp_helpstandard = QLabel(self.widget_4)
        self.label_sp_helpstandard.setObjectName("label_sp_helpstandard")
        sizePolicy5.setHeightForWidth(
            self.label_sp_helpstandard.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_helpstandard.setSizePolicy(sizePolicy5)
        self.label_sp_helpstandard.setPixmap(QPixmap(":/images/images/Help_Icon.svg"))

        self.gridLayout.addWidget(self.label_sp_helpstandard, 1, 2, 1, 2)

        self.label_sp_helpflex = QLabel(self.widget_4)
        self.label_sp_helpflex.setObjectName("label_sp_helpflex")
        self.label_sp_helpflex.setEnabled(False)
        sizePolicy5.setHeightForWidth(
            self.label_sp_helpflex.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_helpflex.setSizePolicy(sizePolicy5)
        self.label_sp_helpflex.setPixmap(QPixmap(":/images/images/Help_Icon.svg"))

        self.gridLayout.addWidget(self.label_sp_helpflex, 5, 2, 1, 1)

        self.label_sp_helpelan = QLabel(self.widget_4)
        self.label_sp_helpelan.setObjectName("label_sp_helpelan")
        self.label_sp_helpelan.setEnabled(False)
        sizePolicy5.setHeightForWidth(
            self.label_sp_helpelan.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_helpelan.setSizePolicy(sizePolicy5)
        self.label_sp_helpelan.setPixmap(QPixmap(":/images/images/Help_Icon.svg"))

        self.gridLayout.addWidget(self.label_sp_helpelan, 4, 2, 1, 1)

        self.radbtn_sp_standard = QRadioButton(self.widget_4)
        self.radbtn_sp_standard.setObjectName("radbtn_sp_standard")
        sizePolicy4.setHeightForWidth(
            self.radbtn_sp_standard.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_sp_standard.setSizePolicy(sizePolicy4)
        self.radbtn_sp_standard.setFont(font3)
        self.radbtn_sp_standard.setIconSize(QSize(16, 16))
        self.radbtn_sp_standard.setChecked(True)
        self.radbtn_sp_standard.setAutoExclusive(True)

        self.gridLayout.addWidget(self.radbtn_sp_standard, 1, 0, 1, 1)

        self.radbtn_sp_praat = QRadioButton(self.widget_4)
        self.radbtn_sp_praat.setObjectName("radbtn_sp_praat")
        self.radbtn_sp_praat.setEnabled(False)
        sizePolicy4.setHeightForWidth(
            self.radbtn_sp_praat.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_sp_praat.setSizePolicy(sizePolicy4)
        self.radbtn_sp_praat.setFont(font3)
        self.radbtn_sp_praat.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.radbtn_sp_praat, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(
            25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 1, 1, 1)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.gridLayout_7.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget = QWidget(SpeakerIdTab)
        self.widget.setObjectName("widget")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_sp_detectedspeakerstitle = QLabel(self.widget)
        self.label_sp_detectedspeakerstitle.setObjectName(
            "label_sp_detectedspeakerstitle"
        )
        sizePolicy2.setHeightForWidth(
            self.label_sp_detectedspeakerstitle.sizePolicy().hasHeightForWidth()
        )
        self.label_sp_detectedspeakerstitle.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_sp_detectedspeakerstitle.setFont(font4)
        self.label_sp_detectedspeakerstitle.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_sp_detectedspeakerstitle)

        self.widget_sp_reactivefeedbackcontents = QWidget(self.widget)
        self.widget_sp_reactivefeedbackcontents.setObjectName(
            "widget_sp_reactivefeedbackcontents"
        )
        self.gridLayout_2 = QGridLayout(self.widget_sp_reactivefeedbackcontents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_expand_wordinfo = QPushButton(self.widget_sp_reactivefeedbackcontents)
        self.btn_expand_wordinfo.setObjectName("btn_expand_wordinfo")
        font5 = QFont()
        font5.setFamilies(["Segoe UI"])
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        self.btn_expand_wordinfo.setFont(font5)
        self.btn_expand_wordinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_expand_wordinfo.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 1px solid white;\n"
            "	color: grey;\n"
            '	font: 20pt "Segoe UI";\n'
            "	min-height: 25px;\n"
            "	max-height: 25px;\n"
            "	min-width: 25px;\n"
            "	max-width: 25px;\n"
            "	margin-bottom: 2px\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: black; \n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:focus {\n"
            "    border: 1px solid white;\n"
            "}\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "    image: none;\n"
            "}\n"
            ""
        )
        self.btn_expand_wordinfo.setCheckable(True)
        self.btn_expand_wordinfo.setChecked(False)

        self.gridLayout_2.addWidget(self.btn_expand_wordinfo, 3, 2, 1, 1)

        self.btn_expand_speakerinfo = QPushButton(
            self.widget_sp_reactivefeedbackcontents
        )
        self.btn_expand_speakerinfo.setObjectName("btn_expand_speakerinfo")
        self.btn_expand_speakerinfo.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.btn_expand_speakerinfo.sizePolicy().hasHeightForWidth()
        )
        self.btn_expand_speakerinfo.setSizePolicy(sizePolicy7)
        self.btn_expand_speakerinfo.setMinimumSize(QSize(27, 29))
        self.btn_expand_speakerinfo.setFont(font5)
        self.btn_expand_speakerinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_expand_speakerinfo.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 1px solid white;\n"
            "	color: grey;\n"
            '	font: 20pt "Segoe UI";\n'
            "	min-height: 25px;\n"
            "	max-height: 25px;\n"
            "	min-width: 25px;\n"
            "	max-width: 25px;\n"
            "	margin-bottom: 2px\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: black; \n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:focus {\n"
            "    border: 1px solid white;\n"
            "}\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "    image: none;\n"
            "}\n"
            ""
        )
        self.btn_expand_speakerinfo.setCheckable(True)
        self.btn_expand_speakerinfo.setChecked(False)

        self.gridLayout_2.addWidget(self.btn_expand_speakerinfo, 1, 2, 1, 1)

        self.label_8 = QLabel(self.widget_sp_reactivefeedbackcontents)
        self.label_8.setObjectName("label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setPointSize(14)
        font6.setItalic(True)
        self.label_8.setFont(font6)

        self.gridLayout_2.addWidget(self.label_8, 3, 3, 1, 1)

        self.label_distinctspeakercount = QLabel(
            self.widget_sp_reactivefeedbackcontents
        )
        self.label_distinctspeakercount.setObjectName("label_distinctspeakercount")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_distinctspeakercount.setFont(font7)

        self.gridLayout_2.addWidget(self.label_distinctspeakercount, 1, 5, 1, 1)

        self.label_unassignedwordcount = QLabel(self.widget_sp_reactivefeedbackcontents)
        self.label_unassignedwordcount.setObjectName("label_unassignedwordcount")
        self.label_unassignedwordcount.setFont(font7)

        self.gridLayout_2.addWidget(self.label_unassignedwordcount, 3, 5, 1, 1)

        self.label_9 = QLabel(self.widget_sp_reactivefeedbackcontents)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font6)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.tableWidget_distinctspeakers = QTableWidget(
            self.widget_sp_reactivefeedbackcontents
        )
        if self.tableWidget_distinctspeakers.columnCount() < 2:
            self.tableWidget_distinctspeakers.setColumnCount(2)
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8)
        self.tableWidget_distinctspeakers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8)
        self.tableWidget_distinctspeakers.setHorizontalHeaderItem(
            1, __qtablewidgetitem1
        )
        self.tableWidget_distinctspeakers.setObjectName("tableWidget_distinctspeakers")
        self.tableWidget_distinctspeakers.setFrameShape(QFrame.NoFrame)
        self.tableWidget_distinctspeakers.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tableWidget_distinctspeakers.setSelectionMode(
            QAbstractItemView.NoSelection
        )
        self.tableWidget_distinctspeakers.setShowGrid(False)
        self.tableWidget_distinctspeakers.setRowCount(0)
        self.tableWidget_distinctspeakers.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_distinctspeakers.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidget_distinctspeakers, 2, 2, 1, 4)

        self.tableWidget_unassignedwords = QTableWidget(
            self.widget_sp_reactivefeedbackcontents
        )
        if self.tableWidget_unassignedwords.columnCount() < 2:
            self.tableWidget_unassignedwords.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8)
        self.tableWidget_unassignedwords.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font8)
        self.tableWidget_unassignedwords.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_unassignedwords.setObjectName("tableWidget_unassignedwords")
        self.tableWidget_unassignedwords.setFrameShape(QFrame.NoFrame)
        self.tableWidget_unassignedwords.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tableWidget_unassignedwords.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_unassignedwords.setSelectionBehavior(
            QAbstractItemView.SelectItems
        )
        self.tableWidget_unassignedwords.setShowGrid(False)
        self.tableWidget_unassignedwords.setRowCount(0)
        self.tableWidget_unassignedwords.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_unassignedwords.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidget_unassignedwords, 4, 2, 1, 4)

        self.verticalLayout_3.addWidget(self.widget_sp_reactivefeedbackcontents)

        self.gridLayout_7.addWidget(self.widget, 0, 2, 2, 1, Qt.AlignTop)

        self.widget_sp_savebuttoncontainer = QWidget(SpeakerIdTab)
        self.widget_sp_savebuttoncontainer.setObjectName(
            "widget_sp_savebuttoncontainer"
        )
        self.gridLayout_5 = QGridLayout(self.widget_sp_savebuttoncontainer)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, 30, -1)
        self.btn_sp_save = QPushButton(self.widget_sp_savebuttoncontainer)
        self.btn_sp_save.setObjectName("btn_sp_save")
        self.btn_sp_save.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_sp_save.sizePolicy().hasHeightForWidth())
        self.btn_sp_save.setSizePolicy(sizePolicy8)
        self.btn_sp_save.setFont(font)
        self.btn_sp_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sp_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_sp_save.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )

        self.gridLayout_5.addWidget(self.btn_sp_save, 0, 1, 1, 1, Qt.AlignRight)

        self.btn_sp_cancel = QPushButton(self.widget_sp_savebuttoncontainer)
        self.btn_sp_cancel.setObjectName("btn_sp_cancel")
        self.btn_sp_cancel.setFont(font)
        self.btn_sp_cancel.setStyleSheet(
            "QPushButton {\n"
            "	color: black;\n"
            "	background-color: white;\n"
            "	border-style: solid;\n"
            "	border-color: black;\n"
            "	border-width: 2px;\n"
            "	border-radius: 10px;\n"
            "    min-width: 250px;\n"
            "	min-height: 80px;\n"
            "    margin-top: 10px; \n"
            "    margin-bottom: 10px;\n"
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

        self.gridLayout_5.addWidget(self.btn_sp_cancel, 0, 0, 1, 1, Qt.AlignLeft)

        self.gridLayout_7.addWidget(
            self.widget_sp_savebuttoncontainer, 1, 0, 1, 1, Qt.AlignBottom
        )

        self.line = QFrame(SpeakerIdTab)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line, 0, 1, 2, 1)

        self.retranslateUi(SpeakerIdTab)

        QMetaObject.connectSlotsByName(SpeakerIdTab)

    # setupUi

    def retranslateUi(self, SpeakerIdTab):
        self.label_sp_h.setText(
            QCoreApplication.translate("SpeakerIdTab", "Speaker identification", None)
        )
        self.label_sp_description_2.setText(
            QCoreApplication.translate(
                "SpeakerIdTab",
                "CorpusCompass can only process documents that have a clear and consistent format of indicating which text is spoken by which speaker. This requires a consistent transcription format. You can see examples and select your used format below, on which the menu on the right will provide feedback. If no format applies to your corpus, we suggest you to adapt your corpus format!",
                None,
            )
        )
        self.label_sp_subheader.setText(
            QCoreApplication.translate(
                "SpeakerIdTab",
                "Specify your transcription format so that CorpusCompass can detect and identify all speakers in your corpus and associate them to their spoken text!",
                None,
            )
        )
        self.radbtn_sp_flex.setText(
            QCoreApplication.translate("SpeakerIdTab", "Flex", None)
        )
        self.label_sp_helppraat.setText("")
        self.radbtn_sp_elan.setText(
            QCoreApplication.translate("SpeakerIdTab", "ELAN", None)
        )
        # if QT_CONFIG(tooltip)
        self.label_sp_helpstandard.setToolTip(
            QCoreApplication.translate(
                "SpeakerIdTab",
                '<html><head/><body><p><span style=" font-size:11pt; font-weight:700; font-style:italic;">Example of the Standard-Format:</span></p><p>&quot;A&quot;: Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text Paragraph-Text</p><p>&quot;B&quot;: NewParagraph-Text NewParagraph-Text NewParagraph-Text NewParagraph-Text NewParagraph-Text</p><p>&quot;A&quot;: NewParagraph-Text</p><p>&quot;C&quot;: NewParagraph-Text</p><p><br/></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_sp_helpstandard.setText("")
        self.label_sp_helpflex.setText("")
        self.label_sp_helpelan.setText("")
        self.radbtn_sp_standard.setText(
            QCoreApplication.translate("SpeakerIdTab", "CorpusCompass-Standard", None)
        )
        self.radbtn_sp_praat.setText(
            QCoreApplication.translate("SpeakerIdTab", "Praat", None)
        )
        self.label_sp_detectedspeakerstitle.setText(
            QCoreApplication.translate(
                "SpeakerIdTab", "Detected speakers\nfor selected format", None
            )
        )
        self.btn_expand_wordinfo.setText(
            QCoreApplication.translate("SpeakerIdTab", "\u25b6", None)
        )
        self.btn_expand_speakerinfo.setText(
            QCoreApplication.translate("SpeakerIdTab", "\u25b6", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("SpeakerIdTab", "Unassigned words:", None)
        )
        self.label_distinctspeakercount.setText(
            QCoreApplication.translate("SpeakerIdTab", "12", None)
        )
        self.label_unassignedwordcount.setText(
            QCoreApplication.translate("SpeakerIdTab", "292", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("SpeakerIdTab", "Distinct speakers:", None)
        )
        ___qtablewidgetitem = self.tableWidget_distinctspeakers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("SpeakerIdTab", "Speaker", None)
        )
        ___qtablewidgetitem1 = self.tableWidget_distinctspeakers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("SpeakerIdTab", "in Files", None)
        )
        ___qtablewidgetitem2 = self.tableWidget_unassignedwords.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("SpeakerIdTab", "File", None)
        )
        ___qtablewidgetitem3 = self.tableWidget_unassignedwords.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("SpeakerIdTab", "Amount", None)
        )
        self.btn_sp_save.setText(
            QCoreApplication.translate("SpeakerIdTab", "Save", None)
        )
        self.btn_sp_cancel.setText(
            QCoreApplication.translate("SpeakerIdTab", "Cancel", None)
        )
        pass

    # retranslateUi
