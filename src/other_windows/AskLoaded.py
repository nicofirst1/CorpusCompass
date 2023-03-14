from PySide6 import QtWidgets, QtCore

from src.common.GeneralWindow import GeneralWindow
from src.common.Memory import Memory


class AskLoading(GeneralWindow):
    finished = QtCore.Signal()

    def __init__(self, mem: Memory):
        super().__init__(mem, "Use loaded files?")

        self.separator = self.mem.lfp.get("separator") or ";"
        self.mem.lfp["separator"] = self.separator
        self.load = False

    def create_widgets(self):
        self.message = QtWidgets.QLabel()
        self.load_message()

        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.yes = QtWidgets.QPushButton("Yes")
        self.yes.clicked.connect(self.conclude)

        self.no = QtWidgets.QPushButton("No")
        self.no.clicked.connect(self.conclude)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.message)
        layout.addWidget(self.yes)
        layout.addWidget(self.no)

        self.setLayout(layout)

    def load_message(self):
        msg = "Found loaded files from previous session. Do you want to use them?"

        self.message.setText(msg)

    def conclude(self):
        # get sender
        sender = self.sender()
        if sender == self.yes:
            self.load = False
        elif sender == self.no:
            self.load = True

        self.finished.emit()
        self.close()
