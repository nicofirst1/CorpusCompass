"""
This module contains the class CorpusCompassApp, which is the main class to
run CorpussCompass
"""

from PySide6.QtWidgets import QApplication
from corpuscompass.view.corpus_compass_view import CorpusCompassView
from corpuscompass.model import CorpusCompassModel
from corpuscompass.controller import Controller
from corpuscompass.utils.exception_handling import setup_exception_handling
import logging
from pathlib import Path


class CorpusCompassApp(QApplication):
    """
    Class that contains the CorpusCompassApp. Has three major components:
        - model: Stores data and provides necessary functions for the corpus
                 analysis
        - view: Manages the user interface
        - controller: connects input from the view (e.g. a button is pressed)
                      with actions/functions in the model and updates the view
                      afterwards
    """

    def __init__(self, sys_argv, write_to_logfile: bool = False):
        super(CorpusCompassApp, self).__init__(sys_argv)

        if write_to_logfile:
            # Set up the logging file for logging all messages
            log_dir = Path.home() / "CorpusCompassLogs"
            log_dir.mkdir(exist_ok=True)
            log_file = log_dir / "corpus_compass.log"

            logging.basicConfig(
                filename=log_file,
                filemode="a",  # Append to the log file
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                level=logging.INFO,  # Log INFO level and above
            )
            # Also add a stream handler to see logs in the console during development
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            console_handler.setFormatter(formatter)
            logging.getLogger().addHandler(console_handler)

            logging.info("CorpusCompass application started.")

        # Initialize model
        self.model = CorpusCompassModel()

        # Initialize the view
        self.view = CorpusCompassView()

        # Initialize the controller
        self.controller = Controller(self.model, self.view)

        # Redirect uncaught exceptions to be logged in a file.
        setup_exception_handling()

    def start(self) -> int:
        """Starts the CorpusCompass Application, which leads to the ui showing up

        Returns:
            int: The exit code. is usually 0, if the program terminated in an expected way
        """
        self.view.show()
        exit_code = self.exec()
        self.model.close_project()
        return exit_code
