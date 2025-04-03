from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


from corpuscompass.view.generated.ui_variable_detection_help_dialog import (
    Ui_VariableDetectionHelpDialog,
)


class VariableDetectionHelpDialog(QDialog, Ui_VariableDetectionHelpDialog):
    """
    Dialog that holds information about how the detection of variable variants works.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Help: Detected DV-Variants")
