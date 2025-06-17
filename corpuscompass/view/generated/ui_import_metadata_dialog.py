# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_metadata_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ImportMetadataDialog(object):
    def setupUi(self, ImportMetadataDialog):
        if not ImportMetadataDialog.objectName():
            ImportMetadataDialog.setObjectName(u"ImportMetadataDialog")
        ImportMetadataDialog.resize(974, 638)
        self.verticalLayout_5 = QVBoxLayout(ImportMetadataDialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_importcontent = QWidget(ImportMetadataDialog)
        self.widget_importcontent.setObjectName(u"widget_importcontent")
        self.verticalLayout_4 = QVBoxLayout(self.widget_importcontent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_header = QLabel(self.widget_importcontent)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_header.setFont(font)

        self.verticalLayout_4.addWidget(self.label_header)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_subheader = QLabel(self.widget_importcontent)
        self.label_subheader.setObjectName(u"label_subheader")
        self.label_subheader.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_subheader)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.groupBox_ivs = QGroupBox(self.widget_importcontent)
        self.groupBox_ivs.setObjectName(u"groupBox_ivs")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_ivs)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_ivimportcontainer = QWidget(self.groupBox_ivs)
        self.widget_ivimportcontainer.setObjectName(u"widget_ivimportcontainer")
        self.horizontalLayout = QHBoxLayout(self.widget_ivimportcontainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_import_ivfile = QPushButton(self.widget_ivimportcontainer)
        self.btn_import_ivfile.setObjectName(u"btn_import_ivfile")

        self.horizontalLayout.addWidget(self.btn_import_ivfile)

        self.label_seliv = QLabel(self.widget_ivimportcontainer)
        self.label_seliv.setObjectName(u"label_seliv")

        self.horizontalLayout.addWidget(self.label_seliv)

        self.label_help_iv = QLabel(self.widget_ivimportcontainer)
        self.label_help_iv.setObjectName(u"label_help_iv")
        self.label_help_iv.setMaximumSize(QSize(24, 24))
        self.label_help_iv.setPixmap(QPixmap(u":/images/images/Help_Icon.svg"))
        self.label_help_iv.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_help_iv)


        self.horizontalLayout_4.addWidget(self.widget_ivimportcontainer)

        self.widget_ivbtn_container = QWidget(self.groupBox_ivs)
        self.widget_ivbtn_container.setObjectName(u"widget_ivbtn_container")
        self.verticalLayout = QVBoxLayout(self.widget_ivbtn_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radiobtn_extiv = QRadioButton(self.widget_ivbtn_container)
        self.radiobtn_extiv.setObjectName(u"radiobtn_extiv")
        self.radiobtn_extiv.setChecked(True)

        self.verticalLayout.addWidget(self.radiobtn_extiv)

        self.radiobtn_repiv = QRadioButton(self.widget_ivbtn_container)
        self.radiobtn_repiv.setObjectName(u"radiobtn_repiv")

        self.verticalLayout.addWidget(self.radiobtn_repiv)


        self.horizontalLayout_4.addWidget(self.widget_ivbtn_container, 0, Qt.AlignRight)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.groupBox_ivs)

        self.groupBox_dvs = QGroupBox(self.widget_importcontent)
        self.groupBox_dvs.setObjectName(u"groupBox_dvs")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_dvs)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_dvimportcontainer = QWidget(self.groupBox_dvs)
        self.widget_dvimportcontainer.setObjectName(u"widget_dvimportcontainer")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_dvimportcontainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_import_dvfile = QPushButton(self.widget_dvimportcontainer)
        self.btn_import_dvfile.setObjectName(u"btn_import_dvfile")

        self.horizontalLayout_3.addWidget(self.btn_import_dvfile)

        self.label_seldv = QLabel(self.widget_dvimportcontainer)
        self.label_seldv.setObjectName(u"label_seldv")

        self.horizontalLayout_3.addWidget(self.label_seldv)

        self.label_help_dv = QLabel(self.widget_dvimportcontainer)
        self.label_help_dv.setObjectName(u"label_help_dv")
        self.label_help_dv.setMaximumSize(QSize(24, 24))
        self.label_help_dv.setPixmap(QPixmap(u":/images/images/Help_Icon.svg"))
        self.label_help_dv.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_help_dv)


        self.horizontalLayout_5.addWidget(self.widget_dvimportcontainer)

        self.widget_dvbtn_container = QWidget(self.groupBox_dvs)
        self.widget_dvbtn_container.setObjectName(u"widget_dvbtn_container")
        self.verticalLayout_2 = QVBoxLayout(self.widget_dvbtn_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radiobtn_extdv = QRadioButton(self.widget_dvbtn_container)
        self.radiobtn_extdv.setObjectName(u"radiobtn_extdv")
        self.radiobtn_extdv.setChecked(True)

        self.verticalLayout_2.addWidget(self.radiobtn_extdv)

        self.radiobtn_repdv = QRadioButton(self.widget_dvbtn_container)
        self.radiobtn_repdv.setObjectName(u"radiobtn_repdv")

        self.verticalLayout_2.addWidget(self.radiobtn_repdv)


        self.horizontalLayout_5.addWidget(self.widget_dvbtn_container, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.groupBox_dvs)

        self.groupBox_speakers = QGroupBox(self.widget_importcontent)
        self.groupBox_speakers.setObjectName(u"groupBox_speakers")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_speakers)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_spimportcontainer = QWidget(self.groupBox_speakers)
        self.widget_spimportcontainer.setObjectName(u"widget_spimportcontainer")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_spimportcontainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_import_speakerfile = QPushButton(self.widget_spimportcontainer)
        self.btn_import_speakerfile.setObjectName(u"btn_import_speakerfile")

        self.horizontalLayout_2.addWidget(self.btn_import_speakerfile)

        self.label_selspeaker = QLabel(self.widget_spimportcontainer)
        self.label_selspeaker.setObjectName(u"label_selspeaker")

        self.horizontalLayout_2.addWidget(self.label_selspeaker)

        self.label_help_speaker = QLabel(self.widget_spimportcontainer)
        self.label_help_speaker.setObjectName(u"label_help_speaker")
        self.label_help_speaker.setMaximumSize(QSize(24, 24))
        self.label_help_speaker.setPixmap(QPixmap(u":/images/images/Help_Icon.svg"))
        self.label_help_speaker.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_help_speaker)


        self.horizontalLayout_6.addWidget(self.widget_spimportcontainer)

        self.widget_spbtn_container = QWidget(self.groupBox_speakers)
        self.widget_spbtn_container.setObjectName(u"widget_spbtn_container")
        self.verticalLayout_3 = QVBoxLayout(self.widget_spbtn_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radiobtn_extsp = QRadioButton(self.widget_spbtn_container)
        self.radiobtn_extsp.setObjectName(u"radiobtn_extsp")
        self.radiobtn_extsp.setChecked(True)

        self.verticalLayout_3.addWidget(self.radiobtn_extsp)

        self.radiobtn_repsp = QRadioButton(self.widget_spbtn_container)
        self.radiobtn_repsp.setObjectName(u"radiobtn_repsp")

        self.verticalLayout_3.addWidget(self.radiobtn_repsp)


        self.horizontalLayout_6.addWidget(self.widget_spbtn_container, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.groupBox_speakers)

        self.label = QLabel(self.widget_importcontent)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.widget_importcontent, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(ImportMetadataDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.retranslateUi(ImportMetadataDialog)
        self.buttonBox.accepted.connect(ImportMetadataDialog.accept)
        self.buttonBox.rejected.connect(ImportMetadataDialog.reject)

        QMetaObject.connectSlotsByName(ImportMetadataDialog)
    # setupUi

    def retranslateUi(self, ImportMetadataDialog):
        ImportMetadataDialog.setWindowTitle(QCoreApplication.translate("ImportMetadataDialog", u"Dialog", None))
        self.label_header.setText(QCoreApplication.translate("ImportMetadataDialog", u"Import Metadata", None))
        self.label_subheader.setText(QCoreApplication.translate("ImportMetadataDialog", u"You can import IVs, DVs and Speakers with JSON-Files, which can be exported from projects in CorpusCompass! Please add all files that you want to import below. You can also decide for each file if it should replace the current paramaters (if already set), or if it should extend them (meaning that old metadata will remain unchanged while only new elements will be added; duplicate elements will be skipped).", None))
        self.groupBox_ivs.setTitle(QCoreApplication.translate("ImportMetadataDialog", u"Import IVs", None))
        self.btn_import_ivfile.setText(QCoreApplication.translate("ImportMetadataDialog", u"Import IV-File", None))
        self.label_seliv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Selected file: -", None))
#if QT_CONFIG(tooltip)
        self.label_help_iv.setToolTip(QCoreApplication.translate("ImportMetadataDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Expected JSON Structure for IVs:</span></p>\n"
"<pre><code>{\n"
"    \"Variables\": [\n"
"        {\n"
"            \"Name\": \"IV_Name_1\",\n"
"            \"VariableValues\": [\n"
"                VariableValue_1,\n"
"                VariableValue_2\n"
"                ...\n"
"            ]\n"
"        },\n"
"        {\n"
"            \"Name\": \"IV_Name_2\",\n"
"            \"VariableValues\": [\n"
"                VariableValue_1,\n"
"                VariableValue_2\n"
"                ...\n"
"            ]\n"
"        }, \n"
"        ...\n"
"    ]\n"
"}</code></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radiobtn_extiv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Extend current IVs", None))
        self.radiobtn_repiv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Replace current IVs", None))
        self.groupBox_dvs.setTitle(QCoreApplication.translate("ImportMetadataDialog", u"Import DVs", None))
        self.btn_import_dvfile.setText(QCoreApplication.translate("ImportMetadataDialog", u"Import DV-File", None))
        self.label_seldv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Selected file: -", None))
#if QT_CONFIG(tooltip)
        self.label_help_dv.setToolTip(QCoreApplication.translate("ImportMetadataDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Expected JSON Structure for DVs:</span></p>\n"
"<pre><code>{\n"
"    \"Variables\": [\n"
"        {\n"
"            \"Name\": \"DV_Name_1\",\n"
"            \"VariableValues\": [\n"
"                \"Value1\",\n"
"                \"Value2\"\n"
"                ...\n"
"            ]\n"
"        },\n"
"        {\n"
"            \"Name\": \"DV_Name_2\",\n"
"            \"VariableValues\": [\n"
"                \"Value1\",\n"
"                \"Value2\"\n"
"                ...\n"
"            ]\n"
"        }\n"
"    ]\n"
"}</code></pre>\n"
"<p>Note: 'VariableValues' at the root is a flat list of ALL possible DV values, while the nested 'VariableValues' assigns them to specific DVs.</p>\n"
"</body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radiobtn_extdv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Extend current DVs", None))
        self.radiobtn_repdv.setText(QCoreApplication.translate("ImportMetadataDialog", u"Replace current DVs", None))
        self.groupBox_speakers.setTitle(QCoreApplication.translate("ImportMetadataDialog", u"Import Speakers", None))
        self.btn_import_speakerfile.setText(QCoreApplication.translate("ImportMetadataDialog", u"Import Speaker-File", None))
        self.label_selspeaker.setText(QCoreApplication.translate("ImportMetadataDialog", u"Selected file: -", None))
#if QT_CONFIG(tooltip)
        self.label_help_speaker.setToolTip(QCoreApplication.translate("ImportMetadataDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Expected JSON Structure for Speakers:</span></p>\n"
"<pre><code>{\n"
"    \"Speakers\": [\n"
"        {\n"
"            \"Name\": \"SpeakerName1\",\n"
"            \"Color\": \"#00ff00\",\n"
"            \"Variables\": {\n"
"                \"IV_Name_1\": \"Value1\",\n"
"                \"IV_Name_2\": \"Value3\"\n"
"            }\n"
"        }\n"
"    ]\n"
"}</code></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radiobtn_extsp.setText(QCoreApplication.translate("ImportMetadataDialog", u"Extend current speakers", None))
        self.radiobtn_repsp.setText(QCoreApplication.translate("ImportMetadataDialog", u"Replace current speakers", None))
    # retranslateUi

