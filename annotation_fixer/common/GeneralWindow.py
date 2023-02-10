from PySide6 import QtWidgets

from annotation_fixer.common import Memory


class GeneralWindow(QtWidgets.QWidget):
    def __init__(self, mem: Memory):
        super().__init__()

        self.mem = mem
        self.resize(*self.mem.settings.get("window_size"))

    # listen to resize event
    def resizeEvent(self, event):
        super().resizeEvent(event)

        # save the new size
        self.mem.settings["window_size"] = (self.width(), self.height())
