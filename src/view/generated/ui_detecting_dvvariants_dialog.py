# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detecting_dvvariants_dialogOgpQkE.ui'
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
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QDialog,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_DetectVariantsDialog(object):
    def setupUi(self, DetectVariantsDialog):
        if not DetectVariantsDialog.objectName():
            DetectVariantsDialog.setObjectName("DetectVariantsDialog")
        DetectVariantsDialog.resize(902, 631)
        self.verticalLayout_2 = QVBoxLayout(DetectVariantsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_explanations = QWidget(DetectVariantsDialog)
        self.widget_explanations.setObjectName("widget_explanations")
        self.verticalLayout = QVBoxLayout(self.widget_explanations)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_header = QLabel(self.widget_explanations)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout.addWidget(self.label_header)

        self.label_detectionsummary = QLabel(self.widget_explanations)
        self.label_detectionsummary.setObjectName("label_detectionsummary")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_detectionsummary.setFont(font1)
        self.label_detectionsummary.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_detectionsummary)

        self.label_detectedvariants = QLabel(self.widget_explanations)
        self.label_detectedvariants.setObjectName("label_detectedvariants")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_detectedvariants.sizePolicy().hasHeightForWidth()
        )
        self.label_detectedvariants.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        self.label_detectedvariants.setFont(font2)
        self.label_detectedvariants.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_detectedvariants)

        self.tableWidget_variants = QTableWidget(self.widget_explanations)
        if self.tableWidget_variants.columnCount() < 2:
            self.tableWidget_variants.setColumnCount(2)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3)
        self.tableWidget_variants.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4)
        self.tableWidget_variants.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_variants.setObjectName("tableWidget_variants")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.tableWidget_variants.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget_variants.setSizePolicy(sizePolicy1)
        self.tableWidget_variants.setMinimumSize(QSize(0, 300))
        self.tableWidget_variants.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_variants.setStyleSheet(
            "QTableWidget {\n    font-size: 10pt; /* Set the font size */\n}\n\n"
        )
        self.tableWidget_variants.setFrameShape(QFrame.Box)
        self.tableWidget_variants.setFrameShadow(QFrame.Plain)
        self.tableWidget_variants.setLineWidth(2)
        self.tableWidget_variants.setMidLineWidth(2)
        self.tableWidget_variants.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_variants.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_variants.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_variants.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_variants.setDragEnabled(True)
        self.tableWidget_variants.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_variants.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_variants.setShowGrid(True)
        self.tableWidget_variants.setSortingEnabled(False)
        self.tableWidget_variants.setWordWrap(True)
        self.tableWidget_variants.setCornerButtonEnabled(False)
        self.tableWidget_variants.setRowCount(0)
        self.tableWidget_variants.horizontalHeader().setVisible(True)
        self.tableWidget_variants.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_variants.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_variants.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_variants.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_variants.verticalHeader().setVisible(False)
        self.tableWidget_variants.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout.addWidget(self.tableWidget_variants)

        self.verticalLayout_2.addWidget(self.widget_explanations, 0, Qt.AlignTop)

        self.widget_recommendation = QWidget(DetectVariantsDialog)
        self.widget_recommendation.setObjectName("widget_recommendation")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.widget_recommendation.sizePolicy().hasHeightForWidth()
        )
        self.widget_recommendation.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.widget_recommendation)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_recommendation = QLabel(self.widget_recommendation)
        self.label_recommendation.setObjectName("label_recommendation")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_recommendation.setFont(font5)
        self.label_recommendation.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_recommendation, 0, Qt.AlignBottom)

        self.verticalLayout_2.addWidget(self.widget_recommendation)

        self.widget_btncontainer = QWidget(DetectVariantsDialog)
        self.widget_btncontainer.setObjectName("widget_btncontainer")
        sizePolicy2.setHeightForWidth(
            self.widget_btncontainer.sizePolicy().hasHeightForWidth()
        )
        self.widget_btncontainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_btncontainer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_extractlater = QPushButton(self.widget_btncontainer)
        self.btn_extractlater.setObjectName("btn_extractlater")
        self.btn_extractlater.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_extractlater)

        self.btn_extractnow = QPushButton(self.widget_btncontainer)
        self.btn_extractnow.setObjectName("btn_extractnow")

        self.horizontalLayout.addWidget(self.btn_extractnow)

        self.verticalLayout_2.addWidget(self.widget_btncontainer)

        self.retranslateUi(DetectVariantsDialog)
        self.btn_extractlater.clicked.connect(DetectVariantsDialog.reject)
        self.btn_extractnow.clicked.connect(DetectVariantsDialog.accept)

        QMetaObject.connectSlotsByName(DetectVariantsDialog)

    # setupUi

    def retranslateUi(self, DetectVariantsDialog):
        DetectVariantsDialog.setWindowTitle(
            QCoreApplication.translate("DetectVariantsDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog",
                "Automatically detect Dependent Variable Variants",
                None,
            )
        )
        self.label_detectionsummary.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog",
                "With the specified annotation format(s), CorpusCompass was able to detect 54 annotations and 12 Dependent Variable - Variants for these annotations",
                None,
            )
        )
        self.label_detectedvariants.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog", "Detected Variants:", None
            )
        )
        ___qtablewidgetitem = self.tableWidget_variants.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("DetectVariantsDialog", "Detected Variant", None)
        )
        ___qtablewidgetitem1 = self.tableWidget_variants.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("DetectVariantsDialog", "Occurences", None)
        )
        self.label_recommendation.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog",
                "If you wish to directly add all found DV-Variants to your database already, press the button on the bottom right. If you still want to make changes to your corpus or change the annotation format again, you can also choose to do the extraction of DV-Variants later. However, keep in mind that the detection of DV-Variants is required for the analysis to work!",
                None,
            )
        )
        self.btn_extractlater.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog", "Extract Later... (For now, always store)", None
            )
        )
        self.btn_extractnow.setText(
            QCoreApplication.translate(
                "DetectVariantsDialog", "Store detected DV-Variants...", None
            )
        )

    # retranslateUi
