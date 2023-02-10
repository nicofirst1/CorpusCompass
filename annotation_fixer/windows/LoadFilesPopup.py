import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QComboBox, QScrollArea

from annotation_fixer.common import Memory, GeneralWindow


def load_csv2pandas(path: str, encoding: str, sep: str) -> pd.DataFrame:
    """
    Load a csv file into a pandas dataframe
    """
    with open(path, "rb") as f:
        content = f.read().decode(encoding)
    # find the separator by counting the number of most common separator
    content = pd.read_csv(path, encoding=encoding, sep=sep, on_bad_lines='skip')

    return content


class LoadFilesPopup(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)

        self.corpus_files = None
        self.corpus_text = {}
        self.annotation_info = None
        self.annotation_info_csv = ""
        self.missing_annotations = None
        self.missing_annotations_csv = ""
        self.message = None
        self.encodings = ["UTF-8", "UTF-16"]
        enc_idx = self.mem.lfp.get("encoding") or 0
        self.encoding = self.encodings[enc_idx]

        self.separator = self.mem.lfp.get("separator") or ";"
        self.mem.lfp["separator"] = self.separator

        self.setWindowTitle("Load Files")

        self.create_widgets()
        self.has_finished = False

    def create_widgets(self):
        self.message = QtWidgets.QLabel("Please upload corpus and annotation:\n"
                                        "- Corpus not uploaded\n"
                                        "- Annotation not uploaded\n"
                                        "- Missing annotation not uploaded\n")
        self.message.setStyleSheet("color: white; background-color: black")

        self.message_scroll = QScrollArea()
        self.message_scroll.setWidget(self.message)
        self.message_scroll.setWidgetResizable(True)

        self.corpus_message = QtWidgets.QTextEdit("")
        self.corpus_message.setStyleSheet("color: white; background-color: black")


        self.corpus_message_scroll = QScrollArea()
        self.corpus_message_scroll.setWidget(self.corpus_message)
        self.corpus_message_scroll.setWidgetResizable(True)

        self.corpus_button = QtWidgets.QPushButton("Load Corpus Files")
        self.corpus_button.clicked.connect(self.load_corpus)

        self.annotation_info_button = QtWidgets.QPushButton("Load Annotation Info")
        self.annotation_info_button.clicked.connect(self.load_annotation_info)

        self.missing_annotation_info_button = QtWidgets.QPushButton("Load Missing Annotation Info")
        self.missing_annotation_info_button.clicked.connect(self.load_missing_annotation_info)

        self.encoding_label = QtWidgets.QLabel("Encoding:")
        self.encoding_combo_box = QComboBox()
        for encoding in self.encodings:
            self.encoding_combo_box.addItem(encoding)

        self.encoding_combo_box.activated[int].connect(self.handle_encoding_change)
        self.encoding_combo_box.setCurrentText(self.encoding)

        self.finish_button = QtWidgets.QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish)
        self.finish_button.setEnabled(False)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.encoding_label)
        layout.addWidget(self.encoding_combo_box)
        layout.addWidget(self.corpus_button)
        layout.addWidget(self.annotation_info_button)
        layout.addWidget(self.missing_annotation_info_button)
        layout.addWidget(self.message_scroll)
        layout.addWidget(self.corpus_message_scroll)
        layout.addWidget(self.finish_button)

        self.setLayout(layout)

    def handle_encoding_change(self, index):
        self.encoding = self.encodings[index]
        self.mem.lfp["encoding"] = index

    def load_corpus(self):
        """
        Load corpus files
        """
        dir = self.mem.lfp.get("corpus_dir") or ""
        self.corpus_files = QFileDialog.getOpenFileNames(
            self, "Select Corpus Files", dir, "Text Files (*.txt);;All Files (*.*)"
        )[0]

        if self.corpus_files:
            self.mem.lfp["corpus_dir"] = self.corpus_files[0].rsplit("/", 1)[0]

            for p in self.corpus_files:
                try:
                    with open(p, "rb") as f:
                        self.corpus_text[p] = f.read().decode(self.encoding)
                except Exception as e:
                    err_msg = f"Error loading corpus files ({p}):\n{e}\n Please try again"
                    self.corpus_message.setText(err_msg)
                    # change color to red
                    self.corpus_message.setStyleSheet("color: red; background-color: black")

                    return

            self.message.setText("Please upload corpus and annotation:\n"
                                 "- Corpus file loaded:\n\t--" +
                                 "\n\t--".join(self.corpus_files) +
                                 "\n- Annotation not uploaded\n"
                                 "- Missing annotation not uploaded\n")
            # change color to green
            self.corpus_message.setStyleSheet("color: green; background-color: black")
            self.corpus_message.setText(
                "Corpus files loaded:\n" + "\n".join(list(self.corpus_text.values())[:10]) + "...")

            if self.annotation_info and self.missing_annotations:
                self.finish_button.setEnabled(True)

    def load_annotation_info(self):
        dir = self.mem.lfp.get("annotation_dir") or ""
        self.annotation_info = QFileDialog.getOpenFileName(
            self, "Select Annotation Info CSV", dir, "CSV Files (*.csv)"
        )[0]

        if self.annotation_info:
            self.mem.lfp["annotation_dir"] = self.annotation_info.rsplit("/", 1)[0]

            # read annotation info file
            try:
                self.annotation_info_csv = load_csv2pandas(self.annotation_info, self.encoding, self.separator)
            except Exception as e:
                err_msg = f"Error loading annotation file ({self.annotation_info}):\n{e}\n Please try again"
                self.corpus_message.setText(err_msg)
                # change color to red
                self.corpus_message.setStyleSheet("color: red; background-color: black")
                return

            self.message.setText("Please upload corpus and annotation:\n"
                                 "- Corpus file loaded:\n\t--" +
                                 "\n\t--".join(self.corpus_files) +
                                 "\n- Annotation file loaded:\n\t--" + self.annotation_info + "\n"
                                                                                        "- Missing annotation not uploaded")
            # change color to green
            self.corpus_message.setStyleSheet("color: green; background-color: black")
            self.corpus_message.setText(
                "Corpus files loaded:\n" + "\n".join(list(self.corpus_text.values())[:10]) + "...")

            if self.corpus_files and self.missing_annotations:
                self.finish_button.setEnabled(True)

    def load_missing_annotation_info(self):
        dir = self.mem.lfp.get("missing_annotation_dir") or ""
        self.missing_annotations = QFileDialog.getOpenFileName(
            self, "Select Missing Annotation Info CSV", dir, "CSV Files (*.csv)"
        )[0]

        if self.missing_annotations:
            self.mem.lfp["missing_annotation_dir"] = self.missing_annotations.rsplit("/", 1)[0]

            # read annotation info file
            try:
                self.missing_annotations_csv = load_csv2pandas(self.missing_annotations, encoding=self.encoding,
                                                               sep=self.separator)

            except Exception as e:
                err_msg = f"Error loading missing annotation file ({self.missing_annotations}):\n{e}\n Please try again"
                self.corpus_message.setText(err_msg)
                # change color to red
                self.corpus_message.setStyleSheet("color: red; background-color: black")
                return

        self.message.setText("Please upload corpus and annotation:\n"
                             "- Corpus file loaded:\n\t--" +
                             "\n\t--".join(self.corpus_files) +
                             "\n- Annotation file loaded:\n\t--" + self.annotation_info
                             + "\n- Missing annotation file loaded:\n\t--" + self.missing_annotations)

        if self.corpus_files and self.annotation_info:
            self.finish_button.setEnabled(True)

    def finish(self):
        if self.corpus_text and self.annotation_info and self.missing_annotations:
            self.has_finished = True
            # close window
            self.close()
