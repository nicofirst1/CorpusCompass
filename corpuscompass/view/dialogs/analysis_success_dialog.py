from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QFileDialog,
)


from corpuscompass.view.generated.ui_analysis_success_dialog import (
    Ui_AnalysisSuccessDialog,
)
from corpuscompass.view.utils import set_abbreviate_label


class AnalysisSuccessDialog(QDialog, Ui_AnalysisSuccessDialog):
    """
    Class for the success-dialog that opens upon analysing
    a corpus. Also provides possibilites to select a save
    location for the results and directly open the selected
    save location
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Success: Analysis Completed")
        self.selected_folder = None

    def on_select_target_file_path_clicked(self):
        """
        Opens a file dialog to select a new folder that contains the projects.
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        # if a folder is selected, set the path to the selected folder
        # --> dialog.exec() returns True if a folder is selected, False if not
        if dialog.exec():
            # send signal to the model
            self.selected_folder = dialog.selectedFiles()[0]
            set_abbreviate_label(self.label_filepath, self.selected_folder, 60, False)
            self.btn_save.setEnabled(True)
        else:
            # if no new folder is selected, do nothing
            pass

    def get_selected_folder(self) -> str | None:
        """Gives you back the folder that the user selected for saving the analysis results of the corpus.
        If the user did not select a folder, None is returned.

        Returns:
            str | None: The path to the selected folder.
        """
        return self.selected_folder

    def accept(self) -> None:
        super().accept()

        # send a signal to the model so that the analysis is saved to the selected location
