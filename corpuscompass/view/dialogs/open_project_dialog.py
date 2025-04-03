from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QFileDialog,
)


from corpuscompass.view.generated.ui_open_project_dialog import Ui_OpenProjectDialog
from corpuscompass.view.utils import set_abbreviate_label


class OpenProjectDialog(QDialog, Ui_OpenProjectDialog):
    """
    Class for the dialog window for opening new projects.
    The window contains a list of all available projects, of
    which one can be selected.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Open Project")

    def on_change_path_clicked(self):
        """
        Opens a file dialog to select a new folder that contains the projects.
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        # if a folder is selected, set the path to the selected folder
        # --> dialog.exec() returns True if a folder is selected, False if not
        if dialog.exec():
            selected_folder = dialog.selectedFiles()[0]
            # TODO: send signal to model
            set_abbreviate_label(self.label_repositorypath, selected_folder, 55, False)
        else:
            # if no new folder is selected, do nothing
            pass
