# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invalid_input_warning_dialogcolLbZ.ui'
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

class Ui_InvalidInputWarningDialog(object):
    def setupUi(self, InvalidInputWarningDialog):
        if not InvalidInputWarningDialog.objectName():
            InvalidInputWarningDialog.setObjectName(u"InvalidInputWarningDialog")
        InvalidInputWarningDialog.resize(400, 185)
        self.verticalLayout = QVBoxLayout(InvalidInputWarningDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_header = QLabel(InvalidInputWarningDialog)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout.addWidget(self.label_header, 0, Qt.AlignTop)

        self.label_2 = QLabel(InvalidInputWarningDialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(InvalidInputWarningDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(InvalidInputWarningDialog)
        self.buttonBox.accepted.connect(InvalidInputWarningDialog.accept)
        self.buttonBox.rejected.connect(InvalidInputWarningDialog.reject)

        QMetaObject.connectSlotsByName(InvalidInputWarningDialog)
    # setupUi

    def retranslateUi(self, InvalidInputWarningDialog):
        InvalidInputWarningDialog.setWindowTitle(QCoreApplication.translate("InvalidInputWarningDialog", u"Dialog", None))
        self.label_header.setText(QCoreApplication.translate("InvalidInputWarningDialog", u"Warning!", None))
        self.label_2.setText(QCoreApplication.translate("InvalidInputWarningDialog", u"It seems like some of your input data is not in a valid format! Check your formats again and look out for indicators that highlight the wrong formats. Correct it to the rules accordingly. ", None))
    # retranslateUi

