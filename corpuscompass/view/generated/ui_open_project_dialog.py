# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_project_dialoglmRsfU.ui'
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
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_OpenProjectDialog(object):
    def setupUi(self, OpenProjectDialog):
        if not OpenProjectDialog.objectName():
            OpenProjectDialog.setObjectName("OpenProjectDialog")
        OpenProjectDialog.resize(699, 607)
        self.verticalLayout = QVBoxLayout(OpenProjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_contents = QWidget(OpenProjectDialog)
        self.widget_contents.setObjectName("widget_contents")
        self.gridLayout = QGridLayout(self.widget_contents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_selectedprojectcontent = QLabel(self.widget_contents)
        self.label_selectedprojectcontent.setObjectName("label_selectedprojectcontent")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_selectedprojectcontent.setFont(font)

        self.gridLayout.addWidget(self.label_selectedprojectcontent, 5, 1, 1, 1)

        self.label_header = QLabel(self.widget_contents)
        self.label_header.setObjectName("label_header")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_header.setFont(font1)

        self.gridLayout.addWidget(self.label_header, 0, 0, 1, 1)

        self.label_repodescription = QLabel(self.widget_contents)
        self.label_repodescription.setObjectName("label_repodescription")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(True)
        self.label_repodescription.setFont(font2)

        self.gridLayout.addWidget(self.label_repodescription, 1, 0, 1, 1)

        self.label_selectedproject = QLabel(self.widget_contents)
        self.label_selectedproject.setObjectName("label_selectedproject")
        self.label_selectedproject.setFont(font)

        self.gridLayout.addWidget(self.label_selectedproject, 5, 0, 1, 1)

        self.label_repositorypath = QLabel(self.widget_contents)
        self.label_repositorypath.setObjectName("label_repositorypath")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_repositorypath.setFont(font3)

        self.gridLayout.addWidget(self.label_repositorypath, 1, 1, 1, 1)

        self.listWidget_projectlist = QListWidget(self.widget_contents)
        QListWidgetItem(self.listWidget_projectlist)
        QListWidgetItem(self.listWidget_projectlist)
        self.listWidget_projectlist.setObjectName("listWidget_projectlist")
        self.listWidget_projectlist.setStyleSheet(
            "QListWidget{\n"
            "	font: 16pt;\n"
            "}\n"
            "\n"
            "QListWidget::item {\n"
            "    margin: 10px; /* Adjust margin to increase/decrease the size of items */\n"
            "}\n"
            "\n"
            "QListWidget::item:selected {\n"
            "    /* Style the selected item in the QTreeWidget */\n"
            "}"
        )
        self.listWidget_projectlist.setSpacing(1)

        self.gridLayout.addWidget(self.listWidget_projectlist, 4, 0, 1, 2)

        self.label_selectheader = QLabel(self.widget_contents)
        self.label_selectheader.setObjectName("label_selectheader")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setItalic(True)
        self.label_selectheader.setFont(font4)

        self.gridLayout.addWidget(self.label_selectheader, 3, 0, 1, 2)

        self.btn_changepath = QPushButton(self.widget_contents)
        self.btn_changepath.setObjectName("btn_changepath")

        self.gridLayout.addWidget(self.btn_changepath, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.widget_contents)

        self.buttonBox = QDialogButtonBox(OpenProjectDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Open
        )

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OpenProjectDialog)
        self.buttonBox.accepted.connect(OpenProjectDialog.accept)
        self.buttonBox.rejected.connect(OpenProjectDialog.reject)
        self.listWidget_projectlist.itemClicked.connect(
            self.label_selectedprojectcontent.clear
        )

        QMetaObject.connectSlotsByName(OpenProjectDialog)

    # setupUi

    def retranslateUi(self, OpenProjectDialog):
        OpenProjectDialog.setWindowTitle(
            QCoreApplication.translate("OpenProjectDialog", "Dialog", None)
        )
        self.label_selectedprojectcontent.setText(
            QCoreApplication.translate("OpenProjectDialog", "Project 1", None)
        )
        self.label_header.setText(
            QCoreApplication.translate("OpenProjectDialog", "Open Project", None)
        )
        self.label_repodescription.setText(
            QCoreApplication.translate(
                "OpenProjectDialog", "Current repository-path for saved projects:", None
            )
        )
        self.label_selectedproject.setText(
            QCoreApplication.translate("OpenProjectDialog", "Selected Project:", None)
        )
        self.label_repositorypath.setText(
            QCoreApplication.translate("OpenProjectDialog", "C:...", None)
        )

        __sortingEnabled = self.listWidget_projectlist.isSortingEnabled()
        self.listWidget_projectlist.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_projectlist.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("OpenProjectDialog", "Project 1", None)
        )
        ___qlistwidgetitem1 = self.listWidget_projectlist.item(1)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate("OpenProjectDialog", "Project 2", None)
        )
        self.listWidget_projectlist.setSortingEnabled(__sortingEnabled)

        self.label_selectheader.setText(
            QCoreApplication.translate(
                "OpenProjectDialog", "Select a project to open:", None
            )
        )
        self.btn_changepath.setText(
            QCoreApplication.translate("OpenProjectDialog", "Change path...", None)
        )

    # retranslateUi
