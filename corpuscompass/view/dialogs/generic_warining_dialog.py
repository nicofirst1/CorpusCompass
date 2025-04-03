from corpuscompass.view.generated.ui_generic_warning_dialog import (
    Ui_GenericWarningDialog,
)

from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


class GenericWarningDialog(QDialog, Ui_GenericWarningDialog):
    """
    Class for a generic warning dialog. Text inside the dialog
    can be changed as required. Serves no purpose to the
    model, but is just feedback for the user.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Warning")
