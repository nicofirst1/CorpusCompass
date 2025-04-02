# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metadata_deletion_warning_dialogIMneWK.ui'
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
    QGridLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MetadataDeletionWarningDialog(object):
    def setupUi(self, MetadataDeletionWarningDialog):
        if not MetadataDeletionWarningDialog.objectName():
            MetadataDeletionWarningDialog.setObjectName("MetadataDeletionWarningDialog")
        MetadataDeletionWarningDialog.resize(554, 290)
        self.gridLayout_2 = QGridLayout(MetadataDeletionWarningDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_headercontents = QWidget(MetadataDeletionWarningDialog)
        self.widget_headercontents.setObjectName("widget_headercontents")
        self.verticalLayout_2 = QVBoxLayout(self.widget_headercontents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_header = QLabel(self.widget_headercontents)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_2.addWidget(self.label_header)

        self.label_subheader = QLabel(self.widget_headercontents)
        self.label_subheader.setObjectName("label_subheader")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_subheader.setFont(font1)
        self.label_subheader.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_subheader)

        self.gridLayout_2.addWidget(self.widget_headercontents, 5, 0, 1, 2, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(MetadataDeletionWarningDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 2)

        self.gridLayout_changescontents = QGridLayout()
        self.gridLayout_changescontents.setObjectName("gridLayout_changescontents")
        self.gridLayout_changescontents.setVerticalSpacing(1)
        self.label_effect_header = QLabel(MetadataDeletionWarningDialog)
        self.label_effect_header.setObjectName("label_effect_header")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_effect_header.sizePolicy().hasHeightForWidth()
        )
        self.label_effect_header.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(True)
        self.label_effect_header.setFont(font2)

        self.gridLayout_changescontents.addWidget(
            self.label_effect_header, 0, 0, 1, 1, Qt.AlignHCenter
        )

        self.label_nbrheader = QLabel(MetadataDeletionWarningDialog)
        self.label_nbrheader.setObjectName("label_nbrheader")
        sizePolicy.setHeightForWidth(
            self.label_nbrheader.sizePolicy().hasHeightForWidth()
        )
        self.label_nbrheader.setSizePolicy(sizePolicy)
        self.label_nbrheader.setFont(font2)
        self.label_nbrheader.setStyleSheet("QLabel{color: rgb(149, 148, 148);}")

        self.gridLayout_changescontents.addWidget(
            self.label_nbrheader, 0, 1, 1, 1, Qt.AlignHCenter
        )

        self.label_effect = QLabel(MetadataDeletionWarningDialog)
        self.label_effect.setObjectName("label_effect")
        sizePolicy.setHeightForWidth(self.label_effect.sizePolicy().hasHeightForWidth())
        self.label_effect.setSizePolicy(sizePolicy)

        self.gridLayout_changescontents.addWidget(
            self.label_effect, 1, 0, 1, 1, Qt.AlignHCenter
        )

        self.label_nbraffectedcases = QLabel(MetadataDeletionWarningDialog)
        self.label_nbraffectedcases.setObjectName("label_nbraffectedcases")
        sizePolicy.setHeightForWidth(
            self.label_nbraffectedcases.sizePolicy().hasHeightForWidth()
        )
        self.label_nbraffectedcases.setSizePolicy(sizePolicy)
        self.label_nbraffectedcases.setStyleSheet("QLabel{color: rgb(149, 148, 148);}")

        self.gridLayout_changescontents.addWidget(
            self.label_nbraffectedcases, 1, 1, 1, 1, Qt.AlignHCenter
        )

        self.gridLayout_2.addLayout(self.gridLayout_changescontents, 6, 0, 1, 2)

        self.label_proceed = QLabel(MetadataDeletionWarningDialog)
        self.label_proceed.setObjectName("label_proceed")
        sizePolicy.setHeightForWidth(
            self.label_proceed.sizePolicy().hasHeightForWidth()
        )
        self.label_proceed.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(10)
        self.label_proceed.setFont(font3)

        self.gridLayout_2.addWidget(self.label_proceed, 7, 1, 1, 1, Qt.AlignRight)

        self.retranslateUi(MetadataDeletionWarningDialog)
        self.buttonBox.rejected.connect(MetadataDeletionWarningDialog.reject)
        self.buttonBox.accepted.connect(MetadataDeletionWarningDialog.accept)

        QMetaObject.connectSlotsByName(MetadataDeletionWarningDialog)

    # setupUi

    def retranslateUi(self, MetadataDeletionWarningDialog):
        MetadataDeletionWarningDialog.setWindowTitle(
            QCoreApplication.translate("MetadataDeletionWarningDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "MetadataDeletionWarningDialog", "Warning!", None
            )
        )
        self.label_subheader.setText(
            QCoreApplication.translate(
                "MetadataDeletionWarningDialog",
                "Deleting the selected elements from your metadata could result in inconsistencies in your corpus and analysis. The change cannot be reverted! See below for more information on the impact of deleting the selected elements.",
                None,
            )
        )
        self.label_effect_header.setText(
            QCoreApplication.translate("MetadataDeletionWarningDialog", "Effect", None)
        )
        self.label_nbrheader.setText(
            QCoreApplication.translate(
                "MetadataDeletionWarningDialog", "Affected cases", None
            )
        )
        self.label_effect.setText(
            QCoreApplication.translate("MetadataDeletionWarningDialog", "-", None)
        )
        self.label_nbraffectedcases.setText(
            QCoreApplication.translate(
                "MetadataDeletionWarningDialog", "Will be implemented soon...", None
            )
        )
        self.label_proceed.setText(
            QCoreApplication.translate(
                "MetadataDeletionWarningDialog", "Do you still wish to proceed?", None
            )
        )

    # retranslateUi
