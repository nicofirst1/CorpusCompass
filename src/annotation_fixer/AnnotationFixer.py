import copy
import re
from collections import OrderedDict, Counter
from typing import Dict, Any

import pandas as pd
from PySide6 import QtWidgets, QtGui, QtCore

from src.annotation_fixer.Find import FindDialog
from src.annotation_fixer.af_utils import (
    corpus_dict2text,
    remove_independent_vars,
    find_annotation_regex,
    find_annotation_context,
)
from src.common import GeneralWindow, Memory, AppLogger
from src.other_windows import Settings


class AnnotationFixer(GeneralWindow):
    def __init__(
        self,
        mem: Memory,
        preloaded_data: Dict[str, Any],
        postprocess_data: Dict[str, Any],
    ):
        self.corpus_dict = OrderedDict(preloaded_data["corpus_text"])
        self.corpus_text = corpus_dict2text(self.corpus_dict)
        self.df_annotation_info = postprocess_data["annotation_info"]
        self.df_missed_annotations = postprocess_data["missed_annotations"]
        self.df_dataset = postprocess_data["dataset"]
        self.df_binary_dataset = postprocess_data["binary_dataset"]

        self.independent_variables = preloaded_data["independent_variables"]
        self.dependent_variables = preloaded_data["dependent_variables"]

        self.dependent_variables = remove_independent_vars(
            self.dependent_variables, self.independent_variables
        )

        self.list_to_fix = []
        self.saved_lists = []
        self.mode_idx = 0

        self.queue = []
        self.queue_index = 0
        self.general_index = 0
        self.low_reps = None
        self.current_match = None

        self.logger = AppLogger(mem, "annotation_fixer.log")
        self.history = History(self)

        super().__init__(mem, "Annotation Fixer")

        self.history.add_buttons(self.undo_button, self.redo_button)
        self.history.save_state()

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

        # set the dropdown menu to the settings
        if self.mem.settings["data_source"] == "info":
            self.dropdown.setCurrentIndex(0)
            self.mode_idx = 0
        else:
            self.dropdown.setCurrentIndex(1)
            self.mode_idx = 1

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
        self.annotate_all_button.clicked.connect(self.annotate_all)
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_corpus_dict)

        self.settings_button = QtWidgets.QPushButton("Settings", self)
        self.settings_button.clicked.connect(self.open_settings)

        self.undo_button = QtWidgets.QPushButton("Undo", self)
        self.undo_button.clicked.connect(self.history.undo)
        self.redo_button = QtWidgets.QPushButton("Redo", self)
        self.redo_button.clicked.connect(self.history.redo)

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

        # layout
        layout = QtWidgets.QHBoxLayout()
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.dropdown)

        undo_redo_layout = QtWidgets.QHBoxLayout()
        undo_redo_layout.addWidget(self.undo_button)
        undo_redo_layout.addWidget(self.redo_button)
        right_layout.addLayout(undo_redo_layout)

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

        self.init_list_to_fix()

        # Override keyPressEvent to handle key events

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        modifiers = event.modifiers()
        key = event.key()

        # Handle Command key for macOS
        if modifiers & QtCore.Qt.MetaModifier or modifiers & QtCore.Qt.ControlModifier:
            if key == QtCore.Qt.Key_Z:
                self.history.undo()
            elif key == QtCore.Qt.Key_Z and modifiers & QtCore.Qt.ShiftModifier:
                self.history.redo()
            elif event.key() == QtCore.Qt.Key_F:
                self.show_find_dialog()
            # Handle Control key for other platforms

        else:
            super().keyPressEvent(event)

    def open_settings(self):
        self.settings_window = Settings(self.mem)
        self.settings_window.show()
        self.settings_window.settingsChanged.connect(self.set_style)

    def show_find_dialog(self):
        self.find_dialog = FindDialog(self)
        self.find_dialog.show()

    def on_text_changed(self):
        self.save_button.setEnabled(True)

    def init_list_to_fix(self):
        index = self.dropdown.currentIndex()

        # save settings
        min_reps = self.mem.settings["minimum_repetitions"]
        # get the rows where 'annotated' is less than the minimum repetition
        low_reps = self.df_annotation_info[
            self.df_annotation_info["annotated"] <= min_reps
            ]
        self.saved_lists.append(low_reps)

        # save settings
        self.saved_lists.append(self.df_missed_annotations)

        self.list_to_fix = self.saved_lists[index]

        self.update_list_to_fix()

    def update_list_to_fix(self):
        # get checked checkboxes

        index = self.dropdown.currentIndex()

        self.saved_lists[self.mode_idx] = copy.deepcopy(self.list_to_fix)
        self.list_to_fix = self.saved_lists[index]
        self.mode_idx = index

        if index == 0:
            self.mem.settings["data_source"] = "info"
            # change the text of the deannotate button
            self.annotate_button.setText("Deannotate")
            self.annotate_all_button.setText("Deannotate All")

        else:
            self.mem.settings["data_source"] = "missing"

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
            # self.change_button_status(True)
            self.next_button.setEnabled(True)
            self.prev_button.setEnabled(True)
            self.highlight_current_word()

    def ignore_all(self):
        row = self.current_match["row"]

        self.drop_row(row)

        self.queue = []
        self.queue_index = 0

        self.change_button_status(False)
        self.history.save_state()

    def ignore(self):
        row = self.current_match["row"]
        if len(self.queue) > 0:
            # remove the found from the queue
            self.queue.pop(self.queue_index % len(self.queue))
        # drop the row from the dataframe based on index
        if len(self.queue) == 0:
            self.drop_row(row)
            if self.queue_index > 0:
                self.queue_index = 0

        self.change_button_status(False)
        self.history.save_state()

    def annotate_all(self):
        suggestes = self.current_match.get("suggest_annotation", None)
        for found in reversed(self.queue):
            found, row = found
            self.current_match = dict(
                path=found[0], match=found[1], row=row, suggest_annotation=suggestes
            )

            match = found[1]
            self.annotation_rule(wait_refresh=True)

        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        start = match.fc_start
        end = match.fc_end
        self.text_cursor.setPosition(end)
        self.text_cursor.setPosition(start, QtGui.QTextCursor.KeepAnchor)

        self.text_area.setTextCursor(self.text_cursor)
        # move the scroll bar
        self.text_area.ensureCursorVisible()

        self.queue = []
        self.queue_index = 0
        self.change_button_status(False)
        self.history.save_state()

    def annotation_rule(self, wait_refresh=False):
        # get the current highlighted word based on the cursor position
        path = self.current_match["path"]
        match = self.current_match["match"]
        row = self.current_match["row"]

        def replaceincorpus(replacement, original):
            """
            Replace the current word in the corpus with the replacement
            """
            c = self.corpus_dict[path]
            n_gram = (-10, 10)
            n_gram = (n_gram[0] + match.start, n_gram[1] + match.end)
            n_gram = (max(0, n_gram[0]), min(len(c), n_gram[1]))

            # get the substring of the current word
            sub_string = c[n_gram[0] : n_gram[1]]

            # replace match
            sub_string = sub_string.replace(original, replacement, 1)

            # update c
            c = c[: n_gram[0]] + sub_string + c[n_gram[1] :]
            self.corpus_dict[path] = c

        if self.dropdown.currentIndex() == 0:
            # deannotate
            original = match.match.group()
            replacement = original.split(".")[-1].split("]")[0]
            replacement = f" {replacement} "

            replaceincorpus(replacement, original)
        else:
            # annotate
            suggestion = self.current_match["suggest_annotation"]
            original = match.token

            replacement = f" [${'.'.join(suggestion)}.{original}] "
            replaceincorpus(replacement, original)

        # update the annotation info dropping the row
        if len(self.queue) == 0:
            self.drop_row(row)

            if self.queue_index > 0:
                self.queue_index = 0
        else:
            size_diff = len(replacement) - len(original)
            self.queue.pop(self.queue_index % len(self.queue))
            self.queue_index -= 1

            # update match in queue
            for i in range(len(self.queue)):
                found, row = self.queue[i]
                m = found[1]
                m.start += size_diff
                m.end += size_diff
                m.fc_start += size_diff
                m.fc_end += size_diff
                self.queue[i] = (found, row)

        # update the text area
        if not wait_refresh:
            self.text_area.setText(corpus_dict2text(self.corpus_dict))
            start = match.fc_start
            end = match.fc_end
            self.text_cursor.setPosition(end)
            self.text_cursor.setPosition(start, QtGui.QTextCursor.KeepAnchor)

            self.text_area.setTextCursor(self.text_cursor)
            # move the scroll bar
            self.text_area.ensureCursorVisible()
            self.change_button_status(False)
            self.history.save_state()

        # self.queue = []
        # self.queue_index = 0
        # self.index -= 1

    def drop_row(self, row):
        try:
            self.list_to_fix = self.list_to_fix.drop(row.name)
            self.logger.info(f"Dropped row: {row.name}\n{row}\n")
        except KeyError:
            self.logger.warning(f"Row not found: {row.name}\n{row}\n")
            pass

    def fill_notes(self, row: pd.Series) -> str:
        """
        Fill the notes with the current word
        """
        note = ""
        if self.dropdown.currentIndex() == 0:
            for col in row.index:
                note += f"-{col}: {row[col]}\n"
        else:
            token = row["token"]
            cols = list(row.index)
            cols = [x for x in cols if "context" in x]
            note += f"--token: {token}\n"
            note += f"-- # of founds: {len(cols)}\n"

            # find in dataset_df the row where the token is the same
            # and get the context
            matches = self.df_dataset[self.df_dataset["token"] == token]

            # drop columns that are all nan
            matches = matches.dropna(axis=1, how="all")

            # drop columns called token, context
            matches = matches.drop(
                columns=["token", "context", "Unnamed: 0"], errors="ignore"
            )

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

            dependent_var = {
                k: v
                for k, v in counters.items()
                if k in self.dependent_variables.keys()
            }

            # convert counters values to percentages and keep only the highest if above threshold
            trh = self.mem.settings["auto_annotation_thr"]
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

            # cast to str
            dependent_var = [str(x) for x in dependent_var]

            self.current_match["suggest_annotation"] = dependent_var

            # if there are dependent variables, add them to the note as suggestions
            if len(dependent_var) > 0:
                note += f"-- Suggestions: {'.'.join(dependent_var)}\n"
            else:
                note += f"-- Suggestions: Data is too variable for suggestion\n"
                self.annotate_button.setEnabled(False)

        if len(self.queue) > 0:
            note += f"-- {len(self.queue)} words in queue\n"

        return note

    def highlight_current_word(self) -> bool:
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

            word = row["token"]

            if self.dropdown.currentIndex() == 0:
                found = find_annotation_regex(
                    self.corpus_dict,
                    word,
                    self.annotation_regex,
                    use_strict_rule=self.mem.settings["use_strict_rule"],
                )
            else:
                cols = list(row.index)
                cols = [x for x in cols if "context" in x]

                found = find_annotation_context(self.corpus_dict, word, list(row[cols]))

            if len(found) == 0:
                print(f"Could not find {word} in corpus text")
                return False
            elif len(found) > 1:
                print(
                    f"Found more than one instance of {word} in corpus text, adding to queue"
                )
                self.queue += [(x, row) for x in found]
                self.queue_index = 0
                found = found[0]

                self.ignore_all_button.setEnabled(True)
                self.annotate_all_button.setEnabled(True)
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
        note = (
            f"General :{curr_idx} of {max_idx} "
            f"rows left ({curr_idx / max_idx * 100:.2f}%)\n"
            f"-File: {file}\n\n"
            f"Specific:\n"
        )

        # fill notes
        note += self.fill_notes(row)

        # set note
        self.info_text.setText(note)
        self.change_button_status(True)

        return True

    def save_corpus_dict(self):
        # save the corpus dict
        for path, text in self.corpus_dict.items():
            # use encoding in mem
            with open(path, "w", encoding=self.mem.settings["encoding"]) as f:
                f.write(text)

        # save the annotation info

        self.df_annotation_info.to_csv(
            self.mem.postprocess_paths["annotation_info"],
            index=False,
            sep=self.mem.settings["separator"],
        )
        self.df_missed_annotations.to_csv(
            self.mem.postprocess_paths["missed_annotations"],
            index=False,
            sep=self.mem.settings["separator"],
        )

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
            self.ignore_all_button.setEnabled(True)
            self.annotate_all_button.setEnabled(True)
            if (
                self.current_match is not None
                and "suggest_annotation" in self.current_match.keys()
                and len(self.current_match["suggest_annotation"]) == 0
            ):
                self.annotate_button.setEnabled(False)
                self.annotate_all_button.setEnabled(False)
            if len(self.queue) == 0:
                self.ignore_all_button.setEnabled(False)
                self.annotate_all_button.setEnabled(False)

        else:
            self.annotate_button.setEnabled(False)
            self.ignore_button.setEnabled(False)
            self.ignore_all_button.setEnabled(False)
            self.annotate_all_button.setEnabled(False)

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

    def update_gui(self):
        self.text_area.setText(corpus_dict2text(self.corpus_dict))
        self.highlight_current_word()
        self.change_button_status(True)


class History:
    def __init__(self, ann_fixer: AnnotationFixer):
        self.ann_fixer = ann_fixer
        self.history = []
        self.index = 0

        self.save_attributes = [
            "corpus_dict",
            "df_annotation_info",
            "df_missed_annotations",
            "list_to_fix",
            "general_index",
            "queue",
            "queue_index",
        ]

    def add_buttons(
        self, undo_button: QtWidgets.QPushButton, redo_button: QtWidgets.QPushButton
    ):
        self.undo_button = undo_button
        self.redo_button = redo_button

    def save_state(self):
        state = {}
        for attr in self.save_attributes:
            state[attr] = copy.deepcopy(getattr(self.ann_fixer, attr))
        self.history.append(state)
        self.index = len(self.history) - 1

        # keep only the last 10 states
        if len(self.history) > 10:
            self.history = self.history[-10:]

        self.undo_button.setEnabled(True)

    def undo(self):
        if self.index > 0:
            self.index -= 1
            self.restore_state()

        if self.index == 0:
            self.undo_button.setEnabled(False)
        self.redo_button.setEnabled(True)

    def redo(self):
        if self.index < len(self.history) - 1:
            self.index += 1
            self.restore_state()

        if self.index == len(self.history) - 1:
            self.redo_button.setEnabled(False)
        self.undo_button.setEnabled(True)

    def restore_state(self):
        state = self.history[self.index]
        for attr in self.save_attributes:
            setattr(self.ann_fixer, attr, state[attr])
        self.ann_fixer.update_gui()
