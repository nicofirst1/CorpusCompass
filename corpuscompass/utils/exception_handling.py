"""Provides methods for handling uncaught exceptions. These are then written in
a log.
"""

import sys
import logging


def setup_exception_handling():
    """Sets up the handling of uncaught exceptions by putting them in a log."""
    sys.excepthook = handle_unhandled_exception


def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    """Handles uncaught exceptions by putting them in a log.

    Args:
        exc_type (type): The type of the exception
        exc_value (class): Tells you what the occurred exception is.
        exc_traceback (traceback): What other methods were called beforehand.
    """

    if issubclass(exc_type, KeyboardInterrupt):
        # Will call default excepthook
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Create a critical level log message with info from the except hook.
    logging.critical(
        "Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback)
    )
