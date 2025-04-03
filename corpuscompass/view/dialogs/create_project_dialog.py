from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)
from PySide6.QtCore import Signal


from corpuscompass.view.generated.ui_create_project_dialog import Ui_CreateProjectDialog


class CreateProjectDialog(QDialog, Ui_CreateProjectDialog):
    """
    The dialog is opened, if a new project should be created.
    """

    create_proj_accepted = Signal(str)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

    def accept(self) -> None:
        """
        Method is called, if the user clicks on "OK" in the dialog window. The
        Method checks first, if the necessary informations are provided by the
        user before sending a signal to the controller.
        """
        proj_name = self.proj_name_lineedit.text()

        # Check if the user provided a project name
        if len(proj_name) == 0:
            self.display_error_message("The project name cannot be empty!")
            return

        print("emitting signal")
        # Send a signal to the controller
        self.create_proj_accepted.emit(proj_name)

        # Close the Window
        self.done(0)

    def reject(self) -> None:
        """
        Method is called, if the user clickes on "Cancel" in the dialog window.
        Closes the window.
        """
        self.done(0)

    def display_error_message(self, text: str) -> None:
        """
        Method displays a red error message at the bottom of the dialog window.

        Args:
            text (str): The error-message, that should be displayed.
        """
        self.error_message_label.setText(text)
