import io
import logging
import sys

from PySide6 import QtGui, QtWidgets, QtCore


class QTextEditStream(io.StringIO):
    def __init__(self, text_edit: QtWidgets.QTextEdit):
        super().__init__()
        self.text_edit = text_edit
        self.last_line = ''

    def write(self, string):
        if "\r" in string:
            if self.last_line:
                # If there's a carriage return, move the cursor to the beginning of the line
                self.text_edit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
                self.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.MoveAnchor)
            # Replace the last line with the new one (excluding the carriage return)
            self.last_line = string.split("\r")[-1]
            self.text_edit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
            self.text_edit.insertPlainText(self.last_line)

        else:
            if self.last_line:
                # put a new line  with br at the start of the string
                string = f"<br>{string}"

            # substitute the new line with br
            string = string.replace("\n", "<br>")
            # If there's no carriage return, just append the string to the text edit
            self.text_edit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.text_edit.insertHtml(string)
            self.last_line = ''


class AppLogger:
    def __init__(self, filename, level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # log to file
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # log to stdout
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def addHandler(self, handler):
        self.logger.addHandler(handler)


class QthreadLogger:
    def __init__(self, signal: QtCore.Signal, level=logging.DEBUG):
        self.logger = signal
        self.level = level
        self.formatter = HtmlColorFormatter("%(message)s")
        self.text_edit_stream=None

    def debug(self, msg):
        if self.level > logging.DEBUG:
            return
        msg = self.formatter.format(logging.makeLogRecord({"msg": msg, "levelno": logging.DEBUG}))
        self.logger.emit(msg)

    def info(self, msg):
        if self.level > logging.INFO:
            return
        msg = self.formatter.format(logging.makeLogRecord({"msg": msg, "levelno": logging.INFO}))
        self.logger.emit(msg)

    def warning(self, msg):
        if self.level > logging.WARNING:
            return
        msg = self.formatter.format(logging.makeLogRecord({"msg": msg, "levelno": logging.WARNING}))
        self.logger.emit(msg)

    def error(self, msg):
        if self.level > logging.ERROR:
            return
        msg = self.formatter.format(logging.makeLogRecord({"msg": msg, "levelno": logging.ERROR}))
        self.logger.emit(msg)

    def critical(self, msg):
        if self.level > logging.CRITICAL:
            return
        msg = self.formatter.format(logging.makeLogRecord({"msg": msg, "levelno": logging.CRITICAL}))
        self.logger.emit(msg)


class DataCreatorLogger(AppLogger):

    def __init__(self, filename, text_edit: QtWidgets.QTextEdit, level=logging.DEBUG, ):
        super().__init__(filename, level)

        formatter = HtmlColorFormatter("%(message)s")

        if isinstance(text_edit, QtWidgets.QTextEdit):
            self.text_edit_stream = QTextEditStream(text_edit)
            stream_handler = logging.StreamHandler(self.text_edit_stream)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
        else:
            raise TypeError("Stream must be a QTextEdit")


class HtmlColorFormatter(logging.Formatter):
    def __init__(self, format):
        super().__init__(format)

    def format(self, record):
        level_colors = {
            logging.DEBUG: "#FFFF00",  # Yellow
            logging.INFO: "#000000",  # Black
            logging.WARNING: "#FFA500",  # Orange
            logging.ERROR: "#FF0000",  # Red
            logging.CRITICAL: "#8B0000"  # Dark Red
        }
        level_name = record.levelname
        level_color = level_colors[record.levelno]
        message = record.getMessage()

        # Add color to level name

        # Add color to message
        message = f'<span style="color: {level_color}">{message}</span><br/>'

        record.msg = message
        return super().format(record)
