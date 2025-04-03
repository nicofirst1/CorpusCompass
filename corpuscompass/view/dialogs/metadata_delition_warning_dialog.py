from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


from corpuscompass.view.generated.ui_metadata_deletion_warning_dialog import (
    Ui_MetadataDeletionWarningDialog,
)


class MetadataDeletionWarningDialog(QDialog, Ui_MetadataDeletionWarningDialog):
    """
    Dialog for displaying a warning message when deleting metadata.

    This dialog is used to display a warning message when the user tries to delete metadata.
    It inherits from QDialog and Ui_MetadataDeletionWarningDialog.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Warning: Deleting Metadata")
