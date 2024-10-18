# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iv_editor_dialogNqdemd.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_IVEditorDialog(object):
    def setupUi(self, IVEditorDialog):
        if not IVEditorDialog.objectName():
            IVEditorDialog.setObjectName(u"IVEditorDialog")
        IVEditorDialog.resize(566, 505)
        self.verticalLayout = QVBoxLayout(IVEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(IVEditorDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_selectiv = QComboBox(self.widget)
        self.comboBox_selectiv.setObjectName(u"comboBox_selectiv")
        self.comboBox_selectiv.setMinimumSize(QSize(119, 25))
        self.comboBox_selectiv.setStyleSheet(u"QComboBox {\n"
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
        self.comboBox_selectiv.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout.addWidget(self.comboBox_selectiv, 2, 0, 1, 2)

        self.btn_removevalue = QPushButton(self.widget)
        self.btn_removevalue.setObjectName(u"btn_removevalue")

        self.gridLayout.addWidget(self.btn_removevalue, 11, 0, 1, 2)

        self.tableWidget_storedvalues = QTableWidget(self.widget)
        if (self.tableWidget_storedvalues.columnCount() < 2):
            self.tableWidget_storedvalues.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_storedvalues.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_storedvalues.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_storedvalues.setObjectName(u"tableWidget_storedvalues")
        self.tableWidget_storedvalues.setStyleSheet(u"QAbstractItemView::indicator{\n"
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
"")
        self.tableWidget_storedvalues.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_storedvalues.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_storedvalues.setAlternatingRowColors(True)
        self.tableWidget_storedvalues.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_storedvalues.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_storedvalues.setShowGrid(False)
        self.tableWidget_storedvalues.setRowCount(0)
        self.tableWidget_storedvalues.horizontalHeader().setVisible(False)
        self.tableWidget_storedvalues.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_storedvalues.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget_storedvalues.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_storedvalues.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget_storedvalues, 10, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.lineEdit_nameinput = QLineEdit(self.widget)
        self.lineEdit_nameinput.setObjectName(u"lineEdit_nameinput")
        self.lineEdit_nameinput.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_nameinput.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameinput.setSizePolicy(sizePolicy1)
        self.lineEdit_nameinput.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.lineEdit_nameinput, 5, 0, 1, 2)

        self.lineEdit_valueinput = QLineEdit(self.widget)
        self.lineEdit_valueinput.setObjectName(u"lineEdit_valueinput")
        self.lineEdit_valueinput.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_valueinput, 8, 0, 1, 2)

        self.btn_editconfirm = QPushButton(self.widget)
        self.btn_editconfirm.setObjectName(u"btn_editconfirm")
        self.btn_editconfirm.setEnabled(False)
        self.btn_editconfirm.setMinimumSize(QSize(25, 25))
        self.btn_editconfirm.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/images/images/checked_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editconfirm.setIcon(icon)

        self.gridLayout.addWidget(self.btn_editconfirm, 5, 2, 1, 1)

        self.label_ivname = QLabel(self.widget)
        self.label_ivname.setObjectName(u"label_ivname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_ivname.sizePolicy().hasHeightForWidth())
        self.label_ivname.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_ivname.setFont(font)

        self.gridLayout.addWidget(self.label_ivname, 4, 0, 1, 1)

        self.btn_delete_iv = QPushButton(self.widget)
        self.btn_delete_iv.setObjectName(u"btn_delete_iv")
        self.btn_delete_iv.setEnabled(False)
        self.btn_delete_iv.setMinimumSize(QSize(25, 25))
        self.btn_delete_iv.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/images/images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_iv.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_delete_iv, 2, 2, 1, 1)

        self.label_header = QLabel(self.widget)
        self.label_header.setObjectName(u"label_header")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_header.setFont(font1)

        self.gridLayout.addWidget(self.label_header, 0, 0, 1, 2)

        self.btn_addvalue = QPushButton(self.widget)
        self.btn_addvalue.setObjectName(u"btn_addvalue")
        self.btn_addvalue.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_addvalue.sizePolicy().hasHeightForWidth())
        self.btn_addvalue.setSizePolicy(sizePolicy3)
        self.btn_addvalue.setMinimumSize(QSize(25, 25))
        self.btn_addvalue.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/images/Plus_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addvalue.setIcon(icon2)
        self.btn_addvalue.setCheckable(True)

        self.gridLayout.addWidget(self.btn_addvalue, 8, 2, 1, 1)

        self.label_storedvals = QLabel(self.widget)
        self.label_storedvals.setObjectName(u"label_storedvals")
        self.label_storedvals.setFont(font)
        self.label_storedvals.setWordWrap(True)

        self.gridLayout.addWidget(self.label_storedvals, 9, 0, 1, 1, Qt.AlignTop)

        self.label_valuename = QLabel(self.widget)
        self.label_valuename.setObjectName(u"label_valuename")
        sizePolicy2.setHeightForWidth(self.label_valuename.sizePolicy().hasHeightForWidth())
        self.label_valuename.setSizePolicy(sizePolicy2)
        self.label_valuename.setFont(font)

        self.gridLayout.addWidget(self.label_valuename, 7, 0, 1, 1)

        self.label_ivselect = QLabel(self.widget)
        self.label_ivselect.setObjectName(u"label_ivselect")
        self.label_ivselect.setFont(font)

        self.gridLayout.addWidget(self.label_ivselect, 1, 0, 1, 2)

        self.label_valueinputwarning = QLabel(self.widget)
        self.label_valueinputwarning.setObjectName(u"label_valueinputwarning")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_valueinputwarning.setFont(font2)
        self.label_valueinputwarning.setStyleSheet(u"QLabel{color:red;}")

        self.gridLayout.addWidget(self.label_valueinputwarning, 7, 1, 1, 1, Qt.AlignRight)

        self.label_variableinputwarning = QLabel(self.widget)
        self.label_variableinputwarning.setObjectName(u"label_variableinputwarning")
        self.label_variableinputwarning.setFont(font2)
        self.label_variableinputwarning.setStyleSheet(u"QLabel{color:red;}")

        self.gridLayout.addWidget(self.label_variableinputwarning, 4, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(IVEditorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(IVEditorDialog)
        self.buttonBox.accepted.connect(IVEditorDialog.accept)
        self.buttonBox.rejected.connect(IVEditorDialog.reject)

        QMetaObject.connectSlotsByName(IVEditorDialog)
    # setupUi

    def retranslateUi(self, IVEditorDialog):
        IVEditorDialog.setWindowTitle(QCoreApplication.translate("IVEditorDialog", u"Dialog", None))
        self.comboBox_selectiv.setCurrentText("")
        self.comboBox_selectiv.setPlaceholderText(QCoreApplication.translate("IVEditorDialog", u"Select Independent Variable...", None))
        self.btn_removevalue.setText(QCoreApplication.translate("IVEditorDialog", u"Remove selected", None))
        ___qtablewidgetitem = self.tableWidget_storedvalues.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("IVEditorDialog", u"Delete", None));
        ___qtablewidgetitem1 = self.tableWidget_storedvalues.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("IVEditorDialog", u"IV-Value", None));
        self.lineEdit_nameinput.setPlaceholderText(QCoreApplication.translate("IVEditorDialog", u"Select IV above...", None))
        self.lineEdit_valueinput.setPlaceholderText(QCoreApplication.translate("IVEditorDialog", u"IV-Value (\"Young\", \"Old\", ...)", None))
#if QT_CONFIG(tooltip)
        self.btn_editconfirm.setToolTip(QCoreApplication.translate("IVEditorDialog", u"<html><head/><body><p>Confirm changes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_editconfirm.setText("")
        self.label_ivname.setText(QCoreApplication.translate("IVEditorDialog", u"Change name (confirm with button on the right):", None))
        self.btn_delete_iv.setText("")
        self.label_header.setText(QCoreApplication.translate("IVEditorDialog", u"Independent Variable - Editor", None))
#if QT_CONFIG(tooltip)
        self.btn_addvalue.setToolTip(QCoreApplication.translate("IVEditorDialog", u"<html><head/><body><p>Add input value to current IV</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_addvalue.setText("")
        self.label_storedvals.setText(QCoreApplication.translate("IVEditorDialog", u"Current values for selected IV:", None))
        self.label_valuename.setText(QCoreApplication.translate("IVEditorDialog", u"Add value:", None))
        self.label_ivselect.setText(QCoreApplication.translate("IVEditorDialog", u"Select Independent Variable to edit:", None))
        self.label_valueinputwarning.setText("")
        self.label_variableinputwarning.setText("")
    # retranslateUi

