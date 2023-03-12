import logging
import os.path
import sys

from src.common.Memory import Memory


class AppLogger:
    def __init__(self, memory: Memory, filename: str, level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # log to file

        filename = os.path.join(memory.dir, filename)
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
