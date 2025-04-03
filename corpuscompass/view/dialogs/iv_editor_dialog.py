from typing import Dict, List
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QTableWidgetItem,
    QDialogButtonBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QKeyEvent,
)


from corpuscompass.view.generated.ui_iv_editor_dialog import Ui_IVEditorDialog


class IVEditorDialog(QDialog, Ui_IVEditorDialog):
    """
    Class for the dialog that enables editing
    IVs and their values, as well as deleting IVs.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Editor: Independent Variables")

        self.current_ivs_temp: Dict[str, List[str]] = {}

        # Set initial properties (that are the same for every dialog and independent of dynamic data)
        self.comboBox_selectiv.setCurrentIndex(-1)
        # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)
        self.tableWidget_storedvalues.setColumnWidth(0, 25)

        # list for ivs that will be added during the add-iv-dialog use
        # --> different from the edit-workflow as the ivs are not added to the complete "temporary model" directly, but only after the user confirms the dialog, as there wont be an entry in the "temporary model" with the not yet confirmed iv name
        # --> edit workflow: ivs are added to the temporary model directly, as the ivs are already in the temporary model (dictioanry) and can be edited directly
        self.values_to_add = []

    def accept(self) -> None:
        """
        Accepts the changes made in the IV editor dialog. Differs between the add-iv-dialog and the edit-iv-dialog, as for the add-iv-dialog, the ivs are not yet in the temporary model and have to be added after the user confirms the dialog.
        After the accept button is clicked, the ivs are added to the temporary model which data can be requested by the controller in order to propagate everything to the actual model.
        """
        # check if add or edit menu was used
        # --> If the combobox is hidden, the add-iv-dialog was used, otherwise the edit-iv-dialog was used (cannot use index != -1 as this can also happen for the edit-iv-dialog if the user deletes all ivs)
        if self.comboBox_selectiv.isHidden():
            # if add menu was used, add the ivs to the temporary model with the now confirmed and valid iv name
            new_iv_name = self.lineEdit_nameinput.text()
            self.current_ivs_temp[new_iv_name] = self.values_to_add.copy()

        super().accept()

    def on_combobox_activated(self):
        """
        View-Changes if an element in the combobox is selected.
        En-/Disables elements and controls text in the dialog.
        """
        if self.comboBox_selectiv.currentIndex() != -1:
            self.btn_delete_iv.setEnabled(True)
            self.lineEdit_nameinput.setEnabled(True)
            self.lineEdit_valueinput.setEnabled(True)
            self.btn_editconfirm.setEnabled(True)
            self.btn_addvalue.setEnabled(True)
            self.lineEdit_nameinput.setText(self.comboBox_selectiv.currentText())

            # set the stored values for the selected IV
            self.tableWidget_storedvalues.setRowCount(0)  # clear the table widget
            for var, variables in self.current_ivs_temp.items():
                if var == self.comboBox_selectiv.currentText():
                    for value in reversed(variables):
                        self.add_item_to_stored_values(
                            item_text=value, item_column=1, checkbox_column=0
                        )

            # lastly, manually call the name input change function, to avoid a bug where the user types in a duplicate name, does not confirm it and switches to the iv with the duplicate name, for which no name change is detected and the save button is falsly disabled
            self.check_varname_changed()

        else:
            self.btn_delete_iv.setEnabled(False)
            self.lineEdit_nameinput.setEnabled(False)
            self.lineEdit_valueinput.setEnabled(False)
            self.btn_editconfirm.setEnabled(False)
            self.btn_addvalue.setEnabled(False)
            self.lineEdit_nameinput.setText("")
            # if combobox empty (all variables deleted), always enable save-button
            self.tableWidget_storedvalues.setRowCount(0)  # clear the table widget
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)

    def on_input_change_confirmed(self):
        """
        This method is called when the change of the IV-name is confirmed by the user after clicking the confirm button.

        It checks the name and sets the model accordingly.
        """

        old_name = self.comboBox_selectiv.currentText()
        new_name = self.lineEdit_nameinput.text()

        # check if the new name is the same as the old name, if so, do nothing
        # --> Bug exists as the user can change the name to the same name, which would and should not trigger the invalid name errors (save button disabled, ...).
        if new_name == old_name:
            return

        self.comboBox_selectiv.setItemText(
            self.comboBox_selectiv.currentIndex(), new_name
        )
        # update the temporary model with the new name
        # 1. copy the values of the old iv
        variables_copy = self.current_ivs_temp[old_name].copy()
        # 2. add a new entry with the new name and the copied values
        self.current_ivs_temp[new_name] = variables_copy
        # 3. remove the old entry
        del self.current_ivs_temp[old_name]

        # the result is that the old iv is removed and a new iv with the new name is added to the temporary model. Also the combobox is updated with the new name.
        # --> Any newly added values or removed values are now stored in the temporary model under the new name, as the temporary model is in sync with the combobox again
        return

    def add_new_iv_value(self):
        """
        Adds a new value to the stored values in the table widget.

        This method checks if the input value is valid and not a duplicate. If the input value is valid and not a duplicate,
        it adds the value to the table widget and clears the input field. Otherwise, it displays an error message.
        """
        # TODO: Check for conformity with model in controller/only do if no duplicates etc.
        new_value = self.lineEdit_valueinput.text()

        # check if input is given, if not inform user about the error and return
        if new_value == "":
            self.lineEdit_valueinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_valueinputwarning.setText("Please input a name!")
            return

        if new_value.isspace() or new_value.startswith(" ") or new_value.endswith(" "):
            self.lineEdit_valueinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_valueinputwarning.setText(
                "Name not valid! (No space at start/end)"
            )
            self.lineEdit_valueinput.setText("")
            return

        old_row_count = self.tableWidget_storedvalues.rowCount()

        # TODO: Outsource in "global" function -> Check if value to add is already in the stored values
        is_duplicate = False
        for row in range(old_row_count):
            if new_value == self.tableWidget_storedvalues.item(row, 1).text():
                is_duplicate = True
                break

        if is_duplicate:
            self.lineEdit_valueinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_valueinputwarning.setText("Duplicate values not allowed!")
        else:
            self.lineEdit_valueinput.setText("")
            self.add_item_to_stored_values(
                item_text=new_value, item_column=1, checkbox_column=0
            )

            # NOTE: Idea of the combobox is that it is always in sync with the/a direct representation of the temporary model, which means the combobox entries should always be the same as the keys in the temporary model
            # add the new value either to the temporary model (if the iv is already in the temporary model) or to the list of values to add (if the iv is not yet in the temporary model)
            if (
                self.comboBox_selectiv.currentIndex() != -1
            ):  # --> Current index == -1 means that either no IV is selected or the editor is called for the add-IV-dialog, where the hidden combobox is empty and therefore the index is -1
                for var, variables in self.current_ivs_temp.items():
                    if var == self.comboBox_selectiv.currentText():
                        variables.append(new_value)
                        # sort the values in the temporary model alphabetically
                        variables.sort()
            else:  # if the IV is not yet in the temporary model (add-iv-workflow), add the value to the list of values to add
                self.values_to_add.append(new_value)
                # sort the values alphabetically
                self.values_to_add.sort()

            self.lineEdit_valueinput.setStyleSheet(
                "QLineEdit { border: 1px solid black; }"
            )
            self.label_valueinputwarning.setText("")

        self.lineEdit_valueinput.setFocus()

    # TODO: Testfunction for adding checkboxes and new items in general to table widgets --> Make it global maybe later
    def add_item_to_stored_values(
        self, item_text: str, item_column: int, checkbox_column: int
    ):
        """
        Adds a checkbox with the correct style at the correct position and a new item at the correct position to the table widget.

        Parameters:
        - item_text (str): The text of the new item.
        - item_column (int): The column in which the new item should be added.
        """
        self.tableWidget_storedvalues.insertRow(0)

        new_item = QTableWidgetItem(item_text)
        self.tableWidget_storedvalues.setItem(0, item_column, new_item)

        checkbox_item = QTableWidgetItem()
        checkbox_item.setFlags(
            Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled
        )
        checkbox_item.setCheckState(Qt.CheckState.Unchecked)
        self.tableWidget_storedvalues.setItem(0, checkbox_column, checkbox_item)

    def remove_selected_values(self):
        """
        Removes the selected values from the table widget that
        contains all variants for the IV.
        """
        for row in range(self.tableWidget_storedvalues.rowCount() - 1, -1, -1):
            if (
                self.tableWidget_storedvalues.item(row, 0).checkState()
                == Qt.CheckState.Checked
            ):
                value_name = self.tableWidget_storedvalues.item(row, 1).text()
                self.tableWidget_storedvalues.removeRow(row)
                # remove the value from the temporary model or the list of values to add
                if (
                    self.comboBox_selectiv.currentIndex() != -1
                ):  # --> Current index == -1 means that either no IV is selected or the editor is called for the add-IV-dialog, where the hidden combobox is empty and therefore the index is -1
                    for var, variables in self.current_ivs_temp.items():
                        if var == self.comboBox_selectiv.currentText():
                            # remove the value from the temporary model
                            for value in variables:
                                if value == value_name:
                                    variables.remove(value)
                else:  # if the IV is not yet in the temporary model (add-iv-workflow), remove the value from the list of values to add
                    for elem in self.values_to_add:
                        if elem == value_name:
                            self.values_to_add.remove(elem)

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

        # return if combobox is empty (all variables deleted) and visible ("add"-dialog always has count == 0 so would always return, but there the combobox is hidden), as name-change is initiated by the system (not the user) as no variable to display is left
        # --> is handled in on_combobox_activated(), which is the source of the "exception"
        if (
            self.comboBox_selectiv.count() == 0
            and self.comboBox_selectiv.isVisible()
        ):
            return

        variable_name = self.lineEdit_nameinput.text()
        # TODO: Also check if name is duplciate
        if (
            not variable_name.strip()
            or variable_name.startswith(" ")
            or variable_name.endswith(" ")
        ):  # or variable_name_is_duplicate == False
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_variableinputwarning.setText("No (valid) name input!")
            self.btn_editconfirm.setEnabled(False)
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(
                False
            )
        elif (
            variable_name in self.current_ivs_temp.keys()
            and variable_name != self.comboBox_selectiv.currentText()
        ):  # duplicate name check, which is only relevant if the name is not the same as the name of the currently selected IV (as the name of the currently selected IV is always in the temporary model before the user changes it, so it is always a duplicate)
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid red; }"
            )
            self.label_variableinputwarning.setText("Duplicate name!")
            self.btn_editconfirm.setEnabled(False)
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(
                False
            )
        else:
            self.lineEdit_nameinput.setStyleSheet(
                "QLineEdit { border: 1px solid black; }"
            )
            self.label_variableinputwarning.setText("")
            self.btn_editconfirm.setEnabled(True)
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)

    # Override Keypress-Event -> Dont close Dialog while pressing enter/escape
    def keyPressEvent(self, arg__1: QKeyEvent) -> None:
        pass
        # if(arg__1.key() == Qt.Key.Key_Enter):
        #     self.add_iv_value()

    def remove_current_iv(self):
        """
        Remove the currently selected item from the combo box and add it to the list of removed formats.

        This method removes the currently selected item from the combo box `comboBox_selectiv` and deletes it from the temporary model.
        The selected item is determined by the current index of the combo box.

        Note:
        - The method only removes the item if an iv is selected (i.e., the selected index is not -1).
        - The delete button should be enabled only when a format is selected.

        """
        selected_index = self.comboBox_selectiv.currentIndex()
        if (
            selected_index != -1
        ):  # Check if an item is selected (should always be as delete-button only enabled if format is selected)
            # self.list_of_removed_ivs.append(self.comboBox_selectiv.itemText(selected_index))
            remove_iv_name = self.comboBox_selectiv.itemText(selected_index)
            self.comboBox_selectiv.removeItem(selected_index)
            # remove the iv from the temporary model dictionary
            del self.current_ivs_temp[remove_iv_name]

    def return_temporary_iv_data(self):
        """
        Returns the temporary IVs to the controller. The controller can then propagate the changes to the model, if the user saves the changes.

        Returns:
        - Dict[str, List[str]]: The temporary IVs.
        """
        return self.current_ivs_temp
