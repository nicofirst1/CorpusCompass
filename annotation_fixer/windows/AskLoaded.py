from PySide6 import QtWidgets, QtCore

from annotation_fixer.common import Memory, GeneralWindow



class AskLoading(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)

        self.separator = self.mem.lfp.get("separator") or ";"
        self.mem.lfp["separator"] = self.separator
        self.load = False


    def create_widgets(self):
        self.message = QtWidgets.QLabel("Found loaded files from previous session. Do you want to use them?")
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.yes = QtWidgets.QPushButton("Yes")
        self.yes.clicked.connect(self.use_loaded)

        self.no = QtWidgets.QPushButton("No")
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
