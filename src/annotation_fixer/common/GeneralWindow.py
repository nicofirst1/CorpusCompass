from typing import Optional

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QPushButton, QTextEdit, QComboBox, QLabel, QLineEdit, QScrollArea, QMessageBox
from annotation_fixer.common import Memory

STYLES = [
    {
        "color": "#ffffff",
        "background-color": "#000000",
        "border-style": "dotted",
        "border-width": "2px",
        "border-color": "#ffffff",

    },
    {
        "color": "#000000",
        "background-color": "#ffffff",
        "border-style": "solid",
        "border-width": "1px",
        "border-color": "#000000",
    },

    {
        "color": "#0000ff",
        "background-color": "#ffff00",
        "border-style": "dashed",
        "border-width": "3px",
        "border-color": "#00ff00",

    },

    {
        "color": "#00ff00",
        "background-color": "#ff00ff",
        "border-style": "double",
        "border-width": "4px",
        "border-color": "#0000ff",

    },
    {
        "color": "#8b0000",
        "background-color": "#ffff00",
        "border-style": "dotted",
        "border-width": "2px",
        "border-color": "#8b0000",

    },

    {
        "color": "#006400",
        "background-color": "#add8e6",
        "border-style": "dashed",
        "border-width": "3px",
        "border-color": "#006400",

    },

    {
        "color": "#4b0082",
        "background-color": "#ffd700",
        "border-style": "double",
        "border-width": "4px",
        "border-color": "#4b0082",

    },

    {
        "color": "#ffd700",
        "background-color": "#4b0082",
        "border-style": "groove",
        "border-width": "5px",
        "border-color": "#ffd700",

    },

    {
        "color": "#add8e6",
        "background-color": "#006400",
        "border-style": "ridge",
        "border-width": "6px",
        "border-color": "#add8e6",

    },
]


class GeneralWindow(QtWidgets.QWidget):
    def __init__(self, mem: Memory, title: Optional[str] = ""):
        super().__init__()

        self.mem = mem

        # apply the window size setting
        self.resize(*self.mem.settings.get("window_size", (640, 480)))

        # set the window title
        self.setWindowTitle(title)

        # apply the background color setting
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.mem.settings.get("background_color", QtGui.QColor(255, 255, 255)))
        self.setPalette(p)

        # apply the text font and size setting

        self.create_widgets()

        self.set_style()

    def set_style(self):

        font = self.mem.settings.get("text_font", "Arial")
        size = self.mem.settings.get("text_size", 12)
        self.setFont(QtGui.QFont(font, size))

        style = self.mem.settings.get("style", "s1")
        style = int(style[1])
        chosen_style = STYLES[style]

        types = [QScrollArea, QMessageBox, QComboBox, QTextEdit, QPushButton, QLabel, QLineEdit]
        sheet = [f"{prop}: {value}" for prop, value in chosen_style.items()]
        sheet = ";".join(sheet)

        for widget_type in types:
            widgets = self.findChildren(widget_type)
            # get the class name
            class_name = widget_type.__name__
            for widget in widgets:
                # s = f"{class_name}{widget.styleSheet()};{sheet}"
                s = class_name + " { " + widget.styleSheet() + ";" + sheet + " }"

                if isinstance(widget, QPushButton):
                    s += "QPushButton:disabled { background-color: lightgray; color: darkgray; }"

                widget.setStyleSheet(s)

        # set selected style for self
        # sheet += ";QPushButton:disabled { background-color: lightgray; color: darkgray; }"

        self.setStyleSheet(self.styleSheet() + ";" + sheet)

        self.repaint()

    # listen to resize event
    def resizeEvent(self, event):
        super().resizeEvent(event)

        # save the new size
        self.mem.settings["window_size"] = (self.width(), self.height())

    def create_widgets(self):
        raise NotImplemented()
