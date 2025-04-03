from typing import List
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QListWidgetItem,
)


from corpuscompass.view.font_configs import FontConfig
from corpuscompass.view.generated.ui_analysis_settings_confirmation_dialog import (
    Ui_AnalysisSettingsConfirmationDialog,
)


class AnalysisSettingsConfirmationDialog(
    QDialog, Ui_AnalysisSettingsConfirmationDialog
):
    """
    Class for a the confirmation dialog after changing the analysis settings.
    Enables the user to either confirm changes or discard changes to the default
    parameters (default = complete analysis with all variables).
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.btn_includeall.hide()

        self.setWindowTitle("Attention: Analysis Settings Changed")

    def add_all_dvs_to_list(self, dependent_variables_variants: List[str]):
        """
        Adds all dependent variables to the dependent variable list widget in the dialog.

        Parameters:
        - dependent_variables_variants (List[str]): A list of dependent variables to add to the list widget.
        """
        # clear the list widget before adding new items
        self.clear_dv_list()
        for dv in dependent_variables_variants:
            self.add_row_to_dv_list(dv)

    def add_row_to_dv_list(self, item_text: str):
        """
        Adds a new row to the dependent variable list widget in the dialog.

        Parameters:
        - item_text (str): The text for the new row.
        """
        new_item = QListWidgetItem(item_text)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listWidget_dvlist.addItem(new_item)

    def add_all_speakers_to_list(self, speakers: List[str]):
        """
        Adds all speakers to the speaker list widget in the dialog.

        Parameters:
        - speakers (List[str]): A list of speakers to add to the list widget.
        """
        # clear the list widget before adding new items
        self.clear_speaker_list()
        for speaker in speakers:
            self.add_row_to_speaker_list(speaker)

    def add_row_to_speaker_list(self, item_text: str):
        """
        Adds a new row to the speaker list widget in the dialog.

        Parameters:
        - item_text (str): The text for the new row.
        """
        new_item = QListWidgetItem(item_text)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listWidget_speakerlist.addItem(new_item)

    def clear_settings_lists(self):
        """
        Clears the list widgets in the dialog that display the selected and unselected settings.
        """
        self.clear_speaker_list()
        self.clear_dv_list()

    def clear_speaker_list(self):
        """
        Clears the speaker list widget in the dialog.
        """
        self.listWidget_speakerlist.clear()

    def clear_dv_list(self):
        """
        Clears the dependent variable list widget in the dialog.
        """
        self.listWidget_dvlist.clear()
