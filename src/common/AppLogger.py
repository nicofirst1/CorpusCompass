import io
import logging
import sys

from PySide6 import QtCore


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
