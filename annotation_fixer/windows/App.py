import re
from collections import OrderedDict
from typing import Dict

import pandas as pd
from PySide6 import QtWidgets, QtGui

from annotation_fixer.common import Memory, GeneralWindow, corpus_dict2text, find_annotation


class AnnotationFixer(GeneralWindow):
    def __init__(self, mem: Memory, corpus_dict: Dict[str, str], annotation_info_df: pd.DataFrame,
                 missing_annotations_df: pd.DataFrame):
        super().__init__(mem)

        self.corpus_dict = OrderedDict(corpus_dict)
        self.corpus_text = corpus_dict2text(corpus_dict)
        self.annotation_info_df = annotation_info_df
        self.missing_annotations_df = missing_annotations_df
        self.list_to_fix = []
        self.queue = []
        self.current_index = 0
        self.low_reps = None
        self.current_match = None

        self.annotation_regex = self.mem.settings["annotation_regex"]
        self.annotation_regex = re.compile(self.annotation_regex)

        # create the central text area
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        self.text_area.setReadOnly(False)

        # create the checkboxes
        self.annotation_info_checkbox = QtWidgets.QCheckBox("Use Annotation Info", self)
        self.missing_annotations_checkbox = QtWidgets.QCheckBox("Use Missing Annotations", self)
        # add logic to the checkboxes
        self.annotation_info_checkbox.stateChanged.connect(self.update_list_to_fix)
        self.missing_annotations_checkbox.stateChanged.connect(self.update_list_to_fix)

        # create the buttons
        self.prev_button = QtWidgets.QPushButton("Prev", self)
        self.prev_button.clicked.connect(self.go_to_prev)
        self.next_button = QtWidgets.QPushButton("Next", self)
        self.next_button.clicked.connect(self.go_to_next)
        self.deannotate_button = QtWidgets.QPushButton("De-annotate", self)
        self.deannotate_button.clicked.connect(self.deannotate)
        self.ignore_button = QtWidgets.QPushButton("Ignore", self)
        self.ignore_button.clicked.connect(self.ignore)
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_corpus_dict)

        # create the info text area
        self.info_text = QtWidgets.QLabel("Info", self)
        self.info_text_scroll = QtWidgets.QScrollArea(self)
        self.info_text_scroll.setWidget(self.info_text)
        self.info_text_scroll.setWidgetResizable(True)
        # set size policy to not be more than 20% of the window
        self.info_text_scroll.setMaximumWidth(self.width() * 0.2)
        self.info_text_scroll.setMinimumHeight(self.height() * 0.5)

        # layout
        layout = QtWidgets.QHBoxLayout()
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.annotation_info_checkbox)
        right_layout.addWidget(self.missing_annotations_checkbox)
        right_layout.addWidget(self.prev_button)
        right_layout.addWidget(self.next_button)
        right_layout.addWidget(self.deannotate_button)
        right_layout.addWidget(self.save_button)

        layout.addWidget(self.info_text_scroll)
        layout.addWidget(self.text_area)
        layout.addLayout(right_layout)
        self.setLayout(layout)

        self.update_list_to_fix()

    def update_list_to_fix(self):
        # get checked checkboxes
        checked = []
        if self.annotation_info_checkbox.isChecked():
            checked.append("annotation_info")
        if self.missing_annotations_checkbox.isChecked():
            checked.append("missing_annotations")

        min_reps = self.mem.settings['minimum_repetitions']
        # get the rows where 'annotated' is less than the minimum repetition
        low_reps = self.annotation_info_df[self.annotation_info_df['annotated'] <= min_reps]
        self.list_to_fix = low_reps

    def go_to_prev(self):
        while self.current_index > 0:
            self.current_index -= 1
            if self.highlight_current_word():
                break

    def go_to_next(self):
        while self.current_index < len(self.list_to_fix) - 1:
            self.current_index += 1
            if self.highlight_current_word():
                break

    def ignore(self):

        row = self.current_match["row"]

        # drop the row from the dataframe
        self.annotation_info_df = self.annotation_info_df.drop(row.name)

    def deannotate(self):
        """
        De-annotate the current word
        """

        # get the current highlighted word based on the cursor position
        path = self.current_match["path"]
        match = self.current_match["match"]
        row = self.current_match["row"]

        c = self.corpus_dict[path]
        n_gram = (-20, 20)
        n_gram = (n_gram[0] + match.start, n_gram[1] + match.end)
        n_gram = (max(0, n_gram[0]), min(len(c), n_gram[1]))

        # get the substring of the current word
        sub_string = c[n_gram[0]:n_gram[1]]

        # replace match
        annotation = match.match.group(0)
        not_annotated_w = annotation.split(".")[-1].split("]")[0]
        not_annotated_w = f" {not_annotated_w} "
        sub_string = sub_string.replace(annotation, not_annotated_w)

        # update c
        c = c[:n_gram[0]] + sub_string + c[n_gram[1]:]
        self.corpus_dict[path] = c

        # update the annotation info dropping the row
        self.annotation_info_df = self.annotation_info_df.drop(row.name)

        # update the text area
        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        start = match.fc_start
        end = match.fc_end
        self.text_cursor.setPosition(end)
        self.text_cursor.setPosition(start, QtGui.QTextCursor.KeepAnchor)

        self.text_area.setTextCursor(self.text_cursor)

        # move the scroll bar
        self.text_area.ensureCursorVisible()

    def highlight_current_word(self) -> bool:

        # todo: add queue support
        if len(self.queue) > 0:
            found = self.queue.pop(0)
            found, row = found
        else:
            row = self.list_to_fix.iloc[self.current_index]
            row = row[row != 0]

            word = row['token']
            found = find_annotation(self.corpus_dict, word, self.annotation_regex, use_strict_rule=False)

            if len(found) == 0:
                print(f"Could not find {word} in corpus text")
                return False
            elif len(found) > 1:
                print(f"Found more than one instance of {word} in corpus text, adding to queue")
                self.queue += [(x, row) for x in found[1:]]
                found = found[0]
            else:
                found = found[0]

        file = found[0]
        match = found[1]
        self.current_match = dict(path=found[0], match=found[1], row=row)

        self.text_cursor = self.text_area.textCursor()
        start = match.fc_start
        end = match.fc_end
        self.text_cursor.setPosition(end)
        self.text_cursor.setPosition(start, QtGui.QTextCursor.KeepAnchor)

        self.text_area.setTextCursor(self.text_cursor)

        # move the scroll bar
        self.text_area.ensureCursorVisible()

        curr_idx = self.current_index + len(self.queue)
        max_idx = len(self.list_to_fix) + len(self.queue)
        note = f"General :{curr_idx} of {max_idx} " \
               f"rows left ({curr_idx / max_idx * 100:.2f}%)\n" \
               f"Specific:\n"

        for col in row.index:
            note += f"\t-{col}: {row[col]}\n"

        note += f"\t-File: {file}"

        # set note
        self.info_text.setText(note)
        return True

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

    def save_corpus_dict(self):
        pass
