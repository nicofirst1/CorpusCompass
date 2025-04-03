
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer

class LazySignalTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._signals_connected = False
        self._controller_callback = None  # Set externally

    def set_controller_callback(self, controller_callback):
        self._controller_callback = controller_callback

    def showEvent(self, event):
        super().showEvent(event)
        if not self._signals_connected and self._controller_callback:
            QTimer.singleShot(0, self._connect_signals_safe)

    def _connect_signals_safe(self):
        if self._controller_callback:
            self.connect_signals(self._controller_callback())
            self._signals_connected = True

    def connect_signals(self, controller: "Controller"):
        raise NotImplementedError("Subclasses must implement connect_signals.")
