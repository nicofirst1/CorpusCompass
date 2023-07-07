from collections import OrderedDict
from collections import OrderedDict
from typing import Dict, Any

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog

from src.annotation_fixer.af_utils import corpus_dict2text
from src.common import (
    GeneralWindow,
    Memory,
    AppLogger, create_input,
)


class DatasetUpdater(GeneralWindow):
    def __init__(self, mem: Memory, preloaded: Dict[str, Any], postprocess: Dict[str, Any]):
        self.corpus_dict = OrderedDict(preloaded["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)
        self.postprocessed = postprocess

        self.independent_variables = preloaded["independent_variables"]
        self.dependent_variables = preloaded["dependent_variables"]
        self.speakers = preloaded["speakers"]

        self.new_data_file = None
        self.old_data_file = None
        self.corpus_dir = None


        super().__init__(mem, "Dataset Updater")
        self.logger = AppLogger(mem, "dataset_updater.log")

    def create_widgets(self):
        # Create QLineEdit widgets with hover help
        self.new_data_file_button=QtWidgets.QPushButton("New Data File")
        self.new_data_file_button.clicked.connect(self.open_file)

        self.old_data_file_button=QtWidgets.QPushButton("Old Data File")
        self.old_data_file_button.clicked.connect(self.open_file)

        self.corpus_dir_button=QtWidgets.QPushButton("Corpus Directory")
        self.corpus_dir_button.clicked.connect(self.open_file)


        # Create "Generate Dataset" button
        self.generate_dataset_button = QtWidgets.QPushButton("Generate Dataset")



        # Create vertical layout for all widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.new_data_file_button)
        layout.addWidget(self.old_data_file_button)
        layout.addWidget(self.corpus_dir_button)
        layout.addWidget(self.generate_dataset_button)




        self.setLayout(layout)

    def open_file(self):
        # get sender object
        sender = self.sender()

        # distinguish between buttons
        if sender == self.new_data_file_button:
            # open file dialog
            file_name = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.csv)")[0]
            # set text to line edit
            self.new_data_file.setText(file_name)
        elif sender == self.old_data_file_button:
            # open file dialog
            file_name = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.csv)")[0]
            # set text to line edit
            self.old_data_file.setText(file_name)
        elif sender == self.corpus_dir_button:
            # open file dialog
            dir_name = QFileDialog.getExistingDirectory(self, "Open Directory", "")
            # set text to line edit
            self.corpus_dir.setText(dir_name)
        else:
            raise ValueError("Unknown sender object")