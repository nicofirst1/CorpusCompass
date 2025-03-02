# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_metadata_dialogtEANvg.ui'
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
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ImportMetadataDialog(object):
    def setupUi(self, ImportMetadataDialog):
        if not ImportMetadataDialog.objectName():
            ImportMetadataDialog.setObjectName("ImportMetadataDialog")
        ImportMetadataDialog.resize(974, 638)
        self.verticalLayout_5 = QVBoxLayout(ImportMetadataDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_importcontent = QWidget(ImportMetadataDialog)
        self.widget_importcontent.setObjectName("widget_importcontent")
        self.verticalLayout_4 = QVBoxLayout(self.widget_importcontent)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_header = QLabel(self.widget_importcontent)
        self.label_header.setObjectName("label_header")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_4.addWidget(self.label_header)

        self.verticalSpacer = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_subheader = QLabel(self.widget_importcontent)
        self.label_subheader.setObjectName("label_subheader")
        self.label_subheader.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_subheader)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.groupBox_ivs = QGroupBox(self.widget_importcontent)
        self.groupBox_ivs.setObjectName("groupBox_ivs")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_ivs)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_ivimportcontainer = QWidget(self.groupBox_ivs)
        self.widget_ivimportcontainer.setObjectName("widget_ivimportcontainer")
        self.horizontalLayout = QHBoxLayout(self.widget_ivimportcontainer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_import_ivfile = QPushButton(self.widget_ivimportcontainer)
        self.btn_import_ivfile.setObjectName("btn_import_ivfile")

        self.horizontalLayout.addWidget(self.btn_import_ivfile)

        self.label_seliv = QLabel(self.widget_ivimportcontainer)
        self.label_seliv.setObjectName("label_seliv")

        self.horizontalLayout.addWidget(self.label_seliv)

        self.horizontalLayout_4.addWidget(self.widget_ivimportcontainer)

        self.widget_ivbtn_container = QWidget(self.groupBox_ivs)
        self.widget_ivbtn_container.setObjectName("widget_ivbtn_container")
        self.verticalLayout = QVBoxLayout(self.widget_ivbtn_container)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radiobtn_extiv = QRadioButton(self.widget_ivbtn_container)
        self.radiobtn_extiv.setObjectName("radiobtn_extiv")
        self.radiobtn_extiv.setChecked(True)

        self.verticalLayout.addWidget(self.radiobtn_extiv)

        self.radiobtn_repiv = QRadioButton(self.widget_ivbtn_container)
        self.radiobtn_repiv.setObjectName("radiobtn_repiv")

        self.verticalLayout.addWidget(self.radiobtn_repiv)

        self.horizontalLayout_4.addWidget(self.widget_ivbtn_container, 0, Qt.AlignRight)

        self.horizontalSpacer_2 = QSpacerItem(
            25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addWidget(self.groupBox_ivs)

        self.groupBox_dvs = QGroupBox(self.widget_importcontent)
        self.groupBox_dvs.setObjectName("groupBox_dvs")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_dvs)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_dvimportcontainer = QWidget(self.groupBox_dvs)
        self.widget_dvimportcontainer.setObjectName("widget_dvimportcontainer")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_dvimportcontainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_import_dvfile = QPushButton(self.widget_dvimportcontainer)
        self.btn_import_dvfile.setObjectName("btn_import_dvfile")

        self.horizontalLayout_3.addWidget(self.btn_import_dvfile)

        self.label_seldv = QLabel(self.widget_dvimportcontainer)
        self.label_seldv.setObjectName("label_seldv")

        self.horizontalLayout_3.addWidget(self.label_seldv)

        self.horizontalLayout_5.addWidget(self.widget_dvimportcontainer)

        self.widget_dvbtn_container = QWidget(self.groupBox_dvs)
        self.widget_dvbtn_container.setObjectName("widget_dvbtn_container")
        self.verticalLayout_2 = QVBoxLayout(self.widget_dvbtn_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radiobtn_extdv = QRadioButton(self.widget_dvbtn_container)
        self.radiobtn_extdv.setObjectName("radiobtn_extdv")
        self.radiobtn_extdv.setChecked(True)

        self.verticalLayout_2.addWidget(self.radiobtn_extdv)

        self.radiobtn_repdv = QRadioButton(self.widget_dvbtn_container)
        self.radiobtn_repdv.setObjectName("radiobtn_repdv")

        self.verticalLayout_2.addWidget(self.radiobtn_repdv)

        self.horizontalLayout_5.addWidget(self.widget_dvbtn_container, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(
            20, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_4.addWidget(self.groupBox_dvs)

        self.groupBox_speakers = QGroupBox(self.widget_importcontent)
        self.groupBox_speakers.setObjectName("groupBox_speakers")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_speakers)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_spimportcontainer = QWidget(self.groupBox_speakers)
        self.widget_spimportcontainer.setObjectName("widget_spimportcontainer")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_spimportcontainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_import_speakerfile = QPushButton(self.widget_spimportcontainer)
        self.btn_import_speakerfile.setObjectName("btn_import_speakerfile")

        self.horizontalLayout_2.addWidget(self.btn_import_speakerfile)

        self.label_selspeaker = QLabel(self.widget_spimportcontainer)
        self.label_selspeaker.setObjectName("label_selspeaker")

        self.horizontalLayout_2.addWidget(self.label_selspeaker)

        self.horizontalLayout_6.addWidget(self.widget_spimportcontainer)

        self.widget_spbtn_container = QWidget(self.groupBox_speakers)
        self.widget_spbtn_container.setObjectName("widget_spbtn_container")
        self.verticalLayout_3 = QVBoxLayout(self.widget_spbtn_container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radiobtn_extsp = QRadioButton(self.widget_spbtn_container)
        self.radiobtn_extsp.setObjectName("radiobtn_extsp")
        self.radiobtn_extsp.setChecked(True)

        self.verticalLayout_3.addWidget(self.radiobtn_extsp)

        self.radiobtn_repsp = QRadioButton(self.widget_spbtn_container)
        self.radiobtn_repsp.setObjectName("radiobtn_repsp")

        self.verticalLayout_3.addWidget(self.radiobtn_repsp)

        self.horizontalLayout_6.addWidget(self.widget_spbtn_container, 0, Qt.AlignRight)

        self.verticalLayout_4.addWidget(self.groupBox_speakers)

        self.label = QLabel(self.widget_importcontent)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_5.addWidget(self.widget_importcontent, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(ImportMetadataDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(ImportMetadataDialog)
        self.buttonBox.accepted.connect(ImportMetadataDialog.accept)
        self.buttonBox.rejected.connect(ImportMetadataDialog.reject)

        QMetaObject.connectSlotsByName(ImportMetadataDialog)

    # setupUi

    def retranslateUi(self, ImportMetadataDialog):
        ImportMetadataDialog.setWindowTitle(
            QCoreApplication.translate("ImportMetadataDialog", "Dialog", None)
        )
        self.label_header.setText(
            QCoreApplication.translate("ImportMetadataDialog", "Import Metadata", None)
        )
        self.label_subheader.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog",
                "You can import IVs, DVs and Speakers with JSON-Files, which can be exported from projects in CorpusCompass! Please add all files that you want to import below. You can also decide for each file if it should replace the current paramaters (if already set), or if it should extend them (meaning that old metadata will remain unchanged while only new elements will be added; duplicate elements will be skipped).",
                None,
            )
        )
        self.groupBox_ivs.setTitle(
            QCoreApplication.translate("ImportMetadataDialog", "Import IVs", None)
        )
        self.btn_import_ivfile.setText(
            QCoreApplication.translate("ImportMetadataDialog", "Import IV-File", None)
        )
        self.label_seliv.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Selected file: Test_IVs.json", None
            )
        )
        self.radiobtn_extiv.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Extend current IVs", None
            )
        )
        self.radiobtn_repiv.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Replace current IVs", None
            )
        )
        self.groupBox_dvs.setTitle(
            QCoreApplication.translate("ImportMetadataDialog", "Import DVs", None)
        )
        self.btn_import_dvfile.setText(
            QCoreApplication.translate("ImportMetadataDialog", "Import DV-File", None)
        )
        self.label_seldv.setText(
            QCoreApplication.translate("ImportMetadataDialog", "Selected file: -", None)
        )
        self.radiobtn_extdv.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Extend current DVs", None
            )
        )
        self.radiobtn_repdv.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Replace current DVs", None
            )
        )
        self.groupBox_speakers.setTitle(
            QCoreApplication.translate("ImportMetadataDialog", "Import Speakers", None)
        )
        self.btn_import_speakerfile.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Import Speaker-File", None
            )
        )
        self.label_selspeaker.setText(
            QCoreApplication.translate("ImportMetadataDialog", "Selected file: -", None)
        )
        self.radiobtn_extsp.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Extend current speakers", None
            )
        )
        self.radiobtn_repsp.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog", "Replace current speakers", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "ImportMetadataDialog",
                "TODO: \n"
                "1.Check if imported files are correct (e.g. no duplicate DV Variants, ...)\n"
                " 2. Think about what to do with importing DVs (and Speakers) as they are automatically detected from the corpus as of right now --> Maybe deactivate import-feature for now completely this only gets important when annotation is possible to do in the software\n"
                "3. Generic warning dialog for replacing metadata that previous settings are lost and maybe exporting old data before is smart if needed",
                None,
            )
        )

    # retranslateUi
