"""
This module contains the class CorpusCompassApp, which is the main class to
run CorpussCompass
"""

from PySide6.QtWidgets import QApplication
from src.view.corpus_compass_view import CorpusCompassView
from src.model.corpus_compass_model import CorpusCompassModel
from src.controller import Controller
from src.utils.exception_handling import setup_exception_handling
import logging


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
        # Initialize model
        self.model = CorpusCompassModel()

        # Initialize the view
        self.view = CorpusCompassView()

        # Initialize the controller
        self.controller = Controller(self.model, self.view)

        if write_to_logfile:
            # Set up the logging file for logging unhandled exceptions
            logging.basicConfig(
                filename="log.txt",
                filemode="a",
                format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
                datefmt="%H:%M:%S",
                level=logging.DEBUG,
            )

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
