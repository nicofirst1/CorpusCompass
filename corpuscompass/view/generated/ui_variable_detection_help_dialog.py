# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variable_detection_help_dialogjnVJBy.ui'
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
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_VariableDetectionHelpDialog(object):
    def setupUi(self, VariableDetectionHelpDialog):
        if not VariableDetectionHelpDialog.objectName():
            VariableDetectionHelpDialog.setObjectName("VariableDetectionHelpDialog")
        VariableDetectionHelpDialog.resize(733, 375)
        self.verticalLayout = QVBoxLayout(VariableDetectionHelpDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(VariableDetectionHelpDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_header = QLabel(self.widget)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_2.addWidget(self.label_header, 0, Qt.AlignTop)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignTop)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font1)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.label_4 = QLabel(VariableDetectionHelpDialog)
        self.label_4.setObjectName("label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.buttonBox_2 = QDialogButtonBox(VariableDetectionHelpDialog)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.buttonBox_2.setOrientation(Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.verticalLayout.addWidget(self.buttonBox_2)

        self.retranslateUi(VariableDetectionHelpDialog)
        self.buttonBox_2.accepted.connect(VariableDetectionHelpDialog.accept)
        self.buttonBox_2.rejected.connect(VariableDetectionHelpDialog.reject)

        QMetaObject.connectSlotsByName(VariableDetectionHelpDialog)

    # setupUi

    def retranslateUi(self, VariableDetectionHelpDialog):
        VariableDetectionHelpDialog.setWindowTitle(
            QCoreApplication.translate("VariableDetectionHelpDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "VariableDetectionHelpDialog",
                "Extraction of Dependent Variable-Variants from annotations",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "VariableDetectionHelpDialog",
                "For already annotated corpora, CorpusCompass can detect all annotations in your corpus based on your previously specified annotation-format(s). This is done by detecting all annotations in the corpus that match the specified pattern(s) and then storing all identifiers from each annotation as Dependent-Variable-Variants. ",
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "VariableDetectionHelpDialog",
                "By clicking the button below, you can extract all all variants from all detected annotations. It is recommended to press this button after all annotation formats are correctly specified. This action is mandatory for already annotated corpora, as the analysis cannot be enabled otherwise. However, you can still opt to only analyse a subset of all DVs in the analysis-settings-menu later!",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "VariableDetectionHelpDialog",
                "After extracting all detected DV-Variants from the corpus, you can create Dependent Variables and add the Variants to each DV with the menu on the left. By also selecting a color for the detected variants, you can control in which color they will be highlighted in the corpus, which allows for easier identification.",
                None,
            )
        )
        self.label_4.setText("")

    # retranslateUi
