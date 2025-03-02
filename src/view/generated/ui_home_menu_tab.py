# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_menu_tabZzdRWN.ui'
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
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_HomeMenuTab(object):
    def setupUi(self, HomeMenuTab):
        if not HomeMenuTab.objectName():
            HomeMenuTab.setObjectName("HomeMenuTab")
        HomeMenuTab.resize(1280, 720)
        HomeMenuTab.setStyleSheet(
            "QWidget{\n"
            "	background-color: white;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color:rgb(154, 217, 234) ;\n"
            "	color: white;\n"
            "    min-width: 80px;\n"
            "	min-height: 40px;\n"
            "	border-style: solid;\n"
            "	border-color: rgb(154, 217, 234);\n"
            "	border-width: 5px;\n"
            "	border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background-color:rgb(134, 189, 203) ;\n"
            "	border-color: rgb(134, 189, 203);\n"
            "	color: rgb(245, 245, 245);\n"
            "}"
        )
        self.gridLayout_2 = QGridLayout(HomeMenuTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_analysebuttoncontainer = QWidget(HomeMenuTab)
        self.widget_analysebuttoncontainer.setObjectName(
            "widget_analysebuttoncontainer"
        )
        self.verticalLayout_3 = QVBoxLayout(self.widget_analysebuttoncontainer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_missingforanalysis = QLabel(self.widget_analysebuttoncontainer)
        self.label_missingforanalysis.setObjectName("label_missingforanalysis")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_missingforanalysis.setFont(font)
        self.label_missingforanalysis.setStyleSheet("QLabel{color: red;}")
        self.label_missingforanalysis.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_missingforanalysis)

        self.btn_home_analysecorpus = QPushButton(self.widget_analysebuttoncontainer)
        self.btn_home_analysecorpus.setObjectName("btn_home_analysecorpus")
        self.btn_home_analysecorpus.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_home_analysecorpus.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_analysecorpus.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.btn_home_analysecorpus.setFont(font1)
        self.btn_home_analysecorpus.setStyleSheet(
            "QPushButton {\n"
            "	color: white;\n"
            "	background-color: rgb(0, 170, 0);\n"
            "    min-width: 250px;\n"
            "	min-height: 80px;\n"
            "	border-style: solid;\n"
            "	border-color: rgb(0, 125, 0);\n"
            "	border-width: 2px;\n"
            "	border-radius: 10px;\n"
            "   margin-top: 10px; \n"
            "   margin-bottom: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background-color: rgb(0, 134, 0);\n"
            "}\n"
            "\n"
            "QPushButton:disabled{\n"
            "  background-color: rgb(121, 121, 121);\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.btn_home_analysecorpus, 0, Qt.AlignHCenter)

        self.gridLayout_2.addWidget(
            self.widget_analysebuttoncontainer, 2, 1, 1, 1, Qt.AlignBottom
        )

        self.verticalWidget_contents = QWidget(HomeMenuTab)
        self.verticalWidget_contents.setObjectName("verticalWidget_contents")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_contents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QWidget(self.verticalWidget_contents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.proj_name_label = QLabel(self.widget)
        self.proj_name_label.setObjectName("proj_name_label")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.proj_name_label.sizePolicy().hasHeightForWidth()
        )
        self.proj_name_label.setSizePolicy(sizePolicy1)
        self.proj_name_label.setFont(font1)
        self.proj_name_label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.proj_name_label)

        self.btn_projectinformation = QPushButton(self.widget)
        self.btn_projectinformation.setObjectName("btn_projectinformation")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.btn_projectinformation.setFont(font2)
        self.btn_projectinformation.setStyleSheet(
            "QPushButton {\n"
            "    background-color: white;\n"
            "    border: 1px solid white;\n"
            "	color: grey;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: white;\n"
            "    color: dark grey; \n"
            "	text-decoration: underline;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: white;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    border: 1px solid white;\n"
            "}\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "    image: none;\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(":/images/images/Help_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_projectinformation.setIcon(icon)
        self.btn_projectinformation.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_projectinformation, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignTop)

        self.gridLayout_2.addWidget(self.verticalWidget_contents, 0, 1, 1, 1)

        self.verticalWidget_buttons = QWidget(HomeMenuTab)
        self.verticalWidget_buttons.setObjectName("verticalWidget_buttons")
        self.verticalWidget_buttons.setMinimumSize(QSize(600, 0))
        self.verticalWidget_buttons.setStyleSheet(
            "QPushButton {\n"
            "	color: black;\n"
            "    min-width: 150px;\n"
            "	min-height: 100px;\n"
            "	border-style: solid;\n"
            "	border-color: black;\n"
            "	border-width: 2px;\n"
            "	border-radius: 10px;\n"
            "   margin-top: 10px; \n"
            "   margin-bottom: 10px;\n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.verticalWidget_buttons)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_buttons = QScrollArea(self.verticalWidget_buttons)
        self.scrollArea_buttons.setObjectName("scrollArea_buttons")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.scrollArea_buttons.sizePolicy().hasHeightForWidth()
        )
        self.scrollArea_buttons.setSizePolicy(sizePolicy2)
        self.scrollArea_buttons.setStyleSheet(
            "QScrollBar:vertical {\n"
            "            border: 0px solid #999999;\n"
            "            background:white;\n"
            "            width:10px;    \n"
            "            margin: 0px 0px 0px 0px;\n"
            "        }\n"
            "        QScrollBar::handle:vertical {         \n"
            "       \n"
            "            min-height: 0px;\n"
            "          	border: 0px solid red;\n"
            "			border-radius: 4px;\n"
            "			background-color: rgb(226, 226, 226);\n"
            "        }\n"
            "        QScrollBar::add-line:vertical {       \n"
            "            height: 0px;\n"
            "            subcontrol-position: bottom;\n"
            "            subcontrol-origin: margin;\n"
            "        }\n"
            "        QScrollBar::sub-line:vertical {\n"
            "            height: 0 px;\n"
            "            subcontrol-position: top;\n"
            "            subcontrol-origin: margin;\n"
            "        }"
        )
        self.scrollArea_buttons.setFrameShape(QFrame.NoFrame)
        self.scrollArea_buttons.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 600, 892))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_home_homeimage = QLabel(self.scrollAreaWidgetContents_3)
        self.label_home_homeimage.setObjectName("label_home_homeimage")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_home_homeimage.sizePolicy().hasHeightForWidth()
        )
        self.label_home_homeimage.setSizePolicy(sizePolicy3)
        self.label_home_homeimage.setPixmap(QPixmap(":/images/images/Home_Icon.svg"))

        self.horizontalLayout_2.addWidget(self.label_home_homeimage)

        self.label_home_maintitle = QLabel(self.scrollAreaWidgetContents_3)
        self.label_home_maintitle.setObjectName("label_home_maintitle")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.label_home_maintitle.sizePolicy().hasHeightForWidth()
        )
        self.label_home_maintitle.setSizePolicy(sizePolicy4)
        self.label_home_maintitle.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_home_maintitle)

        self.widget_settingsandclose_container = QWidget(
            self.scrollAreaWidgetContents_3
        )
        self.widget_settingsandclose_container.setObjectName(
            "widget_settingsandclose_container"
        )
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.widget_settingsandclose_container.sizePolicy().hasHeightForWidth()
        )
        self.widget_settingsandclose_container.setSizePolicy(sizePolicy5)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_settingsandclose_container)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_closeproject = QPushButton(self.widget_settingsandclose_container)
        self.btn_closeproject.setObjectName("btn_closeproject")
        self.btn_closeproject.setFont(font)
        self.btn_closeproject.setStyleSheet(
            "QPushButton {\n"
            "	background-color: rgb(255, 92, 92);\n"
            "    border: 2px solid black;\n"
            "	color: black;\n"
            "	min-height: 50px;\n"
            "	max-height:50px;\n"
            "	min-width: 120px;\n"
            "	max-width: 120px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(255, 50, 50);\n"
            "    color: dark grey; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background-color: rgb(255, 120, 120);\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "    image: none;\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(":/images/images/exit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closeproject.setIcon(icon1)
        self.btn_closeproject.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_closeproject)

        self.btn_settings = QPushButton(self.widget_settingsandclose_container)
        self.btn_settings.setObjectName("btn_settings")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.btn_settings.sizePolicy().hasHeightForWidth()
        )
        self.btn_settings.setSizePolicy(sizePolicy6)
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet(
            "QPushButton {\n"
            "	background-color: white;\n"
            "    border: 2px solid black;\n"
            "	color: black;\n"
            "	min-height: 50px;\n"
            "	max-height:50px;\n"
            "	min-width: 120px;\n"
            "	max-width: 120px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(200, 200, 200);\n"
            "    color: dark grey; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(220, 220, 220);\n"
            "}\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "    image: none;\n"
            "}\n"
            ""
        )
        icon2 = QIcon()
        icon2.addFile(
            ":/images/images/settings_symbol.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_settings)

        self.horizontalLayout_2.addWidget(
            self.widget_settingsandclose_container, 0, Qt.AlignRight
        )

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.btn_home_managecorpus_sect = QPushButton(self.scrollAreaWidgetContents_3)
        self.btn_home_managecorpus_sect.setObjectName("btn_home_managecorpus_sect")
        self.btn_home_managecorpus_sect.setEnabled(True)
        sizePolicy7 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(
            self.btn_home_managecorpus_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_managecorpus_sect.setSizePolicy(sizePolicy7)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.btn_home_managecorpus_sect.setFont(font3)
        self.btn_home_managecorpus_sect.setStyleSheet(
            "QPushButton:disabled{\n  background-color: rgb(121, 121, 121);\n}"
        )

        self.verticalLayout_5.addWidget(self.btn_home_managecorpus_sect, 0, Qt.AlignTop)

        self.btn_home_speaker_sect = QPushButton(self.scrollAreaWidgetContents_3)
        self.btn_home_speaker_sect.setObjectName("btn_home_speaker_sect")
        self.btn_home_speaker_sect.setEnabled(True)
        sizePolicy7.setHeightForWidth(
            self.btn_home_speaker_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_speaker_sect.setSizePolicy(sizePolicy7)
        self.btn_home_speaker_sect.setFont(font3)
        self.btn_home_speaker_sect.setStyleSheet(
            "QPushButton:disabled{\n  background-color: rgb(121, 121, 121);\n}"
        )

        self.verticalLayout_5.addWidget(self.btn_home_speaker_sect, 0, Qt.AlignTop)

        self.btn_home_annotformat_sect = QPushButton(self.scrollAreaWidgetContents_3)
        self.btn_home_annotformat_sect.setObjectName("btn_home_annotformat_sect")
        sizePolicy7.setHeightForWidth(
            self.btn_home_annotformat_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_annotformat_sect.setSizePolicy(sizePolicy7)
        self.btn_home_annotformat_sect.setFont(font3)
        self.btn_home_annotformat_sect.setStyleSheet(
            "QPushButton:disabled{\n  background-color: rgb(121, 121, 121);\n}"
        )

        self.verticalLayout_5.addWidget(self.btn_home_annotformat_sect, 0, Qt.AlignTop)

        self.btn_home_varmanag_sect = QPushButton(self.scrollAreaWidgetContents_3)
        self.btn_home_varmanag_sect.setObjectName("btn_home_varmanag_sect")
        sizePolicy7.setHeightForWidth(
            self.btn_home_varmanag_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_varmanag_sect.setSizePolicy(sizePolicy7)
        self.btn_home_varmanag_sect.setFont(font3)
        self.btn_home_varmanag_sect.setStyleSheet(
            "QPushButton:disabled{\n  background-color: rgb(121, 121, 121);\n}"
        )

        self.verticalLayout_5.addWidget(self.btn_home_varmanag_sect, 0, Qt.AlignTop)

        self.btn_home_analysissettings_sect = QPushButton(
            self.scrollAreaWidgetContents_3
        )
        self.btn_home_analysissettings_sect.setObjectName(
            "btn_home_analysissettings_sect"
        )
        sizePolicy7.setHeightForWidth(
            self.btn_home_analysissettings_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_analysissettings_sect.setSizePolicy(sizePolicy7)
        self.btn_home_analysissettings_sect.setFont(font3)
        self.btn_home_analysissettings_sect.setStyleSheet(
            "QPushButton:disabled{\n  background-color: rgb(121, 121, 121);\n}"
        )

        self.verticalLayout_5.addWidget(
            self.btn_home_analysissettings_sect, 0, Qt.AlignTop
        )

        self.btn_home_annotation_sect = QPushButton(self.scrollAreaWidgetContents_3)
        self.btn_home_annotation_sect.setObjectName("btn_home_annotation_sect")
        self.btn_home_annotation_sect.setEnabled(False)
        sizePolicy7.setHeightForWidth(
            self.btn_home_annotation_sect.sizePolicy().hasHeightForWidth()
        )
        self.btn_home_annotation_sect.setSizePolicy(sizePolicy7)
        self.btn_home_annotation_sect.setFont(font3)
        self.btn_home_annotation_sect.setStyleSheet(
            "QPushButton {\n"
            "    background-color:rgb(255, 170, 0) ;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background-color: rgb(229, 153, 0) ;\n"
            "}\n"
            "\n"
            "QPushButton:disabled{\n"
            "  background-color: rgb(121, 121, 121);\n"
            "}"
        )

        self.verticalLayout_5.addWidget(self.btn_home_annotation_sect, 0, Qt.AlignTop)

        self.scrollArea_buttons.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_buttons)

        self.gridLayout_2.addWidget(self.verticalWidget_buttons, 0, 0, 3, 1)

        self.gridWidget = QWidget(HomeMenuTab)
        self.gridWidget.setObjectName("gridWidget")
        sizePolicy8 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy8)
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.label_warning_loaded_files = QLabel(self.gridWidget)
        self.label_warning_loaded_files.setObjectName("label_warning_loaded_files")
        self.label_warning_loaded_files.setMaximumSize(QSize(24, 24))
        self.label_warning_loaded_files.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_loaded_files.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_loaded_files, 0, 0, 1, 1)

        self.label_loadedfiles = QLabel(self.gridWidget)
        self.label_loadedfiles.setObjectName("label_loadedfiles")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_loadedfiles.setFont(font4)

        self.gridLayout.addWidget(self.label_loadedfiles, 0, 1, 1, 1)

        self.label_loadedfiles_content = QLabel(self.gridWidget)
        self.label_loadedfiles_content.setObjectName("label_loadedfiles_content")
        self.label_loadedfiles_content.setFont(font4)

        self.gridLayout.addWidget(
            self.label_loadedfiles_content, 0, 2, 1, 1, Qt.AlignRight
        )

        self.label_warning_speakers = QLabel(self.gridWidget)
        self.label_warning_speakers.setObjectName("label_warning_speakers")
        self.label_warning_speakers.setMaximumSize(QSize(24, 24))
        self.label_warning_speakers.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_speakers.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_speakers, 1, 0, 1, 1)

        self.label_uniquespeakers = QLabel(self.gridWidget)
        self.label_uniquespeakers.setObjectName("label_uniquespeakers")
        self.label_uniquespeakers.setFont(font4)

        self.gridLayout.addWidget(self.label_uniquespeakers, 1, 1, 1, 1)

        self.label_uniquespeakers_content = QLabel(self.gridWidget)
        self.label_uniquespeakers_content.setObjectName("label_uniquespeakers_content")
        self.label_uniquespeakers_content.setFont(font4)

        self.gridLayout.addWidget(
            self.label_uniquespeakers_content, 1, 2, 1, 1, Qt.AlignRight
        )

        self.label_warning_dvs = QLabel(self.gridWidget)
        self.label_warning_dvs.setObjectName("label_warning_dvs")
        self.label_warning_dvs.setMaximumSize(QSize(24, 24))
        self.label_warning_dvs.setPixmap(QPixmap(":/images/images/warning_symbol.png"))
        self.label_warning_dvs.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_dvs, 2, 0, 1, 1)

        self.label_dvs = QLabel(self.gridWidget)
        self.label_dvs.setObjectName("label_dvs")
        self.label_dvs.setFont(font4)

        self.gridLayout.addWidget(self.label_dvs, 2, 1, 1, 1)

        self.label_dvs_content = QLabel(self.gridWidget)
        self.label_dvs_content.setObjectName("label_dvs_content")
        self.label_dvs_content.setFont(font4)

        self.gridLayout.addWidget(self.label_dvs_content, 2, 2, 1, 1, Qt.AlignRight)

        self.label_warning_dv_variants = QLabel(self.gridWidget)
        self.label_warning_dv_variants.setObjectName("label_warning_dv_variants")
        self.label_warning_dv_variants.setMaximumSize(QSize(24, 24))
        self.label_warning_dv_variants.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_dv_variants.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_dv_variants, 3, 0, 1, 1)

        self.label_dv_variants = QLabel(self.gridWidget)
        self.label_dv_variants.setObjectName("label_dv_variants")
        self.label_dv_variants.setFont(font4)

        self.gridLayout.addWidget(self.label_dv_variants, 3, 1, 1, 1)

        self.label_dv_variants_content = QLabel(self.gridWidget)
        self.label_dv_variants_content.setObjectName("label_dv_variants_content")
        self.label_dv_variants_content.setFont(font4)

        self.gridLayout.addWidget(
            self.label_dv_variants_content, 3, 2, 1, 1, Qt.AlignRight
        )

        self.label_warning_ivs = QLabel(self.gridWidget)
        self.label_warning_ivs.setObjectName("label_warning_ivs")
        self.label_warning_ivs.setMaximumSize(QSize(24, 24))
        self.label_warning_ivs.setPixmap(QPixmap(":/images/images/warning_symbol.png"))
        self.label_warning_ivs.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_ivs, 4, 0, 1, 1)

        self.label_ivs = QLabel(self.gridWidget)
        self.label_ivs.setObjectName("label_ivs")
        self.label_ivs.setFont(font4)

        self.gridLayout.addWidget(self.label_ivs, 4, 1, 1, 1)

        self.label_ivs_contents = QLabel(self.gridWidget)
        self.label_ivs_contents.setObjectName("label_ivs_contents")
        self.label_ivs_contents.setFont(font4)

        self.gridLayout.addWidget(self.label_ivs_contents, 4, 2, 1, 1, Qt.AlignRight)

        self.label_warning_iv_values = QLabel(self.gridWidget)
        self.label_warning_iv_values.setObjectName("label_warning_iv_values")
        self.label_warning_iv_values.setMaximumSize(QSize(24, 24))
        self.label_warning_iv_values.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_iv_values.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_iv_values, 5, 0, 1, 1)

        self.label_iv_values = QLabel(self.gridWidget)
        self.label_iv_values.setObjectName("label_iv_values")
        self.label_iv_values.setFont(font4)

        self.gridLayout.addWidget(self.label_iv_values, 5, 1, 1, 1)

        self.label_iv_values_content = QLabel(self.gridWidget)
        self.label_iv_values_content.setObjectName("label_iv_values_content")
        self.label_iv_values_content.setFont(font4)

        self.gridLayout.addWidget(
            self.label_iv_values_content, 5, 2, 1, 1, Qt.AlignRight
        )

        self.label_warning_annotations = QLabel(self.gridWidget)
        self.label_warning_annotations.setObjectName("label_warning_annotations")
        self.label_warning_annotations.setMaximumSize(QSize(24, 24))
        self.label_warning_annotations.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_annotations.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_annotations, 6, 0, 1, 1)

        self.label_annotations = QLabel(self.gridWidget)
        self.label_annotations.setObjectName("label_annotations")
        self.label_annotations.setFont(font4)

        self.gridLayout.addWidget(self.label_annotations, 6, 1, 1, 1)

        self.label_annotations_content = QLabel(self.gridWidget)
        self.label_annotations_content.setObjectName("label_annotations_content")
        self.label_annotations_content.setFont(font4)

        self.gridLayout.addWidget(
            self.label_annotations_content, 6, 2, 1, 1, Qt.AlignRight
        )

        self.label_warning_annotationformats = QLabel(self.gridWidget)
        self.label_warning_annotationformats.setObjectName(
            "label_warning_annotationformats"
        )
        self.label_warning_annotationformats.setMaximumSize(QSize(24, 24))
        self.label_warning_annotationformats.setPixmap(
            QPixmap(":/images/images/warning_symbol.png")
        )
        self.label_warning_annotationformats.setScaledContents(True)

        self.gridLayout.addWidget(self.label_warning_annotationformats, 7, 0, 1, 1)

        self.label_annotationformat = QLabel(self.gridWidget)
        self.label_annotationformat.setObjectName("label_annotationformat")
        self.label_annotationformat.setFont(font4)

        self.gridLayout.addWidget(self.label_annotationformat, 7, 1, 1, 1)

        self.label_annotationformat_contents = QLabel(self.gridWidget)
        self.label_annotationformat_contents.setObjectName(
            "label_annotationformat_contents"
        )
        self.label_annotationformat_contents.setFont(font4)

        self.gridLayout.addWidget(
            self.label_annotationformat_contents, 7, 2, 1, 1, Qt.AlignRight
        )

        self.gridLayout_2.addWidget(self.gridWidget, 1, 1, 1, 1, Qt.AlignTop)

        self.retranslateUi(HomeMenuTab)

        QMetaObject.connectSlotsByName(HomeMenuTab)

    # setupUi

    def retranslateUi(self, HomeMenuTab):
        self.label_missingforanalysis.setText("")
        self.btn_home_analysecorpus.setText(
            QCoreApplication.translate("HomeMenuTab", "Analyse Corpus", None)
        )
        self.proj_name_label.setText(
            QCoreApplication.translate(
                "HomeMenuTab", "Current Project: <Project Name>", None
            )
        )
        self.btn_projectinformation.setText(
            QCoreApplication.translate("HomeMenuTab", "Project Information", None)
        )
        self.label_home_maintitle.setText(
            QCoreApplication.translate("HomeMenuTab", "Menu Selection", None)
        )
        self.btn_closeproject.setText(
            QCoreApplication.translate("HomeMenuTab", "Close Project", None)
        )
        self.btn_settings.setText(
            QCoreApplication.translate("HomeMenuTab", "Settings", None)
        )
        self.btn_home_managecorpus_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Corpus-File-Management", None)
        )
        self.btn_home_speaker_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Speaker-Identification", None)
        )
        self.btn_home_annotformat_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Annotation-Specification", None)
        )
        self.btn_home_varmanag_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Metadata-Management", None)
        )
        self.btn_home_analysissettings_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Analysis-Settings", None)
        )
        self.btn_home_annotation_sect.setText(
            QCoreApplication.translate("HomeMenuTab", "Annotate Corpus", None)
        )
        self.label_warning_loaded_files.setText("")
        self.label_loadedfiles.setText(
            QCoreApplication.translate("HomeMenuTab", "Loaded files in corpus:", None)
        )
        self.label_loadedfiles_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_speakers.setText("")
        self.label_uniquespeakers.setText(
            QCoreApplication.translate("HomeMenuTab", "Unique speakers:", None)
        )
        self.label_uniquespeakers_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_dvs.setText("")
        self.label_dvs.setText(
            QCoreApplication.translate("HomeMenuTab", "Dependent Variables:", None)
        )
        self.label_dvs_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_dv_variants.setText("")
        self.label_dv_variants.setText(
            QCoreApplication.translate("HomeMenuTab", "Unique DV-Variants:", None)
        )
        self.label_dv_variants_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_ivs.setText("")
        self.label_ivs.setText(
            QCoreApplication.translate("HomeMenuTab", "Independent Variables:", None)
        )
        self.label_ivs_contents.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_iv_values.setText("")
        self.label_iv_values.setText(
            QCoreApplication.translate("HomeMenuTab", "Unique IV-Variants:", None)
        )
        self.label_iv_values_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_annotations.setText("")
        self.label_annotations.setText(
            QCoreApplication.translate("HomeMenuTab", "Annotations:", None)
        )
        self.label_annotations_content.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        self.label_warning_annotationformats.setText("")
        self.label_annotationformat.setText(
            QCoreApplication.translate(
                "HomeMenuTab", "Current Annotation Formats:", None
            )
        )
        self.label_annotationformat_contents.setText(
            QCoreApplication.translate("HomeMenuTab", "0", None)
        )
        pass

    # retranslateUi
