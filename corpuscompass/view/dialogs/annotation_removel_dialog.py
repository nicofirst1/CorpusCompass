from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)
from PySide6.QtCore import Signal

from corpuscompass.view.generated.ui_annotformat_deletion_dialog import (
    Ui_AnnotationFormatRemoveDialog,
)


class AnnotationRemovalDialog(QDialog, Ui_AnnotationFormatRemoveDialog):
    """
    Class for the annotation-specification-dialog. This window informs user
    about the irreversibility of deleting a format.
    """

    remove_format_accepted = Signal(bool)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Warning: Deletion of Annotation Format")

    def accept(self) -> None:
        """
        Accepts the deletion of the annotation format and closes the dialog.
        """

        # Check if the user provided a project name
        dont_show_again = self.checkBox_showagain.isChecked()

        # Send a signal to the controller
        self.remove_format_accepted.emit(dont_show_again)

        # Close the Window
        self.done(0)
