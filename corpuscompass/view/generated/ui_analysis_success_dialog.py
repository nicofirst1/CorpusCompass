# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_success_dialogeFPGsq.ui'
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
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_AnalysisSuccessDialog(object):
    def setupUi(self, AnalysisSuccessDialog):
        if not AnalysisSuccessDialog.objectName():
            AnalysisSuccessDialog.setObjectName("AnalysisSuccessDialog")
        AnalysisSuccessDialog.resize(643, 243)
        self.verticalLayout_2 = QVBoxLayout(AnalysisSuccessDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_text = QWidget(AnalysisSuccessDialog)
        self.widget_text.setObjectName("widget_text")
        self.verticalLayout = QVBoxLayout(self.widget_text)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QLabel(self.widget_text)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout.addWidget(self.label_header)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_explanation = QLabel(self.widget_text)
        self.label_explanation.setObjectName("label_explanation")
        self.label_explanation.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_explanation)

        self.verticalLayout_2.addWidget(self.widget_text, 0, Qt.AlignTop)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_filepath_description = QLabel(AnalysisSuccessDialog)
        self.label_filepath_description.setObjectName("label_filepath_description")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_filepath_description.sizePolicy().hasHeightForWidth()
        )
        self.label_filepath_description.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.label_filepath_description.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_filepath_description)

        self.label_filepath = QLabel(AnalysisSuccessDialog)
        self.label_filepath.setObjectName("label_filepath")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_filepath.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_filepath)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.widget_btns = QWidget(AnalysisSuccessDialog)
        self.widget_btns.setObjectName("widget_btns")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_btns.sizePolicy().hasHeightForWidth())
        self.widget_btns.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget_btns)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_savelocation = QPushButton(self.widget_btns)
        self.btn_savelocation.setObjectName("btn_savelocation")

        self.horizontalLayout.addWidget(self.btn_savelocation)

        self.btn_save = QPushButton(self.widget_btns)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_save)

        self.verticalLayout_3.addWidget(self.widget_btns)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(AnalysisSuccessDialog)
        self.btn_save.clicked.connect(AnalysisSuccessDialog.accept)

        QMetaObject.connectSlotsByName(AnalysisSuccessDialog)

    # setupUi

    def retranslateUi(self, AnalysisSuccessDialog):
        AnalysisSuccessDialog.setWindowTitle(
            QCoreApplication.translate("AnalysisSuccessDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "AnalysisSuccessDialog", "Analysis: Success!", None
            )
        )
        self.label_explanation.setText(
            QCoreApplication.translate(
                "AnalysisSuccessDialog",
                "CorpusCompass was able to analyse your corpus with all your parameters! CorpusCompass has created output files that contain the data of your analysis. These results are saved as CSV-Files (use Microsoft Excel to open). Please select the specific location where you want to save the files!",
                None,
            )
        )
        self.label_filepath_description.setText(
            QCoreApplication.translate(
                "AnalysisSuccessDialog", "Selected File-Path:", None
            )
        )
        self.label_filepath.setText(
            QCoreApplication.translate("AnalysisSuccessDialog", "C: ...", None)
        )
        self.btn_savelocation.setText(
            QCoreApplication.translate(
                "AnalysisSuccessDialog", "Select save location...", None
            )
        )
        self.btn_save.setText(
            QCoreApplication.translate("AnalysisSuccessDialog", "Save...", None)
        )

    # retranslateUi
