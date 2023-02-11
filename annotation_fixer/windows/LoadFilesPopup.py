import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QComboBox, QScrollArea

from annotation_fixer.common import Memory, GeneralWindow, open_postprocess


class LoadFilesPopup(GeneralWindow):
    def __init__(self, mem: Memory):
        super().__init__(mem)

        self.corpus_files = None
        self.corpus_text = {}
        self.annotation_info = None
        self.annotation_info_csv = {}
        self.message = None

        self.encodings = ["UTF-8", "UTF-16"]
        enc_idx = self.mem.lfp.get("encoding") or 0
        self.encoding = self.encodings[enc_idx]

        self.separator = self.mem.lfp.get("separator") or ";"

        self.setWindowTitle("Load Files")

        self.create_widgets()
        self.has_finished = False

    def create_widgets(self):
        self.message = QtWidgets.QLabel("Please upload corpus and annotation:\n"
                                        "- Corpus not uploaded\n"
                                        "- Post-process files not uploaded\n")
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

        self.postprocess_button = QtWidgets.QPushButton("Load Pos-Processed data")
        self.postprocess_button.clicked.connect(self.load_postporcess_files)

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
        layout.addWidget(self.postprocess_button)
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

            msg = "Please upload corpus and annotation:\n"
            msg += "- Corpus file loaded:\n\t--" + "\n\t--".join(self.corpus_files) + "\n"

            if self.annotation_info:
                msg += "- Post-process files loaded:\n\t--" + "\n\t--".join(self.annotation_info) + "\n"
            else:
                msg += "- Post-process files not uploaded\n"
            self.message.setText(msg)

            # change color to green
            self.corpus_message.setStyleSheet("color: green; background-color: black")
            self.corpus_message.setText(
                "Corpus files loaded:\n" + "\n".join(list(self.corpus_text.values())[:10]) + "...")

            if self.annotation_info_csv:
                self.finish_button.setEnabled(True)

    def load_postporcess_files(self):
        dir = self.mem.lfp.get("postprocess_dir") or ""
        dir = QFileDialog.getExistingDirectory(
            self, "Select Annotation Folder", dir
        )

        if not dir:
            err_msg = f"Error loading post-process files:\nPlease select a folder and try again"
            self.corpus_message.setText(err_msg)
            # change color to red
            self.corpus_message.setStyleSheet("color: red; background-color: black")

            return

        # save dir
        self.mem.lfp["postprocess_dir"] = dir

        # list all the files in the folder
        files = [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

        # check that all files in self.mem.postprocess_names are in the folder
        found = [f for f in files if os.path.basename(f) in self.mem.postprocess_names]

        if len(found) != len(self.mem.postprocess_names):
            # get missing
            missing = [f for f in self.mem.postprocess_names if f not in [os.path.basename(x) for x in files]]
            err_msg = f"Error loading post-process files:\nCould not find the following files:\n\t--" + "\n\t--".join(
                missing) + "\n Please try again"
            self.corpus_message.setText(err_msg)
            # change color to red
            self.corpus_message.setStyleSheet("color: red; background-color: black")
            return

        postprocess_files, erro_msg = open_postprocess(found, self.encoding, self.separator)

        if erro_msg:
            self.corpus_message.setText(erro_msg)
            # change color to red
            self.corpus_message.setStyleSheet("color: red; background-color: black")
            return

        self.annotation_info_csv = postprocess_files
        self.annotation_info = found

        msg = "Please upload corpus and annotation:\n"

        if self.corpus_files:
            msg += "- Corpus file loaded:\n\t--" + "\n\t--".join(self.corpus_files) + "\n"
        else:
            msg += "- Corpus file not uploaded\n"
        msg += "- Post-process files loaded:\n\t--" + "\n\t--".join(found)
        self.message.setText(msg)

        # change color to green
        self.corpus_message.setStyleSheet("color: green; background-color: black")

        if self.corpus_files:
            self.finish_button.setEnabled(True)

    def finish(self):
        if self.corpus_text and self.annotation_info_csv:
            self.has_finished = True
            # close window
            self.close()
