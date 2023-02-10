from PySide6 import QtWidgets, QtCore

from annotation_fixer.GeneralWindow import GeneralWindow
from annotation_fixer.Memory import Memory


class AskLoading(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)

        self.separator = self.mem.lfp.get("separator") or ";"
        self.mem.lfp["separator"] = self.separator
        self.load = False

        self.create_widgets()

    def create_widgets(self):
        self.setStyleSheet("background-color: #212121;")
        self.message = QtWidgets.QLabel("Found loaded files from previous session. Do you want to use them?")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setStyleSheet("color: white;")

        self.yes = QtWidgets.QPushButton("Yes")
        self.yes.setStyleSheet("background-color: #388e3c; color: white; padding: 10px 20px;")
        self.yes.clicked.connect(self.use_loaded)

        self.no = QtWidgets.QPushButton("No")
        self.no.setStyleSheet("background-color: #d32f2f; color: white; padding: 10px 20px;")
        self.no.clicked.connect(self.load_files)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.message)
        layout.addWidget(self.yes)
        layout.addWidget(self.no)

        self.setLayout(layout)

    def use_loaded(self):
        self.load = True
        self.close()

    def load_files(self):
        self.load = False
        self.close()
