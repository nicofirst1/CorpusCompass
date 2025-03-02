# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_symbol_dialogGXKQck.ui'
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
    QApplication,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QListView,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_AddSymbolsDialog(object):
    def setupUi(self, AddSymbolsDialog):
        if not AddSymbolsDialog.objectName():
            AddSymbolsDialog.setObjectName("AddSymbolsDialog")
        AddSymbolsDialog.resize(456, 463)
        self.gridLayout_2 = QGridLayout(AddSymbolsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QWidget(AddSymbolsDialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_symbolalreadyadded = QLabel(self.widget)
        self.label_symbolalreadyadded.setObjectName("label_symbolalreadyadded")
        self.label_symbolalreadyadded.setStyleSheet("QLabel{color: red}")

        self.gridLayout.addWidget(self.label_symbolalreadyadded, 9, 1, 1, 1)

        self.listwidget_annotformat_oldsymbols = QListWidget(self.widget)
        self.listwidget_annotformat_oldsymbols.setObjectName(
            "listwidget_annotformat_oldsymbols"
        )
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listwidget_annotformat_oldsymbols.sizePolicy().hasHeightForWidth()
        )
        self.listwidget_annotformat_oldsymbols.setSizePolicy(sizePolicy)
        self.listwidget_annotformat_oldsymbols.setMinimumSize(QSize(0, 75))
        self.listwidget_annotformat_oldsymbols.setStyleSheet("")
        self.listwidget_annotformat_oldsymbols.setDragEnabled(True)
        self.listwidget_annotformat_oldsymbols.setDragDropMode(
            QAbstractItemView.DragOnly
        )
        self.listwidget_annotformat_oldsymbols.setDefaultDropAction(Qt.CopyAction)
        self.listwidget_annotformat_oldsymbols.setFlow(QListView.LeftToRight)
        self.listwidget_annotformat_oldsymbols.setProperty("isWrapping", True)
        self.listwidget_annotformat_oldsymbols.setSpacing(3)
        self.listwidget_annotformat_oldsymbols.setViewMode(QListView.ListMode)
        self.listwidget_annotformat_oldsymbols.setUniformItemSizes(False)

        self.gridLayout.addWidget(self.listwidget_annotformat_oldsymbols, 1, 1, 1, 1)

        self.lineEdit_newsymbol = QLineEdit(self.widget)
        self.lineEdit_newsymbol.setObjectName("lineEdit_newsymbol")
        self.lineEdit_newsymbol.setMinimumSize(QSize(0, 30))
        self.lineEdit_newsymbol.setMaxLength(1)

        self.gridLayout.addWidget(self.lineEdit_newsymbol, 6, 1, 1, 1)

        self.listwidget_annotformat_symbolcontainer = QListWidget(self.widget)
        self.listwidget_annotformat_symbolcontainer.setObjectName(
            "listwidget_annotformat_symbolcontainer"
        )
        self.listwidget_annotformat_symbolcontainer.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(4)
        self.listwidget_annotformat_symbolcontainer.setFont(font)
        self.listwidget_annotformat_symbolcontainer.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.listwidget_annotformat_symbolcontainer.setFlow(QListView.LeftToRight)
        self.listwidget_annotformat_symbolcontainer.setSpacing(3)

        self.gridLayout.addWidget(
            self.listwidget_annotformat_symbolcontainer, 3, 1, 1, 1
        )

        self.label_addsymbol = QLabel(self.widget)
        self.label_addsymbol.setObjectName("label_addsymbol")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_addsymbol.setFont(font1)

        self.gridLayout.addWidget(self.label_addsymbol, 4, 1, 1, 1)

        self.btn_addsymbol = QPushButton(self.widget)
        self.btn_addsymbol.setObjectName("btn_addsymbol")

        self.gridLayout.addWidget(self.btn_addsymbol, 7, 1, 1, 1)

        self.label_currentsymbols = QLabel(self.widget)
        self.label_currentsymbols.setObjectName("label_currentsymbols")
        self.label_currentsymbols.setFont(font1)

        self.gridLayout.addWidget(self.label_currentsymbols, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddSymbolsDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(AddSymbolsDialog)
        self.buttonBox.rejected.connect(AddSymbolsDialog.reject)
        self.buttonBox.accepted.connect(AddSymbolsDialog.accept)

        QMetaObject.connectSlotsByName(AddSymbolsDialog)

    # setupUi

    def retranslateUi(self, AddSymbolsDialog):
        AddSymbolsDialog.setWindowTitle(
            QCoreApplication.translate("AddSymbolsDialog", "Dialog", None)
        )
        self.label_symbolalreadyadded.setText(
            QCoreApplication.translate(
                "AddSymbolsDialog", "Symbol already added!", None
            )
        )
        self.lineEdit_newsymbol.setText("")
        self.lineEdit_newsymbol.setPlaceholderText(
            QCoreApplication.translate(
                "AddSymbolsDialog", "Type in symbol to add...", None
            )
        )
        self.label_addsymbol.setText(
            QCoreApplication.translate("AddSymbolsDialog", "Add Symbol:", None)
        )
        self.btn_addsymbol.setText(
            QCoreApplication.translate("AddSymbolsDialog", "+", None)
        )
        self.label_currentsymbols.setText(
            QCoreApplication.translate("AddSymbolsDialog", "Current Symbols:", None)
        )
        self.label.setText(
            QCoreApplication.translate("AddSymbolsDialog", "Newly added symbols:", None)
        )

    # retranslateUi
