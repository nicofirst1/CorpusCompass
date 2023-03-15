import sys
import threading
from typing import Dict, List

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import QProcess

from src.common import QTextLogger, Memory, AppLogger


class DAProcess(QtCore.QProcess):
    def __init__(
        self,
        binary_dataset: pd.DataFrame,
        independent_variables: Dict[str, List[str]],
        dependent_variables: Dict[str, List[str]],
        speakers: Dict[str, List[str]],
        mem: Memory,
    ):
        super().__init__()

        self.binary_dataset = binary_dataset
        self.independent_variables = independent_variables
        self.dependent_variables = dependent_variables
        self.speakers = speakers
        self.mem = mem

        self.text_area_logger = QTextLogger()
        # define the flag to stop the thread
        self.stop_event = threading.Event()

        # Connect the signals from the process to slots
        self.readyReadStandardOutput.connect(self.handle_stdout)
        self.readyReadStandardError.connect(self.handle_stderr)
        self.stateChanged.connect(self.handle_state)
        self.finished.connect(self.handle_finished)

        self.logger = AppLogger(mem, "daprocess.log")

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: "Finished",
            QProcess.Starting: "Starting",
            QProcess.Running: "Running",
        }
        state_name = states[state]
        self.text_area_logger.info(f"{state_name}")
        self.logger.debug(f"State changes to {state_name}")

    def handle_stdout(self):
        stdout = self.readAllStandardOutput()
        self.text_area_logger.info(stdout.data().decode())

    def handle_stderr(self):
        stderr = self.readAllStandardError()
        self.text_area_logger.error(stderr.data().decode())

    @QtCore.Slot(int, QProcess.ExitStatus)
    def handle_finished(self, exit_code, exit_status):
        # Emit the finished signal with the exit code and status
        self.logger.debug(
            f"Process finished with exit code {exit_code} and status {exit_status}"
        )

    def run(self):
        # Set the process arguments to the serialized input
        self.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        cmd = [
            "-m",
            "src.data_analyzer.da_utils",
            self.mem.preloaded_dir,
            self.mem.postprocess_paths["binary_dataset"],
            self.mem.file_settings,
            self.mem.file_analysis_paths,
        ]

        self.logger.debug(
            "Starting analysis, with the following command:\n"
            f" {sys.executable} {' '.join(cmd)}"
        )

        self.start(
            sys.executable,
            cmd,
            mode=QtCore.QIODevice.ReadWrite,
        )

    # add method for terminating the process
    def terminate(self):
        self.logger.debug("Terminate called")
        self.stop_event.set()
        self.kill()
