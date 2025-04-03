from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


from corpuscompass.view.generated.ui_export_metadata_dialog import (
    Ui_ExportMetadataDialog,
)


class ExportMetadataDialog(QDialog, Ui_ExportMetadataDialog):
    """
    Class for the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Export Metadata")
