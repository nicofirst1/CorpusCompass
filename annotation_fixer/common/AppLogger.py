import io
import logging
import sys

from PySide6 import QtGui, QtWidgets
from tqdm import tqdm


class QTextEditStream(io.StringIO):
    def __init__(self, text_edit:QtWidgets.QTextEdit):
        super().__init__()
        self.text_edit = text_edit

    def write(self, string):
        self.text_edit.moveCursor(QtGui.QTextCursor.End)
        self.text_edit.insertPlainText(string)
        self.text_edit.moveCursor(QtGui.QTextCursor.End)


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

class TqdmWithLogOutput(tqdm):
    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 order=None, dynamic_ncols=False, smoothing=0.3, bar_format=None,
                 initial=0, position=None, gui=False, logger=None):
        super().__init__(iterable, desc, total, leave, file, ncols, mininterval, maxinterval, miniters,
                         order, dynamic_ncols, smoothing, bar_format, initial, position, gui)
        self.logger = logger
        self.text_edit_stream = QTextEditStream(file)

    def write(self, msg='', end='\n', refresh=True):
        if self.logger is not None:
            self.logger.info(msg)
        self.text_edit_stream.write(msg + end)
        if refresh:
            self.refresh()
class DataCreatorLogger(AppLogger):

    def __init__(self, filename,  text_edit:QtWidgets.QTextEdit,level=logging.DEBUG,):
        super().__init__(filename, level)

        formatter = logging.Formatter("%(message)s")

        if isinstance(text_edit, QtWidgets.QTextEdit):
            self.text_edit_stream = QTextEditStream(text_edit)
            stream_handler = logging.StreamHandler(self.text_edit_stream)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
        else:
            raise TypeError("Stream must be a QTextEdit")

    def add_tqdm(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 order=None, dynamic_ncols=False, smoothing=0.3, bar_format=None,
                 initial=0, position=None, gui=False):
        return TqdmWithLogOutput(iterable, desc, total, leave, self.text_edit_stream, ncols, mininterval, maxinterval, miniters,
                         order, dynamic_ncols, smoothing, bar_format, initial, position, gui, self.logger)
