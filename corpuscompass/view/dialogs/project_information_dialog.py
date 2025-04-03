from corpuscompass.view.generated.ui_project_information_dialog import (
    Ui_ProjectInformationDialog,
)


from PySide6.QtWidgets import (
    QWidget,
    QDialog,
)


class ProjectInformationDialog(QDialog, Ui_ProjectInformationDialog):
    """
    Class for the project-information-dialog. This window allows the user to
    check and specify the project name and description, alongside other project related information.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Project Information")
