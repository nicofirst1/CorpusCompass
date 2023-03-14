import os
import shutil
from collections import OrderedDict
from typing import Dict, Any

from PySide6 import QtWidgets

from src.annotation_fixer.af_utils import corpus_dict2text
from src.common import GeneralWindow, Memory, AppLogger, create_input, QTextEditLog
from src.data_analyzer.DAProcess import DAProcess


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
        self.kmean_analysis_input, kmean_analysis_lay = create_input(
            self, "kmean_analysis", self.mem
        )

        self.kmean_n_clusters_input, kmean_n_clusters_lay = create_input(
            self, "kmean_n_clusters", self.mem
        )
        self.kmean_max_clusters_input, kmean_max_clusters_lay = create_input(
            self, "kmean_max_clusters", self.mem
        )

        (
            self.dependent_variable_analysis_input,
            dependent_variable_analysis_lay,
        ) = create_input(self, "dependent_variable_analysis", self.mem)

        self.variable_analysis_checkbox, variable_analysis_lay = create_input(
            self, "variable_analysis", self.mem
        )

        (
            self.poissont_regression_analysis_checkbox,
            poissont_regression_analysis_lay,
        ) = create_input(self, "poissont_regression_analysis", self.mem)

        # add logging text area
        self.logging_area = QTextEditLog(self)

        # add a button to start analysis
        self.start_analysis_button = QtWidgets.QPushButton("Start Analysis")
        self.start_analysis_button.clicked.connect(self.start_analysis)

        # add layout
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(kmean_analysis_lay)
        layout.addLayout(kmean_n_clusters_lay)
        layout.addLayout(kmean_max_clusters_lay)
        layout.addLayout(dependent_variable_analysis_lay)
        layout.addLayout(variable_analysis_lay)
        layout.addLayout(poissont_regression_analysis_lay)
        layout.addWidget(self.logging_area)
        layout.addWidget(self.start_analysis_button)

        self.setLayout(layout)

    def make_dirs(self):
        if os.path.exists(self.mem.analysis_dir):
            # delete dir if it already exist
            shutil.rmtree(self.mem.analysis_dir)

        os.mkdir(self.mem.analysis_dir)
        for k, p in self.mem.analysis_paths.items():
            os.mkdir(p)

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
        self.logging_area.connect_signal(self.worker_thread.logger.signal)
        self.worker_thread.run()

    def analysis_finished(self):
        self.worker_thread = None
