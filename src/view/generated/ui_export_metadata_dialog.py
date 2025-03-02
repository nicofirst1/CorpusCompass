# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_metadata_dialogjfSBvI.ui'
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
    QCheckBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_ExportMetadataDialog(object):
    def setupUi(self, ExportMetadataDialog):
        if not ExportMetadataDialog.objectName():
            ExportMetadataDialog.setObjectName("ExportMetadataDialog")
        ExportMetadataDialog.resize(974, 259)
        self.verticalLayout_3 = QVBoxLayout(ExportMetadataDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_exportcontent = QWidget(ExportMetadataDialog)
        self.widget_exportcontent.setObjectName("widget_exportcontent")
        self.verticalLayout = QVBoxLayout(self.widget_exportcontent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QLabel(self.widget_exportcontent)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout.addWidget(self.label_header)

        self.label_subheader = QLabel(self.widget_exportcontent)
        self.label_subheader.setObjectName("label_subheader")
        self.label_subheader.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_subheader)

        self.label = QLabel(self.widget_exportcontent)
        self.label.setObjectName("label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.widget_checkboxcontainer = QWidget(self.widget_exportcontent)
        self.widget_checkboxcontainer.setObjectName("widget_checkboxcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.widget_checkboxcontainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_iv = QCheckBox(self.widget_checkboxcontainer)
        self.checkBox_iv.setObjectName("checkBox_iv")
        self.checkBox_iv.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_iv)

        self.checkBox_dv = QCheckBox(self.widget_checkboxcontainer)
        self.checkBox_dv.setObjectName("checkBox_dv")
        self.checkBox_dv.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_dv)

        self.checkBox_speakers = QCheckBox(self.widget_checkboxcontainer)
        self.checkBox_speakers.setObjectName("checkBox_speakers")
        self.checkBox_speakers.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_speakers)

        self.verticalLayout.addWidget(self.widget_checkboxcontainer)

        self.verticalLayout_3.addWidget(self.widget_exportcontent, 0, Qt.AlignTop)

        self.widget = QWidget(ExportMetadataDialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_export = QPushButton(self.widget)
        self.btn_export.setObjectName("btn_export")

        self.horizontalLayout.addWidget(self.btn_export)

        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName("btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignBottom)

        self.retranslateUi(ExportMetadataDialog)
        self.btn_export.clicked.connect(ExportMetadataDialog.accept)
        self.btn_cancel.clicked.connect(ExportMetadataDialog.reject)

        QMetaObject.connectSlotsByName(ExportMetadataDialog)

    # setupUi

    def retranslateUi(self, ExportMetadataDialog):
        ExportMetadataDialog.setWindowTitle(
            QCoreApplication.translate("ExportMetadataDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate("ExportMetadataDialog", "Export Metadata", None)
        )
        self.label_subheader.setText(
            QCoreApplication.translate(
                "ExportMetadataDialog",
                "TODO: Export as JSON files, select location, use standardized name maybe so that its easier to import complete folders without needing to check what is what",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "ExportMetadataDialog", "Select Metadata to export", None
            )
        )
        self.checkBox_iv.setText(
            QCoreApplication.translate("ExportMetadataDialog", "IVs", None)
        )
        self.checkBox_dv.setText(
            QCoreApplication.translate("ExportMetadataDialog", "DVs", None)
        )
        self.checkBox_speakers.setText(
            QCoreApplication.translate("ExportMetadataDialog", "Speakers", None)
        )
        self.btn_export.setText(
            QCoreApplication.translate("ExportMetadataDialog", "Export", None)
        )
        self.btn_cancel.setText(
            QCoreApplication.translate("ExportMetadataDialog", "Cancel", None)
        )

    # retranslateUi
