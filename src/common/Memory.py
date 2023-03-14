import json
import os
from typing import Dict, Any, Optional, List

import pandas as pd
from PySide6 import QtCore, QtWidgets


class SavingDict(dict):
    def __init__(self, save_fn, attr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._save_fn = save_fn
        self._attr = attr

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_fn(self._attr)

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_fn(self._attr)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save_fn(self._attr)

    def pop(self, *args, **kwargs):
        super().pop(*args, **kwargs)
        self._save_fn(self._attr)

    def popitem(self, *args, **kwargs):
        super().popitem(*args, **kwargs)
        self._save_fn(self._attr)


class SettingValue:
    def __init__(
        self,
        value: Any,
        description: Optional[str] = "",
        choices: Optional[List[Any]] = None,
    ):
        super().__init__()

        if choices is not None:
            assert value in choices, f"Value {value} not in the choices {choices}"

        self._value = value
        self.description = description
        self.choices = choices

    def __class__(self):
        return type(self.value)

    def __call__(self, *args, **kwargs):
        return self.value

    def __str__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.choices is not None:
            assert (
                value in self.choices
            ), f"Value {value} not in the choices {self.choices}"
        self._value = value


class Memory(QtCore.QObject):
    """
    Class to store the memory of the annotation fixer
    """

    def __init__(self):
        super().__init__()
        self.dir = ".corpus_compass"
        # create dir if not exists
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

        self.preloaded_dir = os.path.join(self.dir, "preloaded")

        if not os.path.exists(self.preloaded_dir):
            os.mkdir(self.preloaded_dir)

        # create the files
        self.file_lfp = os.path.join(self.dir, "lfp.json")
        self.file_settings = os.path.join(self.dir, "settings.json")
        self.file_postprocess_paths = os.path.join(self.dir, "postprocess_paths.json")

        # create the attributes
        self._lfp = SavingDict(self.save_file, attr="file_lfp")
        self._settings = SavingDict(self.save_file, attr="file_settings")
        self._postprocess_paths = SavingDict(
            self.save_file, attr="file_postprocess_paths"
        )

        self.setting_groups = {}

        self.postprocess_names = [
            "annotation_info.csv",
            "binary_dataset.csv",
            "dataset.csv",
            "missed_annotations.csv",
        ]
        self.variables_names = [
            "independent_variables.json",
            "dependent_variables.json",
            "speakers.json",
        ]

        self.analysis_dir = "analysis"

        self.analysis_paths = {
            "kmean": os.path.join(self.analysis_dir, "kmean"),
            "poisson_regression": os.path.join(self.analysis_dir, "poisson_regression"),
            "variable_analysis": os.path.join(self.analysis_dir, "variable_analysis"),
            "dependent_variable_analysis": os.path.join(
                self.analysis_dir, "dependent_variable_analysis"
            ),
        }

        # load the memory
        self.load_memory()

        self.init_default_settings()

    def init_default_settings(self):
        setting_values = {
            # interface
            "style": "s1",
            "text_font": "Arial",
            "text_size": 12,
            "window_size": (500, 500),
            # general
            "separator": ";",
            "encoding": "utf-16",
            "use_loaded": False,
            "annotation_regex": r"(\[\$[\S ]*?\])",
            "suppress_existent": True,
            # annotation fixer
            "minimum_repetitions": 1,
            "use_strict_rule": True,
            "data_source": "info",
            "auto_annotation_thr": 0.5,
            # dataset creator
            "feat_regex": r"\[\$([\S ]*?)\]",
            "name_regex": r"(^[A-z0-9?._]+) ",
            "previous_line": False,
            "ngram_prev": 10,
            "ngram_next": 10,
            # data analyzer
            "kmean_analysis": True,
            "kmean_n_clusters": -1,
            "kmean_max_clusters": 50,
            "dependent_variable_analysis": True,
            "variable_analysis": True,
            "poissont_regression_analysis": True,
        }

        self.settings_metadata = {
            # interface
            "text_font": ("Text font", []),
            "text_size": ("Text size", []),
            "window_size": ("Window Size", []),
            "style": ("Style for the colors", [f"s{i}" for i in range(10)]),
            # general
            "separator": ("Separator used in the csv files", [",", ";"]),
            "encoding": ("Encoding used in the csv files", ["utf-8", "utf-16"]),
            "use_loaded": (
                "Use the loaded data instead of the loading it from scratch",
                [True, False],
            ),
            "annotation_regex": ("Regex to extract the annotations from the text", []),
            "suppress_existent": (
                "Suppress warnings for overwriting existing files",
                [True, False],
            ),
            # annotation fixer
            "minimum_repetitions": (
                "Minimum number of repetitions to be considered when using the annotation info",
                [],
            ),
            "use_strict_rule": (
                "Use the strict rule to extract the annotations with the regex",
                [True, False],
            ),
            "data_source": (
                "Data source to use for the annotation info, available options: info, missing",
                ["info", "missing"],
            ),
            "auto_annotation_thr": (
                "Threshold to use for the auto annotation",
                [x / 100.0 for x in range(0, 100, 10)],
            ),
            # dataset creator
            "feat_regex": ("Regex to find the content of an annotation.", []),
            "name_regex": (
                "Regex to univocally find the speaker name in the paragraph.",
                [],
            ),
            "previous_line": (
                "Include previous paragraph in final output",
                [True, False],
            ),
            "ngram_prev": (
                "Number of previous words to include in the ngram",
                list(range(1, 20)),
            ),
            "ngram_next": (
                "Number of next words to include in the ngram",
                list(range(1, 20)),
            ),
            # data analyzer
            "kmean_analysis": (
                "Perform kmean analysis",
                [True, False],
            ),
            "kmean_n_clusters": (
                "Number of clusters for the kmean analysis. If -1, the number of clusters is determined by the elbow method.",
                [x for x in list(range(-1, 20)) if x != 0],
            ),
            "kmean_max_clusters": (
                "Maximum number of clusters to try when estimating the number of clusters with the elbow method.",
                list(range(1, 100)),
            ),
            "dependent_variable_analysis": (
                "Perform dependent variable analysis",
                [True, False],
            ),
            "variable_analysis": (
                "Perform variable analysis",
                [True, False],
            ),
            "poissont_regression_analysis": (
                "Perform poisson regression analysis",
                [True, False],
            ),
        }

        self.setting_groups = dict(
            interface=["text_font", "text_size", "window_size", "style"],
            general=[
                "separator",
                "encoding",
                "use_loaded",
                "annotation_regex",
            ],
            annotation_fixer=[
                "minimum_repetitions",
                "use_strict_rule",
                "data_source",
                "auto_annotation_thr",
                "suppress_existent",
            ],
            dataset_creator=[
                "feat_regex",
                "name_regex",
                "previous_line",
                "ngram_prev",
                "ngram_next",
            ],
            data_analyzer=[
                "kmean_analysis",
                "kmean_n_clusters",
                "kmean_max_clusters",
                "dependent_variable_analysis",
                "variable_analysis",
                "poissont_regression_analysis",
            ],
        )

        # update settings with the default if not exists
        for k, v in setting_values.items():
            if k not in self.settings:
                self.settings[k] = v

    def save_preloaded(self, files: Dict[str, Any]):
        """
        Save the preloaded files
        """
        for file_name, value in files.items():
            if isinstance(value, pd.DataFrame):
                value.to_csv(os.path.join(self.preloaded_dir, file_name + ".csv"))
            else:
                # it is a dict of strings, to save it as json
                with open(
                    os.path.join(self.preloaded_dir, file_name + ".json"), "w"
                ) as f:
                    f.write(json.dumps(value))

    def load_all_preloaded(self):
        """
        Load all the preloaded files
        """

        loaded = {}
        for p in os.listdir(self.preloaded_dir):
            if p.endswith(".csv"):
                loaded[p.replace(".csv", "")] = pd.read_csv(
                    os.path.join(self.preloaded_dir, p)
                )
            elif p.endswith(".json"):
                with open(os.path.join(self.preloaded_dir, p), "r") as f:
                    loaded[p.replace(".json", "")] = json.load(f)
            else:
                with open(os.path.join(self.preloaded_dir, p), "r") as f:
                    loaded[p.replace(".txt", "")] = f.read()

        return loaded

    def exist_preloaded(self) -> bool:
        """
        Check if the file is preloaded
        """
        return len(os.listdir(self.preloaded_dir)) > 0

    def load_memory(self):
        """
        Load the memory from the files
        """
        # for all the attributes that end with _paths
        for attr in [a for a in dir(self) if a.startswith("file_")]:
            attr_value = getattr(self, attr)
            # create files if not exists
            if not os.path.exists(attr_value):
                with open(attr_value, "w") as f:
                    json.dump({}, f)

            # get the hidden attribute name without the file_ prefix

            hid_attr = attr.replace("file_", "")

            # load the paths from the file
            with open(attr_value, "r") as f:
                setattr(self, hid_attr, json.load(f))

    def save_file(self, attr=None):
        """
        Save the memory to the files
        """

        if attr is None:
            attrs = [a for a in dir(self) if a.startswith("file_")]
        else:
            attrs = [attr]

        # for all the attributes that end with _paths
        for attr in attrs:
            attr_value = getattr(self, attr)
            # get the hidden attribute name without the file_ prefix
            hid_attr = attr.replace("file_", "_")

            # save the paths to the file
            with open(attr_value, "w") as f:
                json.dump(getattr(self, hid_attr), f)

    def save_setting(self, _parent, _name):
        def inner():
            metadata = self.settings_metadata[_name]
            description, choices = metadata

            if len(choices) == 2 and isinstance(choices[0], bool):
                val = _parent.findChild(QtWidgets.QCheckBox, _name).isChecked()

            elif len(choices) > 0:
                if all(isinstance(x, int) for x in choices):
                    val = _parent.findChild(QtWidgets.QSpinBox, _name).value()
                else:
                    val = _parent.findChild(QtWidgets.QComboBox, _name).currentText()

            else:
                val = _parent.findChild(QtWidgets.QLineEdit, _name).text()

            # cast to type
            old_val = self.settings[_name]
            t = type(old_val)

            if isinstance(old_val, tuple) or isinstance(old_val, list):
                val = eval(val)
            else:
                val = t(val)

            self.settings[_name] = val

        return inner

    @property
    def lfp(self):
        return self._lfp

    @lfp.setter
    def lfp(self, value: Dict[str, str]):
        self._lfp.update(value)
        self.save_file("file_lfp")

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value: Dict[str, Any]):
        self._settings.update(value)
        self.save_file("file_settings")

    @property
    def postprocess_paths(self):
        return self._postprocess_paths

    @postprocess_paths.setter
    def postprocess_paths(self, value: Dict[str, str]):
        self._postprocess_paths.update(value)
        self.save_file("file_postprocess_paths")
