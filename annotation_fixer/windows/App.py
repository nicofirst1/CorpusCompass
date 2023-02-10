from PySide6 import QtWidgets, QtGui

from annotation_fixer.common import Memory, GeneralWindow


class AnnotationFixer(GeneralWindow):
    def __init__(self, mem: Memory, corpus_text, annotation_info_csv, missing_annotations_csv):
        super().__init__(mem)

        self.corpus_text = corpus_text
        self.annotation_info_csv = annotation_info_csv
        self.missing_annotations_csv = missing_annotations_csv
        self.list_to_fix = []
        self.current_index = 0

        # create the central text area
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setText(self.corpus_text)
        self.text_area.setReadOnly(False)

        # create the checkboxes
        self.annotation_info_checkbox = QtWidgets.QCheckBox("Use Annotation Info", self)
        self.missing_annotations_checkbox = QtWidgets.QCheckBox("Use Missing Annotations", self)

        # create the buttons
        self.prev_button = QtWidgets.QPushButton("Prev", self)
        self.prev_button.clicked.connect(self.go_to_prev)
        self.next_button = QtWidgets.QPushButton("Next", self)
        self.next_button.clicked.connect(self.go_to_next)
        self.deannotate_button = QtWidgets.QPushButton("De-annotate", self)
        self.deannotate_button.clicked.connect(self.deannotate)

        # create the info text area
        self.info_text = QtWidgets.QLabel("Info", self)

        # layout
        layout = QtWidgets.QHBoxLayout()
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.annotation_info_checkbox)
        right_layout.addWidget(self.missing_annotations_checkbox)
        right_layout.addWidget(self.prev_button)
        right_layout.addWidget(self.next_button)
        right_layout.addWidget(self.deannotate_button)
        layout.addWidget(self.text_area)
        layout.addLayout(right_layout)
        layout.addWidget(self.info_text)
        self.setLayout(layout)

    def go_to_prev(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.highlight_current()

    def go_to_next(self):
        if self.current_index < len(self.list_to_fix) - 1:
            self.current_index += 1
            self.highlight_current()

    def deannotate(self):
        # replace the current word with "xxx"
        word = self.list_to_fix[self.current_index]
        start = self.corpus_text.index(word)
        end = start
        len(word)
        self.corpus_text = self.corpus_text[:start] + "xxx" + self.corpus_text[end:]
        self.text_area.setPlainText(self.corpus_text)
        self.current_index += 1
        if self.current_index >= len(self.list_to_fix):
            self.current_index = 0
        self.highlight_current_word()

    def highlight_current_word(self):
        word = self.list_to_fix[self.current_index]
        start = self.corpus_text.index(word)
        end = start + len(word)
        self.text_cursor = self.text_area.textCursor()
        self.text_cursor.setPosition(start)
        self.text_cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
        self.text_cursor.select(QtGui.QTextCursor.WordUnderCursor)
        self.text_area.setTextCursor(self.text_cursor)

    def next_word(self):
        self.current_index += 1
        if self.current_index >= len(self.list_to_fix):
            self.current_index = 0
        self.highlight_current_word()

    def prev_word(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.list_to_fix) - 1
        self.highlight_current_word()

    def init_ui(self):
        self.setWindowTitle("Annotation Fixer")
        self.setGeometry(100, 100, 800, 600)
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.text_area = QtWidgets.QPlainTextEdit(self.corpus_text)
        self.grid.addWidget(self.text_area, 0, 1, 6, 3)
        self.text_area.setReadOnly(False)

        self.checkbox_annotation_info = QtWidgets.QCheckBox("Annotation Info", self)
        self.grid.addWidget(self.checkbox_annotation_info, 0, 0, 1, 1)
        self.checkbox_missing_annotations = QtWidgets.QCheckBox("Missing Annotations", self)
        self.grid.addWidget(self.checkbox_missing_annotations, 1, 0, 1, 1)

        self.prev_button = QtWidgets.QPushButton("Prev", self)
        self.grid.addWidget(self.prev_button, 2, 0, 1, 1)
        self.prev_button.clicked.connect(self.prev_word)

        self.next_button = QtWidgets.QPushButton("Next", self)
