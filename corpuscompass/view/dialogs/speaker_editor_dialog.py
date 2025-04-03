from typing import Dict, List, Tuple
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QComboBox,
    QColorDialog,
    QDialogButtonBox,
    QLabel,
)
from PySide6.QtCore import Qt


from corpuscompass.view.generated.ui_speaker_editor_dialog import Ui_SpeakerEditorDialog
from corpuscompass.view.utils import set_abbreviate_label


class SpeakerEditorDialog(QDialog, Ui_SpeakerEditorDialog):
    """
    Class for the speaker-editor-dialog. Opens a dialog that
    allows adding, editing and deleting speakers.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Editor: Speakers")

        # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)

        self.comboBox_selectspeaker.setCurrentIndex(-1)
        # list for ivs that were deleted during dialog/editor use
        # self.list_of_removed_speakers = []

        # self.current_speakers_temp: Dict[str, Tuple[List[str], str]] = {}
        self.current_speakers_temp: Dict[str, Tuple[Dict[str, str], str]] = {}

        self.current_ivs_temp: Dict[str, List[str]] = {}

        # list that contains all comboboxes so that they are accessible in the correct order in case they need to be updated
        self.combobox_order: Dict[str, QComboBox] = {}

        # list for ivs that will be added during the add-speaker-dialog use
        # --> different from the edit-workflow as the speakers are not added to the complete "temporary model" directly, but only after the user confirms the dialog, as there wont be an entry in the "temporary model" with the not yet confirmed speaker name
        self.values_to_add: Dict[str, str] = {}
        self.color_to_add = "FFFFFF"

        # hide elements that should not be visible at the beginning
        self.label_duplicate_color.hide()

    def accept(self) -> None:
        """
        Accepts the changes made in the Speaker editor dialog. Differs between the add-speaker-dialog and the edit-speaker-dialog, as for the add-speaker-dialog,
        the speakers are not yet in the temporary model and have to be added after the user confirms the dialog.
        """
        # check if add or edit menu was used
        # --> If the combobox is hidden, the add-iv-dialog was used, otherwise the edit-iv-dialog was used (cannot use index != -1 as this can also happen for the edit-iv-dialog if the user deletes all ivs)
        if self.comboBox_selectspeaker.isHidden():
            # if add menu was used, add the ivs to the temporary model with the now confirmed and valid iv name
            new_speaker_name = self.lineEdit_nameinput.text()
            # fetch the values from the comboboxes and add them to the temporary model (only if the combobox is not empty)
            for iv_name, combobox in self.combobox_order.items():
                if combobox.currentIndex() != -1:
                    self.values_to_add[iv_name] = combobox.currentText()
            # add the result to the temporary model
            self.current_speakers_temp[new_speaker_name] = (
                self.values_to_add.copy(),
                self.color_to_add,
            )

        # close the dialog and send signals via super method
        super().accept()

    def on_change_color_clicked(self):
        """
        Opens a color dialog to allow the user to select a color. If a valid color is selected,
        it sets the background color of the label to the selected color.
        """
        color_dialog = QColorDialog()
        color = color_dialog.getColor()

        if color.isValid():
            # Set the background color of the label to the selected color

            # check if the color is the same as the color of another speaker
            # --> if the color is the same as the color of another speaker, the color is not valid and the user should be informed about this
            for speaker, speaker_data in self.current_speakers_temp.items():
                # duplicate color --> color is already used by another speaker
                if (
                    speaker_data[1] == color.name()
                    and speaker != self.comboBox_selectspeaker.currentText()
                ):
                    # Inform the user that the color is already used by another speaker by showing a tooltip
                    self.label_duplicate_color.show()
                    return

            self.label_colorsquare.setStyleSheet(
                f"background-color: {color.name()}; border: 3px solid black;	max-height: 20px; max-width: 20px; min-height: 20px; min-width: 20px;"
            )

            # Update the color of the selected speaker in the temporary model
            if self.comboBox_selectspeaker.currentIndex() != -1:
                selected_speaker = self.comboBox_selectspeaker.currentText()
                # change the whole tuple in the temporary model, as the color is stored in the second element of the tuple and tuples are immutable
                # this means copying the dictionary with the IVs and values and then updating the color for the new tuple
                self.current_speakers_temp[selected_speaker] = (
                    self.current_speakers_temp[selected_speaker][0],
                    color.name(),
                )
                self.label_duplicate_color.hide()
            else:
                self.color_to_add = color.name()

    def on_combobox_activated(self):
        """
        View-Changes if an element in the combobox is selected.
        En-/Disables elements and controls text in the dialog.
        """

        # disconnect the comboboxes from the save function, as otherwise the comboboxes are updated with the values of the selected speaker and then the temporary model is updated with the values of the comboboxes. This
        # however should only happen if different IV values are selected manually by the user, not if the IV values changed programmatically due to the selection of a speaker
        for iv_name, combobox in self.combobox_order.items():
            combobox.currentIndexChanged.disconnect(
                self.save_combobox_values_in_temporary_model
            )

        if self.comboBox_selectspeaker.currentIndex() != -1:
            self.btn_delete_speaker.setEnabled(True)
            self.btn_changecolor.setEnabled(True)
            self.scrollArea_ivscontents.setEnabled(True)
            self.lineEdit_nameinput.setText(self.comboBox_selectspeaker.currentText())
            self.label_duplicate_color.hide()
            # update the comboboxes with the values of the selected speaker
            self.update_combobox_values()
            # update the color of the selected speaker
            self.label_colorsquare.setStyleSheet(
                f"background-color: {self.current_speakers_temp[self.comboBox_selectspeaker.currentText()][1]}; border: 3px solid black;	max-height: 20px; max-width: 20px; min-height: 20px; min-width: 20px;"
            )

        else:
            self.btn_delete_speaker.setEnabled(False)
            self.btn_changecolor.setEnabled(False)
            self.scrollArea_ivscontents.setEnabled(False)
            self.lineEdit_nameinput.setText("")
            self.label_duplicate_color.hide()

            # reset the comboboxes to their default values
            for cb_label, combobox in self.combobox_order.items():
                combobox.setCurrentIndex(-1)
            # reset the color of the color label
            self.label_colorsquare.setStyleSheet(
                "background-color: white; border: 3px solid black;	max-height: 20px; max-width: 20px; min-height: 20px; min-width: 20px;"
            )
            # if combobox empty (all variables deleted), always enable save-button
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)

        # reconnect the comboboxes to the save function
        for iv_name, combobox in self.combobox_order.items():
            combobox.currentIndexChanged.connect(
                self.save_combobox_values_in_temporary_model
            )

    def add_iv_item_row(
        self, iv_name: str, iv_values: List[str], selected_value: str = None
    ):
        """ "
        Adds a new row to the scroll area that contains the IVs and their values for the selected speaker. Is called when the editor dialog is opened to display the IVs of the selected speaker (or default values if no speaker is selected/new speaker is added).

        Parameters:
        - iv_name (str): The name of the IV.
        - iv_values (List[str]): The values of the IV inside the combobox.
        - selected_value (str): The selected value of the IV.
        """
        # Create a new widget for the IV
        iv_name_label = QLabel("")
        set_abbreviate_label(iv_name_label, iv_name, 20, True)

        # set default properties for each added combobox
        iv_combobox = QComboBox()
        iv_combobox.addItems(iv_values)
        iv_combobox.setObjectName(iv_name)

        iv_combobox.setPlaceholderText("Select Value...")
        if selected_value is not None and selected_value in iv_values:
            iv_combobox.setCurrentText(selected_value)
        else:
            iv_combobox.setCurrentIndex(-1)

        # Add the combobox to the list of comboboxes
        self.combobox_order[iv_name] = iv_combobox

        # connect the combobox to the save function, so that changes are saved in the temporary model after every change
        iv_combobox.currentIndexChanged.connect(
            self.save_combobox_values_in_temporary_model
        )

        # Create a grid layout
        layout = self.scrollArea_ivscontents.layout()

        # Add widgets to the layout
        row = len(self.combobox_order) - 1
        layout.addWidget(iv_name_label, row, 0)
        layout.addWidget(iv_combobox, row, 1)

        layout.setAlignment(iv_name_label, Qt.AlignmentFlag.AlignLeft)
        # layout.setAlignment(iv_combobox, Qt.AlignmentFlag.AlignRight)

        # Set the layout to the widget
        self.scrollArea_ivscontents.setLayout(layout)

    def update_combobox_values(self):
        """
        Updates the values of the IVs for the selected speaker in the scroll area.
        """

        for iv_name, combobox in self.combobox_order.items():
            if (
                iv_name
                in self.current_speakers_temp[
                    self.comboBox_selectspeaker.currentText()
                ][0].keys()
            ):
                selected_value = self.current_speakers_temp[
                    self.comboBox_selectspeaker.currentText()
                ][0][iv_name]
                self.combobox_order[iv_name].setCurrentIndex(
                    self.combobox_order[iv_name].findText(selected_value)
                )
            else:  # if the IV is not in the temporary model, set the selected value to the default value (index -1)
                self.combobox_order[iv_name].setCurrentIndex(-1)

        return

    def save_combobox_values_in_temporary_model(self):
        """
        Saves the selected values of the IVs for the selected speaker in the temporary model. Function is called whenever the users changes any value in the comboboxes. This means that
        there are more updates than necessary, but it is the easiest way to ensure that the temporary model is always in sync with the comboboxes.
        """
        # check if a speaker is selected, if not return without saving any values as there is no speaker in the temporary model yet to save the values for (add-speaker-dialog)
        if self.comboBox_selectspeaker.currentIndex() == -1:
            return

        for iv_name, combobox in self.combobox_order.items():
            selected_value = combobox.currentText()
            if self.combobox_order[iv_name].currentIndex() != -1:
                self.current_speakers_temp[self.comboBox_selectspeaker.currentText()][
                    0
                ][iv_name] = selected_value

            else:  # if the combobox is set to the default value (index -1), remove the IV from the temporary model
                # check if the IV is in the temporary model, if so, remove it
                if (
                    iv_name
                    in self.current_speakers_temp[
                        self.comboBox_selectspeaker.currentText()
                    ][0].keys()
                ):
                    del self.current_speakers_temp[
                        self.comboBox_selectspeaker.currentText()
                    ][0][iv_name]

    def check_varname_changed(self):
        """
        Check if the variable name has changed and perform necessary validations.

        If the combobox is empty (all variables deleted), the method returns without performing any checks,
        as the name change is initiated by the system (not the user) when no variable to display is left.

        If the variable name is empty, contains leading/trailing spaces, or is a duplicate, the method updates
        the UI elements to indicate an invalid input and disables the confirmation and save buttons.

        Otherwise, if the variable name is valid, the method updates the UI elements to indicate a valid input
        and enables the confirmation and save buttons.
        """

        # return if combobox is empty (all speakers deleted), as name-change is initiated by the system (not the user) as no speaker to display is left
        # --> is handled in on_combobox_activated(), which is the source of the "exception"
        if (
            self.comboBox_selectspeaker.count() == 0
            and self.comboBox_selectspeaker.isVisible()
        ):
            return

        variable_name = self.lineEdit_nameinput.text()
        # TODO: Also check if name is duplciate
        # for count == 0, saving needs to be enabled not disabled, even though the textinput changes to an empty string
        if (
            not variable_name.strip()
            or variable_name.startswith(" ")
            or variable_name.endswith(" ")
        ):  # TODO: or variable_name_is_duplicate == False
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_variableinputwarning.setText("No (valid) name input!")
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(
                False
            )
        elif (
            variable_name in self.current_speakers_temp.keys()
            and variable_name != self.comboBox_selectspeaker.currentText()
        ):  # duplicate name check, which is only relevant if the name is not the same as the name of the currently selected IV (as the name of the currently selected IV is always in the temporary model before the user changes it, so it is always a duplicate)
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_variableinputwarning.setText("Duplicate name!")
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(
                False
            )
        else:
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid black; }"
            )
            self.label_variableinputwarning.setText("")
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)

    def remove_current_speaker(self):
        """
        Remove the currently selected speaker from the combo box and add it to the list of removed formats.

        This method removes the currently selected speaker from the combo box `comboBox_selectspeaker` and adds it to the
        `list_of_removed_speakers`. The selected speaker is determined by the current index of the combo box. If no item is
        selected, nothing happens.
        """
        selected_index = self.comboBox_selectspeaker.currentIndex()
        if (
            selected_index != -1
        ):  # Check if an item is selected (should always be as delete-button only enabled if format is selected)
            # remove the speaker from the temporary model
            del self.current_speakers_temp[self.comboBox_selectspeaker.currentText()]
            self.comboBox_selectspeaker.removeItem(selected_index)

    def return_temporary_speaker_data(self):
        """
        Returns the temporary speakers to the model. IVs are not changed during the dialog, so they do not have to be returned.

        Returns:
        - Dict[str, Tuple[Dict[str, str], str]]: The temporary speakers.
        """
        return self.current_speakers_temp
