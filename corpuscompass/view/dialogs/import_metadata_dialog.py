from corpuscompass.view.generated.ui_import_metadata_dialog import (
    Ui_ImportMetadataDialog,
)

from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)




class ImportMetadataDialog(QDialog, Ui_ImportMetadataDialog):
    """
    Class for a the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Import Metadata")
