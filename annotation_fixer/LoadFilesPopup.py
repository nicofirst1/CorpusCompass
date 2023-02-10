from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QComboBox, QScrollArea

from annotation_fixer.Memory import Memory


class LoadFilesPopup(QtWidgets.QWidget):
    def __init__(self, mem: Memory):
        super().__init__()

        self.mem = mem
        self.corpus_files = None
        self.corpus_text = ""
        self.annotation_info = None
        self.message = None
        self.encodings = ["UTF-8", "UTF-16"]
        enc_idx = self.mem.lfp.get("encoding") or 0
        self.encoding = self.encodings[enc_idx]
        self.setFixedSize(500, 500)

        self.setWindowTitle("Load Files")

        self.create_widgets()

    def create_widgets(self):
        self.message = QtWidgets.QLabel("Please upload corpus and annotation:\n"
                                        "- Corpus not uploaded\n"
                                        "- Annotation not uploaded")
        self.message.setStyleSheet("color: white; background-color: black")

        self.message_scroll = QScrollArea()
        self.message_scroll.setWidget(self.message)
        self.message_scroll.setWidgetResizable(True)

        self.corpus_message = QtWidgets.QLabel("")
        self.corpus_message.setStyleSheet("color: white; background-color: black")

        self.corpus_message_scroll = QScrollArea()
        self.corpus_message_scroll.setWidget(self.corpus_message)
        self.corpus_message_scroll.setWidgetResizable(True)

        self.corpus_button = QtWidgets.QPushButton("Load Corpus Files")
        self.corpus_button.clicked.connect(self.load_corpus)

        self.annotation_info_button = QtWidgets.QPushButton("Load Annotation Info")
        self.annotation_info_button.clicked.connect(self.load_annotation_info)

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
        layout.addWidget(self.message_scroll)
        layout.addWidget(self.corpus_message_scroll)
        layout.addWidget(self.finish_button)

        self.setLayout(layout)

    def handle_encoding_change(self, index):
        self.encoding = self.encodings[index]
        self.mem.lfp["encoding"] = index

    def load_corpus(self):
        dir = self.mem.lfp.get("corpus_dir") or ""
        self.corpus_files = QFileDialog.getOpenFileNames(
            self, "Select Corpus Files", dir, "Text Files (*.txt);;All Files (*.*)"
        )[0]

        if self.corpus_files:
            self.mem.lfp["corpus_dir"] = self.corpus_files[0].rsplit("/", 1)[0]

            for p in self.corpus_files:
                try:
                    with open(p, "rb") as f:
                        self.corpus_text += f.read().decode(self.encoding) + "\n"
                except Exception as e:
                    err_msg = f"Error loading corpus files ({p}):\n{e}\n Please try again"
                    self.corpus_message.setText(err_msg)
                    # change color to red
                    self.corpus_message.setStyleSheet("color: red; background-color: black")

                    return

            self.message.setText("Please upload corpus and annotation:\n"
                                 "- Corpus file loaded:\n\t--" +
                                 "\n\t--".join(self.corpus_files) +
                                 "\n- Annotation not uploaded")
            # change color to green
            self.corpus_message.setStyleSheet("color: green; background-color: black")
            self.corpus_message.setText(
                "Corpus files loaded:\n" + "\n".join(self.corpus_text.split("\n")[:10] + ["..."]))

            if self.annotation_info:
                self.finish_button.setEnabled(True)

    def load_annotation_info(self):
        dir = self.mem.lfp.get("annotation_dir") or ""
        self.annotation_info = QFileDialog.getOpenFileName(
            self, "Select Annotation Info CSV", dir, "CSV Files (*.csv);;All Files (*.*)"
        )[0]

        if self.annotation_info:
            self.mem.lfp["annotation_dir"] = self.annotation_info.rsplit("/", 1)[0]

            self.message.setText("Please upload corpus and annotation:\n"
                                 "- Corpus file loaded:\n\t--" +
                                 "\n\t--".join(self.corpus_files) +
                                 "\n- Annotation file loaded:" + self.annotation_info)
            # change color to green
            self.corpus_message.setStyleSheet("color: green; background-color: black")
            self.corpus_message.setText(
                "Corpus files loaded:\n" + "\n".join(self.corpus_text.split("\n")[:10] + ["..."]))

            if self.corpus_files:
                self.finish_button.setEnabled(True)

    def finish(self):
        if self.corpus_text and self.annotation_info:
            # close window
            self.close()
