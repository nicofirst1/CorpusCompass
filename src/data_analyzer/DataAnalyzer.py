from collections import OrderedDict
from typing import Dict, Any

from src.annotation_fixer.af_utils import corpus_dict2text
from src.common import GeneralWindow, Memory, AppLogger


class DataAnalyzer(GeneralWindow):
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

        super().__init__(mem, "Data Analyzer")
        self.logger = AppLogger(mem, "data_analyzer.log")

    def create_widgets(self):

        pass


