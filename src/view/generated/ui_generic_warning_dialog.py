# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generic_warning_dialogkoOcFf.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_GenericWarningDialog(object):
    def setupUi(self, GenericWarningDialog):
        if not GenericWarningDialog.objectName():
            GenericWarningDialog.setObjectName(u"GenericWarningDialog")
        GenericWarningDialog.resize(400, 195)
        self.verticalLayout = QVBoxLayout(GenericWarningDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_header = QLabel(GenericWarningDialog)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout.addWidget(self.label_header, 0, Qt.AlignTop)

        self.label_2 = QLabel(GenericWarningDialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(GenericWarningDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(GenericWarningDialog)
        self.buttonBox.accepted.connect(GenericWarningDialog.accept)
        self.buttonBox.rejected.connect(GenericWarningDialog.reject)

        QMetaObject.connectSlotsByName(GenericWarningDialog)
    # setupUi

    def retranslateUi(self, GenericWarningDialog):
        GenericWarningDialog.setWindowTitle(QCoreApplication.translate("GenericWarningDialog", u"Dialog", None))
        self.label_header.setText(QCoreApplication.translate("GenericWarningDialog", u"Warning!", None))
        self.label_2.setText(QCoreApplication.translate("GenericWarningDialog", u"If you do not wish to save your changes, all progress since the last save will be lost! Proceed?", None))
    # retranslateUi

