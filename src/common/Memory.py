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
            assert value in self.choices, (
                f"Value {value} not in the choices {self.choices}"
            )
        self._value = value


class Memory(QtCore.QObject):
    """
    Class to store the memory of the annotation fixer
    """

    def __init__(self):
        super().__init__()
        # get current working directory
        self.dir = os.path.dirname(os.path.abspath(__file__))

        # find the index of the corpus compass folder by splitting with the os separator
        index = [
            ind
            for ind in range(len(self.dir.split(os.sep)))
            if "CorpusCompass" in self.dir.split(os.sep)[ind]
        ][0]

        # get the corpus compass folder
        self.dir = os.sep.join(self.dir.split(os.sep)[: index + 1])

        # append the corpus compass folder
        self.dir = os.path.join(self.dir, ".corpus_compass")

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
        self.file_analysis_paths = os.path.join(self.dir, "analysis_paths.json")

        # create the attributes
        self._lfp = SavingDict(self.save_file, attr="file_lfp")
        self._settings = SavingDict(self.save_file, attr="file_settings")
        self._postprocess_paths = SavingDict(
            self.save_file, attr="file_postprocess_paths"
        )
        self._analysis_paths = SavingDict(self.save_file, attr="file_analysis_paths")

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
        # make it absolute
        self.analysis_dir = os.path.abspath(self.analysis_dir)

        self.analysis_paths = {
            "kmean": os.path.join(self.analysis_dir, "kmean"),
            "poisson_regression": os.path.join(self.analysis_dir, "poisson_regression"),
            "pair_wise_frequency_analysis": os.path.join(
                self.analysis_dir, "pair_wise_frequency"
            ),
            "proportions_analysis": os.path.join(
                self.analysis_dir, "proportions_analysis"
            ),
            "cross_tabulation_analysis": os.path.join(
                self.analysis_dir, "cross_tabulation"
            ),
            "chi_square_analysis": os.path.join(self.analysis_dir, "chi_square"),
            "logistic_regression_analysis": os.path.join(
                self.analysis_dir, "logistic_regression_analysis"
            ),
            "point_biserial_analysis": os.path.join(
                self.analysis_dir, "point_biserial_analysis"
            ),
            "t_test_analysis": os.path.join(self.analysis_dir, "t_test"),
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
            "pair_wise_frequency_analysis": True,
            "pair_wise_frequency_normalizer_multiplier": 1000,
            "poisson_regression_analysis": True,
            "proportions_analysis": True,
            "cross_tabulation_analysis": True,
            "chi_square_analysis": True,
            "logistic_regression_analysis": True,
            "point_biserial_analysis": True,
            "t_test_analysis": True,
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
            "pair_wise_frequency_analysis": (
                "Perform analysis of the pair wise frequency of the annotations",
                [True, False],
            ),
            "pair_wise_frequency_normalizer_multiplier": (
                "Multiplier to use for the normalizer of the pair wise frequency analysis",
                [1, 10, 100, 1000, 10000, 100000],
            ),
            "poisson_regression_analysis": (
                "Perform poisson regression analysis",
                [True, False],
            ),
            "proportions_analysis": (
                "Perform proportions analysis",
                [True, False],
            ),
            "cross_tabulation_analysis": (
                "Perform cross tabulation analysis",
                [True, False],
            ),
            "chi_square_analysis": (
                "Perform chi square analysis",
                [True, False],
            ),
            "logistic_regression_analysis": (
                "Perform logistic regression analysis",
                [True, False],
            ),
            "point_biserial_analysis": (
                "Perform point biserial analysis",
                [True, False],
            ),
            "t_test_analysis": (
                "Perform t test analysis",
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
                "suppress_existent",
            ],
            annotation_fixer=[
                "minimum_repetitions",
                "use_strict_rule",
                "data_source",
                "auto_annotation_thr",
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
                "pair_wise_frequency_analysis",
                "pair_wise_frequency_normalizer_multiplier",
                "poisson_regression_analysis",
                "proportions_analysis",
                "cross_tabulation_analysis",
                "chi_square_analysis",
                "logistic_regression_analysis",
                "point_biserial_analysis",
                "t_test_analysis",
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

    @property
    def analysis_paths(self):
        return self._analysis_paths

    @analysis_paths.setter
    def analysis_paths(self, value: Dict[str, str]):
        self._analysis_paths.update(value)
        self.save_file("file_analysis_paths")
