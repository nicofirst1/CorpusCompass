# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotationformat_editor_dialogzzqlPN.ui'
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
    QCheckBox,
    QComboBox,
    QDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QListView,
    QListWidget,
    QListWidgetItem,
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


class Ui_EditorAnnotationformatDialog(object):
    def setupUi(self, EditorAnnotationformatDialog):
        if not EditorAnnotationformatDialog.objectName():
            EditorAnnotationformatDialog.setObjectName("EditorAnnotationformatDialog")
        EditorAnnotationformatDialog.resize(1387, 795)
        self.verticalLayout_2 = QVBoxLayout(EditorAnnotationformatDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_annotdial_overall = QWidget(EditorAnnotationformatDialog)
        self.widget_annotdial_overall.setObjectName("widget_annotdial_overall")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_annotdial_overall.sizePolicy().hasHeightForWidth()
        )
        self.widget_annotdial_overall.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_annotdial_overall)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_specificationcontents = QWidget(self.widget_annotdial_overall)
        self.widget_specificationcontents.setObjectName("widget_specificationcontents")
        self.widget_specificationcontents.setEnabled(False)
        sizePolicy.setHeightForWidth(
            self.widget_specificationcontents.sizePolicy().hasHeightForWidth()
        )
        self.widget_specificationcontents.setSizePolicy(sizePolicy)
        self.widget_specificationcontents.setMaximumSize(QSize(16777215, 400))
        self.gridLayout_2 = QGridLayout(self.widget_specificationcontents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_resetseparator = QPushButton(self.widget_specificationcontents)
        self.btn_resetseparator.setObjectName("btn_resetseparator")
        self.btn_resetseparator.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 1px solid white;\n"
            "	color: white;\n"
            " 	height: 30px;\n"
            "	width: 30px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: lightgrey;\n"
            "    color: dark grey; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: darkgrey;\n"
            "}\n"
            ""
        )
        icon = QIcon()
        icon.addFile(
            ":/images/images/refresh_icon.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_resetseparator.setIcon(icon)
        self.btn_resetseparator.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_resetseparator, 6, 4, 1, 1)

        self.label_3 = QLabel(self.widget_specificationcontents)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(3)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(":/images/images/trash_icon_fat.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_3, 7, 3, 1, 1, Qt.AlignHCenter)

        self.btn_annotdial_resetformat = QPushButton(self.widget_specificationcontents)
        self.btn_annotdial_resetformat.setObjectName("btn_annotdial_resetformat")
        self.btn_annotdial_resetformat.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 1px solid white;\n"
            "	color: white;\n"
            " 	height: 30px;\n"
            "	width: 30px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: lightgrey;\n"
            "    color: dark grey; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: darkgrey;\n"
            "}\n"
            ""
        )
        self.btn_annotdial_resetformat.setIcon(icon)
        self.btn_annotdial_resetformat.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.btn_annotdial_resetformat, 4, 4, 1, 1)

        self.listwidget_annotformat_tokenidentcontainer = QListWidget(
            self.widget_specificationcontents
        )
        self.listwidget_annotformat_tokenidentcontainer.setObjectName(
            "listwidget_annotformat_tokenidentcontainer"
        )
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.listwidget_annotformat_tokenidentcontainer.sizePolicy().hasHeightForWidth()
        )
        self.listwidget_annotformat_tokenidentcontainer.setSizePolicy(sizePolicy1)
        self.listwidget_annotformat_tokenidentcontainer.setMinimumSize(QSize(0, 75))
        self.listwidget_annotformat_tokenidentcontainer.setMaximumSize(
            QSize(16777215, 100)
        )
        self.listwidget_annotformat_tokenidentcontainer.setDragEnabled(True)
        self.listwidget_annotformat_tokenidentcontainer.setDragDropMode(
            QAbstractItemView.DragOnly
        )
        self.listwidget_annotformat_tokenidentcontainer.setDefaultDropAction(
            Qt.MoveAction
        )
        self.listwidget_annotformat_tokenidentcontainer.setFlow(QListView.TopToBottom)

        self.gridLayout_2.addWidget(
            self.listwidget_annotformat_tokenidentcontainer, 8, 0, 1, 1
        )

        self.label_annotdial_helpinput = QLabel(self.widget_specificationcontents)
        self.label_annotdial_helpinput.setObjectName("label_annotdial_helpinput")
        self.label_annotdial_helpinput.setToolTipDuration(-1)
        self.label_annotdial_helpinput.setPixmap(
            QPixmap(":/images/images/Help_Icon.svg")
        )

        self.gridLayout_2.addWidget(
            self.label_annotdial_helpinput, 3, 3, 1, 1, Qt.AlignRight
        )

        self.vwidget_corpuspreview = QWidget(self.widget_specificationcontents)
        self.vwidget_corpuspreview.setObjectName("vwidget_corpuspreview")
        self.verticalLayout_4 = QVBoxLayout(self.vwidget_corpuspreview)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_corpuspreview = QLabel(self.vwidget_corpuspreview)
        self.label_corpuspreview.setObjectName("label_corpuspreview")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.label_corpuspreview.sizePolicy().hasHeightForWidth()
        )
        self.label_corpuspreview.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_corpuspreview.setFont(font1)
        self.label_corpuspreview.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_corpuspreview)

        self.tablewidget_annotdial_corpuspreview = QTableWidget(
            self.vwidget_corpuspreview
        )
        if self.tablewidget_annotdial_corpuspreview.columnCount() < 3:
            self.tablewidget_annotdial_corpuspreview.setColumnCount(3)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2)
        self.tablewidget_annotdial_corpuspreview.setHorizontalHeaderItem(
            0, __qtablewidgetitem
        )
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2)
        self.tablewidget_annotdial_corpuspreview.setHorizontalHeaderItem(
            1, __qtablewidgetitem1
        )
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2)
        self.tablewidget_annotdial_corpuspreview.setHorizontalHeaderItem(
            2, __qtablewidgetitem2
        )
        self.tablewidget_annotdial_corpuspreview.setObjectName(
            "tablewidget_annotdial_corpuspreview"
        )
        self.tablewidget_annotdial_corpuspreview.setStyleSheet(
            "QTableWidget {\n"
            "    font-size: 10pt; /* Set the font size */\n"
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
            "    background-color: lightgray; /* Example: change background color when hovering */\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:checked:hover {\n"
            "    /* Adjust the appearance of the checked checkbox when hovering */\n"
            "    background-color: rgb(255, 166, 167); /* Example: change background color of checked checkbox when hovering */\n"
            "\n"
            "}"
        )
        self.tablewidget_annotdial_corpuspreview.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tablewidget_annotdial_corpuspreview.setRowCount(0)
        self.tablewidget_annotdial_corpuspreview.horizontalHeader().setDefaultSectionSize(
            125
        )
        self.tablewidget_annotdial_corpuspreview.horizontalHeader().setStretchLastSection(
            True
        )
        self.tablewidget_annotdial_corpuspreview.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.tablewidget_annotdial_corpuspreview)

        self.label_total_detected_annotations = QLabel(self.vwidget_corpuspreview)
        self.label_total_detected_annotations.setObjectName(
            "label_total_detected_annotations"
        )
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_total_detected_annotations.setFont(font3)

        self.verticalLayout_4.addWidget(
            self.label_total_detected_annotations, 0, Qt.AlignLeft
        )

        self.btn_testcurrentformat = QPushButton(self.vwidget_corpuspreview)
        self.btn_testcurrentformat.setObjectName("btn_testcurrentformat")

        self.verticalLayout_4.addWidget(self.btn_testcurrentformat)

        self.btn_loadmore = QPushButton(self.vwidget_corpuspreview)
        self.btn_loadmore.setObjectName("btn_loadmore")

        self.verticalLayout_4.addWidget(self.btn_loadmore)

        self.label_4 = QLabel(self.vwidget_corpuspreview)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("QLabel{color:red;}")

        self.verticalLayout_4.addWidget(self.label_4)

        self.gridLayout_2.addWidget(self.vwidget_corpuspreview, 3, 6, 16, 1)

        self.label_inputwarningmessage = QLabel(self.widget_specificationcontents)
        self.label_inputwarningmessage.setObjectName("label_inputwarningmessage")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_inputwarningmessage.setFont(font4)
        self.label_inputwarningmessage.setStyleSheet("QLabel{color:red;}")

        self.gridLayout_2.addWidget(self.label_inputwarningmessage, 3, 1, 1, 1)

        self.listwidget_annotdial_inputformat = QListWidget(
            self.widget_specificationcontents
        )
        self.listwidget_annotdial_inputformat.setObjectName(
            "listwidget_annotdial_inputformat"
        )
        sizePolicy1.setHeightForWidth(
            self.listwidget_annotdial_inputformat.sizePolicy().hasHeightForWidth()
        )
        self.listwidget_annotdial_inputformat.setSizePolicy(sizePolicy1)
        self.listwidget_annotdial_inputformat.setMinimumSize(QSize(0, 55))
        self.listwidget_annotdial_inputformat.setMaximumSize(QSize(16777215, 120))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.listwidget_annotdial_inputformat.setFont(font5)
        self.listwidget_annotdial_inputformat.setStyleSheet("")
        self.listwidget_annotdial_inputformat.setFrameShape(QFrame.Box)
        self.listwidget_annotdial_inputformat.setFrameShadow(QFrame.Plain)
        self.listwidget_annotdial_inputformat.setLineWidth(2)
        self.listwidget_annotdial_inputformat.setMidLineWidth(0)
        self.listwidget_annotdial_inputformat.setDragEnabled(True)
        self.listwidget_annotdial_inputformat.setDragDropMode(
            QAbstractItemView.DragDrop
        )
        self.listwidget_annotdial_inputformat.setDefaultDropAction(Qt.MoveAction)
        self.listwidget_annotdial_inputformat.setFlow(QListView.LeftToRight)
        self.listwidget_annotdial_inputformat.setSpacing(5)

        self.gridLayout_2.addWidget(self.listwidget_annotdial_inputformat, 4, 0, 1, 4)

        self.label_inputformat = QLabel(self.widget_specificationcontents)
        self.label_inputformat.setObjectName("label_inputformat")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_inputformat.sizePolicy().hasHeightForWidth()
        )
        self.label_inputformat.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setPointSize(12)
        font6.setItalic(True)
        self.label_inputformat.setFont(font6)

        self.gridLayout_2.addWidget(self.label_inputformat, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.widget_multipleall = QWidget(self.widget_specificationcontents)
        self.widget_multipleall.setObjectName("widget_multipleall")
        self.horizontalLayout = QHBoxLayout(self.widget_multipleall)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkbox_annotdial_multipleannot = QCheckBox(self.widget_multipleall)
        self.checkbox_annotdial_multipleannot.setObjectName(
            "checkbox_annotdial_multipleannot"
        )
        font7 = QFont()
        font7.setPointSize(12)
        self.checkbox_annotdial_multipleannot.setFont(font7)
        self.checkbox_annotdial_multipleannot.setChecked(True)

        self.horizontalLayout.addWidget(self.checkbox_annotdial_multipleannot)

        self.label_separator = QLabel(self.widget_multipleall)
        self.label_separator.setObjectName("label_separator")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(True)
        self.label_separator.setFont(font8)

        self.horizontalLayout.addWidget(self.label_separator)

        self.listwidget_annotdial_separatorsymbols = QListWidget(
            self.widget_multipleall
        )
        self.listwidget_annotdial_separatorsymbols.setObjectName(
            "listwidget_annotdial_separatorsymbols"
        )
        self.listwidget_annotdial_separatorsymbols.setEnabled(False)
        self.listwidget_annotdial_separatorsymbols.setMinimumSize(QSize(0, 45))
        self.listwidget_annotdial_separatorsymbols.setMaximumSize(QSize(16777215, 80))
        self.listwidget_annotdial_separatorsymbols.setLayoutDirection(Qt.LeftToRight)
        self.listwidget_annotdial_separatorsymbols.setDragEnabled(True)
        self.listwidget_annotdial_separatorsymbols.setDragDropMode(
            QAbstractItemView.DragDrop
        )
        self.listwidget_annotdial_separatorsymbols.setDefaultDropAction(Qt.MoveAction)
        self.listwidget_annotdial_separatorsymbols.setFlow(QListView.LeftToRight)

        self.horizontalLayout.addWidget(self.listwidget_annotdial_separatorsymbols)

        self.gridLayout_2.addWidget(self.widget_multipleall, 6, 0, 1, 4)

        self.label = QLabel(self.widget_specificationcontents)
        self.label.setObjectName("label")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.label.setFont(font9)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 7, 0, 1, 1)

        self.listwidget_annotformat_removeelems = QListWidget(
            self.widget_specificationcontents
        )
        self.listwidget_annotformat_removeelems.setObjectName(
            "listwidget_annotformat_removeelems"
        )
        sizePolicy1.setHeightForWidth(
            self.listwidget_annotformat_removeelems.sizePolicy().hasHeightForWidth()
        )
        self.listwidget_annotformat_removeelems.setSizePolicy(sizePolicy1)
        self.listwidget_annotformat_removeelems.setMinimumSize(QSize(0, 75))
        self.listwidget_annotformat_removeelems.setMaximumSize(QSize(60, 100))
        self.listwidget_annotformat_removeelems.setStyleSheet(
            "QListWidget { background-color: rgb(255, 176, 177); }"
        )
        self.listwidget_annotformat_removeelems.setDragEnabled(True)
        self.listwidget_annotformat_removeelems.setDragDropMode(
            QAbstractItemView.DropOnly
        )

        self.gridLayout_2.addWidget(self.listwidget_annotformat_removeelems, 8, 3, 1, 1)

        self.btn_annotdial_addsymbols = QPushButton(self.widget_specificationcontents)
        self.btn_annotdial_addsymbols.setObjectName("btn_annotdial_addsymbols")

        self.gridLayout_2.addWidget(self.btn_annotdial_addsymbols, 9, 1, 1, 1)

        self.label_annotdial_customdescription = QLabel(
            self.widget_specificationcontents
        )
        self.label_annotdial_customdescription.setObjectName(
            "label_annotdial_customdescription"
        )
        font10 = QFont()
        font10.setPointSize(11)
        self.label_annotdial_customdescription.setFont(font10)

        self.gridLayout_2.addWidget(self.label_annotdial_customdescription, 0, 0, 1, 7)

        self.label_2 = QLabel(self.widget_specificationcontents)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font9)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 7, 1, 1, 2)

        self.listwidget_annotformat_symbolcontainer = QListWidget(
            self.widget_specificationcontents
        )
        self.listwidget_annotformat_symbolcontainer.setObjectName(
            "listwidget_annotformat_symbolcontainer"
        )
        sizePolicy1.setHeightForWidth(
            self.listwidget_annotformat_symbolcontainer.sizePolicy().hasHeightForWidth()
        )
        self.listwidget_annotformat_symbolcontainer.setSizePolicy(sizePolicy1)
        self.listwidget_annotformat_symbolcontainer.setMinimumSize(QSize(0, 75))
        self.listwidget_annotformat_symbolcontainer.setMaximumSize(QSize(16777215, 100))
        self.listwidget_annotformat_symbolcontainer.setStyleSheet(
            "QListWidget::item {\n"
            "    margin: 6px; /* Adjust margin to increase/decrease the size of items */\n"
            "}"
        )
        self.listwidget_annotformat_symbolcontainer.setDragEnabled(True)
        self.listwidget_annotformat_symbolcontainer.setDragDropMode(
            QAbstractItemView.DragOnly
        )
        self.listwidget_annotformat_symbolcontainer.setDefaultDropAction(Qt.CopyAction)
        self.listwidget_annotformat_symbolcontainer.setFlow(QListView.LeftToRight)
        self.listwidget_annotformat_symbolcontainer.setProperty("isWrapping", True)
        self.listwidget_annotformat_symbolcontainer.setSpacing(3)
        self.listwidget_annotformat_symbolcontainer.setItemAlignment(
            Qt.AlignAbsolute
            | Qt.AlignBaseline
            | Qt.AlignBottom
            | Qt.AlignCenter
            | Qt.AlignHCenter
            | Qt.AlignJustify
            | Qt.AlignVCenter
        )

        self.gridLayout_2.addWidget(
            self.listwidget_annotformat_symbolcontainer, 8, 1, 1, 1
        )

        self.gridLayout_3.addWidget(self.widget_specificationcontents, 3, 0, 1, 1)

        self.groupBox_softwarebtns = QGroupBox(self.widget_annotdial_overall)
        self.groupBox_softwarebtns.setObjectName("groupBox_softwarebtns")
        self.gridLayout_4 = QGridLayout(self.groupBox_softwarebtns)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radbtn_annotdial_elanformat = QRadioButton(self.groupBox_softwarebtns)
        self.radbtn_annotdial_elanformat.setObjectName("radbtn_annotdial_elanformat")
        self.radbtn_annotdial_elanformat.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.radbtn_annotdial_elanformat.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_annotdial_elanformat.setSizePolicy(sizePolicy4)
        self.radbtn_annotdial_elanformat.setFont(font9)

        self.gridLayout_4.addWidget(self.radbtn_annotdial_elanformat, 1, 0, 1, 1)

        self.radbtn_annotdial_praatformat = QRadioButton(self.groupBox_softwarebtns)
        self.radbtn_annotdial_praatformat.setObjectName("radbtn_annotdial_praatformat")
        self.radbtn_annotdial_praatformat.setEnabled(False)
        sizePolicy4.setHeightForWidth(
            self.radbtn_annotdial_praatformat.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_annotdial_praatformat.setSizePolicy(sizePolicy4)
        self.radbtn_annotdial_praatformat.setFont(font9)

        self.gridLayout_4.addWidget(self.radbtn_annotdial_praatformat, 3, 0, 1, 1)

        self.radbtn_annotdial_flexformat = QRadioButton(self.groupBox_softwarebtns)
        self.radbtn_annotdial_flexformat.setObjectName("radbtn_annotdial_flexformat")
        self.radbtn_annotdial_flexformat.setEnabled(False)
        sizePolicy4.setHeightForWidth(
            self.radbtn_annotdial_flexformat.sizePolicy().hasHeightForWidth()
        )
        self.radbtn_annotdial_flexformat.setSizePolicy(sizePolicy4)
        self.radbtn_annotdial_flexformat.setFont(font9)

        self.gridLayout_4.addWidget(self.radbtn_annotdial_flexformat, 0, 0, 1, 1)

        self.label_annotdial_help_praat = QLabel(self.groupBox_softwarebtns)
        self.label_annotdial_help_praat.setObjectName("label_annotdial_help_praat")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.label_annotdial_help_praat.sizePolicy().hasHeightForWidth()
        )
        self.label_annotdial_help_praat.setSizePolicy(sizePolicy5)
        self.label_annotdial_help_praat.setPixmap(
            QPixmap(":/images/images/Help_Icon.svg")
        )

        self.gridLayout_4.addWidget(self.label_annotdial_help_praat, 0, 1, 1, 1)

        self.label_annotdial_help_elan = QLabel(self.groupBox_softwarebtns)
        self.label_annotdial_help_elan.setObjectName("label_annotdial_help_elan")
        sizePolicy5.setHeightForWidth(
            self.label_annotdial_help_elan.sizePolicy().hasHeightForWidth()
        )
        self.label_annotdial_help_elan.setSizePolicy(sizePolicy5)
        self.label_annotdial_help_elan.setPixmap(
            QPixmap(":/images/images/Help_Icon.svg")
        )

        self.gridLayout_4.addWidget(self.label_annotdial_help_elan, 1, 1, 1, 1)

        self.label_annotdial_help_flex = QLabel(self.groupBox_softwarebtns)
        self.label_annotdial_help_flex.setObjectName("label_annotdial_help_flex")
        sizePolicy5.setHeightForWidth(
            self.label_annotdial_help_flex.sizePolicy().hasHeightForWidth()
        )
        self.label_annotdial_help_flex.setSizePolicy(sizePolicy5)
        self.label_annotdial_help_flex.setPixmap(
            QPixmap(":/images/images/Help_Icon.svg")
        )

        self.gridLayout_4.addWidget(self.label_annotdial_help_flex, 3, 1, 1, 1)

        self.gridLayout_3.addWidget(
            self.groupBox_softwarebtns, 6, 0, 1, 1, Qt.AlignLeft
        )

        self.radbtn_annotdial_customstyle = QRadioButton(self.widget_annotdial_overall)
        self.radbtn_annotdial_customstyle.setObjectName("radbtn_annotdial_customstyle")
        self.radbtn_annotdial_customstyle.setFont(font5)
        self.radbtn_annotdial_customstyle.setChecked(True)

        self.gridLayout_3.addWidget(
            self.radbtn_annotdial_customstyle, 2, 0, 1, 1, Qt.AlignTop
        )

        self.radbtn_annotdial_colorbased = QRadioButton(self.widget_annotdial_overall)
        self.radbtn_annotdial_colorbased.setObjectName("radbtn_annotdial_colorbased")
        self.radbtn_annotdial_colorbased.setEnabled(False)
        self.radbtn_annotdial_colorbased.setFont(font5)

        self.gridLayout_3.addWidget(
            self.radbtn_annotdial_colorbased, 7, 0, 1, 2, Qt.AlignTop
        )

        self.radbtn_annotdial_othersoft = QRadioButton(self.widget_annotdial_overall)
        self.radbtn_annotdial_othersoft.setObjectName("radbtn_annotdial_othersoft")
        self.radbtn_annotdial_othersoft.setEnabled(False)
        self.radbtn_annotdial_othersoft.setFont(font5)

        self.gridLayout_3.addWidget(self.radbtn_annotdial_othersoft, 5, 0, 1, 2)

        self.widget = QWidget(self.widget_annotdial_overall)
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_ivselect = QLabel(self.widget)
        self.label_ivselect.setObjectName("label_ivselect")
        font11 = QFont()
        font11.setPointSize(11)
        font11.setItalic(True)
        self.label_ivselect.setFont(font11)

        self.gridLayout.addWidget(self.label_ivselect, 1, 0, 1, 1)

        self.comboBox_selectformat = QComboBox(self.widget)
        self.comboBox_selectformat.setObjectName("comboBox_selectformat")
        self.comboBox_selectformat.setMinimumSize(QSize(173, 25))
        self.comboBox_selectformat.setStyleSheet(
            "QComboBox {\n"
            "    background-color: white;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 18px 1px 3px;\n"
            "    min-width: 6px;\n"
            "	min-width: 150px; \n"
            "	font-size: 16px;\n"
            "   font-weight: bold;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 20px;\n"
            "}\n"
            ""
        )
        self.comboBox_selectformat.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout.addWidget(self.comboBox_selectformat, 2, 0, 1, 1)

        self.btn_delete_annotformat = QPushButton(self.widget)
        self.btn_delete_annotformat.setObjectName("btn_delete_annotformat")
        self.btn_delete_annotformat.setEnabled(False)
        sizePolicy4.setHeightForWidth(
            self.btn_delete_annotformat.sizePolicy().hasHeightForWidth()
        )
        self.btn_delete_annotformat.setSizePolicy(sizePolicy4)
        self.btn_delete_annotformat.setMinimumSize(QSize(35, 35))
        self.btn_delete_annotformat.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(
            ":/images/images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_delete_annotformat.setIcon(icon1)
        self.btn_delete_annotformat.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_delete_annotformat, 2, 1, 1, 1)

        self.label_header = QLabel(self.widget)
        self.label_header.setObjectName("label_header")
        font12 = QFont()
        font12.setPointSize(18)
        font12.setBold(True)
        self.label_header.setFont(font12)

        self.gridLayout.addWidget(self.label_header, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.widget_annotdial_overall, 0, Qt.AlignTop)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_save = QPushButton(EditorAnnotationformatDialog)
        self.btn_save.setObjectName("btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(EditorAnnotationformatDialog)
        self.btn_cancel.setObjectName("btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(EditorAnnotationformatDialog)
        self.radbtn_annotdial_customstyle.toggled.connect(
            self.widget_specificationcontents.setVisible
        )
        self.radbtn_annotdial_othersoft.toggled.connect(
            self.groupBox_softwarebtns.setVisible
        )
        self.btn_cancel.clicked.connect(EditorAnnotationformatDialog.reject)

        QMetaObject.connectSlotsByName(EditorAnnotationformatDialog)

    # setupUi

    def retranslateUi(self, EditorAnnotationformatDialog):
        EditorAnnotationformatDialog.setWindowTitle(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Dialog", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_resetseparator.setToolTip(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                '<html><head/><body><p><span style=" font-weight:700;">Reset separator</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_resetseparator.setText("")
        self.label_3.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_annotdial_resetformat.setToolTip(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                '<html><head/><body><p><span style=" font-weight:700;">Reset input</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_annotdial_resetformat.setText("")
        # if QT_CONFIG(tooltip)
        self.label_annotdial_helpinput.setToolTip(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:700; text-decoration: underline;">How to specify the annotation format:</span></p><p><span style=" font-size:10pt;">The format can be built by dragging and dropping the corresponding elements in the &quot;input&quot; field at the top and (optionally) the &quot;separator&quot; field below. </span></p><p><span style=" font-size:10pt;">1. Each annotation-format needs to contain the &quot;token&quot; and &quot;identifier&quot;, which indicate where the original word (&quot;token&quot;), and where the added DV-Variant (&quot;identifier&quot;) is located in the annotation.</span></p><p><span style=" font-size:10pt;">2. To complete the annotation format, the symbols that were used to mark the annotations in the original corpus need to be placed and the correct position that matches the pattern of the original annotations.</span></p><p><span style=" font-size:10pt;">3. If the original corpus contains annotations with multiple DV-Variants in just'
                ' one annotation, the user may input the symbols that were used to separate these variants by checking the checkbox and dragging the symbols in the &quot;separator&quot;-field.</span></p><p><span style=" font-size:10pt; font-style:italic;">For more detailled information, click the &quot;Help-Button&quot; in the previous window that contains the table with all annotation formats.</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_annotdial_helpinput.setText("")
        self.label_corpuspreview.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Preview", None)
        )
        ___qtablewidgetitem = (
            self.tablewidget_annotdial_corpuspreview.horizontalHeaderItem(0)
        )
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Token", None)
        )
        ___qtablewidgetitem1 = (
            self.tablewidget_annotdial_corpuspreview.horizontalHeaderItem(1)
        )
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "#Annotations", None
            )
        )
        ___qtablewidgetitem2 = (
            self.tablewidget_annotdial_corpuspreview.horizontalHeaderItem(2)
        )
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Identifiers", None
            )
        )
        self.label_total_detected_annotations.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Total detected annotations: X", None
            )
        )
        self.btn_testcurrentformat.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Test current input", None
            )
        )
        self.btn_loadmore.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Load more...", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                "Could not identify any more annotations!",
                None,
            )
        )
        self.label_inputwarningmessage.setText("")
        self.label_inputformat.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Input your Annotation-Format:", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.checkbox_annotdial_multipleannot.setToolTip(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                '<html><head/><body><p>Check the box and add the separator symbol(s) (by dragging them in from above), if your corpus includes words that have more than one annotation.</p><p><span style=" font-weight:700; font-style:italic;">Multiple Identifiers </span><span style=" font-style:italic;">refer to tokens (&quot;words&quot;) in the corpus, that are annotated more than once. For each annotation, the corresponding identifer of the Dependent Variable Variant should be included in the annotation. The separator indicates the symbol that was used to separate the identifiers in the annotations.</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkbox_annotdial_multipleannot.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                "Multiple identifiers per token possible?",
                None,
            )
        )
        self.label_separator.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Separator: ", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Token & Identifier", None
            )
        )
        self.btn_annotdial_addsymbols.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Add more symbols...", None
            )
        )
        self.label_annotdial_customdescription.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                "Define the style/format you used for annotations in your already annotated corpus by dragging the elements in their corresponding position",
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Available Symbols", None
            )
        )
        self.groupBox_softwarebtns.setTitle("")
        self.radbtn_annotdial_elanformat.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "ELAN", None)
        )
        self.radbtn_annotdial_praatformat.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Praat", None)
        )
        self.radbtn_annotdial_flexformat.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Flex", None)
        )
        self.label_annotdial_help_praat.setText("")
        self.label_annotdial_help_elan.setText("")
        self.label_annotdial_help_flex.setText("")
        self.radbtn_annotdial_customstyle.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Specify custom annotation format", None
            )
        )
        self.radbtn_annotdial_colorbased.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Color-based annotation ", None
            )
        )
        self.radbtn_annotdial_othersoft.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog",
                "Select annotation format from other software",
                None,
            )
        )
        self.label_ivselect.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Select annotationformat to edit:", None
            )
        )
        self.comboBox_selectformat.setCurrentText("")
        self.comboBox_selectformat.setPlaceholderText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Select Annotation Format...", None
            )
        )
        self.btn_delete_annotformat.setText("")
        self.label_header.setText(
            QCoreApplication.translate(
                "EditorAnnotationformatDialog", "Annotation Format - Editor", None
            )
        )
        self.btn_save.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Save", None)
        )
        self.btn_cancel.setText(
            QCoreApplication.translate("EditorAnnotationformatDialog", "Cancel", None)
        )

    # retranslateUi
