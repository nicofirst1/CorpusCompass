import sys
import threading
from typing import Dict, List

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import QProcess

from src.common import QTextLogger, Memory


class DAProcess(QtCore.QProcess):
    def __init__(
            self,
            binary_dataset: pd.DataFrame,
            independent_variables: Dict[str, List[str]],
            dependent_variables: Dict[str, List[str]],
            speakers: Dict[str, List[str]],
            settings: Memory,
    ):
        super().__init__()

        self.binary_dataset = binary_dataset
        self.independent_variables = independent_variables
        self.dependent_variables = dependent_variables
        self.speakers = speakers
        self.settings = settings

        self.logger = QTextLogger()
        # define the flag to stop the thread
        self.stop_event = threading.Event()
        self.results = None
        self.input_file = None

        # Connect the signals from the process to slots
        self.readyReadStandardOutput.connect(self.handle_stdout)
        self.readyReadStandardError.connect(self.handle_stderr)
        self.stateChanged.connect(self.handle_state)
        self.finished.connect(self.handle_finished)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: "Finished",
            QProcess.Starting: "Starting",
            QProcess.Running: "Running",
        }
        state_name = states[state]
        self.logger.info(f"{state_name}..")

    def handle_stdout(self):
        stdout = self.readAllStandardOutput()
        self.logger.info(stdout.data().decode())

    def handle_stderr(self):
        stderr = self.readAllStandardError()
        self.logger.error(stderr.data().decode())

    @QtCore.Slot(int, QProcess.ExitStatus)
    def handle_finished(self, exit_code, exit_status):
        # Emit the finished signal with the exit code and status
        print(f"Process finished with exit code {exit_code} and status {exit_status}")

    def run(self):
        if self.settings.settings["kmean_analysis"]:
            # Set the process arguments to the serialized input
            self.setProcessChannelMode(QtCore.QProcess.MergedChannels)

            cmd = [
                "-m",
                "src.data_analyzer.da_utils",
                self.settings.preloaded_dir,
                self.settings.postprocess_paths['binary_dataset'],
                self.settings.file_settings,
                self.settings.file_analysis_paths,
            ]

            print("Starting analysis, with the following command:\n"
                  f" {sys.executable} {' '.join(cmd)}")

            self.start(
                sys.executable,
                cmd,
                mode=QtCore.QIODevice.ReadWrite,
            )

    # add method for terminating the process
    def terminate(self):
        self.stop_event.set()
        self.kill()