# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_settings_confirmation_dialogYhOxhV.ui'
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
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_AnalysisSettingsConfirmationDialog(object):
    def setupUi(self, AnalysisSettingsConfirmationDialog):
        if not AnalysisSettingsConfirmationDialog.objectName():
            AnalysisSettingsConfirmationDialog.setObjectName(
                "AnalysisSettingsConfirmationDialog"
            )
        AnalysisSettingsConfirmationDialog.resize(885, 506)
        self.verticalLayout = QVBoxLayout(AnalysisSettingsConfirmationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_contents = QWidget(AnalysisSettingsConfirmationDialog)
        self.widget_contents.setObjectName("widget_contents")
        self.verticalLayout_2 = QVBoxLayout(self.widget_contents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_header = QLabel(self.widget_contents)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.label_header.setFont(font)
        self.label_header.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_header)

        self.label_speakers = QLabel(self.widget_contents)
        self.label_speakers.setObjectName("label_speakers")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_speakers.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_speakers)

        self.listWidget_speakerlist = QListWidget(self.widget_contents)
        self.listWidget_speakerlist.setObjectName("listWidget_speakerlist")
        self.listWidget_speakerlist.setStyleSheet(
            "QListWidget {\n	font-size: 16px;\n}"
        )

        self.verticalLayout_2.addWidget(self.listWidget_speakerlist)

        self.label_dvs = QLabel(self.widget_contents)
        self.label_dvs.setObjectName("label_dvs")
        self.label_dvs.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_dvs)

        self.listWidget_dvlist = QListWidget(self.widget_contents)
        self.listWidget_dvlist.setObjectName("listWidget_dvlist")
        self.listWidget_dvlist.setStyleSheet("QListWidget {\n	font-size: 16px;\n}")

        self.verticalLayout_2.addWidget(self.listWidget_dvlist)

        self.verticalLayout.addWidget(self.widget_contents)

        self.widget_btns = QWidget(AnalysisSettingsConfirmationDialog)
        self.widget_btns.setObjectName("widget_btns")
        self.horizontalLayout = QHBoxLayout(self.widget_btns)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QPushButton(self.widget_btns)
        self.btn_cancel.setObjectName("btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_includeall = QPushButton(self.widget_btns)
        self.btn_includeall.setObjectName("btn_includeall")

        self.horizontalLayout.addWidget(self.btn_includeall)

        self.btn_savesettings = QPushButton(self.widget_btns)
        self.btn_savesettings.setObjectName("btn_savesettings")

        self.horizontalLayout.addWidget(self.btn_savesettings)

        self.verticalLayout.addWidget(self.widget_btns)

        self.retranslateUi(AnalysisSettingsConfirmationDialog)
        self.btn_cancel.clicked.connect(AnalysisSettingsConfirmationDialog.reject)
        self.btn_savesettings.clicked.connect(AnalysisSettingsConfirmationDialog.accept)

        QMetaObject.connectSlotsByName(AnalysisSettingsConfirmationDialog)

    # setupUi

    def retranslateUi(self, AnalysisSettingsConfirmationDialog):
        AnalysisSettingsConfirmationDialog.setWindowTitle(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Dialog", None
            )
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog",
                "Attention: Only the following speakers and variables will be considered for the analysis!",
                None,
            )
        )
        self.label_speakers.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Speakers:", None
            )
        )
        self.label_dvs.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Dependent Variables:", None
            )
        )
        self.btn_cancel.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Cancel", None
            )
        )
        self.btn_includeall.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Discard changes...", None
            )
        )
        self.btn_savesettings.setText(
            QCoreApplication.translate(
                "AnalysisSettingsConfirmationDialog", "Save settings...", None
            )
        )

    # retranslateUi
