from PySide6 import QtWidgets

from src.annotation_fixer import AnnotationFixer
from src.common import GeneralWindow, Memory, load_postprocess
from src.data_analyzer import DataAnalyzer
from src.dataset_creator import DatasetCreator
from src.other_windows import LoadFiles, Settings
from src.other_windows.AskLoaded import AskLoading


class Main(GeneralWindow):
    def __init__(self, mem: Memory):
        self.postprocess_data = None
        self.preloaded_data = None

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
            self.window_ask.finished.connect(self.ask_finished)

    def create_widgets(self):
        # create a button for the loading files
        self.load_files_button = QtWidgets.QPushButton("Load Files")
        self.load_files_button.clicked.connect(self.open_window)

        # create a button for the dataset creator
        self.dataset_creator_button = QtWidgets.QPushButton("Dataset Creator")
        self.dataset_creator_button.clicked.connect(self.open_window)
        self.dataset_creator_button.setEnabled(False)

        # create a button for the annotation fixer
        self.annotation_fixer_button = QtWidgets.QPushButton("Annotation Fixer")
        self.annotation_fixer_button.clicked.connect(self.open_window)
        self.annotation_fixer_button.setEnabled(False)

        # create a button for the data_analyzer
        self.data_analyzer_button = QtWidgets.QPushButton("Data Analyzer")
        self.data_analyzer_button.clicked.connect(self.open_window)
        self.data_analyzer_button.setEnabled(False)

        # create a button for the setting
        self.setting_button = QtWidgets.QPushButton("Setting")
        self.setting_button.clicked.connect(self.open_window)

        # create vertical layout
        self.layout = QtWidgets.QVBoxLayout()

        # add widgets to the layout

        self.layout.addWidget(self.load_files_button)
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
            self.window_file_loader.finished.connect(self.loader_finished)
            self.window_file_loader.show()
        else:
            self.preloaded_data = self.mem.load_all_preloaded()
            self.postprocess_data, error = load_postprocess(
                self.mem.postprocess_paths.values(),
                self.mem.settings["encoding"],
                self.mem.settings["separator"],
            )

            if error:
                raise Exception(error)

        self.activate_buttons()

    def loader_finished(self):
        if not self.window_file_loader.what_is_loaded:
            raise Exception("The user closed the window without loading the files")

        if self.window_file_loader.what_is_loaded > 0:
            # save the self.file_loader values
            preloaded_data = dict(
                corpus_text=self.window_file_loader.corpus_text,
            )
            preloaded_data.update(self.window_file_loader.variables_csv)
            self.mem.save_preloaded(preloaded_data)
            self.preloaded_data = preloaded_data

        if self.window_file_loader.what_is_loaded > 1:
            self.postprocess_data = self.window_file_loader.postprocess_data

        self.activate_buttons()

    def dataset_creator_finished(self):
        self.postprocess_data = self.window_dataset_creator.postprocessed
        self.activate_buttons()

    def activate_buttons(self):
        if self.preloaded_data is not None:
            self.dataset_creator_button.setEnabled(True)
        if self.postprocess_data is not None:
            self.annotation_fixer_button.setEnabled(True)
            self.data_analyzer_button.setEnabled(True)

    def open_window(self):
        # get the sender
        sender = self.sender()

        has_preloaded = self.preloaded_data is not None
        has_postprocess = self.postprocess_data is not None

        if sender == self.dataset_creator_button and has_preloaded:
            self.window_dataset_creator = DatasetCreator(self.mem, self.preloaded_data)
            self.window_dataset_creator.show()
            self.window_dataset_creator.finished.connect(self.dataset_creator_finished)
        elif (
            sender == self.annotation_fixer_button and has_postprocess and has_preloaded
        ):
            self.window_annotation_fixer = AnnotationFixer(
                self.mem, self.preloaded_data, self.postprocess_data
            )
            self.window_annotation_fixer.show()
        elif sender == self.data_analyzer_button and has_postprocess and has_preloaded:
            self.window_data_analyzer = DataAnalyzer(self.mem,self.preloaded_data , self.postprocess_data)
            self.window_data_analyzer.show()

        elif sender == self.load_files_button:
            self.window_file_loader = LoadFiles(self.mem)
            self.window_file_loader.show()
            self.window_file_loader.finished.connect(self.loader_finished)
        elif sender == self.setting_button:
            self.window_settings = Settings(self.mem)
            self.window_settings.show()
