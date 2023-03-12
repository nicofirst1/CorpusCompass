import io
import logging

from PySide6 import QtCore


class FakeStream(io.StringIO):
    """
    used to redirect tqdm output to text area
    """

    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def write(self, string):
        self.signal.emit(string)


class QthreadLogger:
    def __init__(self, signal: QtCore.Signal, level=logging.DEBUG):
        self.logger = signal
        self.level = level
        self.formatter = HtmlColorFormatter("%(message)s")
        self.text_edit_stream = FakeStream(signal)

    def debug(self, msg):
        if self.level > logging.DEBUG:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.DEBUG})
        )
        self.logger.emit(msg)

    def info(self, msg):
        if self.level > logging.INFO:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.INFO})
        )
        self.logger.emit(msg)

    def warning(self, msg):
        if self.level > logging.WARNING:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.WARNING})
        )
        self.logger.emit(msg)

    def error(self, msg):
        if self.level > logging.ERROR:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.ERROR})
        )
        self.logger.emit(msg)

    def critical(self, msg):
        if self.level > logging.CRITICAL:
            return
        msg = self.formatter.format(
            logging.makeLogRecord({"msg": msg, "levelno": logging.CRITICAL})
        )
        self.logger.emit(msg)


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
