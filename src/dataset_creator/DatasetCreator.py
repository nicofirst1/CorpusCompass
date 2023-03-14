import os
import subprocess
import sys
from collections import OrderedDict
from typing import Dict, Any

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QToolTip, QLineEdit

from src.annotation_fixer.af_utils import corpus_dict2text
from src.common import (
    GeneralWindow,
    Memory,
    AppLogger,
    save_postprocess,
    QTextEditLog,
    create_input,
)
from src.dataset_creator.DatasetThread import DatasetThread


def create_input_lineedit(label, default_value="", hover_help="", delay=500):
    # Create QLineEdit widget
    input_widget = QLineEdit()
    input_widget.setPlaceholderText(default_value)
    input_widget.setText(default_value)

    # Set tooltip with hover help text
    if hover_help:

        def show_tooltip():
            QToolTip.showText(
                QCursor.pos(), hover_help, input_widget, input_widget.rect()
            )

        def hide_tooltip():
            QToolTip.hideText()

        def on_hover(_):
            QTimer.singleShot(delay, show_tooltip)

        def on_leave(_):
            QTimer.singleShot(0, hide_tooltip)

        input_widget.enterEvent = on_hover
        input_widget.leaveEvent = on_leave

    # Add label and input widget to layout
    layout = QtWidgets.QFormLayout()
    layout.addRow(label, input_widget)
    return input_widget, layout


class DatasetCreator(GeneralWindow):
    def __init__(self, mem: Memory, preloaded: Dict[str, Any]):
        self.corpus_dict = OrderedDict(preloaded["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)
        self.postprocessed = None

        self.independent_variables = preloaded["independent_variables"]
        self.dependent_variables = preloaded["dependent_variables"]
        self.speakers = preloaded["speakers"]

        self.worker_thread = None
        self.worker_thread_started = False

        super().__init__(mem, "Dataset Creator")
        self.logger = AppLogger(mem, "dataset_creator.log")

    def create_widgets(self):
        # Create QLineEdit widgets with hover help
        square_regex_help = "Regex to find the complete annotation rule."
        name = "annotation_regex"
        self.square_regex_input, square_regex_lay = create_input(
            self, "annotation_regex", self.mem
        )

        self.feat_regex_input, feat_regex_lay = create_input(
            self, "feat_regex", self.mem
        )

        self.name_regex_input, name_regex_lay = create_input(
            self, "name_regex", self.mem
        )

        self.previous_line_checkbox, previous_line_lay = create_input(
            self, "previous_line", self.mem
        )

        # Create QSpinBox widgets for ngram_params
        self.ngram_prev_input = QtWidgets.QSpinBox(self)
        self.ngram_prev_input.setMinimum(0)
        self.ngram_prev_input.setMaximum(100)
        self.ngram_prev_input.setValue(10)

        self.ngram_next_input = QtWidgets.QSpinBox(self)
        self.ngram_next_input.setMinimum(0)
        self.ngram_next_input.setMaximum(100)
        self.ngram_next_input.setValue(5)

        # Create "Generate Dataset" button
        self.generate_dataset_button = QtWidgets.QPushButton("Generate Dataset")
        self.generate_dataset_button.clicked.connect(self.start_generate_dataset)

        # Create "stop generation" button
        self.stop_generation_button = QtWidgets.QPushButton("Stop Generation")
        self.stop_generation_button.clicked.connect(self.stop_generation)
        self.stop_generation_button.setEnabled(False)

        # add a "go to annotation fixer" button
        self.finish_button = QtWidgets.QPushButton("Finish")
        self.finish_button.clicked.connect(self.close)
        self.finish_button.setEnabled(False)

        # add a "open files" button
        self.open_files_button = QtWidgets.QPushButton("Open Files")
        self.open_files_button.clicked.connect(self.open_files)
        self.open_files_button.setEnabled(False)

        # Create non-editable log window
        self.log_window = QTextEditLog(self)
        self.log_window.setAcceptRichText(True)
        self.log_window.setReadOnly(True)

        # Create layout for ngram inputs
        ngram_lay = QtWidgets.QHBoxLayout()
        ngram_lay.addWidget(QtWidgets.QLabel("n-gram context:"))
        ngram_lay.addWidget(self.ngram_prev_input)
        ngram_lay.addWidget(self.ngram_next_input)

        # Create vertical layout for all widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(square_regex_lay)
        layout.addLayout(feat_regex_lay)
        layout.addLayout(name_regex_lay)
        layout.addLayout(previous_line_lay)
        layout.addLayout(ngram_lay)
        layout.addWidget(self.log_window)

        # add buttons to layout
        start_stop_lay = QtWidgets.QHBoxLayout()
        start_stop_lay.addWidget(self.generate_dataset_button)
        start_stop_lay.addWidget(self.stop_generation_button)
        layout.addLayout(start_stop_lay)

        next_lay = QtWidgets.QHBoxLayout()
        next_lay.addWidget(self.finish_button)
        next_lay.addWidget(self.open_files_button)
        layout.addLayout(next_lay)

        self.setLayout(layout)

    def stop_generation(self):
        if self.worker_thread is None:
            return

        self.worker_thread.stop()
        self.worker_thread = None
        self.worker_thread_started = False

        # clear log window
        self.log_window.append("Generation stopped.")

        self.stop_generation_button.setEnabled(False)
        self.generate_dataset_button.setEnabled(True)

    def start_generate_dataset(self):
        if self.worker_thread is not None:
            QtWidgets.QMessageBox.warning(
                self, "Warning", "Generation already in progress."
            )
            return

        self.stop_generation_button.setEnabled(True)
        self.generate_dataset_button.setEnabled(False)
        self.log_window.clear()

        # get inputs
        previous_line = self.previous_line_checkbox.isChecked()
        ngram_prev = self.ngram_prev_input.value()
        ngram_next = self.ngram_next_input.value()
        # get regexes
        square_regex = self.square_regex_input.text()
        feat_regex = self.feat_regex_input.text()
        name_regex = self.name_regex_input.text()

        inputs = [
            square_regex,
            feat_regex,
            name_regex,
            previous_line,
            ngram_prev,
            ngram_next,
        ]

        self.worker_thread = DatasetThread(
            inputs,
            self.corpus_dict,
            self.independent_variables,
            self.dependent_variables,
            self.speakers,
        )

        self.worker_thread.finished.connect(self.on_generate_dataset_finished)
        self.log_window.connect_signal(self.worker_thread.logger.signal)
        self.worker_thread.start()
        self.worker_thread_started = True

    def on_generate_dataset_finished(self):
        print("on_generate_dataset_finished called")
        if not self.worker_thread_started:
            return
        # make qmessagebox not blocking
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        if self.worker_thread is None:
            pass
        elif isinstance(self.worker_thread.results, str):
            msg.setText(self.worker_thread.results)
            msg.setWindowTitle("Warning")

        elif isinstance(self.worker_thread.results, Dict):
            msg.setText("Dataset generated successfully.")
            msg.setWindowTitle("Success")
            # save dataset
            save_postprocess(self.worker_thread.results, self.mem)
            self.postprocessed = self.worker_thread.results

            # log where the dataset is saved
            path_dict = self.mem.postprocess_paths
            self.log_window.append("Dataset saved in: \n")

            for key in path_dict:
                self.log_window.append(key + ": " + path_dict[key])

            self.log_window.ensureCursorVisible()

            # enable buttons
            self.finish_button.setEnabled(True)
            self.open_files_button.setEnabled(True)

        else:
            msg.setText("Failed to generate dataset.")
            msg.setWindowTitle("Warning")

        self.worker_thread = None
        self.generate_dataset_button.setEnabled(True)
        self.stop_generation_button.setEnabled(False)
        self.worker_thread_started = False

        msg.exec_()

    def close(self) -> bool:
        self.finished.emit()
        return super().close()

    def open_files(self):
        """Based on the system, open the files in the default program"""
        file_path = self.mem.postprocess_paths["dataset"]
        file_dir = os.path.dirname(file_path)
        if sys.platform == "win32":
            os.startfile(file_dir)
        elif sys.platform == "darwin":
            subprocess.call(["open", file_dir])
        else:
            subprocess.call(["xdg-open", file_dir])
