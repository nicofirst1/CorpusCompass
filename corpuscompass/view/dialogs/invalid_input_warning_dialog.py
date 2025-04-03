from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


from corpuscompass.view.generated.ui_invalid_input_warning_dialog import (
    Ui_InvalidInputWarningDialog,
)


class InvalidInputWarningDialog(QDialog, Ui_InvalidInputWarningDialog):
    """
    Dialog that displays a warning message when the user tries to confirm an invalid input.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Warning: Invalid Input")
