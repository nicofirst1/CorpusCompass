from collections import OrderedDict
from collections import OrderedDict
from typing import Dict, Any

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QToolTip, QLineEdit

from annotation_fixer.common import Memory, GeneralWindow, corpus_dict2text, GenerateDatasetThread
from annotation_fixer.common.AppLogger import DataCreatorLogger


def create_input_lineedit(label, default_value='', hover_help='', delay=500):
    # Create QLineEdit widget
    input_widget = QLineEdit()
    input_widget.setPlaceholderText(default_value)
    input_widget.setText(default_value)

    # Set tooltip with hover help text
    if hover_help:
        def show_tooltip():
            QToolTip.showText(QCursor.pos(), hover_help, input_widget, input_widget.rect())

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
    def __init__(self, mem: Memory, postprocess_data: Dict[str, Any]):
        self.corpus_dict = OrderedDict(postprocess_data["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)

        self.independent_variables = postprocess_data["independent_variables"]
        self.dependent_variables = postprocess_data["dependent_variables"]
        self.speakers = postprocess_data["speakers"]
        self.worker_thread = None

        super().__init__(mem, "Dataset Creator")
        self.logger = DataCreatorLogger(".annotation_fixer/dataset_creator.log", self.log_window)

    def create_widgets(self):
        # Create QLineEdit widgets with hover help
        square_regex_help = "Regex to find the complete annotation rule."
        self.square_regex_input, square_regex_lay = create_input_lineedit("Square regex: ",
                                                                          default_value=r"(\[\$[\S ]*?\])",
                                                                          hover_help=square_regex_help)

        feat_regex_help = "Regex to find the content of an annotation."
        self.feat_regex_input, feat_regex_lay = create_input_lineedit("Feat regex: ",
                                                                      default_value=r'\[\$([\S ]*?)\]',
                                                                      hover_help=feat_regex_help)

        name_regex_help = "Regex to univocally find the speaker name in the paragraph."
        self.name_regex_input, name_regex_lay = create_input_lineedit("Name regex: ",
                                                                      default_value=r"(^[A-z0-9?._]+) ",
                                                                      hover_help=name_regex_help)

        # Create QCheckBox widget for previous_line
        self.previous_line_checkbox = QtWidgets.QCheckBox("Include previous paragraph in final output", self)
        self.previous_line_checkbox.setChecked(False)

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

        # Create non-editable log window
        self.log_window = QtWidgets.QTextEdit(self)
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
        layout.addWidget(self.previous_line_checkbox)
        layout.addLayout(ngram_lay)
        layout.addWidget(self.log_window)
        layout.addWidget(self.generate_dataset_button)
        self.setLayout(layout)

    def start_generate_dataset(self):

        if self.worker_thread is not None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Generation already in progress.")
            return

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
            square_regex, feat_regex, name_regex, previous_line, ngram_prev, ngram_next
        ]

        self.worker_thread = GenerateDatasetThread(inputs, self.corpus_dict, self.independent_variables,
                                                   self.dependent_variables, self.speakers,
                                                   self.mem.settings['separator'])

        self.worker_thread.finished.connect(self.on_generate_dataset_finished)
        self.worker_thread.signal.connect(self.log_window.append)
        self.worker_thread.start()

    def on_generate_dataset_finished(self):
        if isinstance(self.worker_thread.results, str):
            QtWidgets.QMessageBox.warning(self, "Warning", self.worker_thread.results)
        elif isinstance(self.worker_thread.results, Dict):
            QtWidgets.QMessageBox.information(self, "Information", "Dataset generated successfully.")
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Failed to generate dataset.")
        self.worker_thread = None
