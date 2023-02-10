import sys
import tkinter as tk
from tkinter import ttk

from qtpy import QtWidgets

from annotation_fixer.LoadFilesPopup import LoadFilesPopup
from annotation_fixer.Memory import Memory

if __name__ == '__main__':

    mem=Memory()

    app = QtWidgets.QApplication(sys.argv)

    # set size of window
    app.setApplicationName("Annotation Fixer")
    app.setApplicationVersion("0.1")
    app.setOrganizationName("University of Sapienza")
    app.setDesktopFileName("Annotation Fixer")
    app.setApplicationDisplayName("Annotation Fixer")

    window = LoadFilesPopup(mem)
    # set window size
    window.resize(800, 600)
    window.show()

    app.exec_()

    a=1




