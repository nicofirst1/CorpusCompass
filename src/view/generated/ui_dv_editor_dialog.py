# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dv_editor_dialogKRczYv.ui'
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
    QAbstractButton,
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_DVEditorDialog(object):
    def setupUi(self, DVEditorDialog):
        if not DVEditorDialog.objectName():
            DVEditorDialog.setObjectName("DVEditorDialog")
        DVEditorDialog.resize(640, 681)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DVEditorDialog.sizePolicy().hasHeightForWidth())
        DVEditorDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(DVEditorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(DVEditorDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_header = QLabel(self.widget_2)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_header.setFont(font)

        self.gridLayout.addWidget(self.label_header, 0, 0, 1, 1, Qt.AlignTop)

        self.comboBox_selectdv = QComboBox(self.widget_2)
        self.comboBox_selectdv.setObjectName("comboBox_selectdv")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.comboBox_selectdv.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_selectdv.setSizePolicy(sizePolicy2)
        self.comboBox_selectdv.setMinimumSize(QSize(119, 25))
        self.comboBox_selectdv.setStyleSheet(
            "QComboBox {\n"
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
            ""
        )
        self.comboBox_selectdv.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout.addWidget(self.comboBox_selectdv, 2, 0, 1, 1, Qt.AlignTop)

        self.label_selectdv = QLabel(self.widget_2)
        self.label_selectdv.setObjectName("label_selectdv")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_selectdv.setFont(font1)

        self.gridLayout.addWidget(self.label_selectdv, 1, 0, 1, 2, Qt.AlignTop)

        self.btn_delete_dv = QPushButton(self.widget_2)
        self.btn_delete_dv.setObjectName("btn_delete_dv")
        self.btn_delete_dv.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.btn_delete_dv.sizePolicy().hasHeightForWidth()
        )
        self.btn_delete_dv.setSizePolicy(sizePolicy3)
        self.btn_delete_dv.setMinimumSize(QSize(25, 25))
        self.btn_delete_dv.setStyleSheet(
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
        icon = QIcon()
        icon.addFile(":/images/images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_dv.setIcon(icon)

        self.gridLayout.addWidget(self.btn_delete_dv, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_dvname = QLabel(self.widget_2)
        self.label_dvname.setObjectName("label_dvname")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.label_dvname.sizePolicy().hasHeightForWidth()
        )
        self.label_dvname.setSizePolicy(sizePolicy4)
        self.label_dvname.setFont(font1)

        self.horizontalLayout.addWidget(self.label_dvname, 0, Qt.AlignTop)

        self.label_variableinputwarning = QLabel(self.widget_2)
        self.label_variableinputwarning.setObjectName("label_variableinputwarning")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_variableinputwarning.setFont(font2)
        self.label_variableinputwarning.setStyleSheet("QLabel{color:red;}")

        self.horizontalLayout.addWidget(
            self.label_variableinputwarning, 0, Qt.AlignRight
        )

        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_nameinput = QLineEdit(self.widget_2)
        self.lineEdit_nameinput.setObjectName("lineEdit_nameinput")
        self.lineEdit_nameinput.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.lineEdit_nameinput.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_nameinput.setSizePolicy(sizePolicy5)
        self.lineEdit_nameinput.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.lineEdit_nameinput, 0, Qt.AlignTop)

        self.btn_editconfirm = QPushButton(self.widget_2)
        self.btn_editconfirm.setObjectName("btn_editconfirm")
        self.btn_editconfirm.setEnabled(False)
        sizePolicy3.setHeightForWidth(
            self.btn_editconfirm.sizePolicy().hasHeightForWidth()
        )
        self.btn_editconfirm.setSizePolicy(sizePolicy3)
        self.btn_editconfirm.setMinimumSize(QSize(25, 25))
        self.btn_editconfirm.setStyleSheet(
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
            ":/images/images/checked_icon.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_editconfirm.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_editconfirm)

        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox_filter = QGroupBox(self.widget)
        self.groupBox_filter.setObjectName("groupBox_filter")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_filter)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_showonlycurrentvariants = QCheckBox(self.groupBox_filter)
        self.checkBox_showonlycurrentvariants.setObjectName(
            "checkBox_showonlycurrentvariants"
        )
        self.checkBox_showonlycurrentvariants.setEnabled(False)
        self.checkBox_showonlycurrentvariants.setChecked(True)

        self.verticalLayout_2.addWidget(
            self.checkBox_showonlycurrentvariants, 0, Qt.AlignTop
        )

        self.checkBox_unassociated_dvs = QCheckBox(self.groupBox_filter)
        self.checkBox_unassociated_dvs.setObjectName("checkBox_unassociated_dvs")
        self.checkBox_unassociated_dvs.setEnabled(False)
        self.checkBox_unassociated_dvs.setChecked(False)

        self.verticalLayout_2.addWidget(self.checkBox_unassociated_dvs, 0, Qt.AlignTop)

        self.lineEdit_searchvariants = QLineEdit(self.groupBox_filter)
        self.lineEdit_searchvariants.setObjectName("lineEdit_searchvariants")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.lineEdit_searchvariants.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_searchvariants.setSizePolicy(sizePolicy6)
        self.lineEdit_searchvariants.setMinimumSize(QSize(180, 0))
        self.lineEdit_searchvariants.setFrame(True)

        self.verticalLayout_2.addWidget(self.lineEdit_searchvariants)

        self.verticalLayout_3.addWidget(self.groupBox_filter)

        self.tableWidget_dialog_dvaddvariants = QTableWidget(self.widget)
        if self.tableWidget_dialog_dvaddvariants.columnCount() < 3:
            self.tableWidget_dialog_dvaddvariants.setColumnCount(3)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3)
        self.tableWidget_dialog_dvaddvariants.setHorizontalHeaderItem(
            0, __qtablewidgetitem
        )
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setUnderline(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4)
        self.tableWidget_dialog_dvaddvariants.setHorizontalHeaderItem(
            1, __qtablewidgetitem1
        )
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3)
        self.tableWidget_dialog_dvaddvariants.setHorizontalHeaderItem(
            2, __qtablewidgetitem2
        )
        self.tableWidget_dialog_dvaddvariants.setObjectName(
            "tableWidget_dialog_dvaddvariants"
        )
        self.tableWidget_dialog_dvaddvariants.setEnabled(False)
        sizePolicy7 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.tableWidget_dialog_dvaddvariants.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget_dialog_dvaddvariants.setSizePolicy(sizePolicy7)
        self.tableWidget_dialog_dvaddvariants.setMinimumSize(QSize(0, 300))
        self.tableWidget_dialog_dvaddvariants.setMaximumSize(QSize(16777215, 400))
        self.tableWidget_dialog_dvaddvariants.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_dialog_dvaddvariants.setStyleSheet(
            "QAbstractItemView::indicator{\n"
            "	width: 20px;\n"
            "	height: 20px;\n"
            "	margin-left: 20px;\n"
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
            "QTableWidget {\n"
            "    font-size: 12pt; /* Set the font size */\n"
            "    font-weight: bold; /* Set the font weight */\n"
            "}\n"
            "\n"
            "\n"
            "QAbstractItemView::indicator:hover {\n"
            "    /* Adjust the appearance of the hover indicator */\n"
            "    background-color: lightgray; /* Example: change background color when hovering */\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:checked:hover {\n"
            "    /* Adjust the appearance of the checked checkbox when hovering */\n"
            "    background-color: rgb(255, 166,"
            " 167); /* Example: change background color of checked checkbox when hovering */\n"
            "\n"
            "}\n"
            "\n"
            "QAbstractItemView::indicator:unchecked:hover {\n"
            "    /* Adjust the appearance of the unchecked checkbox when hovering */\n"
            "    background-color: lightgreen; /* Example: change background color of unchecked checkbox when hovering */\n"
            "}\n"
            "\n"
            ""
        )
        self.tableWidget_dialog_dvaddvariants.setFrameShape(QFrame.Box)
        self.tableWidget_dialog_dvaddvariants.setFrameShadow(QFrame.Plain)
        self.tableWidget_dialog_dvaddvariants.setLineWidth(2)
        self.tableWidget_dialog_dvaddvariants.setMidLineWidth(2)
        self.tableWidget_dialog_dvaddvariants.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )
        self.tableWidget_dialog_dvaddvariants.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.tableWidget_dialog_dvaddvariants.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContentsOnFirstShow
        )
        self.tableWidget_dialog_dvaddvariants.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tableWidget_dialog_dvaddvariants.setDragEnabled(True)
        self.tableWidget_dialog_dvaddvariants.setAlternatingRowColors(True)
        self.tableWidget_dialog_dvaddvariants.setSelectionMode(
            QAbstractItemView.NoSelection
        )
        self.tableWidget_dialog_dvaddvariants.setShowGrid(False)
        self.tableWidget_dialog_dvaddvariants.setGridStyle(Qt.NoPen)
        self.tableWidget_dialog_dvaddvariants.setSortingEnabled(True)
        self.tableWidget_dialog_dvaddvariants.setWordWrap(True)
        self.tableWidget_dialog_dvaddvariants.setCornerButtonEnabled(False)
        self.tableWidget_dialog_dvaddvariants.setRowCount(0)
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setVisible(True)
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setCascadingSectionResizes(
            False
        )
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setMinimumSectionSize(
            0
        )
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setDefaultSectionSize(
            200
        )
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setProperty(
            "showSortIndicator", True
        )
        self.tableWidget_dialog_dvaddvariants.horizontalHeader().setStretchLastSection(
            True
        )
        self.tableWidget_dialog_dvaddvariants.verticalHeader().setVisible(False)
        self.tableWidget_dialog_dvaddvariants.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_3.addWidget(self.tableWidget_dialog_dvaddvariants)

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(DVEditorDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DVEditorDialog)
        self.buttonBox.rejected.connect(DVEditorDialog.reject)
        self.buttonBox.accepted.connect(DVEditorDialog.accept)

        QMetaObject.connectSlotsByName(DVEditorDialog)

    # setupUi

    def retranslateUi(self, DVEditorDialog):
        DVEditorDialog.setWindowTitle(
            QCoreApplication.translate("DVEditorDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "DVEditorDialog", "Dependent Variable - Editor", None
            )
        )
        self.comboBox_selectdv.setCurrentText("")
        self.comboBox_selectdv.setPlaceholderText(
            QCoreApplication.translate(
                "DVEditorDialog", "Select Dependent Variable...", None
            )
        )
        self.label_selectdv.setText(
            QCoreApplication.translate(
                "DVEditorDialog", "Select Dependent Variable to edit:", None
            )
        )
        self.btn_delete_dv.setText("")
        self.label_dvname.setText(
            QCoreApplication.translate(
                "DVEditorDialog",
                "Change name (confirm with button on the right):",
                None,
            )
        )
        self.label_variableinputwarning.setText("")
        self.lineEdit_nameinput.setPlaceholderText(
            QCoreApplication.translate("DVEditorDialog", "Select DV above...", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_editconfirm.setToolTip(
            QCoreApplication.translate(
                "DVEditorDialog",
                "<html><head/><body><p>Confirm changes</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_editconfirm.setText("")
        self.label.setText(
            QCoreApplication.translate(
                "DVEditorDialog",
                "Tick variants that should be grouped to the selected DV:",
                None,
            )
        )
        self.groupBox_filter.setTitle(
            QCoreApplication.translate("DVEditorDialog", "Filter", None)
        )
        self.checkBox_showonlycurrentvariants.setText(
            QCoreApplication.translate(
                "DVEditorDialog",
                "Only show Variants that belong to the current DV",
                None,
            )
        )
        self.checkBox_unassociated_dvs.setText(
            QCoreApplication.translate(
                "DVEditorDialog",
                "Only show Variants that are not associated to a DV yet",
                None,
            )
        )
        self.lineEdit_searchvariants.setPlaceholderText(
            QCoreApplication.translate("DVEditorDialog", "Search by name...", None)
        )
        ___qtablewidgetitem = (
            self.tableWidget_dialog_dvaddvariants.horizontalHeaderItem(0)
        )
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("DVEditorDialog", "Variant", None)
        )
        ___qtablewidgetitem1 = (
            self.tableWidget_dialog_dvaddvariants.horizontalHeaderItem(1)
        )
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("DVEditorDialog", "Add", None)
        )
        ___qtablewidgetitem2 = (
            self.tableWidget_dialog_dvaddvariants.horizontalHeaderItem(2)
        )
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("DVEditorDialog", "Set Color", None)
        )


# retranslateUi
