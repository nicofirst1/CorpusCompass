from PySide6 import QtWidgets

from src.annotation_fixer import AnnotationFixer
from src.common import GeneralWindow, Memory
from src.dataset_creator import DatasetCreator
from src.other_windows import LoadFiles, Settings
from src.other_windows.AskLoaded import AskLoading


class Main(GeneralWindow):
    def __init__(self, mem: Memory):

        self.postprocess_data = None
        self.window_ask = None
        self.window_file_loader = None
        self.window_dataset_creator = None
        self.window_annotation_fixer = None
        self.window_data_analyzer = None
        self.window_settings = None

        super().__init__(mem, "Corpus Compass")

    def show(self):
        super().show()

        if self.mem.exist_preloaded():
            # open window AskLoading in a new thread
            self.window_ask = AskLoading(self.mem)
            self.window_ask.show()
            # show on top
            self.window_ask.activateWindow()
            self.window_ask.finished.connect(self.ask_finished)

    def create_widgets(self):
        # create a button for the dataset creator
        self.dataset_creator_button = QtWidgets.QPushButton("Dataset Creator")
        self.dataset_creator_button.clicked.connect(self.open_window)

        # create a button for the annotation fixer
        self.annotation_fixer_button = QtWidgets.QPushButton("Annotation Fixer")
        self.annotation_fixer_button.clicked.connect(self.open_window)

        # create a button for the data_analyzer
        self.data_analyzer_button = QtWidgets.QPushButton("Data Analyzer")
        self.data_analyzer_button.clicked.connect(self.open_window)

        # create a button for the setting
        self.setting_button = QtWidgets.QPushButton("Setting")
        self.setting_button.clicked.connect(self.open_window)

        # create vertical layout
        self.layout = QtWidgets.QVBoxLayout()

        # add widgets to the layout
        self.layout.addWidget(self.dataset_creator_button)
        self.layout.addWidget(self.annotation_fixer_button)
        self.layout.addWidget(self.data_analyzer_button)
        self.layout.addWidget(self.setting_button)

        # set the layout
        self.setLayout(self.layout)

    def ask_finished(self):
        to_load = self.window_ask.load

        if to_load:
            self.window_file_loader = LoadFiles(self.mem)
            self.window_file_loader.show()
            self.window_ask.finished.connect(self.loader_finished)
        else:
            self.postprocess_data = self.mem.load_all_preloaded()

    def loader_finished(self):
        if not self.window_file_loader.has_finished:
            raise Exception("The user closed the window without loading the files")

            # save the self.file_loader values
        postprocess_data = dict(
            corpus_text=self.window_file_loader.corpus_text,
        )
        postprocess_data.update(self.window_file_loader.annotation_info_csv)
        postprocess_data.update(self.window_file_loader.variables_csv)
        self.mem.save_preloaded(postprocess_data)
        self.postprocess_data = postprocess_data

    def open_window(self):
        # get the sender
        sender = self.sender()
        if self.postprocess_data is not None:
            if sender == self.dataset_creator_button:
                self.window_dataset_creator = DatasetCreator(self.mem, self.postprocess_data)
                self.window_dataset_creator.show()
            elif sender == self.annotation_fixer_button:
                self.window_annotation_fixer = AnnotationFixer(self.mem, self.postprocess_data)
                self.window_annotation_fixer.show()
            elif sender == self.data_analyzer_button:
                self.window_data_analyzer = DataAnalyzer(self.mem, self.postprocess_data)
                self.window_data_analyzer.show()
        if sender == self.setting_button:
            self.window_settings = Settings(self.mem)
            self.window_settings.show()
