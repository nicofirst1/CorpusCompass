import json
import os
import re
from typing import Dict, Optional, Tuple, List, Any, Union, Literal

import pandas as pd
from PySide6 import QtWidgets, QtGui, QtCore

from src.common.Memory import Memory


def multi_corpus_upload(
    corpus_list: Dict[str, bytes], encoding: Optional[str] = "utf-16"
) -> Tuple[Dict[str, str], List[str]]:
    """
    Upload multiple corpus
    """

    alternative_encodings = [encoding] + [
        "utf-8",
        "utf-16",
        "latin-1",
        "ascii",
        "cp1252",
        "cp1250",
        "cp1251",
        "cp1253",
    ]

    def decode(to_decode) -> Tuple[str, str]:
        idx = 0
        dec = ""
        success = False
        while idx < len(alternative_encodings):
            encoding = alternative_encodings[idx]

            if idx > 0:
                print(f"Trying with the encoding {encoding}.")

            try:
                dec = to_decode.decode(encoding) + "\n"

                if " " not in dec:
                    print(
                        f"The corpus {k} has been read with the encoding {encoding}, but it seems that it did not work."
                    )
                    idx += 1
                    continue

                dec = re.sub(r"[^\S\n]+", " ", dec)

            except UnicodeDecodeError as e:
                print(
                    f"Could not decode the corpus {k} with the encoding {encoding}.\n"
                    f"The error is: {e}\n"
                )
                idx += 1
                continue
            success = True
            break

        if not success:
            msg = f"Could not decode the corpus {k} with any of the encodings {alternative_encodings}.\n"
            f"Please check the encoding of the corpus and try again."
            return "", msg
        else:
            print(f"The corpus {k} has been read with the encoding {encoding}.")
        return dec, ""

    corpus = {}
    errs = []
    for k, v in corpus_list.items():
        corpus[k], err = decode(v)
        errs.append(err)

    errs = [e for e in errs if e != ""]

    return corpus, errs


def load_postprocess(
    paths: List[str], encoding: str, separator: str
) -> Tuple[List[Any], Optional[str]]:
    """
    Open the file and return the content
    :param paths: list of paths
    :return: the content of the file
    """
    content = {}
    encoding = encoding.lower()
    for path in paths:
        file_name = os.path.basename(path).split(".")[0]
        try:
            content[file_name] = pd.read_csv(
                path, encoding=encoding, on_bad_lines="skip", sep=separator
            )
        except UnicodeError as e:
            if encoding == "utf-8":
                encoding = "utf-16"
            elif encoding == "utf-16":
                encoding = "utf-8"
            else:
                error = f"Error while opening the file {path}\n{repr(e)}"
                return content, error

            content[file_name] = pd.read_csv(
                path, encoding=encoding, on_bad_lines="skip", sep=separator
            )
        except Exception as e:
            error = f"Error while opening the file {path}\n{repr(e)}"
            return content, error

    return content, None


def save_postprocess(results: Dict, mem: Memory):
    separator = mem.settings.get("separator", ";")
    # get the name of the output path
    output_dir = "postprocessed"
    # create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_dir = os.path.abspath(output_dir)
    # define the output file names
    dataset_path = os.path.join(output_dir, "dataset.csv")
    binary_dataset_path = os.path.join(output_dir, "binary_dataset.csv")
    annotation_info_path = os.path.join(output_dir, "annotation_info.csv")
    missed_annotation_path = os.path.join(output_dir, "missed_annotations.csv")
    unk_variables_path = os.path.join(output_dir, "unk_variables.csv")
    corpus_stats_path = os.path.join(output_dir, "corpus_stats.json")

    # write the csv
    results["dataset"].to_csv(
        dataset_path, index=False, sep=separator, encoding="utf16"
    )
    results["annotation_info"].to_csv(
        annotation_info_path, index=False, sep=separator, encoding="utf16"
    )
    results["missed_annotations"].to_csv(
        missed_annotation_path, index=False, sep=separator, encoding="utf16"
    )
    results["binary_dataset"].to_csv(
        binary_dataset_path, index=False, sep=separator, encoding="utf16"
    )
    results["unk_variables"].to_csv(
        unk_variables_path, index=False, sep=separator, encoding="utf16"
    )
    # write the corpus stats to json
    with open(corpus_stats_path, "w", encoding="utf16") as f:
        json.dump(results["corpus_stats"], f, indent=4)

    # save the new paths in the memory
    mem.postprocess_paths = dict(
        dataset=dataset_path,
        binary_dataset=binary_dataset_path,
        annotation_info=annotation_info_path,
        missed_annotations=missed_annotation_path,
        unk_variables=unk_variables_path,
    )


def open_variables(
    paths: List[str], encoding: str
) -> Union[Tuple[Dict[str, Any], str], Tuple[Dict[str, Any], None]]:
    """
    Open the file and return the content
    :param paths: list of paths
    :return: the content of the file
    """
    content = {}
    encoding = encoding.lower()
    for path in paths:
        file_name = os.path.basename(path).split(".")[0]
        try:
            with open(path, encoding=encoding) as f:
                content[file_name] = json.load(f)

        except UnicodeError as e:
            if encoding == "utf-8":
                encoding = "utf-16"
            elif encoding == "utf-16":
                encoding = "utf-8"
            else:
                error = f"Error while opening the file {path}\n{repr(e)}"
                return content, error

            with open(path, encoding=encoding) as f:
                content[file_name] = json.load(f)
        except Exception as e:
            error = f"Error while opening the file {path}\n{repr(e)}"
            return content, error

    return content, None


def create_input(
    parent,
    name: str,
    mem: Memory,
    arrange: Literal["vert", "horz"] = "horz",
    delay: int = 2,
) -> Tuple[QtWidgets.QWidget, QtWidgets.QHBoxLayout]:
    """
    Create a widget for a setting
    :param parent: the parent widget
    :param name: the name of the setting
    :param mem: the memory
    :param delay: the delay for the timer
    """
    description, choices = mem.settings_metadata[name]
    value = mem.settings.get(name, None)
    pretty_name = to_pretty_name(name)
    save_setting_method = mem.save_setting(parent, name)

    # make horizontal layout
    if arrange == "vert":
        layout = QtWidgets.QVBoxLayout()

    else:
        layout = QtWidgets.QHBoxLayout()

    label = QtWidgets.QLabel(pretty_name + ":")
    label.setAlignment(QtCore.Qt.AlignRight)

    # check if choices is boolean
    if len(choices) == 2 and isinstance(choices[0], bool):
        widget = QtWidgets.QCheckBox("", parent)
        widget.setObjectName(name)
        widget.setChecked(mem.settings[name])
        widget.stateChanged.connect(save_setting_method)

    elif len(choices) > 0:
        # if choices are all integers
        if all(isinstance(x, int) for x in choices):
            widget = QtWidgets.QSpinBox()
            widget.setObjectName(name)
            widget.setRange(min(choices), max(choices))
            widget.setValue(value)
            widget.valueChanged.connect(save_setting_method)

        else:
            widget = QtWidgets.QComboBox()
            widget.setObjectName(name)
            widget.addItems([str(x) for x in choices])
            widget.setCurrentIndex(choices.index(value))

            # Find the width of the largest item text
            width = 0
            font = widget.font()
            for item in choices:
                fm = QtGui.QFontMetrics(font)
                width = max(width, fm.horizontalAdvance(str(item)))

            # Set the minimum width of the QComboBox
            widget.setMinimumWidth(width + 50)

            widget.currentIndexChanged.connect(save_setting_method)

    else:
        # todo: change from editingFinished to modified
        widget = QtWidgets.QLineEdit()
        widget.setObjectName(name)
        widget.setPlaceholderText("Enter a value...")
        widget.setText(str(value))
        widget.editingFinished.connect(save_setting_method)

    timer = QtCore.QTimer(parent)
    timer.setSingleShot(True)
    timer.timeout.connect(lambda: widget.setToolTip(description))
    widget.enterEvent = lambda _: timer.start(delay)
    widget.leaveEvent = lambda _: timer.stop()

    # add the label and the widget to the layout
    layout.addWidget(label)
    layout.addWidget(widget)

    return widget, layout


def to_pretty_name(name: str) -> str:
    # remove underscores
    name = name.replace("_", " ")

    # capitalize
    name = name.capitalize()

    return name
