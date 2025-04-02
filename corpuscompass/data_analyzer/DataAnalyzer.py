import os
import shutil
from collections import OrderedDict
from typing import Dict, Any

from PySide6 import QtWidgets

from corpuscompass.annotation_fixer.af_utils import corpus_dict2text
from corpuscompass.common import GeneralWindow, Memory, AppLogger, create_input, QTextEditLog
from corpuscompass.data_analyzer.DAProcess import DAProcess


class DataAnalyzer(GeneralWindow):
    def __init__(
        self,
        mem: Memory,
        preloaded_data: Dict[str, Any],
        postprocess_data: Dict[str, Any],
    ):
        self.corpus_dict = OrderedDict(preloaded_data["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)
        self.df_annotation_info = postprocess_data["annotation_info"]
        self.df_missed_annotations = postprocess_data["missed_annotations"]
        self.df_dataset = postprocess_data["dataset"]
        self.df_binary_dataset = postprocess_data["binary_dataset"]

        self.independent_variables = preloaded_data["independent_variables"]
        self.dependent_variables = preloaded_data["dependent_variables"]
        self.speakers = preloaded_data["speakers"]

        self.worker_thread = None

        super().__init__(mem, "Data Analyzer")
        self.logger = AppLogger(mem, "data_analyzer.log")

    def create_widgets(self):
        layout = QtWidgets.QVBoxLayout()

        for set_k in self.mem.setting_groups["data_analyzer"]:
            _, lay = create_input(self, set_k, self.mem)

            layout.addLayout(lay)

        # add logging text area
        self.logging_area = QTextEditLog(self)

        # add a button to start analysis
        self.start_analysis_button = QtWidgets.QPushButton("Start Analysis")
        self.start_analysis_button.clicked.connect(self.start_analysis)

        # add a button to stop analysis
        self.stop_analysis_button = QtWidgets.QPushButton("Stop Analysis")
        self.stop_analysis_button.clicked.connect(self.stop_analysis)
        self.stop_analysis_button.setEnabled(False)

        # add layout for start and stop analysis button
        start_stop_analysis_lay = QtWidgets.QHBoxLayout()
        start_stop_analysis_lay.addWidget(self.start_analysis_button)
        start_stop_analysis_lay.addWidget(self.stop_analysis_button)

        # add layout

        layout.addWidget(self.logging_area)
        layout.addLayout(start_stop_analysis_lay)

        self.setLayout(layout)

    def make_dirs(self):
        if os.path.exists(self.mem.analysis_dir):
            # delete dir if it already exist
            shutil.rmtree(self.mem.analysis_dir)

        os.mkdir(self.mem.analysis_dir)

    def start_analysis(self):
        # check if analysis is already running
        if self.worker_thread is not None:
            return

        # check if analysis path already exist
        if (
            os.path.exists(self.mem.analysis_dir)
            and not self.mem.settings["suppress_existent"]
        ):
            # if analysis path already exist and suppress_existent is false
            # ask user if he wants to overwrite the analysis
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Analysis path already exist")
            msg.setInformativeText("Do you want to overwrite the analysis?")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            ret = msg.exec()
            if ret == QtWidgets.QMessageBox.No:
                return

        # create analysis dir
        self.make_dirs()
        self.logging_area.clear()

        # create a copy of the inputs
        binary_dataset = self.df_binary_dataset.copy()
        independent_variables = self.independent_variables.copy()
        dependent_variables = self.dependent_variables.copy()
        speakers = self.speakers.copy()

        self.worker_thread = DAProcess(
            binary_dataset,
            independent_variables,
            dependent_variables,
            speakers,
            self.mem,
        )

        self.worker_thread.finished.connect(self.analysis_finished)
        self.logging_area.connect_signal(self.worker_thread.text_area_logger.signal)
        self.worker_thread.run()

        self.stop_analysis_button.setEnabled(True)
        self.start_analysis_button.setEnabled(False)

    def stop_analysis(self):
        if self.worker_thread is not None:
            self.worker_thread.terminate()
            self.worker_thread = None
            self.stop_analysis_button.setEnabled(False)
            self.start_analysis_button.setEnabled(True)

    def analysis_finished(self):
        self.worker_thread = None

        self.stop_analysis_button.setEnabled(False)
        self.start_analysis_button.setEnabled(True)
