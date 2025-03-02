# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_screen_tabtuCfPT.ui'
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
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_StartScreenTab(object):
    def setupUi(self, StartScreenTab):
        if not StartScreenTab.objectName():
            StartScreenTab.setObjectName("StartScreenTab")
        StartScreenTab.resize(1280, 720)
        StartScreenTab.setStyleSheet(
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
            "}\n"
            "\n"
            "QPushButton:flat {\n"
            "    border: none; /* no border for a flat push button */\n"
            "}\n"
            "\n"
            "QPushButton:default {\n"
            "    border-color: navy; /* make the default button prominent */\n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(StartScreenTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 4)
        self.help = QLabel(StartScreenTab)
        self.help.setObjectName("help")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setPixmap(QPixmap(":/images/images/Help_Icon.svg"))

        self.verticalLayout.addWidget(self.help, 0, Qt.AlignRight | Qt.AlignTop)

        self.logo = QLabel(StartScreenTab)
        self.logo.setObjectName("logo")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(600, 228))
        self.logo.setMaximumSize(QSize(800, 304))
        self.logo.setPixmap(QPixmap(":/images/images/cc_logo_write.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout.addWidget(self.logo, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.widget_buttons = QWidget(StartScreenTab)
        self.widget_buttons.setObjectName("widget_buttons")
        self.horizontalLayout = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 6)
        self.create_new_project = QPushButton(self.widget_buttons)
        self.create_new_project.setObjectName("create_new_project")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.create_new_project.setFont(font)
        self.create_new_project.setStyleSheet("QPushButton {\n	min-height: 80px;\n}")
        icon = QIcon()
        icon.addFile(":/images/images/Plus_Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_new_project.setIcon(icon)
        self.create_new_project.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.create_new_project)

        self.open_project = QPushButton(self.widget_buttons)
        self.open_project.setObjectName("open_project")
        self.open_project.setFont(font)
        self.open_project.setStyleSheet("QPushButton {\n	min-height: 80px;\n}")
        icon1 = QIcon()
        icon1.addFile(
            ":/images/images/open_icon_white.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.open_project.setIcon(icon1)
        self.open_project.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.open_project)

        self.import_project = QPushButton(self.widget_buttons)
        self.import_project.setObjectName("import_project")
        self.import_project.setFont(font)
        self.import_project.setStyleSheet("QPushButton {\n	min-height: 80px;\n}")
        icon2 = QIcon()
        icon2.addFile(
            ":/images/images/import_icon_white.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.import_project.setIcon(icon2)
        self.import_project.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.import_project)

        self.verticalLayout.addWidget(self.widget_buttons)

        self.retranslateUi(StartScreenTab)

        QMetaObject.connectSlotsByName(StartScreenTab)

    # setupUi

    def retranslateUi(self, StartScreenTab):
        # if QT_CONFIG(tooltip)
        self.help.setToolTip(
            QCoreApplication.translate(
                "StartScreenTab",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:700;">Create Project:</span></p><p>Create a new project by giving it a name and description. For each project, you can load in a set of (text) files that represent your corpus, as well as specify distinct parameters and metadata that help achieving your research goal.</p><p><span style=" font-size:10pt; font-weight:700;">Open Project:</span></p><p>Choose and open a previously created and modified project.</p><p><span style=" font-size:10pt; font-weight:700;">Import Project:</span></p><p>Import a previously created project into the workspace of the tool. You can then choose to open and modify the project with the &quot;<span style=" font-style:italic;">Open Project</span>&quot;-button</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.create_new_project.setText(
            QCoreApplication.translate("StartScreenTab", " Create new project", None)
        )
        self.open_project.setText(
            QCoreApplication.translate("StartScreenTab", "Open Project", None)
        )
        self.import_project.setText(
            QCoreApplication.translate("StartScreenTab", "Import project", None)
        )
        pass

    # retranslateUi
