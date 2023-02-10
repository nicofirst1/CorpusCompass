from tkinter import filedialog

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QWidget


# class for scrollable label
class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, content, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)