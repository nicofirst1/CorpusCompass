from PySide6 import QtWidgets, QtCore

from annotation_fixer.common import Memory, GeneralWindow


class AskSettings(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)
        self.minimum_repetitions = self.mem.settings.get("minimum_repetitions") or 1
        self.annotation_regex = self.mem.settings.get("annotation_regex") or ""

        self.create_widgets()

    def create_widgets(self):
        self.setStyleSheet("background-color: #212121;")
        self.minimum_repetitions_label = QtWidgets.QLabel("Minimum Repetitions:")
        self.minimum_repetitions_label.setAlignment(QtCore.Qt.AlignRight)
        self.minimum_repetitions_label.setStyleSheet("color: white;")

        self.minimum_repetitions_input = QtWidgets.QLineEdit()
        self.minimum_repetitions_input.setPlaceholderText("Enter an integer")
        self.minimum_repetitions_input.setText(str(self.minimum_repetitions))
        self.minimum_repetitions_input.setStyleSheet("background-color: white;")


        self.name_regex_label = QtWidgets.QLabel("Name Regex:")
        self.name_regex_label.setAlignment(QtCore.Qt.AlignRight)
        self.name_regex_label.setStyleSheet("color: white;")


        self.name_regex_input = QtWidgets.QLineEdit()
        self.name_regex_input.setPlaceholderText("Enter a string, or leave empty for default")
        self.name_regex_input.setText(self.annotation_regex)
        self.name_regex_input.setStyleSheet("background-color: white;")


        self.ok = QtWidgets.QPushButton("OK")
        self.ok.setStyleSheet("background-color: #388e3c; color: white; padding: 10px 20px;")
        self.ok.clicked.connect(self.accept_settings)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.minimum_repetitions_label, self.minimum_repetitions_input)
        form_layout.addRow(self.name_regex_label, self.name_regex_input)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addLayout(form_layout)
        layout.addWidget(self.ok)

        self.setLayout(layout)

    def accept_settings(self):
        try:
            self.minimum_repetitions = int(self.minimum_repetitions_input.text())
        except ValueError:
            self.minimum_repetitions_input.setStyleSheet("background-color: #d32f2f;")
            self.minimum_repetitions_input.setPlaceholderText("Invalid input, enter an integer")
            return

        self.annotation_regex = self.name_regex_input.text()
        if not self.annotation_regex:
            self.name_regex_input.setStyleSheet("background-color: #d32f2f;")
            self.name_regex_input.setPlaceholderText("Invalid input, enter a string")
            return

        # Save settings
        self.mem.settings["minimum_repetitions"] = self.minimum_repetitions
        self.mem.settings["annotation_regex"] = self.annotation_regex

        self.close()
