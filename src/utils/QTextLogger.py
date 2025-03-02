import io
import logging

from PySide6 import QtCore, QtWidgets, QtGui


class FakeStream(io.StringIO):
    """
    used to redirect tqdm output to text area
    """

    def __init__(self, signal: QtCore.Signal):
        super().__init__()
        self.signal = signal

    def write(self, string):
        self.signal.emit(string)


class HtmlColorFormatter(logging.Formatter):
    def __init__(self, format):
        super().__init__(format)

    def format(self, record):
        level_colors = {
            logging.DEBUG: "#FFFF00",  # Yellow
            logging.INFO: "#000000",  # Black
            logging.WARNING: "#FFA500",  # Orange
            logging.ERROR: "#FF0000",  # Red
            logging.CRITICAL: "#8B0000",  # Dark Red
        }
        level_name = record.levelname
        level_color = level_colors[record.levelno]
        message = record.getMessage()

        # Add color to level name

        # Add color to message
        message = f'<span style="color: {level_color}">{message}</span><br/>'

        record.msg = message
        return super().format(record)


class QTextLogger(QtCore.QObject):
    signal = QtCore.Signal(str)

    def __init__(self, level=logging.DEBUG):
        super().__init__()

        self.level = level
        self.formatter = HtmlColorFormatter("%(message)s")
        self.text_edit_stream = FakeStream(self.signal)

    def debug(self, msg):
        if self.level > logging.DEBUG:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.DEBUG})
        )
        self.signal.emit(msg)

    def info(self, msg):
        if self.level > logging.INFO:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.INFO})
        )
        self.signal.emit(msg)

    def warning(self, msg):
        if self.level > logging.WARNING:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.WARNING})
        )
        self.signal.emit(msg)

    def error(self, msg):
        if self.level > logging.ERROR:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.ERROR})
        )
        self.signal.emit(msg)

    def critical(self, msg):
        if self.level > logging.CRITICAL:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.CRITICAL})
        )
        self.signal.emit(msg)


class QTextEditLog(QtWidgets.QTextEdit):
    """
    used to write logs to textare, implements rewriter for string starting with '\r'
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_line = ""

        self.setAcceptRichText(True)
        self.setReadOnly(True)

    def connect_signal(self, signal: QtCore.Signal):
        signal.connect(self.write)

    def write(self, string):
        if "\r" in string:
            if self.last_line:
                # If there's a carriage return, move the cursor to the beginning of the line
                self.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
                self.moveCursor(
                    QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.MoveAnchor
                )
            # Replace the last line with the new one (excluding the carriage return)
            self.last_line = string.split("\r")[-1]
            self.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
            self.insertPlainText(self.last_line)

        else:
            if self.last_line:
                # put a new line  with br at the start of the string
                string = f"<br>{string}"

            # substitute the new line with br
            string = string.replace("\n", "<br>")
            # If there's no carriage return, just append the string to the text edit
            self.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.insertHtml(string)
            self.last_line = ""

        self.update()
