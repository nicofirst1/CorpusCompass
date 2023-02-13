import copy
import re
from collections import OrderedDict, Counter
from typing import Dict, Any

import pandas as pd
from PySide6 import QtWidgets, QtGui

from annotation_fixer.common import Memory, GeneralWindow, corpus_dict2text, find_annotation_regex, \
    find_annotation_context, remove_independent_vars
from annotation_fixer.windows.Settings import Settings


class AnnotationFixer(GeneralWindow):
    def __init__(self, mem: Memory, postprocess_data: Dict[str, Any]):

        self.corpus_dict = OrderedDict(postprocess_data["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)
        self.annotation_info_df = postprocess_data["annotation_info"]
        self.missing_annotations_df = postprocess_data["not_annotated_log"]
        self.dataset_df = postprocess_data["dataset"]
        self.binary_dataset_df = postprocess_data["binary_dataset"]

        self.independent_variables = postprocess_data["independent_variables"]
        self.dependent_variables = postprocess_data["dependent_variables"]

        self.dependent_variables = remove_independent_vars(self.dependent_variables, self.independent_variables)

        self.list_to_fix = []
        self.queue = []
        self.queue_index = 0
        self.general_index = 0
        self.low_reps = None
        self.current_match = None

        super().__init__(mem)

    def create_widgets(self):
        self.annotation_regex = self.mem.settings["annotation_regex"]
        self.annotation_regex = re.compile(self.annotation_regex)

        # create the central text area
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        self.text_area.setReadOnly(False)
        self.text_area.textChanged.connect(self.on_text_changed)

        # create the dropdown menu
        self.dropdown = QtWidgets.QComboBox(self)
        self.dropdown.addItem("Use Annotation Info")
        self.dropdown.addItem("Use Missing Annotations")

        # add logic to the dropdown menu
        self.dropdown.currentIndexChanged.connect(self.update_list_to_fix)

        # create the buttons
        self.prev_button = QtWidgets.QPushButton("Prev", self)
        self.prev_button.clicked.connect(self.go_to_prev)
        self.next_button = QtWidgets.QPushButton("Next", self)
        self.next_button.clicked.connect(self.go_to_next)
        self.annotate_button = QtWidgets.QPushButton("", self)
        self.annotate_button.clicked.connect(self.annotation_rule)
        self.ignore_button = QtWidgets.QPushButton("Ignore", self)
        self.ignore_button.clicked.connect(self.ignore)
        self.ignore_all_button = QtWidgets.QPushButton("Ignore All", self)
        self.ignore_all_button.clicked.connect(self.ignore_all)
        self.annotate_all_button = QtWidgets.QPushButton("", self)
        self.annotate_all_button.clicked.connect(self.ignore_all)
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_corpus_dict)

        self.settings_button = QtWidgets.QPushButton("Settings", self)
        self.settings_button.clicked.connect(self.open_settings)

        # set annotation button based on the dropdown menu
        if self.dropdown.currentIndex() == 0:
            self.annotate_button.setText("Deannotate")
            self.annotate_all_button.setText("Deannotate All")
        else:
            self.annotate_button.setText("Annotate")
            self.annotate_all_button.setText("Annotate All")

        # start with ignore and deannotate disabled
        self.annotate_button.setEnabled(False)
        self.ignore_button.setEnabled(False)
        self.ignore_all_button.setEnabled(False)
        self.annotate_all_button.setEnabled(False)

        # create the info text area
        self.info_text = QtWidgets.QLabel("Info", self)
        self.info_text_scroll = QtWidgets.QScrollArea(self)
        self.info_text_scroll.setWidget(self.info_text)
        self.info_text_scroll.setWidgetResizable(True)
        # set size policy to not be more than 20% of the window
        self.info_text_scroll.setMaximumWidth(self.width() * 0.25)
        self.info_text_scroll.setMinimumHeight(self.height() * 0.5)

        # set the dropdown menu to the settings
        if self.mem.settings["data_source"] == "info":
            self.dropdown.setCurrentIndex(0)
        else:
            self.dropdown.setCurrentIndex(1)

        # layout
        layout = QtWidgets.QHBoxLayout()
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.dropdown)

        prev_next_layout = QtWidgets.QHBoxLayout()
        prev_next_layout.addWidget(self.prev_button)
        prev_next_layout.addWidget(self.next_button)
        right_layout.addLayout(prev_next_layout)

        ignore_deannotate_layout = QtWidgets.QHBoxLayout()
        ignore_deannotate_layout.addWidget(self.annotate_button)
        ignore_deannotate_layout.addWidget(self.ignore_button)

        ignore_deannotate_all_layout = QtWidgets.QHBoxLayout()
        ignore_deannotate_all_layout.addWidget(self.annotate_all_button)
        ignore_deannotate_all_layout.addWidget(self.ignore_all_button)

        quatro_layout = QtWidgets.QVBoxLayout()
        quatro_layout.addLayout(ignore_deannotate_layout)
        quatro_layout.addLayout(ignore_deannotate_all_layout)
        right_layout.addLayout(quatro_layout)

        save_settings_layout = QtWidgets.QHBoxLayout()
        save_settings_layout.addWidget(self.save_button)
        save_settings_layout.addWidget(self.settings_button)
        right_layout.addLayout(save_settings_layout)

        layout.addWidget(self.info_text_scroll)
        layout.addWidget(self.text_area)
        layout.addLayout(right_layout)
        self.setLayout(layout)

        self.update_list_to_fix()

    def open_settings(self):
        self.settings_window = Settings(self.mem)
        self.settings_window.show()
        self.settings_window.settingsChanged.connect(self.set_style)

    def on_text_changed(self):
        self.save_button.setEnabled(True)

    def update_list_to_fix(self):
        # get checked checkboxes

        index = self.dropdown.currentIndex()
        if index == 0:
            # save settings
            self.mem.settings["data_source"] = "info"
            min_reps = self.mem.settings['minimum_repetitions']
            # get the rows where 'annotated' is less than the minimum repetition
            low_reps = self.annotation_info_df[self.annotation_info_df['annotated'] <= min_reps]
            self.list_to_fix = low_reps

            # change the text of the deannotate button
            self.annotate_button.setText("Deannotate")
            self.annotate_all_button.setText("Deannotate All")

        else:
            # save settings
            self.mem.settings["data_source"] = "missing"
            self.list_to_fix = self.missing_annotations_df
            # change the text of the deannotate button
            self.annotate_button.setText("Annotate")
            self.annotate_all_button.setText("Annotate All")

        self.queue = []
        self.queue_index = 0
        self.general_index = 0

        if len(self.list_to_fix) == 0:
            self.change_button_status(False)
            self.next_button.setEnabled(False)
            self.prev_button.setEnabled(False)
            self.info_text.setText("No more annotations to fix")
        else:
            self.change_button_status(True)
            self.next_button.setEnabled(True)
            self.prev_button.setEnabled(True)
            self.highlight_current_word()

    def ignore_all(self):
        row = self.current_match["row"]

        try:
            self.annotation_info_df = self.annotation_info_df.drop(row.name)
            print(f"Dropped row: {row.name}")
        except KeyError:
            print(f"Row not found: {row.name}")
            pass

        self.queue = []
        self.queue_index = 0

        self.ignore_all_button.setEnabled(False)

    def ignore(self):

        row = self.current_match["row"]

        # drop the row from the dataframe based on index
        if len(self.queue) == 0:
            try:
                self.annotation_info_df = self.annotation_info_df.drop(row.name)
                print(f"Dropped row: {row.name}")
            except KeyError:
                print(f"Row not found: {row.name}")
                pass
            if self.queue_index > 0:
                self.queue_index = 0
        else:
            self.queue.pop(self.queue_index % len(self.queue))

        self.change_button_status(False)

    def annotation_rule(self):

        # get the current highlighted word based on the cursor position
        path = self.current_match["path"]
        match = self.current_match["match"]
        row = self.current_match["row"]

        def replaceincorpus(replacement, original):
            """
            Replace the current word in the corpus with the replacement
            """
            c = self.corpus_dict[path]
            n_gram = (-20, 20)
            n_gram = (n_gram[0] + match.start, n_gram[1] + match.end)
            n_gram = (max(0, n_gram[0]), min(len(c), n_gram[1]))

            # get the substring of the current word
            sub_string = c[n_gram[0]:n_gram[1]]

            # replace match
            sub_string = sub_string.replace(original, replacement)

            # update c
            c = c[:n_gram[0]] + sub_string + c[n_gram[1]:]
            self.corpus_dict[path] = c

        def annotate():
            # get the row in data_df that corresponds to the current word
            data = self.dataset_df.loc[row.name]
            suggestion = self.current_match["suggest_annotation"]

            annotation = f" [${'.'.join(suggestion)}.{match.token}] "
            replaceincorpus(annotation, match.token)

        def deannotate():
            """
            De-annotate the current word
            """
            annotation = match.match.group()
            not_annotated_w = annotation.split(".")[-1].split("]")[0]
            not_annotated_w = f" {not_annotated_w} "

            replaceincorpus(not_annotated_w, annotation)

        if self.dropdown.currentIndex() == 0:
            deannotate()
        else:
            annotate()

        # update the annotation info dropping the row
        if len(self.queue) == 0:
            try:
                self.annotation_info_df = self.annotation_info_df.drop(row.name)
                print(f"Dropped row: {row.name}")
            except KeyError:
                print(f"Row not found: {row.name}")
                pass

            if self.queue_index > 0:
                self.queue_index = 0

        # update the text area
        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        start = match.fc_start
        end = match.fc_end
        self.text_cursor.setPosition(end)
        self.text_cursor.setPosition(start, QtGui.QTextCursor.KeepAnchor)

        self.text_area.setTextCursor(self.text_cursor)
        # move the scroll bar
        self.text_area.ensureCursorVisible()
        self.change_button_status(False)
        self.queue = []
        self.queue_index = 0
        self.index -= 1

    def fill_notes(self, row: pd.Series) -> str:
        """
        Fill the notes with the current word
        """
        note = ""
        if self.dropdown.currentIndex() == 0:
            for col in row.index:
                note += f"-{col}: {row[col]}\n"
        else:
            token = row['token']
            cols = list(row.index)
            cols = [x for x in cols if "context" in x]
            note += f"--token: {token}\n"
            note += f"-- # of founds: {len(cols)}\n"

            # find in dataset_df the row where the token is the same
            # and get the context
            matches = self.dataset_df[self.dataset_df['token'] == token]

            # drop columns that are all nan
            matches = matches.dropna(axis=1, how='all')

            # drop columns called token, context
            matches = matches.drop(columns=['token', 'context', 'Unnamed: 0'], errors='ignore')

            # for all the columns left, get a counter of the values
            counters = {}
            for col in matches.columns:
                counters[col] = Counter(matches[col])

            total = len(matches[col])
            # present the information in a nice way
            note += f"-- # of annotated instances: {total}\n"
            for col in counters:
                note += f"--- {col}:\n"
                for value in counters[col]:
                    note += f"---- {value}: {counters[col][value]}\n"

            dependent_var = {k: v for k, v in counters.items() if k in self.dependent_variables.keys()}

            # convert counters values to percentages and keep only the highest if above threshold
            trh = self.mem.settings['auto_annotation_thr']
            dependent_var_copy = copy.deepcopy(dependent_var)

            for k in dependent_var_copy:
                for v in dependent_var_copy[k]:
                    # if v is nan
                    if v != v:
                        del dependent_var[k][v]
                        continue
                    perc = dependent_var_copy[k][v] / total
                    if perc < trh:
                        del dependent_var[k][v]

                # remove the key if empty
                if len(dependent_var[k]) == 0:
                    del dependent_var[k]

            dependent_var = list(dependent_var.values())
            dependent_var = [x.keys() for x in dependent_var]
            dependent_var = [list(x)[0] for x in dependent_var]

            self.current_match['suggest_annotation'] = dependent_var

            # if there are dependent variables, add them to the note as suggestions
            if len(dependent_var) > 0:
                note += f"-- Suggestions: {'.'.join(dependent_var)}\n"
            else:
                note += f"-- Suggestions: Data is too variable for suggestion\n"
                self.annotate_button.setEnabled(False)

        if len(self.queue) > 0:
            note += f"-- {len(self.queue)} words left in queue\n"

        return note

    def highlight_current_word(self) -> bool:

        self.annotate_button.setEnabled(True)

        if len(self.queue) > 0:
            found = self.queue[self.queue_index % len(self.queue)]
            found, row = found
        else:

            if len(self.list_to_fix) == 0:
                note = "No more words to annotate"
                self.info_text.setText(note)
                return False

            row = self.list_to_fix.iloc[self.general_index]
            row = row[row != 0]
            # drop nan
            row = row.dropna()

            word = row['token']

            if self.dropdown.currentIndex() == 0:
                found = find_annotation_regex(self.corpus_dict, word, self.annotation_regex,
                                              use_strict_rule=self.mem.settings['use_strict_rule'])
            else:
                cols = list(row.index)
                cols = [x for x in cols if "context" in x]

                found = find_annotation_context(self.corpus_dict, word, list(row[cols]))

            if len(found) == 0:
                print(f"Could not find {word} in corpus text")
                return False
            elif len(found) > 1:
                print(f"Found more than one instance of {word} in corpus text, adding to queue")
                self.queue += [(x, row) for x in found[1:]]
                self.queue_index = 0
                found = found[0]

                self.ignore_all_button.setEnabled(True)
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

        curr_idx = self.general_index + len(self.queue)
        max_idx = len(self.list_to_fix) + len(self.queue)
        note = f"General :{curr_idx} of {max_idx} " \
               f"rows left ({curr_idx / max_idx * 100:.2f}%)\n" \
               f"-File: {file}\n\n" \
               f"Specific:\n"

        # fill notes
        note += self.fill_notes(row)

        # set note
        self.info_text.setText(note)
        return True

    def save_corpus_dict(self):

        # save the corpus dict
        for path, text in self.corpus_dict.items():
            # use encoding in mem
            with open(path, "w", encoding=self.mem.settings['encoding']) as f:
                f.write(text)

        # save the annotation info

        self.annotation_info_df.to_csv(self.mem.postprocess_paths['annotation_info'], index=False,
                                       sep=self.mem.settings['separator'])
        self.missing_annotations_df.to_csv(self.mem.postprocess_paths['not_annotated_log'], index=False,
                                           sep=self.mem.settings['separator'])

        # display message
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Corpus saved")
        msg.setWindowTitle("Corpus saved")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        # disable the save button
        self.save_button.setEnabled(False)

    def change_button_status(self, prev_next: bool):

        if prev_next:

            self.annotate_button.setEnabled(True)
            self.ignore_button.setEnabled(True)
            if self.current_match is not None and \
                    "suggest_annotation" in self.current_match.keys() and \
                    len(self.current_match['suggest_annotation']) == 0:
                self.annotate_button.setEnabled(False)

        else:
            self.annotate_button.setEnabled(False)
            self.ignore_button.setEnabled(False)

    def go_to_prev(self):

        while self.index > 0:
            self.index -= 1

            if self.highlight_current_word():
                break
        self.change_button_status(True)

    def go_to_next(self):
        while self.index < len(self.list_to_fix) - 1:
            self.index += 1
            if self.highlight_current_word():
                break

        self.change_button_status(True)

    @property
    def index(self):
        if len(self.queue) > 0:
            return self.queue_index
        else:
            return self.general_index

    @index.setter
    def index(self, value):
        if len(self.queue) > 0:
            self.queue_index = value
        else:
            self.general_index = value
