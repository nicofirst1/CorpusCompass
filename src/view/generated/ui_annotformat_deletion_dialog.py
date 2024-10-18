# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotformat_deletion_dialogkLlZPq.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_AnnotationFormatRemoveDialog(object):
    def setupUi(self, AnnotationFormatRemoveDialog):
        if not AnnotationFormatRemoveDialog.objectName():
            AnnotationFormatRemoveDialog.setObjectName(u"AnnotationFormatRemoveDialog")
        AnnotationFormatRemoveDialog.resize(443, 234)
        self.gridLayout = QGridLayout(AnnotationFormatRemoveDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_showagain = QCheckBox(AnnotationFormatRemoveDialog)
        self.checkBox_showagain.setObjectName(u"checkBox_showagain")

        self.gridLayout.addWidget(self.checkBox_showagain, 1, 0, 1, 1, Qt.AlignRight)

        self.widget = QWidget(AnnotationFormatRemoveDialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_warning = QLabel(self.widget)
        self.label_warning.setObjectName(u"label_warning")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_warning.setFont(font)

        self.gridLayout_2.addWidget(self.label_warning, 0, 0, 2, 3)

        self.label_cannotbeundone = QLabel(self.widget)
        self.label_cannotbeundone.setObjectName(u"label_cannotbeundone")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_cannotbeundone.setFont(font1)
        self.label_cannotbeundone.setStyleSheet(u"QLabel{color: red}")

        self.gridLayout_2.addWidget(self.label_cannotbeundone, 4, 0, 1, 2)

        self.label_subheader = QLabel(self.widget)
        self.label_subheader.setObjectName(u"label_subheader")
        self.label_subheader.setFont(font1)

        self.gridLayout_2.addWidget(self.label_subheader, 2, 0, 1, 1)

        self.label_annotlost = QLabel(self.widget)
        self.label_annotlost.setObjectName(u"label_annotlost")
        font2 = QFont()
        font2.setItalic(True)
        self.label_annotlost.setFont(font2)

        self.gridLayout_2.addWidget(self.label_annotlost, 7, 0, 1, 2)

        self.label_formatsdelete = QLabel(self.widget)
        self.label_formatsdelete.setObjectName(u"label_formatsdelete")
        self.label_formatsdelete.setFont(font2)

        self.gridLayout_2.addWidget(self.label_formatsdelete, 6, 0, 1, 1)

        self.label_contentannotlost = QLabel(self.widget)
        self.label_contentannotlost.setObjectName(u"label_contentannotlost")

        self.gridLayout_2.addWidget(self.label_contentannotlost, 7, 2, 1, 1)

        self.label_contentformatdelete = QLabel(self.widget)
        self.label_contentformatdelete.setObjectName(u"label_contentformatdelete")

        self.gridLayout_2.addWidget(self.label_contentformatdelete, 6, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, Qt.AlignTop)

        self.horizontalWidget = QWidget(AnnotationFormatRemoveDialog)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ignore = QPushButton(self.horizontalWidget)
        self.btn_ignore.setObjectName(u"btn_ignore")

        self.horizontalLayout.addWidget(self.btn_ignore)

        self.btn_cancel = QPushButton(self.horizontalWidget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.gridLayout.addWidget(self.horizontalWidget, 2, 0, 1, 1, Qt.AlignRight)


        self.retranslateUi(AnnotationFormatRemoveDialog)
        self.btn_ignore.clicked.connect(AnnotationFormatRemoveDialog.accept)
        self.btn_cancel.clicked.connect(AnnotationFormatRemoveDialog.reject)

        QMetaObject.connectSlotsByName(AnnotationFormatRemoveDialog)
    # setupUi

    def retranslateUi(self, AnnotationFormatRemoveDialog):
        AnnotationFormatRemoveDialog.setWindowTitle(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Dialog", None))
        self.checkBox_showagain.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Don't show this warning again", None))
        self.label_warning.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Warning!", None))
        self.label_cannotbeundone.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"This action cannot be undone! ", None))
        self.label_subheader.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Do you really wish to delete all selected annotation formats?", None))
        self.label_annotlost.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Lost annotations after removal of formats:", None))
        self.label_formatsdelete.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Formats to delete:", None))
        self.label_contentannotlost.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"209", None))
        self.label_contentformatdelete.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"2", None))
        self.btn_ignore.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Ignore", None))
        self.btn_cancel.setText(QCoreApplication.translate("AnnotationFormatRemoveDialog", u"Cancel", None))
    # retranslateUi

