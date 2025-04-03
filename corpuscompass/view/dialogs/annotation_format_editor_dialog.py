from typing import Dict, List, Tuple


from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QTableWidgetItem,
    QListWidgetItem,
)
from PySide6.QtCore import Signal, Qt, QModelIndex, QSize
from PySide6.QtGui import (
    QStandardItemModel,
    QDragEnterEvent,
    QDropEvent,
)

from corpuscompass.view.font_configs import FontColors, FontConfig
from corpuscompass.view.generated.ui_annotationformat_editor_dialog import (
    Ui_EditorAnnotationformatDialog,
)
from corpuscompass.view.utils import split_string_with_token_and_identifier


class AnnotationFormatEditorDialog(QDialog, Ui_EditorAnnotationformatDialog):
    """
    Class for the annotation-specification-dialog. This window enables choosing
    and specifying a (custom) annotation format.
    """

    # Signal --> emitted when the user changes the input format in the dialog
    format_changed = Signal()

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Annotation-Format-Editor")

        # save the original drop event functions to call them after the custom drop event function (otherwise the event will not be handled correctly and the drop will not be executed (Bug?))
        self.old_input_drop_event = self.listwidget_annotdial_inputformat.dropEvent
        self.old_symbol_drop_event = (
            self.listwidget_annotdial_separatorsymbols.dropEvent
        )
        self.old_trashcan_drop_event = self.listwidget_annotformat_removeelems.dropEvent

        # Data structure that stores a temporary list of all symbols, formats, ... --> used for saving modifications to the data without overwriting the original data before the user confirms the changes
        self.current_formats_temp: Dict[str, List[str]] = {}

        # temporary data structure to track if the checkbox for a format was checked or not
        # --> Explicitly done as the checkbox state will not be relevant for storing the data in the model
        self.current_format_checkboxes_temp: Dict[str, bool] = {}

        # Store the name of the combobox item that was selected last, the current format, the input format, and the separator symbols
        # --> If the combobox item is changed, the data will be stored in the temporary model and then update to the new selected item
        self.currently_edited_format = ""
        self.current_input_format = ""
        self.current_separator_symbols = []

        # show/hide elements
        self.groupBox_softwarebtns.hide()
        self.label_4.hide()
        self.btn_loadmore.hide()

        # TODO: remove following line later, as en/disabled needs to be dynamically checked for an edited format
        # self.listwidget_annotdial_separatorsymbols.setEnabled(True)

        # bool value that tracks if 'warning'-dialog should be shown
        self.dont_show_removaldialog = False
        self.list_of_removed_formats = []

        self.comboBox_selectformat.setCurrentIndex(-1)

        # NOTE: Test-Data for the listwidget_annotdial_inputformat
        # self.add_row_preview_table("token", "1", "token.identifier")

        # set initial properties
        self.add_init_token_identifier()

    def add_init_token_identifier(self):
        """
        This function adds the initial "token" and "identifier" items to the list widget.
        It sets the font, color, and size of the items to make them stand out.
        """
        self.add_init_token()
        self.add_init_identifier()

    def add_init_token(self):
        """
        This function adds the "token" item to the list widget.
        It sets the font, color, and size of the item to make it stand out.
        """
        font = FontConfig.get_standardized_font(16, True)

        token_item = QListWidgetItem("token")
        token_item.setForeground(FontColors.TOKEN)
        token_item.setFont(font)
        token_item.setSizeHint(token_item.sizeHint() + QSize(10, 0))

        self.listwidget_annotformat_tokenidentcontainer.addItem(token_item)

    def add_init_identifier(self):
        """
        This function adds the "identifier" item to the list widget.
        It sets the font, color, and size of the item to make it stand out.
        """
        font = FontConfig.get_standardized_font(16, True)

        identifier_item = QListWidgetItem("identifier")
        identifier_item.setForeground(FontColors.IDENTIFIER)
        identifier_item.setFont(font)

        self.listwidget_annotformat_tokenidentcontainer.addItem(identifier_item)

    def add_symbol_to_list(self, symbol):
        """
        Adds a symbol to the list widget.

        Parameters:
        - symbol (str): The symbol to add to the list widget.
        """
        add_item = QListWidgetItem(symbol)
        add_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listwidget_annotformat_symbolcontainer.addItem(add_item)

    def fill_symbol_list(self, symbol_list):
        """
        Fills the list widget with all available symbols (set in the model).

        Parameters:
        - symbol_list (List[str]): A list of symbols to fill the list widget with.
        """
        for symbol in symbol_list:
            self.add_symbol_to_list(symbol)
        self.listwidget_annotformat_symbolcontainer.sortItems(
            order=Qt.SortOrder.DescendingOrder
        )

    def clear_input_format(self):
        """
        Clears the input format and token/identifier container in the annotation format editor dialog.
        This function is called when the user clicks the reset button to clear the input format.
        It also adds the initial "token" and "identifier" items to the token/identifier container.
        """
        self.listwidget_annotdial_inputformat.clear()
        self.listwidget_annotformat_tokenidentcontainer.clear()
        self.add_init_token_identifier()
        # manually call reactions to a change input-format, as listwidget.itemChanged.connect() does not automatically detected listwidget.clear() calls, only drag-and-drop
        # -> if input is cleared, then listwidget-items change (undetected due to clear) -> explicit call necessary
        # => Programmer-Note: Explicit call necessary whenever (!) listwidget is cleared/added in the code (so no drag and drop)
        self.on_format_changed()
        self.update_temporary_formats()

        # print("COUNT: ", self.listwidget_annotdial_separatorsymbols.count())

    def clear_separator_symbols(self):
        """
        Clears the field for separator symbols in the annotation format editor dialog.
        This function is called when the user clicks the reset button to clear the separator symbols.
        """
        # manually call reactions to a change input-format, as listwidget.itemChanged.connect() does not automatically detected listwidget.clear() calls, only drag-and-drop
        self.listwidget_annotdial_separatorsymbols.clear()
        self.on_format_changed()
        self.update_temporary_formats()

    def trashcan_separator_drag_enter_event(self, event: QDragEnterEvent):
        """
        Handles the drop event in the annotation format editor dialog.
        This function is called when the user drags any item into the "trashcan" list widget or the multiple annotation symbols list widget.

        Description:
        - This function checks if the mime data has the format 'application/x-qabstractitemmodeldatalist', which is the format of the items in the list widgets.
        - It extracts the item name from fitting events and checks if the item is not "token" or "identifier", as these items should not be moved into the trashcan or the multiple annotation symbols list widget.
        Otherwise, the event is accepted.
        """
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            # --> Retrieves the item name from the event where the mimeData has format application/x-qabstractitemmodeldatalist (can't do .text() due to the format)
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(
                data, Qt.DropAction.CopyAction, 0, 0, QModelIndex()
            )
            item_text = source_item.item(0, 0).text()

            if not (item_text == "token" or item_text == "identifier"):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def input_drag_enter_event(self, event: QDragEnterEvent):
        """
        Handles the drag enter event in the annotation format editor dialog.
        This function is called when the user drags any item into the input format list widget.

        Description:
        - This function checks if the mime data has the format 'application/x-qabstractitemmodeldatalist', which is the format of the items in the list widgets.
        - It checks the source of the drag-event and ignores any events where the source is the input for the separator symbols list widget.
        """
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            # --> Retrieves the item name from the event where the mimeData has format application/x-qabstractitemmodeldatalist (can't do .text() due to the format)
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(
                data, Qt.DropAction.CopyAction, 0, 0, QModelIndex()
            )
            # item_text = source_item.item(0, 0).text()

            if event.source() != self.listwidget_annotdial_separatorsymbols:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def input_change_event(self, event: QDropEvent):
        """
        Handles the drop event in the annotation format editor dialog for the input format field. The function just has to accept the event, but before that, send a signal that the format has changed.
        """
        self.old_input_drop_event(event)
        # after the drop was accepted and the item was added to the list widget, the format has changed --> either update it directly or send a signal to the format_change_handler (just function call works here for now)
        self.update_temporary_formats()
        self.on_format_changed()

    def separator_symbol_change_event(self, event: QDropEvent):
        """
        Handles the drop event in the annotation format editor dialog for the separator symbols field. The function just has to accept the event, but before that, send a signal that the format has changed.
        """
        self.old_symbol_drop_event(event)
        # after the drop was accepted and the item was added to the list widget, the format has changed --> either update it directly or send a signal to the format_change_handler (just function call works here for now)
        self.update_temporary_formats()
        self.on_format_changed()

    def trashcan_drop_event(self, event: QDropEvent):
        """
        Handles the drop event in the annotation format editor dialog.
        This function is called when the user drags and drops any item into the "trashcan" list widget or the multiple annotation symbols list widget.

        Description:
        - This function checks if the mime data has the format 'application/x-qabstractitemmodeldatalist', which is the format of the items in the list widgets.
        - It extracts the item name from fitting events and checks if the item is not "token" or "identifier", as these items should not be moved into the trashcan or the multiple annotation symbols list widget.
        Otherwise, the event is accepted.
        """
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            # --> Retrieves the item name from the event where the mimeData has format application/x-qabstractitemmodeldatalist (can't do .text() due to the format)
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(
                data, Qt.DropAction.CopyAction, 0, 0, QModelIndex()
            )
            item_text = source_item.item(0, 0).text()

            # accept the event if the item is a symbol (not token or identifier) and the source is not the symbol list widget (as the symbol list widget should not be able to receive items from itself, only from the input format list widget. Also, symbols should not be moved from the container to the trashcan)
            if not (item_text == "token" or item_text == "identifier"):
                self.old_trashcan_drop_event(
                    event
                )  # --> Accepts the event and adds the item to the list widget (otherwise the drop will not be executed)
                # NOTE: JUST A TEMPORARY FIX --> If the event is accepted, the item is not immediately removed from the listwidget, but only after the event is handled, which comes after the drop-event in the internal event-handling of the PySide-framework
                # --> Check if item is the last item in the separator symbols list widget, if so, send the information to the format_change_handler that this drop event empties the list widget
                # An accepted event either means that the item was dropped into the trashcan or the multiple annotation symbols list widget. The PySide-framework does not send the correct signal if the item is dropped into the trashcan, so the event is handled here.
                if (
                    self.listwidget_annotdial_separatorsymbols.count() <= 1
                    and event.source() == self.listwidget_annotdial_separatorsymbols
                ):
                    self.on_format_changed(removing_last_separator=True)
                    self.update_temporary_formats()
                else:
                    self.on_format_changed()
                    self.update_temporary_formats()
            else:
                event.ignore()
        else:
            event.ignore()

    # Edit-Functions
    def remove_selected_format(self):
        """
        Remove the selected format from the combo box and add it to the list of removed formats.

        This method removes the currently selected format from the combobox and adds it to a list of removed formats.
        The combo box should always have an item selected when this method is called, as the delete button is only enabled
        when a format is selected.
        """
        selected_index = self.comboBox_selectformat.currentIndex()
        if (
            selected_index != -1
        ):  # Check if an item is selected (should always be as delete-button only enabled if format is selected)
            del self.current_formats_temp[self.comboBox_selectformat.currentText()]
            del self.current_format_checkboxes_temp[
                self.comboBox_selectformat.currentText()
            ]
            self.currently_edited_format = "CALLED_FROM_REMOVE"
            self.comboBox_selectformat.removeItem(selected_index)

    def fetch_current_format(self):
        """
        Fetches the current format from the input format list widget.

        This method fetches the current format from the input format list widget and returns it as a string.
        """
        current_format = ""
        for index in range(self.listwidget_annotdial_inputformat.count()):
            item = self.listwidget_annotdial_inputformat.item(index)
            current_format += item.text()
        return current_format

    def fetch_current_separator_symbols(self):
        """
        Fetches the current separator symbols from the separator symbols list widget.

        This method fetches the current separator symbols from the separator symbols list widget and returns them as a list of strings.
        """
        separator_symbols = []
        if self.checkbox_annotdial_multipleannot.isChecked():
            for index in range(self.listwidget_annotdial_separatorsymbols.count()):
                item = self.listwidget_annotdial_separatorsymbols.item(index)
                separator_symbols.append(item.text())
        return separator_symbols

    def update_temporary_dialog_model(self):
        """
        Saves the current format and separator symbols in the temporary data structure and changes the variables that track the current input format data and separator symbols for the currently selected format.

        Returns: Returns True if the format that is about to be saved is a duplicate, otherwise False.
        """

        # HERE: Check if the input for just the current format is valid (not empty etc.), if so, proceed, otherwise saving will not be done in order to not save invalid data
        if not self.check_for_valid_currently_edited_format():  # if the changes made the format invalid, no data is saved and the software continues like no changes were made NOTE: Later an impl can be added to show an error message to the user
            return False

        # fetch the current format and separator symbols from the list widgets again to get the data for the format that was previously selected in the combobox
        # --> changes to the listwidget are only done in this function after this point, so the data is still valid
        self.update_temporary_formats()

        if (
            self.currently_edited_format != "CALLED_FROM_REMOVE"
        ):  # NOTE: Quickfix to prevent saving a previously removed format
            # save the data from the old format before changing the combobox
            if self.currently_edited_format == self.current_input_format:
                # only update the symbols as the input format stayed the same
                self.current_formats_temp[self.currently_edited_format] = (
                    self.current_separator_symbols
                )
                return False
            elif self.current_input_format in self.current_formats_temp.keys():
                # if the input format was changed to a format that was already in the temp data --> error case (requires future handling) TODO: Implement error handling
                # current error handling: Data changes are just not saved after switching to another format/saving it for the edited format
                if self.comboBox_selectformat.isVisible():
                    self.comboBox_selectformat.setCurrentText(
                        self.currently_edited_format
                    )
                return True  # --> returning here, as the combobox was set back to the old format
            else:  # new format is different form all others --> delete the currently edited format (old) and add the new one
                if self.comboBox_selectformat.isVisible():  # --> if combobox is visible, then the user edits a format which results in the deletion of the old format and the addition of the new one
                    self.current_formats_temp[self.current_input_format] = (
                        self.current_separator_symbols
                    )
                    self.current_format_checkboxes_temp[self.current_input_format] = (
                        self.checkbox_annotdial_multipleannot.isChecked()
                    )
                    del self.current_formats_temp[self.currently_edited_format]
                    del self.current_format_checkboxes_temp[
                        self.currently_edited_format
                    ]
                    # also change the name of the format in the combobox by finding the index of the currently_edited_format and changing the text
                    index = self.comboBox_selectformat.findText(
                        self.currently_edited_format
                    )
                    self.comboBox_selectformat.setItemText(
                        index, self.current_input_format
                    )
                else:  # if not visible, then the user adds a new format, which results in the addition of the new format without deleting the old one (can be done because duplicate check is done before)
                    self.current_formats_temp[self.current_input_format] = (
                        self.current_separator_symbols
                    )
                    self.current_format_checkboxes_temp[self.current_input_format] = (
                        self.checkbox_annotdial_multipleannot.isChecked()
                    )
                return False
        else:
            return False

    def on_combobox_activated(self):
        """
        View-Changes if an element in the combobox is selected.
        En-/Disables elements and controls text in the dialog.

        """
        if self.comboBox_selectformat.currentIndex() != -1:
            # fetch the current format and separator symbols from the list widgets again to get the data for the format that was previously selected in the combobox
            self.update_temporary_dialog_model()

            self.btn_delete_annotformat.setEnabled(True)
            self.widget_specificationcontents.setEnabled(True)
            self.listwidget_annotformat_tokenidentcontainer.clear()
            self.listwidget_annotdial_inputformat.clear()
            self.listwidget_annotdial_separatorsymbols.clear()
            format_as_array = split_string_with_token_and_identifier(
                self.comboBox_selectformat.currentText()
            )
            separator_symbols = self.get_separator_symbols_from_temp(
                self.comboBox_selectformat.currentText()
            )
            # Add all elements of the annotation format to the input format if "edit-format"-option is chosen
            for elem in format_as_array:
                add_item = QListWidgetItem(elem)
                if elem == "token":
                    add_item.setForeground(FontColors.TOKEN)
                elif elem == "identifier":
                    add_item.setForeground(FontColors.IDENTIFIER)
                self.listwidget_annotdial_inputformat.addItem(add_item)

            if len(separator_symbols) > 0:
                for elem in separator_symbols:
                    add_item = QListWidgetItem(elem)
                    add_item.setFont(FontConfig.get_standardized_font(16, True))
                    self.listwidget_annotdial_separatorsymbols.addItem(add_item)
                self.checkbox_annotdial_multipleannot.setChecked(True)
            else:  # if no separator symbols are stored for the selected format, uncheck the checkbox as the user can only save empty separator symbol lists if the checkbox is unchecked
                self.checkbox_annotdial_multipleannot.setChecked(False)

            # manually call reactions to a change input-format, as this is not automatically detected for explicit listwidget.add/clear calls, only for drag-and-drop
            # -> if combobox changes, the input-format changes, which means that the listwidget-items change (undetected), which is why this call is necessary
            # this is only undetected for listwidget.add/clear calls, not for textedit changes
            self.on_format_changed()

            # in the end, set the currently edited format to the new selected format and change the input formats
            self.currently_edited_format = self.comboBox_selectformat.currentText()
            self.update_temporary_formats()

        # if the combobox is empty (all formats deleted), disable all elements and reset editor to initial state
        else:
            self.btn_delete_annotformat.setEnabled(False)
            self.widget_specificationcontents.setEnabled(False)
            self.checkbox_annotdial_multipleannot.setChecked(False)
            self.listwidget_annotdial_inputformat.clear()
            self.listwidget_annotdial_separatorsymbols.clear()
            self.label_inputwarningmessage.setText("")
            self.btn_save.setEnabled(True)
            self.btn_cancel.setEnabled(True)
            # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)
            self.listwidget_annotdial_inputformat.setStyleSheet(
                "QListWidget{ border: 1px solid black ; }"
            )
            self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                "QListWidget{ border: 1px solid black ; }"
            )
            self.add_init_token_identifier()

    def update_temporary_formats(self):
        """
        Updates the temporary format list whenever the user changes the format or the separator symbols in the dialog.
        """
        self.current_input_format = self.fetch_current_format()
        self.current_separator_symbols = self.fetch_current_separator_symbols()

    def on_format_changed(self, removing_last_separator=False):
        """
        Handle the event when the annotation format is changed (by changing the combobox element or by direct user interaction). It updates the view with hints and warnings based on the validity of the input data.

        This function checks if the input format is valid based on the items in the listwidget.
        If both "token" and "identifier" are present in the listwidget, the input is considered valid.
        The function updates the styling and warning message accordingly, and enables/disables the save button.
        """
        # return if combobox is empty (all formats deleted), as format-change is initiated by the system due to the deletion of the last format (not the user) as no format to display is left
        # --> is handled in on_combobox_activated(), which is the source of the "exception"
        if (
            self.comboBox_selectformat.count() == 0
            and self.comboBox_selectformat.isVisible()
        ):
            return

        if self.listwidget_annotdial_inputformat.count() != 0:
            has_token = False
            has_identifier = False

            # Iterate over items in the list
            for index in range(self.listwidget_annotdial_inputformat.count()):
                item = self.listwidget_annotdial_inputformat.item(index)
                if item.text() == "token":
                    has_token = True
                elif item.text() == "identifier":
                    has_identifier = True

            # Check if both "token" and "identifier" are present
            if has_token and has_identifier:
                # only needs to be checked if the checkbox for multiple annotations is checked, as they are only relevant in this case (e.g. empty separator symbol list is valid if checkbox is not checked)
                if self.checkbox_annotdial_multipleannot.isChecked():
                    separator_symbols_valid = self.check_separator_symbols(
                        removing_last_separator=removing_last_separator
                    )
                    if not separator_symbols_valid:
                        self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                            "QListWidget { border: 2px solid red; }"
                        )
                        self.label_inputwarningmessage.setStyleSheet(
                            "QLabel { color: red; }"
                        )
                        self.label_inputwarningmessage.setText(
                            "Invalid Separator Symbols!"
                        )
                        # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False) # NOTE: For simplicity commented out, but includes logic for enabling/disabling save button based on validitiy of input
                        # return if separator symbols are invalid, as the input is invalid in this case, otherwise the code below would be executed as well
                        return
                    else:
                        self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                            "QListWidget { border: 2px solid green; }"
                        )
                # this is done if input and separator symbols are valid
                self.listwidget_annotdial_inputformat.setStyleSheet(
                    "QListWidget { border: 2px solid green; }"
                )
                self.label_inputwarningmessage.setStyleSheet("QLabel { color: green; }")
                self.label_inputwarningmessage.setText("Input is valid")
                # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True) # NOTE: For simplicity commented out, but includes logic for enabling/disabling save button based on validitiy of input
            else:
                self.listwidget_annotdial_inputformat.setStyleSheet(
                    "QListWidget { border: 2px solid red; }"
                )
                self.label_inputwarningmessage.setStyleSheet("QLabel { color: red; }")
                self.label_inputwarningmessage.setText("Missing Token/Identifier!")
                # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False) # NOTE: For simplicity commented out, but includes logic for enabling/disabling save button based on validitiy of input

                # --> Needed for the case where user clicks on reset button for the separator symbols but the input listwidget ist already invalid. In this case, the separator symbols listwidget needs to be updated here
                if self.checkbox_annotdial_multipleannot.isChecked():
                    separator_symbols_valid = self.check_separator_symbols(
                        removing_last_separator=removing_last_separator
                    )
                    if not separator_symbols_valid:
                        self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                            "QListWidget { border: 2px solid red; }"
                        )
                        self.label_inputwarningmessage.setStyleSheet(
                            "QLabel { color: red; }"
                        )
                        return
                    else:
                        self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                            "QListWidget { border: 2px solid green; }"
                        )

        # If the list is empty, the input is invalid
        else:
            self.listwidget_annotdial_inputformat.setStyleSheet(
                "QListWidget { border: 2px solid red; }"
            )
            self.label_inputwarningmessage.setStyleSheet("QLabel { color: red; }")
            self.label_inputwarningmessage.setText("Format cannot be empty!")
            # self.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False) # NOTE: For simplicity commented out, but includes logic for enabling/disabling save button based on validitiy of input

            # --> Needed for the case where user clicks on reset button for the separator symbols but the input listwidget ist already invalid. In this case, the separator symbols listwidget needs to be updated here
            if self.checkbox_annotdial_multipleannot.isChecked():
                separator_symbols_valid = self.check_separator_symbols(
                    removing_last_separator=removing_last_separator
                )
                if not separator_symbols_valid:
                    self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                        "QListWidget { border: 2px solid red; }"
                    )
                    self.label_inputwarningmessage.setStyleSheet(
                        "QLabel { color: red; }"
                    )
                    return
                else:
                    self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                        "QListWidget { border: 2px solid green; }"
                    )

    def check_separator_symbols(self, removing_last_separator):
        """
        Checks if the separator symbols are valid.

        This function checks if the separator symbols are valid based on the items in the listwidget.
        If the listwidget is empty, the separator symbols are considered valid.

        Parameters:
        NOTE: FOR TEMPORARY FIX:
        - removing_last_separator (bool): A boolean value that indicates if the current call of the function is due to the removal of the last separator symbol in the list widget.
        This is done to catch the case where the last separator symbol is removed, but the list widget is not updated yet, as the event is not handled yet, which leads to a count of 1 for the separator symbols list widget.
        """
        if self.listwidget_annotdial_separatorsymbols.count() == 0 or (
            self.listwidget_annotdial_separatorsymbols.count() == 1
            and removing_last_separator
        ):
            return False
        else:
            return True

    def clear_trashcan_symbols(self):
        """
        Clears the trashcan list widget in the annotation format editor dialog.
        This function is called when the user clicks the reset button to clear the trashcan.
        """
        self.listwidget_annotformat_removeelems.takeItem(0)
        # self.on_format_changed(removing_last_separator=False)

    def on_multiple_annot_checked(self):
        """
        Handles the event when the "Multiple Annotations" checkbox is checked or unchecked.

        This function enables/disables the separator symbols list widget based on the state of the checkbox.
        """
        if self.checkbox_annotdial_multipleannot.isChecked():
            self.listwidget_annotdial_separatorsymbols.setEnabled(True)
            self.label_separator.setEnabled(True)
            self.btn_resetseparator.setEnabled(True)
        else:
            self.listwidget_annotdial_separatorsymbols.setStyleSheet(
                "QListWidget{ border: 1px solid black ; }"
            )
            self.listwidget_annotdial_separatorsymbols.setEnabled(False)
            self.label_separator.setEnabled(False)
            self.btn_resetseparator.setEnabled(False)

        # if the dialog is called for edit, the checking of a checkbox needs to be stored in the corresponding temporary data structure
        if self.comboBox_selectformat.isVisible():
            self.current_format_checkboxes_temp[
                self.comboBox_selectformat.currentText()
            ] = self.checkbox_annotdial_multipleannot.isChecked()
        # if the checkbox is changed, the separator symbols have to be checked as well, as they are only relevant if multiple annotations are allowed
        self.on_format_changed()
        # also update the current formats
        self.update_temporary_formats()

    def add_row_preview_table(
        self, left_column_data: str, middle_column_data: str, right_column_data: str
    ):
        """
        Adds a new row to the preview table widget in the annotation format editor dialog.

        Parameters:
        - left_column_data: The data for the left column of the new row.
        - middle_column_data: The data for the middle column of the new row.
        - right_column_data: The data for the right column of the new row.
        """
        font_size = 8

        current_row_count = self.tablewidget_annotdial_corpuspreview.rowCount()
        self.tablewidget_annotdial_corpuspreview.insertRow(current_row_count)

        left_item = QTableWidgetItem(left_column_data)
        left_item.setFont(FontConfig.get_standardized_font(font_size, True))
        left_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tablewidget_annotdial_corpuspreview.setItem(
            current_row_count, 0, left_item
        )

        middle_item = QTableWidgetItem(middle_column_data)
        middle_item.setFont(FontConfig.get_standardized_font(font_size, True))
        middle_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tablewidget_annotdial_corpuspreview.setItem(
            current_row_count, 1, middle_item
        )

        right_item = QTableWidgetItem(str(right_column_data))
        right_item.setFont(FontConfig.get_standardized_font(font_size, True))
        right_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tablewidget_annotdial_corpuspreview.setItem(
            current_row_count, 2, right_item
        )

    def clear_preview_table(self):
        """
        Clears the preview table widget in the annotation format editor dialog.
        """
        self.tablewidget_annotdial_corpuspreview.clearContents()
        self.tablewidget_annotdial_corpuspreview.setRowCount(0)

    def add_all_to_preview_table(self, data_list: List[Tuple[str, str, int]]):
        """
        Adds all corpus elements to the preview table widget in the annotation format editor dialog.

        Parameters:
        - data_list (List[Tuple[str, str, int]]): A list of tuples containing the data for the preview table (token, identifiers and number of identifiers).
        """
        self.clear_preview_table()
        for item in data_list:
            self.add_row_preview_table(item[0], str(item[2]), item[1])

    def get_separator_symbols_from_temp(self, format):
        """
        Retrieves the separator symbols from the temporary format changes.

        Parameters:
        - format (str): The format for which the separator symbols should be retrieved.

        Returns:
        - List[str]: A list of separator symbols for the given format.
        """
        for item, values in self.current_formats_temp.items():
            if item == format:
                return values
        return []

    def get_updated_data(self):
        """
        Retrieves the updated annotation formats from the dialog.

        Returns:
        - Dict[str, List[str]]: A dictionary containing the updated annotation formats.
        """
        return self.current_formats_temp

    # override the accept method to save the changes to the model
    def accept(self):
        """
        Saves the changes to the annotation formats in the dialog to the model.
        """
        # close the dialog and send signals via super method
        super().accept()

    def check_for_valid_currently_edited_format(self):
        """ "
        Checks just the currently edited format if it is valid.

        Returns: True if the format is valid, False otherwise.
        """
        if self.listwidget_annotdial_inputformat.count() == 0:
            return False
        # if not empty, check if it contains the token and identifier blocks
        if self.listwidget_annotdial_inputformat.count() != 0:
            has_token = False
            has_identifier = False
            # Iterate over items in the list
            for index in range(self.listwidget_annotdial_inputformat.count()):
                item = self.listwidget_annotdial_inputformat.item(index)
                if item.text() == "token":
                    has_token = True
                elif item.text() == "identifier":
                    has_identifier = True

            # Check if both "token" and "identifier" are present
            if not (has_token and has_identifier):
                return False
        # if the checkbox for multiple annotations is checked, the separator symbols have to be checked as well
        if (
            self.checkbox_annotdial_multipleannot.isChecked()
            and self.listwidget_annotdial_separatorsymbols.count() == 0
        ):
            return False
        else:
            return True

    def check_for_valid_formats(self):
        """
         Checks if all inputs are valid (if called for editing), or if the only input format is valid (if called for adding a new format).

        Returns:
        - bool: True if all formats are valid, False otherwise.
        """
        # if the dialog is called for adding a new format, only the input format needs to be checked, only if it is called for the edit all the other formats need to be checked as well
        if self.comboBox_selectformat.isVisible():
            # Check if all formats are valid
            for format, symbols in self.current_formats_temp.items():
                # First invalidity check: The format is either empty or does not include the token and identifier symbols
                if (
                    len(format) == 0
                    or "token" not in format
                    or "identifier" not in format
                ):
                    return False
                # Second invalidity check: The format is valid, but the separator symbols are not (which means they are empty and the checkbox for multiple annotations is checked)
                if self.current_format_checkboxes_temp[format] and len(symbols) == 0:
                    return False
        if (
            self.comboBox_selectformat.isHidden()
            or (
                self.comboBox_selectformat.isVisible()
                and self.comboBox_selectformat.currentIndex() != -1
            )
        ):  # if the combobox is visible but no formats exist, checks for an empty format would always return true therefore dont check
            # check if the input format is empty
            if self.listwidget_annotdial_inputformat.count() == 0:
                return False
            # if not empty, check if it contains the token and identifier blocks
            if self.listwidget_annotdial_inputformat.count() != 0:
                has_token = False
                has_identifier = False
                # Iterate over items in the list
                for index in range(self.listwidget_annotdial_inputformat.count()):
                    item = self.listwidget_annotdial_inputformat.item(index)
                    if item.text() == "token":
                        has_token = True
                    elif item.text() == "identifier":
                        has_identifier = True

                # Check if both "token" and "identifier" are present
                if not (has_token and has_identifier):
                    return False
            # if the checkbox for multiple annotations is checked, the separator symbols have to be checked as well
            if (
                self.checkbox_annotdial_multipleannot.isChecked()
                and self.listwidget_annotdial_separatorsymbols.count() == 0
            ):
                return False

        return True

    def get_current_format_as_string(self):
        """
        Retrieves the current format as a string.

        Returns:
        - str: The current format as a string.
        """
        format_text = ""
        for index in range(self.listwidget_annotdial_inputformat.count()):
            item = self.listwidget_annotdial_inputformat.item(index)
            format_text += item.text()

        return format_text
