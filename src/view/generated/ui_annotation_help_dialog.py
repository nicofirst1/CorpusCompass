# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation_help_dialogVSBfRC.ui'
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

class Ui_AnnotationHelpDialog(object):
    def setupUi(self, AnnotationHelpDialog):
        if not AnnotationHelpDialog.objectName():
            AnnotationHelpDialog.setObjectName(u"AnnotationHelpDialog")
        AnnotationHelpDialog.resize(713, 416)
        self.verticalLayout = QVBoxLayout(AnnotationHelpDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AnnotationHelpDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_header = QLabel(self.widget)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_2.addWidget(self.label_header)

        self.label_symoblbased = QLabel(self.widget)
        self.label_symoblbased.setObjectName(u"label_symoblbased")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        font1.setUnderline(True)
        self.label_symoblbased.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_symoblbased)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_colorbased = QLabel(self.widget)
        self.label_colorbased.setObjectName(u"label_colorbased")
        self.label_colorbased.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_colorbased)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(AnnotationHelpDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AnnotationHelpDialog)
        self.buttonBox.accepted.connect(AnnotationHelpDialog.accept)
        self.buttonBox.rejected.connect(AnnotationHelpDialog.reject)

        QMetaObject.connectSlotsByName(AnnotationHelpDialog)
    # setupUi

    def retranslateUi(self, AnnotationHelpDialog):
        AnnotationHelpDialog.setWindowTitle(QCoreApplication.translate("AnnotationHelpDialog", u"Dialog", None))
        self.label_header.setText(QCoreApplication.translate("AnnotationHelpDialog", u"How to specify an annotation format?", None))
        self.label_symoblbased.setText(QCoreApplication.translate("AnnotationHelpDialog", u"Information on symbol-based annotation", None))
        self.label_2.setText(QCoreApplication.translate("AnnotationHelpDialog", u"\n"
"Symbol-based annotation involves the identification and tagging of words or tokens within a corpus using symbols to highlight elements deemed significant for analysis. Annotations detectable with CorpusCompass can be tailored through the specification of an annotation format, enabling the recognition of each user's unique annotation style. However, there are specific foundational elements that CorpusCompass expects to find within individual annotations. Each annotation needs to refer to and include a word (=\"token\") in the corpus, as well as a Dependent-Variable-Variant (=\"Identifier\"), which can be surrounded by an arbitrary number of other keyboard symbols.", None))
        self.label_colorbased.setText(QCoreApplication.translate("AnnotationHelpDialog", u"Information on color-based annotation", None))
        self.label_3.setText(QCoreApplication.translate("AnnotationHelpDialog", u"Coming soon... (detecting words that are annotation with colors in Microsoft Word-files automatically)", None))
    # retranslateUi

