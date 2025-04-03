from typing import Dict, List, Tuple
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QHeaderView,
    QTableWidgetItem,
    QColorDialog,
    QDialogButtonBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
)


from corpuscompass.view.font_configs import FontConfig
from corpuscompass.view.generated.ui_dv_editor_dialog import Ui_DVEditorDialog


class DVEditorDialog(QDialog, Ui_DVEditorDialog):
    """
    Class for the dialog that enables adding, editing and deleting DVs, as
    well as grouping the found variants inside them.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Editor: Dependent Variables")

        # Set initial properties (that are the same for every dialog and independent of dynamic data)
        self.comboBox_selectdv.setCurrentIndex(-1)
        self.tableWidget_dialog_dvaddvariants.setColumnWidth(1, 70)
        # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)

        # contains all of the current DVs and the corresponding variants that are grouped in them
        self.current_dvs_temp: Dict[str, Tuple[List[str], List[str]]] = {}

        # contains all of the detected variants
        self.detected_variants_temp: Dict[str, Tuple[int, str, str]] = {}

        # dict that has each variant as a key and the checkbox object as the value
        # --> used to access the checkbox object of a variant in the table widget
        self.variant_checkboxes: Dict[str, QTableWidgetItem] = {}

        # connect the cell changed signal to update the grouped dvs after a variant is checked/unchecked (only reacts to changes in the checkbox column)
        self.tableWidget_dialog_dvaddvariants.cellChanged.connect(
            self.update_dv_grouping
        )

        for column in range(self.tableWidget_dialog_dvaddvariants.columnCount()):
            self.tableWidget_dialog_dvaddvariants.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

        # list for dvs variants that will be grouped during the add-iv-dialog use
        # --> just store the name of the variants, as the re-grouping is done after the user confirms the dialog
        self.variants_to_add: List[str] = []

        # list for ivs that were deleted during dialog/editor use
        # self.list_of_removed_dvs = []

        # list for variants that will be grouped to a dv during the add-dv-dialog use
        # --> different from the edit-workflow as the variants are not added to the complete "temporary model" directly, but only after the user confirms the dialog, as there wont be an entry in the "temporary model" with the not yet confirmed dv name
        # stores the variant name and the color of the variant (hexadecimal code)
        # self.variants_to_add: Tuple[List[str], List[str]] = [] # TODO: PROBLEM -> Tuple is not mutable so maybe use something else as the elements in the tuple may need to change

    def accept(self) -> None:
        """
        Is called whenuser is accepting the dialog for adding or editing a
        DV and its variants. The method updates the final temporary model that will
        be returned to the controller later and closes the dialog.
        """
        # if the combobox is hidden -> temporary dv model does not yet include a key for the new dv, so add the new dv to the temporary model
        # --> if add-workflow: add the dv as a group to each grouped variant stored in the variants_to_add list (all variants that are grouped to the new dv, ungrouping from the old dv is done in the update_dv_grouping method)
        if self.comboBox_selectdv.isHidden():
            new_dv_name = self.lineEdit_nameinput.text()
            self.current_dvs_temp[new_dv_name] = ([], [])
            # add the variants to the temporary detected variants model
            # => this dictionary references to the DVs and can only contain DVs that are in the temporary model, so DV can be filled with the according variants
            for variant in self.variants_to_add:
                old_variant_data = self.detected_variants_temp[variant]
                self.detected_variants_temp[variant] = (
                    old_variant_data[0],
                    new_dv_name,
                    old_variant_data[2],
                )

        # clear the old data in the temporary model
        for dv in self.current_dvs_temp.keys():
            self.current_dvs_temp[dv] = ([], [])

        # fill the DVs with the variants that are grouped to them
        for detected_var, var_data in self.detected_variants_temp.items():
            # append DV with the variant (if the variant is grouped to a DV)
            if var_data[1] is not None:
                self.current_dvs_temp[var_data[1]][0].append(detected_var)
                # append the DV with the color of the variant
                self.current_dvs_temp[var_data[1]][1].append(var_data[2])

        # for other cases, the ivs are already in the temporary model and can be used directly
        # Close the Window
        super().accept()

    def on_combobox_activated(self):
        """
        View-Changes if an element in the combobox is selected.
        En-/Disables elements and controls text in the dialog.
        """

        # disconnect the cell changed signal as the combobox switch will trigger checkbox changes (to display the correct check states for the new DV)
        # and the cell changed signal will then regroup the variants, which should not be done as the user doesnt actively change the check states
        self.tableWidget_dialog_dvaddvariants.cellChanged.disconnect(
            self.update_dv_grouping
        )

        if self.comboBox_selectdv.currentIndex() != -1:
            self.btn_delete_dv.setEnabled(True)
            self.lineEdit_nameinput.setEnabled(True)
            self.btn_editconfirm.setEnabled(True)
            self.tableWidget_dialog_dvaddvariants.setEnabled(True)
            self.lineEdit_nameinput.setText(self.comboBox_selectdv.currentText())

            # set the stored values for the selected IV
            self.tableWidget_dialog_dvaddvariants.setRowCount(
                0
            )  # clear the table widget to load all variants of the selected DV again

            checked_variants = []
            unchecked_variants = []

            # reset the checkbox data structure (as the checkboxes are removed and added again)
            self.variant_checkboxes = {}

            for variant, variant_data in self.detected_variants_temp.items():
                # check if the variant is part of the newly selected DV
                if variant_data[1] == self.comboBox_selectdv.currentText():
                    checked_variants.append((variant, variant_data[2]))
                else:
                    unchecked_variants.append((variant, variant_data[2]))

            # Add unchecked variants first (will be pushed down to the bottom)
            for variant, color in unchecked_variants:
                self.add_item_to_variant_list(
                    item_text=variant, is_grouped_to_dv=False, variant_color=color
                )

            # Add checked variants after
            for variant, color in checked_variants:
                self.add_item_to_variant_list(
                    item_text=variant, is_grouped_to_dv=True, variant_color=color
                )

        else:
            self.btn_delete_dv.setEnabled(False)
            self.lineEdit_nameinput.setEnabled(False)
            self.btn_editconfirm.setEnabled(False)
            # uncheck all checkboxes
            for variant, checkbox in self.variant_checkboxes.items():
                checkbox.setCheckState(Qt.CheckState.Unchecked)

            self.tableWidget_dialog_dvaddvariants.setEnabled(False)
            self.lineEdit_nameinput.setText("")
            # if combobox empty (all variables deleted), always enable save-button
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)

        # reconnect the cell changed signal
        self.tableWidget_dialog_dvaddvariants.cellChanged.connect(
            self.update_dv_grouping
        )

    def on_input_change_confirmed(self):
        """
        This method is called when the change of the DV-name is confirmed by the user after clicking the confirm button.

        It checks the name and looks through all detected variants that had the old name --> updates the name of the DVs for theses variants.
        """
        old_name = self.comboBox_selectdv.currentText()
        new_name = self.lineEdit_nameinput.text()
        for detected_var, var_data in self.detected_variants_temp.items():
            if var_data[1] == old_name:
                self.detected_variants_temp[detected_var] = (
                    var_data[0],
                    new_name,
                    var_data[2],
                )
        # also change other temporary data structures
        if (
            old_name in self.current_dvs_temp.keys()
        ):  # check if the DV is already in the temporary model (which it should, but this prevents key errors)
            old_data = self.current_dvs_temp.pop(old_name)
            self.current_dvs_temp[new_name] = old_data
        self.comboBox_selectdv.setItemText(
            self.comboBox_selectdv.currentIndex(), new_name
        )

    def on_change_color_double_click(self, row, column):
        """
        Opens a color-selection-dialog, in which user can select a color.
        This color is then associated with the corresponding DV-Variant
        in the model.
        """

        # TODO: Check if another variable already has this color via the hexadecimal code

        # Only react on doubleClick on the last column (index == 2), as color should only be changed for this column
        if column == 2:
            color = QColorDialog.getColor()
            if color.isValid():
                item = QTableWidgetItem()
                item.setBackground(color)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                # Set flags -> No Text-Changes and no Selection-Highlighting
                flags = item.flags()
                flags &= ~Qt.ItemFlag.ItemIsEditable
                flags &= ~Qt.ItemFlag.ItemIsSelectable
                item.setFlags(flags)

                # Set color as a tooltip for user to know exact Hexadecimal-Code
                color_hexcode = color.name()
                item.setToolTip("Hexadecimal: " + color_hexcode)

                # Set item
                self.tableWidget_dialog_dvaddvariants.setItem(row, column, item)

                # get the name of the edited variant at position row, column 0
                variant_name = self.tableWidget_dialog_dvaddvariants.item(row, 0).text()

                for detected_var, var_data in self.detected_variants_temp.items():
                    if detected_var == variant_name:
                        self.detected_variants_temp[detected_var] = (
                            var_data[0],
                            var_data[1],
                            color_hexcode,
                        )

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
        # return if combobox is empty (all variables deleted), as name-change is initiated by the system (not the user) as no variable to display is left
        # --> is handled in on_combobox_activated(), which is the source of the "exception"
        if (
            self.comboBox_selectdv.count() == 0
            and self.comboBox_selectdv.isVisible()
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
            self.label_variableinputwarning.setText("No name (valid) input!")
            self.btn_editconfirm.setEnabled(False)
            self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(
                False
            )
        elif (
            variable_name in self.current_dvs_temp.keys()
            and variable_name != self.comboBox_selectdv.currentText()
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

    def filter_dv_names(self):
        """
        Filters the DV variant names in the table based on the text entered in the search variants line edit.

        The method retrieves the text from the search variants line edit, strips leading and trailing whitespace,
        and converts it to lowercase. It then iterates over each row in the table and checks if the name in the
        first column matches the entered text. If the name does not contain the entered text, the corresponding
        row in the table is hidden.
        """
        text = self.lineEdit_searchvariants.text().strip().lower()
        for row in range(self.tableWidget_dialog_dvaddvariants.rowCount()):
            item = self.tableWidget_dialog_dvaddvariants.item(row, 0)
            if item is not None:
                name = item.text().lower()
                self.tableWidget_dialog_dvaddvariants.setRowHidden(
                    row, text not in name
                )

    def remove_current_dv(self):
        """
        Remove the currently selected item from the combo box and add it to the list of removed formats.

        This method removes the currently selected item from the combo box `comboBox_selectdv` and adds it to the
        `list_of_removed_dvs`. The selected item is determined by the current index of the combo box.

        Note:
        - The method only removes the item if an item is selected (i.e., the selected index is not -1).
        - The delete button should be enabled only when a format is selected.

        """
        selected_index = self.comboBox_selectdv.currentIndex()
        if (
            selected_index != -1
        ):  # Check if an item is selected (should always be as delete-button only enabled if format is selected)
            # delete the dv from the temporary model dictionary
            del self.current_dvs_temp[self.comboBox_selectdv.itemText(selected_index)]
            # also remove the dv from all variants that are grouped to it
            for variant, variant_data in self.detected_variants_temp.items():
                if variant_data[1] == self.comboBox_selectdv.currentText():
                    self.detected_variants_temp[variant] = (
                        variant_data[0],
                        None,
                        variant_data[2],
                    )
            self.comboBox_selectdv.removeItem(selected_index)

    def add_item_to_variant_list(
        self, item_text: str, is_grouped_to_dv: bool, variant_color: str = None
    ):
        """
        Adds a checkbox with the correct style at the correct position and a new item at the correct position to the table widget.
        """
        self.tableWidget_dialog_dvaddvariants.insertRow(0)

        variant_name = QTableWidgetItem(item_text)
        variant_data = self.detected_variants_temp[item_text]
        if (
            variant_data[1] != self.comboBox_selectdv.currentText()
            and variant_data[1] is not None
        ):
            # if variant is already grouped to another DV, show this by changing the color of the text and adding a tooltip
            variant_name.setForeground(QColor("orange"))
            variant_name.setToolTip(
                "<b>Already grouped to: <u>"
                + variant_data[1]
                + "</u>. Checking the checkbox in this row will remove the variant from the other DV and add it to this DV.</b>"
            )
        else:
            variant_name.setForeground(QColor("black"))

        variant_name.setFont(FontConfig.get_standardized_font(10, True))

        self.tableWidget_dialog_dvaddvariants.setItem(0, 0, variant_name)

        checkbox_item = QTableWidgetItem()
        checkbox_item.setFlags(
            Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled
        )
        if is_grouped_to_dv:
            checkbox_item.setCheckState(Qt.CheckState.Checked)
        else:
            checkbox_item.setCheckState(Qt.CheckState.Unchecked)

        self.tableWidget_dialog_dvaddvariants.setItem(0, 1, checkbox_item)

        # add the variant to the checkbox data structure
        self.variant_checkboxes[item_text] = checkbox_item

        color_item = QTableWidgetItem()
        color_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        if variant_color is not None:
            # Set flags -> No Text-Changes and no Selection-Highlighting
            flags = color_item.flags()
            flags &= ~Qt.ItemFlag.ItemIsEditable
            flags &= ~Qt.ItemFlag.ItemIsSelectable
            color_item.setFlags(flags)

            # Set color as a tooltip for user to know exact Hexadecimal-Code
            color_hexcode = variant_color
            color_item.setToolTip("Hexadecimal: " + color_hexcode)
            color_item.setBackground(QColor(variant_color))
        else:
            color_item.setFont(FontConfig.get_standardized_font(10, True))
            color_item.setText("+ add color")
        self.tableWidget_dialog_dvaddvariants.setItem(0, 2, color_item)

    def update_dv_grouping(self, row: int, column: int):
        """
        Updates the grouping of a DV variant based on the updated checkbox state.
        """
        if column != 1:
            return  # return if the checkbox column was not changed
        else:
            changed_variant_name = self.tableWidget_dialog_dvaddvariants.item(
                row, 0
            ).text()
            if (
                self.tableWidget_dialog_dvaddvariants.item(row, column).checkState()
                == Qt.CheckState.Checked
            ):
                # add the variant to the DV (ALSO: if add-dv-dialog, the combobox index is -1 and the DV is not yet in the temporary model --> Follow different workflow)
                if self.comboBox_selectdv.currentIndex() != -1:
                    # --> this also automatically removes the variant from the DV it was previously grouped to (if it was grouped to another DV)
                    self.detected_variants_temp[changed_variant_name] = (
                        self.detected_variants_temp[changed_variant_name][0],
                        self.comboBox_selectdv.currentText(),
                        self.detected_variants_temp[changed_variant_name][2],
                    )
                else:
                    # remove them from their old DV if they were grouped to one and group them in a supporting structure thats used just for the add dialog
                    if self.detected_variants_temp[changed_variant_name][1] is not None:
                        self.detected_variants_temp[changed_variant_name] = (
                            self.detected_variants_temp[changed_variant_name][0],
                            None,
                            self.detected_variants_temp[changed_variant_name][2],
                        )
                    self.variants_to_add.append(changed_variant_name)
            else:
                # remove the variant from the DV, but only if the variant is actually grouped to currently selected DV (also differ between add- and edit-dialog)
                if self.comboBox_selectdv.currentIndex() != -1:
                    if (
                        self.detected_variants_temp[changed_variant_name][1]
                        == self.comboBox_selectdv.currentText()
                    ):
                        self.detected_variants_temp[changed_variant_name] = (
                            self.detected_variants_temp[changed_variant_name][0],
                            None,
                            self.detected_variants_temp[changed_variant_name][2],
                        )
                else:
                    # remove the variant from the list of variants to add (if the variant was added to the list before)
                    if changed_variant_name in self.variants_to_add:
                        self.variants_to_add.remove(changed_variant_name)

    def return_temporary_dv_data(self):
        """
        Returns the temporary DVs as well as the updated variants to the controller. The controller can then propagate the changes to the model, if the user saves the changes.
        Has to return two structures as both are changed during the dialog and have to be updated in the model.

        Returns:
        - Dict[str, List[str]]: The temporary DVs.
        - Dict[str, Tuple[int, str, str]]: The temporary variants.
        """
        return self.current_dvs_temp, self.detected_variants_temp
