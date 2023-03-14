import threading
import traceback

from PySide6 import QtCore

from src.common import QTextLogger, Memory
from src.data_analyzer.da_utils import kmeans_analysis


class DAThread(QtCore.QProcess):
    def __init__(
        self,
        binary_dataset,
        independent_variables,
        dependent_variables,
        speakers,
        settings: Memory,
    ):
        super().__init__()

        self.binary_dataset = binary_dataset
        self.independent_variables = independent_variables
        self.dependent_variables = dependent_variables
        self.speakers = speakers
        self.settings = settings

        self.logger = QTextLogger()
        # define the flag to stop the thread
        self.stop_event = threading.Event()
        self.results = None

    def stop(self) -> None:
        self.stop_event.set()

    def run(self):
        try:
            tokens = self.binary_dataset["token"]
            context = self.binary_dataset["context"]
            binary_dataset = self.binary_dataset.drop(columns=["token", "context"])


            if self.settings.settings["kmean_analysis"]:
                self.logger.info("K-mean analysis started.")
                self.results = kmeans_analysis(
                    df=binary_dataset,
                    tokens=tokens,
                    custom_path=self.settings.analysis_paths["kmean"],
                    num_clusters=self.settings.settings["kmean_n_clusters"],
                    max_clusters=self.settings.settings["kmean_max_clusters"],
                    logger=self.logger,
                )
                self.logger.info("K-mean analysis finished.")

            a = 1

        except Exception as e:
            err_msg = (
                f"An error occurred while generating the dataset: {e}\n"
                f"{traceback.format_exc()}"
            )
            self.logger.error(err_msg)

            self.results = err_msg

        finally:
            self.finished.emit()
