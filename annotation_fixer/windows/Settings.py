from PySide6 import QtWidgets, QtCore, QtGui

from annotation_fixer.common import Memory, GeneralWindow


class Settings(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)
        self.mem = mem

        self.setWindowTitle("Settings")


    def create_widgets(self):

        form_layout = QtWidgets.QFormLayout()
        form_layout.setAlignment(QtCore.Qt.AlignCenter)

        for name, setting in self.mem.settings.items():
            label = QtWidgets.QLabel(name.capitalize() + ":")
            label.setAlignment(QtCore.Qt.AlignRight)
            label.setStyleSheet("color: white;")
            form_layout.addRow(label, self.create_input(name, setting))

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addLayout(form_layout)

        self.ok = QtWidgets.QPushButton("Save")
        self.ok.setStyleSheet("background-color: #388e3c; color: white; padding: 10px 20px;")
        self.ok.clicked.connect(self.accept_settings)
        layout.addWidget(self.ok)

        self.setLayout(layout)

    def create_input(self, name, setting):
        metadata = self.mem.settings_metadata[name]
        description, choices = metadata

        if isinstance(setting, str):
            setting = setting.lower()

        if len(choices) > 0:
            widget = QtWidgets.QComboBox()
            widget.setObjectName(name)
            widget.addItems([str(x) for x in choices])
            widget.setStyleSheet("background-color: white; color: black;")
            widget.setCurrentIndex(choices.index(setting))

            # Find the width of the largest item text
            width = 0
            font = widget.font()
            for item in choices:
                fm = QtGui.QFontMetrics(font)
                width = max(width, fm.horizontalAdvance(str(item)))

            # Set the minimum width of the QComboBox
            widget.setMinimumWidth(width + 30)
        else:
            widget = QtWidgets.QLineEdit()
            widget.setObjectName(name)
            widget.setPlaceholderText("Enter an integer")
            widget.setText(str(setting))
            widget.setStyleSheet("background-color: white;")

        timer = QtCore.QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: widget.setToolTip(description))
        widget.enterEvent = lambda _: timer.start(2)
        widget.leaveEvent = lambda _: timer.stop()

        return widget

    def accept_settings(self):
        for name, setting in self.mem.settings.items():

            # get choices
            metadata = self.mem.settings_metadata[name]
            description, choices = metadata

            if len(choices) > 0:
                val = self.findChild(QtWidgets.QComboBox, name).currentText()
            else:
                val = self.findChild(QtWidgets.QLineEdit, name).text()

            # cast to type
            old_val = self.mem.settings[name]
            t = type(old_val)

            if isinstance(old_val, tuple) or isinstance(old_val, list):
                val = eval(val)
            else:
                val = t(val)

            self.mem.settings[name] = val

        self.close()
