from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QPushButton, QTextEdit, QComboBox, QLabel

from annotation_fixer.common import Memory


class GeneralWindow(QtWidgets.QWidget):
    def __init__(self, mem: Memory):
        super().__init__()

        self.mem = mem

        # apply the window size setting
        self.resize(*self.mem.settings.get("window_size", (640, 480)))

        # apply the background color setting
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.mem.settings.get("background_color", QtGui.QColor(255, 255, 255)))
        self.setPalette(p)

        # apply the text color setting
        self.setStyleSheet("color: {}".format(self.mem.settings.get("text_color", "black")))

        # apply the text font and size setting
        font = self.mem.settings.get("text_font", "Arial")
        size = self.mem.settings.get("text_size", 12)
        self.setFont(QtGui.QFont(font, size))
        self.create_widgets()
        self.set_colors()

    def set_colors(self):
        styles = {
            "color": "#000000",
            "background-color": "#ffffff",
            "border-style": "solid",
            "border-width": "1px",
            "border-color": "#000000",
        }

        types = [QComboBox, QTextEdit, QPushButton,QLabel]

        for widget_type in types:
            widgets = self.findChildren(widget_type)
            for widget in widgets:
                for prop, value in styles.items():
                    widget.setStyleSheet(f"{prop}: {value};")

    # listen to resize event
    def resizeEvent(self, event):
        super().resizeEvent(event)

        # save the new size
        self.mem.settings["window_size"] = (self.width(), self.height())

    def create_widgets(self):
        raise NotImplemented()
