from corpuscompass.view.generated.ui_annotation_help_dialog import (
    Ui_AnnotationHelpDialog,
)


from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)




class AnnotationHelpDialog(QDialog, Ui_AnnotationHelpDialog):
    """
    Class for a the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Help: Annotation Format")
