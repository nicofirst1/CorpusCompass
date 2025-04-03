"""
The module contains the controller class, which is used to connect the view
with the model.
"""

import os
from typing import Dict, List, Tuple
from PySide6.QtCore import Slot, Signal, QObject, Qt, QModelIndex, QRegularExpression
from PySide6.QtWidgets import (
    QListWidgetItem,
    QDialog,
    QLabel,
    QTreeWidgetItem,
    QRadioButton,
    QFileDialog,
)
from PySide6.QtGui import QTextCharFormat, QColor, QTextCursor, QTextDocument
from corpuscompass.model import CorpusCompassModel, FileLoader, File
from corpuscompass.view.corpus_compass_view import CorpusCompassView
from corpuscompass.view.tabs.tab import Tab
import pandas as pd
import logging
from pathlib import Path


class Controller(QObject):
    """
    Connects the view with the model. Uses signals from the view and handles
    them by calling functions/actions in the model and by updating the view.
    """

    def __init__(self, model: CorpusCompassModel, view: CorpusCompassView) -> None:
        super().__init__()

        # Save a reference to the model and the view
        self.model = model
        self.view = view

        # Connect Signals from the view for all widgets/tabs (--> Dialogs and their signals are created dynamically)

        # Start Screen
        start_screen_tab = self.view.start_screen_tab
        start_screen_tab.create_new_project.clicked.connect(
            self.on_create_project_clicked
        )
        start_screen_tab.open_project.clicked.connect(self.on_open_project_clicked)
        start_screen_tab.import_project.clicked.connect(self.on_import_project_clicked)

        # Home Menu Tab
        self.view.home_menu_tab.set_controller_callback(lambda: self)


        # General-Settings-Tab
        general_settings_tab = self.view.general_settings_tab
        general_settings_tab.btn_back.clicked.connect(
            lambda: self.on_home_section_button_clicked(Tab.HOME_TAB)
        )

        # Speaker-Identification-Section
        speaker_section_tab = self.view.speaker_tab
        speaker_section_tab.btn_sp_save.clicked.connect(
            self.on_speaker_format_saved_clicked
        )
        speaker_section_tab.btn_sp_cancel.clicked.connect(
            self.on_speaker_cancel_button_clicked
        )

        speaker_section_tab.btn_expand_speakerinfo.clicked.connect(
            self.view.speaker_tab.on_speaker_expand_clicked
        )
        speaker_section_tab.btn_expand_wordinfo.clicked.connect(
            self.view.speaker_tab.on_words_expand_clicked
        )

        speaker_section_tab.radbtn_sp_standard.toggled.connect(
            lambda: self.on_speaker_format_changed(
                speaker_section_tab.radbtn_sp_standard
            )
        )
        speaker_section_tab.radbtn_sp_praat.toggled.connect(
            lambda: self.on_speaker_format_changed(speaker_section_tab.radbtn_sp_praat)
        )
        speaker_section_tab.radbtn_sp_flex.toggled.connect(
            lambda: self.on_speaker_format_changed(speaker_section_tab.radbtn_sp_flex)
        )
        speaker_section_tab.radbtn_sp_elan.toggled.connect(
            lambda: self.on_speaker_format_changed(speaker_section_tab.radbtn_sp_elan)
        )

        # Annotation-Format-Section
        annot_format_tab = self.view.annotation_format_tab
        annot_format_tab.btn_annotformat_save.clicked.connect(
            self.on_annotformat_section_saved_clicked
        )
        # annot_format_tab.btn_annotformat_removerows.clicked.connect(self.on_annotformat_section_removeformats_clicked)
        annot_format_tab.btn_help.clicked.connect(
            self.on_annotformat_help_button_clicked
        )
        annot_format_tab.btn_annotformat_cancel.clicked.connect(
            self.on_annotformat_cancel_button_clicked
        )
        annot_format_tab.btn_annotformat_addnew.clicked.connect(
            lambda: self.on_open_annotation_format_editor(
                row=-1, column=-1, called_for_add=True
            )
        )
        annot_format_tab.btn_annotformat_edit.clicked.connect(
            lambda: self.on_open_annotation_format_editor(
                row=-1, column=-1, called_for_add=False
            )
        )
        annot_format_tab.tableWidget_annotformats.cellDoubleClicked.connect(
            self.on_open_annotation_format_editor
        )  # Call without lambda to send row and column automatically (thats why called_for_add is default False, which is what the function will be called with)

        # Load File Tab
        load_files_tab = self.view.load_files_tab
        load_files_tab.btn_add_file.clicked.connect(self.on_add_file_clicked)
        load_files_tab.btn_remove_file.clicked.connect(
            self.on_remove_selected_files_clicked
        )
        load_files_tab.list_loaded_filenames.cellDoubleClicked.connect(
            self.on_file_double_clicked
        )
        load_files_tab.btn_finished.clicked.connect(self.on_load_files_finished_clicked)

        # Variable Management Tab
        variable_management_tab = self.view.variable_management_tab
        variable_management_tab.btn_save_changes.clicked.connect(
            self.on_metadata_saved_clicked
        )
        # variable_management_tab.btn_cancel.clicked.connect(self.on_metadata_cancel_clicked)
        variable_management_tab.btn_help.clicked.connect(self.on_metadata_help_clicked)

        variable_management_tab.btn_add_iv.clicked.connect(
            lambda: self.on_open_metadata_iv_editor(
                item=None, column=0, called_for_add=True
            )
        )
        variable_management_tab.btn_edit_ivs.clicked.connect(
            lambda: self.on_open_metadata_iv_editor(
                item=None, column=0, called_for_add=False
            )
        )  # If not double-clicked, then explicitely send item=None to ensure that no item is selected in the dialog initially
        variable_management_tab.treeWidget_ivs.itemDoubleClicked.connect(
            self.on_open_metadata_iv_editor
        )  # Call without lambda to send item automatically via the signal (called_for_add is default False, which is what the function will be called with the argument is not further specified here)

        variable_management_tab.btn_add_dv.clicked.connect(
            lambda: self.on_open_metadata_dv_editor(
                item=None, column=0, called_for_add=True
            )
        )
        variable_management_tab.btn_edit_dvs.clicked.connect(
            lambda: self.on_open_metadata_dv_editor(
                item=None, column=0, called_for_add=False
            )
        )  # If not double-clicked, then explicitely send item=None to ensure that no item is selected in the dialog initially
        variable_management_tab.treeWidget_dvs.itemDoubleClicked.connect(
            self.on_open_metadata_dv_editor
        )  # Call without lambda to send item automatically via the signal (called_for_add is default False, which is what the function will be called with the argument is not further specified here)

        variable_management_tab.btn_add_speaker.clicked.connect(
            lambda: self.on_open_metadata_speaker_editor(
                item=None, column=0, called_for_add=True
            )
        )
        variable_management_tab.btn_edit_speakers.clicked.connect(
            lambda: self.on_open_metadata_speaker_editor(
                item=None, column=0, called_for_add=False
            )
        )  # If not double-clicked, then explicitely send item=None to ensure that no item is selected in the dialog initially
        variable_management_tab.treeWidget_speakers.itemDoubleClicked.connect(
            self.on_open_metadata_speaker_editor
        )  # Call without lambda to send item automatically via the signal (called_for_add is default False, which is what the function will be called with the argument is not further specified here)

        variable_management_tab.btn_import_metadata.clicked.connect(
            self.on_import_metadata_button_clicked
        )
        variable_management_tab.btn_export_metadata.clicked.connect(
            self.on_export_metadata_button_clicked
        )

        variable_management_tab.btn_detectvariants.clicked.connect(
            self.on_detect_variants_clicked
        )

        # Analysis Settings Tab
        analysis_settings_tab = self.view.analysis_settings_tab
        analysis_settings_tab.btn_close_overview.clicked.connect(
            self.on_close_analysis_overview_button_clicked
        )
        analysis_settings_tab.btn_save_settings.clicked.connect(
            self.on_analysis_settings_save_button_clicked
        )

        analysis_settings_tab.checkBox_showannotations.toggled.connect(
            self.on_highlight_dvs_clicked
        )
        analysis_settings_tab.checkBox_showspeakers.toggled.connect(
            self.on_underline_speakers_clicked
        )
        analysis_settings_tab.checkBox_showfileindicators.toggled.connect(
            self.view.analysis_settings_tab.toggle_file_indicator
        )

        # TODO: Implement these button functions later, for now they are deactivated
        start_screen_tab.open_project.setEnabled(False)

    def on_highlight_dvs_clicked(self, toggled: bool):
        """
        Is called when the user toggles the "highlight variants" checkbox in the analysis settings tab.
        Highlights the variants in the text editor if the checkbox is checked.

        Args:
            toggled (bool): True if the checkbox is checked, False otherwise.
        """
        # also get the speaker and dv colors from the model
        dv_values = self.model.current_project.get_dv_values_printable()

        self.view.analysis_settings_tab.highlight_dvs(
            toggled, dv_values, self.model.current_project.get_detected_annotations()
        )

    def on_underline_speakers_clicked(self, toggled: bool):
        """
        Is called when the user toggles the "underline speakers" checkbox in the analysis settings tab.
        Underlines the speakers in the text editor if the checkbox is checked.

        Args:
            toggled (bool): True if the checkbox is checked, False otherwise.
        """
        speakers = self.model.current_project.get_speakers_printable()
        self.view.analysis_settings_tab.underline_speakers(
            toggled, speakers, self.model.current_project.get_detected_speakers()
        )

    @Slot()
    def on_create_project_clicked(self) -> None:
        """
        Is called, when the user clicks on "create new Project" in the start-tab.
        Opens a dialog window for creating a new project.
        """
        self.view.create_create_proj_dialog()

        self.view.create_proj_dialog.create_proj_accepted.connect(
            self.on_create_project_accepted
        )

        self.view.create_proj_dialog.exec()

        self.view.delete_create_proj_dialog()

    def on_create_project_accepted(self, proj_name: str) -> None:
        """
        Is called, when the user clicked on "OK" in the "Create New Project"-Dialog.
        Creates a new Project in the model and changes the view tab to the home-tab.

        Args:
            proj_name (str): The name of the project.
        """
        # Choose the home directory as the main directory
        # Alternative: Ask for directory #str(QFileDialog.getExistingDirectory(self.view, "Select Directory"))
        proj_dir = os.path.join(Path.home(), "CorpusCompassProjects")
        self.model.create_new_project(proj_name, proj_dir=proj_dir)
        self.view.switch_to_tab(Tab.HOME_TAB)
        self.view.proj_name_changed.emit(proj_name)
        # Connect the Project Signals
        self.connect_signals_to_project()

    def connect_signals_to_project(self):
        """Connects all signals from the current project to methods inside the
        controller.
        """
        # Connect Project Signals
        self.model.current_project.file_added_signal.connect(self.on_file_added)
        self.model.current_project.error_occurred_signal.connect(self.on_error_occurred)

        self.model.current_project.iv_changed_signal.connect(
            self.on_metadata_iv_changed
        )
        self.model.current_project.dv_changed_signal.connect(
            self.on_metadata_dv_changed
        )
        self.model.current_project.dv_values_changed_signal.connect(
            self.on_metadata_dv_values_changed
        )
        self.model.current_project.speaker_changed_signal.connect(
            self.on_metadata_speaker_changed
        )

        self.model.current_project.annotation_formats_changed_signal.connect(
            self.on_annotation_formats_changed
        )
        self.model.current_project.speaker_preview_signal.connect(
            self.on_speaker_preview_changed
        )
        self.model.current_project.annotation_preview_signal.connect(
            self.on_annotation_preview_changed
        )

        self.model.current_project.corpus_analysis_data_signal.connect(
            self.on_analysis_finished
        )

    def on_open_project_clicked(self):
        """
        Is called when the user clicks on "open project" in the start-tab.
        Opens a dialog window for selecting an existing project.
        """
        self.view.create_open_project_dialog()

        self.view.open_project_dialog.btn_changepath.clicked.connect(
            self.view.open_project_dialog.on_change_path_clicked
        )

        self.view.open_project_dialog.exec()

        self.view.delete_open_project_dialog()

    def on_import_project_clicked(self):
        """
        Is called when the user clicks on "import project" in the start-tab.
        Opens a dialog window for importing an existing project.
        """
        proj_dir = str(
            QFileDialog.getExistingDirectory(
                parent=self.view,
                caption="Select Directory",
                dir=os.path.join(Path.home()),
            )
        )
        self.model.import_project(proj_dir)
        self.connect_signals_to_project()
        self.model.current_project.send_update_to_frontend()
        self.view.proj_name_changed.emit(self.model.current_project.get_name())
        self.view.switch_to_tab(Tab.HOME_TAB)

    # Home-Buttons

    def on_project_closed_clicked(self):
        """
        Is called when the user clicks the "close project" button in the homee-tab.
        Closes the project and switches to the start-tab.
        """
        self.view.switch_to_tab(Tab.START_TAB)
        self.model.close_project()

    def on_home_section_button_clicked(self, target_tab: Tab):
        """
        Is called, when the user clicks on any navigation button in the home-tab.
        Opens a new widget of the corresponding tab.

        Args:
            target_tab (Tab): The enum-literal of the target tab
        """
        self.view.switch_to_tab(target_tab)

        if (
            target_tab == Tab.SPEAKER_TAB
        ):  # Update the speaker preview, if user goes into speaker tab
            self.update_speaker_preview()

    def on_analyse_corpus_button_clicked(self):
        """
        Is called, when the user clicks on the "analyse corpus" button in the home-tab.
        Starts the analysis process and shows the analysis success dialog afterwards.
        """
        self.view.home_menu_tab.btn_home_analysecorpus.setEnabled(False)
        self.model.current_project.create_datasets()

    def on_analysis_finished(self, data: dict) -> None:
        """Method is called when the model is finished with the analysis of the
        corpus. Notifies the user and asks about the saving location.

        Args:
            data (dict): The analysis data from the model.
        """
        self.view.home_menu_tab.btn_home_analysecorpus.setEnabled(True)

        # If the analysis was no success
        if len(data) == 0:
            return

        self.view.create_analysis_success_dialog()
        self.view.analysis_success_dialog.btn_savelocation.clicked.connect(
            self.view.analysis_success_dialog.on_select_target_file_path_clicked
        )
        self.view.analysis_success_dialog.exec()
        selected_folder = self.view.analysis_success_dialog.get_selected_folder()
        self.model.current_project.save_datasets(selected_folder, data)
        self.view.delete_analysis_success_dialog()

    def on_projectinformation_clicked(self):
        """
        Opens a dialog window with information about the current project.
        """
        # self.view.create_project_information_dialog(self.model.current_project.get_name, self.model.current_project.get_description) # TODO: Implement functions in model
        self.view.create_project_information_dialog()  # TODO: Replace with above
        self.view.project_information_dialog.exec()
        self.view.delete_create_proj_dialog()

    # Buttons in sections

    # Speaker-Format section

    def on_speaker_format_saved_clicked(self):
        """
        Is called, when the user clicks on the "save-button" in speaker identification section.
        Saves settings and returns back to homescreen.
        """
        speaker_format = self.view.speaker_tab.get_selected_format()
        self.model.current_project.set_speaker_format(speaker_format)
        self.model.current_project.save_project_metadata()
        self.model.current_project.detect_speakers(
            is_synchronous=False, save_detected_speakers=True
        )
        self.view.switch_to_tab(Tab.HOME_TAB)

    def on_speaker_format_changed(self, button: QRadioButton):
        """Is called, when the user changes the speaker format by selecting a radio button.
        Updates the speaker preview"""
        if not button.isChecked():  # If the button gets unchecked, do nothing
            return
        self.update_speaker_preview()

    def update_speaker_preview(self):
        """Causes the model to create a new speaker preview. This data is then
        send to the controller via the "on_speaker_preview_changed"-Signal
        """
        speaker_format = self.view.speaker_tab.get_selected_format()
        self.model.current_project.get_speaker_preview(speaker_format)

    def on_speaker_cancel_button_clicked(self):
        """
        Is called when the user clicks on the "cancel-button" in speaker identification section.
        Opens a warning dialog about losing the changes and returns back to homescreen if the user accepts the warning.
        """
        # TODO: Only open the dialogwindow if changes were made

        self.view.create_generic_warning_dialog()
        dialog_result = self.view.generic_warning_dialog.exec()
        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.switch_to_tab(
                Tab.HOME_TAB
            )  # Only switch to Home-Tab if "Save settings" is clicked

        self.view.delete_generic_warning_dialog()

    def on_speaker_preview_changed(self, data: dict):
        """Handles the "speaker_preview_changed_signal". Updates the preview of
        the detected speakers.

        Args:
            data (dict): _description_
        """
        self.view.speaker_tab.update_labels(data["Speaker_Total"], 0)

        self.view.speaker_tab.clear_speaker_table()
        self.view.speaker_tab.add_all_speakers_to_table(data["Speaker_Data"])
        # => UI-Updates: 1. Speaker Ident. Tabellen 2. Metadata Speaker List 3. Analysis Settings angezeigte Speaker 4. Analysis Settings refreshen von underlined speakers
        self.on_metadata_speaker_changed()

    # Annot-Section

    def on_annotformat_section_saved_clicked(self):
        """
        Is called, when the user clicks on the "save-button" in annotation format section.
        Saves current settings and returns back to homescreen.
        """
        # Store the annotation formats in the project files
        self.model.current_project.save_project_metadata()

        # Detect the annotations based on all input annotation formats
        self.model.current_project.detect_annotations()  # TODO: Make async
        self.model.current_project.save_detected_annotations()

        self.on_annotation_formats_changed(
            self.model.current_project.get_annotation_formats_printable()
        )

        self.view.create_detect_variants_dialog(
            detected_variants=self.model.current_project.get_dv_values_printable()
        )
        dialog_result = self.view.detect_variants_dialog.exec()

        # If Dialog was accepted, variable value extraction was confirmed -> Move to DV-Management-Tab
        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.switch_to_tab(Tab.VARMANAGEMENT_TAB)
            self.view.variable_management_tab.switch_tab(1)
        else:
            self.view.switch_to_tab(Tab.HOME_TAB)

        self.view.delete_detect_variants_dialog()

    def on_annotationformat_remove_clicked(self):
        """
        Is called when the user clicks on the "remove-formats" button in
        the annotation format section. This prompts a warning-dialog about
        the irreversibility of the removal-action.
        """
        if self.view.annotationformat_editor_dialog.dont_show_removaldialog == False:
            self.view.create_annotation_removal_dialog()
            self.view.annotation_removal_dialog.remove_format_accepted.connect(
                self.on_annotformat_section_removeformat_accepted
            )
            self.view.annotation_removal_dialog.exec()
            self.view.delete_annotation_removal_dialog()
        else:
            self.on_annotformat_section_removeformat_accepted(dont_show_again=True)

    def on_annotformat_section_removeformat_accepted(self, dont_show_again: bool):
        """
        Calls function that removes the annotation-format-items from the
        table widget that contains all annotation formats.
        """
        self.view.annotationformat_editor_dialog.dont_show_removaldialog = (
            dont_show_again
        )
        self.view.annotationformat_editor_dialog.remove_selected_format()
        # self.view.annotation_format_tab.remove_format_item_from_table() TODO -> Call this after the whole Editor-Dialog is closed with "accept", so that only after saving all changes that changes are made in the format tab

    def on_open_annotation_format_editor(
        self, row: int, column: int, called_for_add: bool = False
    ):
        """
        Is called, when the user clicks on either the "add annotationformat" button or the "edit annotation-format" button
        in the annotation section, or if the user double-clicks an annotation-format-item in the table.
        Opens a dialog window for adding or editing (selected) annotation formats.
        """

        symbols = self.model.current_project.get_annotation_symbols()
        formats = self.model.current_project.get_annotation_formats_printable()

        # First if-statement is for the case that the dialog is opened for adding a new annotation format
        if called_for_add:
            # This create-function creates a dialog with the default format for adding a new annotation format
            self.view.create_annotation_specify_dialog(symbols=symbols, formats=formats)

        else:  # --> Called for editing an existing annotation format, therefore dialog is opened with the corresponding format
            # This create-function creates a dialog with the default format for editing an existing annotation format
            self.view.create_annotationformat_editor_dialog(
                row, column, symbols, formats
            )

            # connect signals for the editor-dialog, as these signals are only needed if the user wishes to edit an existing format (as the corresponding elements are only available in this workflow)
            self.view.annotationformat_editor_dialog.btn_delete_annotformat.clicked.connect(
                self.on_annotationformat_remove_clicked
            )
            self.view.annotationformat_editor_dialog.comboBox_selectformat.currentIndexChanged.connect(
                self.view.annotationformat_editor_dialog.on_combobox_activated
            )

        # Connect signals for both cases (adding and editing) to the same functions, as the functions are the same for both cases
        self.view.annotationformat_editor_dialog.btn_annotdial_resetformat.clicked.connect(
            self.view.annotationformat_editor_dialog.clear_input_format
        )  # Connect signal directly to view if only view-changes are made/maybe also all in the view
        self.view.annotationformat_editor_dialog.btn_resetseparator.clicked.connect(
            self.view.annotationformat_editor_dialog.clear_separator_symbols
        )
        self.view.annotationformat_editor_dialog.btn_annotdial_addsymbols.clicked.connect(
            self.on_annotformat_addsymbols_clicked
        )
        self.view.annotationformat_editor_dialog.btn_testcurrentformat.clicked.connect(
            self.on_test_annotation_format_clicked
        )

        self.view.annotationformat_editor_dialog.btn_save.clicked.connect(
            self.on_save_annotation_format_clicked
        )

        # Handle drag/drop events -> calls dropEvent()-function in dialog-class
        self.view.annotationformat_editor_dialog.listwidget_annotformat_removeelems.dragEnterEvent = self.view.annotationformat_editor_dialog.trashcan_separator_drag_enter_event
        self.view.annotationformat_editor_dialog.listwidget_annotdial_separatorsymbols.dragEnterEvent = self.view.annotationformat_editor_dialog.trashcan_separator_drag_enter_event
        self.view.annotationformat_editor_dialog.listwidget_annotdial_inputformat.dragEnterEvent = self.view.annotationformat_editor_dialog.input_drag_enter_event

        # NOTE: THIS COULD BE REMOVED AND THE SAVING WOULD STILL WORK PROBABLY (FOR EDIT WORKFLOW) AS SAVES ARE DONE AFTER COMBOBOX SWITCH AND SAVE BUTTON CLICK
        # --> NO NEED TO SAVE AFTER EVERY INTERACTION WITH THE LISTWIDGETS, BUT THESE FUNCTIONS CAN BE USED IN THE FUTURE TO MAKE FEEDBACK MORE INTERACTIVE AND RIGHT NOW THEY
        # DONT HURT THE FUNCTIONALITY, THEY JUST INCREASE THE AMOUNT OF SAVES WHICH IS NOT THAT MUCH OF PROCESSING POWER LOST (USER WILL NOT NOTICE)

        # PROBLEM WITH DROP EVENTS: THE UPDATES ARE NOT TRACKED PROPERLY, AS THE TARGET OF THE DROP WILL BE THE UPDATED VERSION AT CALL TIME, HOWEVER THE SOURCE OF THE DROP WILL BE THE OLD VERSION AND THEREFORE
        # IN CASES WHERE THINGS ARE MOVED OUT OF A LISTWIDGET, THE OLD VERSION WILL FALSELY BE USED TO UPDATE THE MODEL WITH. HOWEVER, THIS IS PREVENTED HERE DUE TO THE COMMENT ABOVE (ALL SAVES ARE DONE AFTER COMBOBOX SWITCH AND SAVE BUTTON CLICK
        # WHERE EACH TIME THE CURRENT CONTENTS OF THE INPUT DATA FIELDS ARE EXPLICITELY FETCHED AGAIN)
        self.view.annotationformat_editor_dialog.listwidget_annotformat_removeelems.dropEvent = self.view.annotationformat_editor_dialog.trashcan_drop_event
        self.view.annotationformat_editor_dialog.listwidget_annotdial_inputformat.dropEvent = self.view.annotationformat_editor_dialog.input_change_event
        self.view.annotationformat_editor_dialog.listwidget_annotdial_separatorsymbols.dropEvent = self.view.annotationformat_editor_dialog.separator_symbol_change_event

        self.view.annotationformat_editor_dialog.listwidget_annotformat_removeelems.itemChanged.connect(
            self.view.annotationformat_editor_dialog.clear_trashcan_symbols
        )

        self.view.annotationformat_editor_dialog.checkbox_annotdial_multipleannot.toggled.connect(
            self.view.annotationformat_editor_dialog.on_multiple_annot_checked
        )

        dialog_result = self.view.annotationformat_editor_dialog.exec()

        # if the user clicks "save", the changes are saved in the model and the view is updated --> New/Changed formats are added to the table
        if dialog_result == QDialog.DialogCode.Accepted:
            # self.view.annotation_format_tab.add_format_to_table("New Format", "$§$$")
            if called_for_add:
                self.view.delete_annotation_specify_dialog()
            else:
                self.view.delete_annotationformat_editor_dialog()

        else:  # --> If the user clicks "cancel", the dialog is closed and no changes are saved, which means we can just pass
            if called_for_add:
                self.view.delete_annotation_specify_dialog()
            else:
                self.view.delete_annotationformat_editor_dialog()

        # Delete dialog after it was closed

    def on_test_annotation_format_clicked(self):
        """
        Is called when the user clicks the "test annotation format" button in the annotation format section.
        Starts the detection process of the annotation format for just the current input format and displays the results in the table in the dialog.
        """
        preview_data = self.model.current_project.get_detected_annotations()
        current_format_as_string = (
            self.view.annotationformat_editor_dialog.get_current_format_as_string()
        )
        self.model.current_project.get_annotation_preview(
            current_format_as_string, is_synchronous=False
        )

    def on_annotation_preview_changed(self, preview_data: pd.DataFrame) -> None:
        """Updates the preview for showing detected annotations with a given
        annotation format

        Args:
            preview_data (pd.Dataframe): The preview data from the model
        """
        tokens = preview_data["token"]
        identifiers = preview_data["identifier"]
        identifier_length = identifiers.apply(len)
        tuple_list: List[Tuple[str, str, int]] = list(
            zip(tokens, identifiers, identifier_length)
        )
        self.view.annotationformat_editor_dialog.add_all_to_preview_table(tuple_list)

    def on_save_annotation_format_clicked(self):
        """
        Is called when the user clicks the save button in the annotationformat editor window. Checks if all inputs are valid (if called for editing), or if the only input format is valid (if called for adding a new format).
        If all inputs are valid, the accept-press is propagated to the dialog, which then closes the dialog, otherwise the user is prompted to correct the input.
        """
        # if save is clicked -> update the model again to save the changes of the current window (NOTE: just to be sure in case there are bugs in the view)
        is_duplicate = (
            self.view.annotationformat_editor_dialog.update_temporary_dialog_model()
        )
        current_formats = self.view.annotationformat_editor_dialog.get_updated_data()
        if (
            self.view.annotationformat_editor_dialog.check_for_valid_formats()
            and not is_duplicate
        ):  # --> If the format is valid, the dialog is closed
            # Close dialog
            self.view.annotationformat_editor_dialog.accept()
            # Update annotation formats in the model
            self.model.current_project.update_annotation_formats_from_frontend(
                current_formats
            )
        else:  # --> If the format is not valid, the user is prompted to correct the input
            self.view.create_invalid_input_warning_dialog()
            self.view.invalid_input_warning_dialog.exec()
            self.view.delete_invalid_input_warning_dialog()
            # --> Annotationformat-Editor-Dialog stays open, as the user needs to correct the input

    def on_annotformat_addsymbols_clicked(self):
        """
        Is called when the "add new symbols"-button is clicked in the
        dialog for specifying new annotation formats. Opens another
        dialog in which new symbols can be added to the annotation
        format builder.
        """

        # NOTE: Following comments are meant as general guidelines for the programmers to understand the process of creating a dialog dynamically as part of this application

        # 0. Get all data from model that is needed for the dialog (e.g. all symbols that are already in the model)
        symbols = self.model.current_project.get_annotation_symbols()

        # 1. Create Dialog dynamically (--> Create function should take care of adapting the dialog-elements to the model)
        self.view.create_addsymbol_dialog(symbols)

        # 2. Connect buttons and elements (Important: Connect them to other Controller-Functions + hand over dialog objects as they are only locally created on demand, not globally available)
        self.view.add_symbol_dialog.btn_addsymbol.clicked.connect(
            self.on_add_symbol_to_annotsymbols_clicked
        )

        # 3. Execute Dialog
        dialog_result = self.view.add_symbol_dialog.exec()

        # 4. Save data from dialog in variables before deleting dialog (if user saves data changes)
        new_symbols = []
        if dialog_result == QDialog.DialogCode.Accepted:
            # Save all new symbols in a list
            while (
                self.view.add_symbol_dialog.listwidget_annotformat_symbolcontainer.count()
                > 0
            ):
                new_symbols.append(
                    self.view.add_symbol_dialog.listwidget_annotformat_symbolcontainer.takeItem(
                        0
                    )
                )
            # Add new symbols to model
            for symbol in new_symbols:
                self.model.current_project.add_annotation_symbol(symbol)

            # 5. Update view with new data (if necessary)
            self.view.annotationformat_editor_dialog.fill_symbol_list(new_symbols)

        # 6. Set variable to none in view to delete it
        self.view.delete_addsymbol_dialog()

    def on_add_symbol_to_annotsymbols_clicked(self):
        """
        Is called when the "add symbol"-button is clicked in the
        dialog adding symbols in the annotation builder. Adds
        symbol to the view and the model
        """
        self.view.add_symbol_dialog.on_add_symbol_clicked()

    def on_annotformat_help_button_clicked(self):
        """
        Opens and executes the annotation help dialog, after user clicks the corresponding button.
        """
        self.view.create_annotation_help_dialog()
        self.view.annotation_help_dialog.exec()
        self.view.delete_annotation_help_dialog()

    def on_annotformat_cancel_button_clicked(self):
        """
        Opens and exectues the warning dialog, after user clicks the corresponding button.
        If the user accepts the warning, which means he is okay with losing all changes, the view switches to the home tab.
        """
        # TODO: Only open the dialogwindow if changes were made
        self.view.create_generic_warning_dialog()
        dialog_result = self.view.generic_warning_dialog.exec()
        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.switch_to_tab(
                Tab.HOME_TAB
            )  # Only switch to Home-Tab if "Save settings" is clicked

        self.view.delete_generic_warning_dialog()

    # Variable-Management-Section

    def on_metadata_saved_clicked(self):
        """
        Is called, when the user clicks on the "save-button" in the metadata-management section.
        Saves settings and returns back to homescreen.
        """
        # Save the data in the project files
        self.model.current_project.save_iv_data()
        self.model.current_project.save_dv_data()
        self.model.current_project.save_speaker_data()

        self.view.switch_to_tab(Tab.HOME_TAB)

    def on_metadata_help_clicked(self):
        """
        Is called, when the user clicks on the "help-button" in the metadata-management section.
        Opens a dialog window with help information.
        """
        self.view.create_dv_detection_help_dialog()
        self.view.dv_detection_help_dialog.exec()
        self.view.delete_dv_detection_help_dialog()

    def on_open_metadata_iv_editor(
        self, item: QTreeWidgetItem, column, called_for_add: bool = False
    ):
        """
        Opens the IV-Editor-Dialog with the selected IV and its values. Checks if a dialog is opened for adding a new IV or for editing an existing IV
        and calls the corresponding functions in the view. It also connects the signals of the dialog with the corresponding functions based on if the dialog is opened for adding or editing IVs.

        Parameters:
        -item (QTreeWidgetItem): The selected item in the tree widget.
        -column (int): The column of the selected item.
        -called_for_add (bool): True if the dialog is opened for adding a new IV, False if it is opened for editing IVs.
        """

        model_ivs: Dict[str, List[str]] = self.model.current_project.get_iv_printable()
        if called_for_add:
            self.view.create_add_iv_dialog(current_variables=model_ivs)
        else:
            # Always get "root" (=IV) -> Necessary if variant in tree widget is double clicked, so that the editor for the overarching dv is opened
            # but only if item is not none, if it is none, then the "edit" button was clicked explcitely and no items need to be handled as item stays = None
            if item is not None:
                item = self.get_tree_item_parent(item)
            # get all current IVs from the model
            self.view.create_edit_iv_dialog(
                item, column=column, current_variables=model_ivs
            )

            # connect signals that are only needed if the dialog is opened for editing existing IVs
            self.view.iv_editor_dialog.comboBox_selectiv.currentIndexChanged.connect(
                self.view.iv_editor_dialog.on_combobox_activated
            )
            self.view.iv_editor_dialog.btn_editconfirm.clicked.connect(
                self.view.iv_editor_dialog.on_input_change_confirmed
            )
            self.view.iv_editor_dialog.btn_delete_iv.clicked.connect(
                self.on_iv_delete_button_clicked
            )

        # connect signals that are needed in both cases (adding and editing)
        self.view.iv_editor_dialog.btn_removevalue.clicked.connect(
            self.on_iv_values_remove_clicked
        )
        self.view.iv_editor_dialog.btn_addvalue.clicked.connect(
            self.on_add_iv_value_button_clicked
        )
        self.view.iv_editor_dialog.lineEdit_nameinput.textChanged.connect(
            self.view.iv_editor_dialog.check_varname_changed
        )

        dialog_result = self.view.iv_editor_dialog.exec()

        if dialog_result == QDialog.DialogCode.Accepted:
            updated_ivs = self.view.iv_editor_dialog.return_temporary_iv_data()
            # send data to model
            self.model.current_project.update_iv_from_frontend(updated_ivs)

        if called_for_add:
            self.view.delete_add_iv_dialog()
        else:
            self.view.delete_edit_iv_dialog()

    def on_iv_values_remove_clicked(self):
        """
        Is called when the user clicks the "remove-value" button in the IV-Editor-Dialog. Removes the selected value from the list.
        """
        self.view.iv_editor_dialog.remove_selected_values()

    def on_add_iv_value_button_clicked(self):
        """
        Is called when the user clicks the "add-iv-value" button in the IV-Editor-Dialog. Adds the selected value from the list.
        """
        # TODO: Idea -> Dialog must already have information about all IVs and Values in the model on creation (as they need to be displayed)
        # -> Checks if new value is duplicate or new IV is duplicate etc can all be done in the view
        # -> If view is closed, is is assured that all changes to the IVs are valid
        # -> Only propagate changes to the model if "accept" in dialog was clicked, otherwise discard changes (before: Warning message that changes are discarded)
        # Propagate: Probably with a Signal that sends all IVs and Values in "accept()" as a dict, and as all values should be valid they can just override the
        # existing IVs completely (instead of checking for correctness)
        # --> Use temporary dictionary in the view that holds all IVs + all changes
        self.view.iv_editor_dialog.add_new_iv_value()

    def on_iv_delete_button_clicked(self):
        """
        Handles the event when the IV delete button is clicked.

        This function displays a metadata deletion warning dialog and removes the current IV
        if the dialog is accepted.
        """
        # TODO Different behaviour based on where it was called from
        self.view.create_metadata_deletion_warning_dialog("IV")
        dialog_result = self.view.metadata_deletion_warning_dialog.exec()
        self.view.delete_metadata_deletion_warning_dialog()

        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.iv_editor_dialog.remove_current_iv()  # Only remove IV if dialog is accepted

    def on_open_metadata_dv_editor(
        self, item: QTreeWidgetItem, column, called_for_add: bool = False
    ):
        """
        Opens the DV-Editor-Dialog with the selected DV and its variants. Checks if a dialog is opened for adding a new DV or for editing an existing DV
        and calls the corresponding functions in the view. It also connects the signals of the dialog with the corresponding functions based on if the dialog is opened for adding or editing DVs.

        Parameters:
        -item (QTreeWidgetItem): The selected item in the tree widget.
        -column (int): The column of the selected item.
        -called_for_add (bool): True if the dialog is opened for adding a new DV, False if it is opened for editing DVs.
        """

        detected_variants = self.model.current_project.get_dv_values_printable()
        current_variables = self.model.current_project.get_dv_printable()

        if called_for_add:
            self.view.create_add_dv_dialog(
                detected_variants=detected_variants, current_variables=current_variables
            )
        else:
            # Always get "root" (=DV) -> Necessary if variant in tree widget is double clicked, so that the editor for the overarching dv is opened
            # but only if item is not none, if it is none, then the "edit" button was clicked explcitely and no items need to be handled as item stays = None
            if item is not None:
                item = self.get_tree_item_parent(item)
            self.view.create_edit_dv_dialog(
                clicked_item=item,
                column=column,
                detected_variants=detected_variants,
                current_variables=current_variables,
            )

            # connect signals that are only needed if the dialog is opened for editing existing DVs
            self.view.dv_editor_dialog.comboBox_selectdv.currentIndexChanged.connect(
                self.view.dv_editor_dialog.on_combobox_activated
            )
            self.view.dv_editor_dialog.btn_editconfirm.clicked.connect(
                self.view.dv_editor_dialog.on_input_change_confirmed
            )
            self.view.dv_editor_dialog.btn_delete_dv.clicked.connect(
                self.on_dv_delete_button_clicked
            )

        # connect signals that are needed in both cases (adding and editing)
        self.view.dv_editor_dialog.lineEdit_nameinput.textChanged.connect(
            self.view.dv_editor_dialog.check_varname_changed
        )
        self.view.dv_editor_dialog.lineEdit_searchvariants.textChanged.connect(
            self.view.dv_editor_dialog.filter_dv_names
        )
        self.view.dv_editor_dialog.tableWidget_dialog_dvaddvariants.cellDoubleClicked.connect(
            self.on_edit_dv_change_color_double_clicked
        )

        dialog_result = self.view.dv_editor_dialog.exec()

        # if the user clicks "save", the changes are saved in the model and the view is updated --> New/Changed formats are added to the table
        if dialog_result == QDialog.DialogCode.Accepted:
            updated_dvs, updated_variants = (
                self.view.dv_editor_dialog.return_temporary_dv_data()
            )
            # send data to model
            self.model.current_project.update_dv_values_from_frontend(updated_variants)
            self.model.current_project.update_dv_from_frontend(updated_dvs)

            # update the table in the metadata tab
            self.view.variable_management_tab.update_detected_variants_table(
                updated_variants
            )

        if called_for_add:
            self.view.delete_add_dv_dialog()
        else:
            self.view.delete_edit_dv_dialog()

    def on_dv_delete_button_clicked(self):
        """
        Handles the event when the DV delete button is clicked.

        This function displays a metadata deletion warning dialog and removes the current DV
        if the dialog is accepted.
        """
        # TODO Different behaviour based on where it was called from
        self.view.create_metadata_deletion_warning_dialog("DV")
        dialog_result = self.view.metadata_deletion_warning_dialog.exec()
        self.view.delete_metadata_deletion_warning_dialog()

        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.dv_editor_dialog.remove_current_dv()  # Only remove IV if dialog is accepted

    def on_open_metadata_speaker_editor(
        self, item: QTreeWidgetItem, column, called_for_add: bool = False
    ):
        """
        Opens the Speaker-Editor-Dialog with the selected speaker and its values. Checks if a dialog is opened for adding a new speaker or for editing an existing speaker
        and calls the corresponding functions in the view. It also connects the signals of the dialog with the corresponding functions based on if the dialog is opened for adding or editing speakers.

        Parameters:
        -item (QTreeWidgetItem): The selected item in the tree widget.
        -column (int): The column of the selected item.
        -called_for_add (bool): True if the dialog is opened for adding a new speaker, False if it is opened for editing speakers.
        """

        current_speakers = self.model.current_project.get_speakers_printable()
        current_ivs = self.model.current_project.get_iv_printable()

        if called_for_add:
            self.view.create_add_speaker_dialog(
                current_speakers=current_speakers, current_ivs=current_ivs
            )
            # connect signals that are only needed if the dialog is opened for adding new speakers
            self.view.speaker_editor_dialog.btn_changecolor.clicked.connect(
                self.on_addspeaker_change_color_clicked
            )
            self.view.speaker_editor_dialog.lineEdit_nameinput.textChanged.connect(
                self.view.speaker_editor_dialog.check_varname_changed
            )
        else:
            # Always get "root" (=speaker) -> Necessary if variant in tree widget is double clicked, so that the editor for the overarching dv is opened
            # but only if item is not none, if it is none, then the "edit" button was clicked explcitely and no items need to be handled as item stays = None
            if item is not None:
                item = self.get_tree_item_parent(item)
            self.view.create_edit_speaker_dialog(
                clicked_item=item,
                column=column,
                current_speakers=current_speakers,
                current_ivs=current_ivs,
            )

            # connect signals that are only needed if the dialog is opened for editing existing speakers
            self.view.speaker_editor_dialog.btn_delete_speaker.clicked.connect(
                self.on_speaker_delete_button_clicked
            )
            self.view.speaker_editor_dialog.btn_changecolor.clicked.connect(
                self.on_editspeaker_change_color_clicked
            )

        # connect signals that are needed in both cases (adding and editing)
        self.view.speaker_editor_dialog.comboBox_selectspeaker.currentIndexChanged.connect(
            self.view.speaker_editor_dialog.on_combobox_activated
        )

        dialog_result = self.view.speaker_editor_dialog.exec()

        if dialog_result == QDialog.DialogCode.Accepted:
            updated_speakers = (
                self.view.speaker_editor_dialog.return_temporary_speaker_data()
            )

            # send data to model
            self.model.current_project.update_speakers_from_frontend(updated_speakers)

        if called_for_add:
            self.view.delete_add_speaker_dialog()
        else:
            self.view.delete_edit_speaker_dialog()

    def on_speaker_delete_button_clicked(self):
        """
        Handles the event when the speaker delete button is clicked.

        This function displays a metadata deletion warning dialog and removes the current speaker
        if the dialog is accepted.
        """
        # TODO Different behaviour based on where it was called from
        self.view.create_metadata_deletion_warning_dialog("SPEAKER")
        dialog_result = self.view.metadata_deletion_warning_dialog.exec()
        self.view.delete_metadata_deletion_warning_dialog()

        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.speaker_editor_dialog.remove_current_speaker()  # Only remove IV if dialog is accepted

    def on_import_metadata_button_clicked(self):
        """
        Is called when the user clicks the "export metadata" button in the
        variable-management tab. Opens a dialog that allows importing
        IVs, DVs, and speakers from JSON-files, as well as controlling
        further import-settings.
        """
        self.view.create_import_metadata_dialog()
        self.view.import_metadata_dialog.exec()
        self.view.delete_import_metadata_dialog()

    def on_export_metadata_button_clicked(self):
        """
        Is called when the user clicks the "export metadata" button in the
        variable-management tab. Opens a dialog that allows exporting
        IVs, DVs, and speakers into JSON-files.
        """
        self.view.create_export_metadata_dialog()
        self.view.export_metadata_dialog.exec()
        self.view.delete_export_metadata_dialog()

    def on_edit_dv_change_color_double_clicked(self, row, column):
        """
        Is called when the user double-clicks on a cell in the DV-Editor-Dialog. Only reacts to double-clicks in the color-column
        and will open a color-picker dialog.
        """
        # self.view.edit_dv_dialog.on_change_color_double_click(row, column)
        self.view.dv_editor_dialog.on_change_color_double_click(row, column)

    def on_addspeaker_change_color_clicked(self):
        """
        Is called when the user clicks the color-edit-button in the speaker dialog and will open a color-picker dialog.
        """
        # TODO Set information in model/catch if color is "wrong" like duplicate (would need to get the color, check it in model via controller, and only then set it in the view if color is correct)
        self.view.speaker_editor_dialog.on_change_color_clicked()

    def on_editspeaker_change_color_clicked(self):
        """
        Is called when the user clicks the color-edit-button in the speaker dialog and will open a color-picker dialog.
        (second function for edit-speakers as it may involve different behaviour than adding a new speaker in the future)
        """
        # TODO Set information in model/catch if color is "wrong" like duplicate (would need to get the color, check it in model via controller, and only then set it in the view if color is correct)
        self.view.speaker_editor_dialog.on_change_color_clicked()

    def on_detect_variants_clicked(self):
        """
        TODO --> not finished yet
        """
        # TODO: Go over complete corpus again with annotation format(s) and send new data to the view so it can update
        self.view.variable_management_tab.update_detected_data()

    # Analysis-Settings-Section
    def on_analysis_settings_save_button_clicked(self):
        """
        Handles the event when the analysis settings save button is clicked.

        This method creates a confirmation dialog for the analysis settings and waits for the user's response.
        If the user accepts the confirmation, it switches to the Home tab. Otherwise, no explicit action is taken (yet).
        """
        # get a list of the selected dvs and speakers from the view which is marked by the checkboxes
        sel_dvs = self.view.analysis_settings_tab.get_list_of_selected_dvs()
        sel_speakers = self.view.analysis_settings_tab.get_list_of_selected_speakers()

        self.view.create_analysis_settings_confirmation_dialog(sel_dvs, sel_speakers)
        dialog_result = self.view.analysis_settings_confirmation_dialog.exec()
        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.switch_to_tab(
                Tab.HOME_TAB
            )  # Only switch to Home-Tab if "Save settings" is clicked

        self.view.delete_analysis_settings_confirmation_dialog()

    def on_close_analysis_overview_button_clicked(self):
        """
        Handles the event when the analysis settings save button is clicked.

        This method is responsible for showing a warning dialog if changes were made to the settings menu.
        If the user accepts the dialog, it switches to the Home-Tab.
        """
        # TODO: Only show dialog if changes were made to the settings menu
        self.view.create_generic_warning_dialog()
        dialog_result = self.view.generic_warning_dialog.exec()
        if dialog_result == QDialog.DialogCode.Accepted:
            self.view.switch_to_tab(
                Tab.HOME_TAB
            )  # Only switch to Home-Tab if "Save settings" is clicked

        self.view.delete_generic_warning_dialog()

    # File-Loading-Section
    def on_add_file_clicked(self) -> None:
        """
        Opens a file explorer dialog to select one or more files to add to the current project.
        """
        current_dir = os.path.curdir
        file_paths = self.view.open_file_explorer(current_dir)

        if len(file_paths) == 0:
            return

        self.model.current_project.load_files(file_paths)

    def on_file_added(self, file: File) -> None:
        """
        Is called when a file is added. Adds the file to the list of loaded files in the view.
        """
        file_name = file.name

        self.view.load_files_tab.add_file(file_name)
        files = self.model.current_project.get_files()
        self.view.analysis_settings_tab.add_all_files(files)
        self.view.home_menu_tab.update_loaded_files(len(files))

    def on_file_double_clicked(self, row: int, column: int) -> None:
        """
        Adds a preview of the file to the view when the user double-clicks on a file in the list of loaded files.
        """
        # column 0 == checkbox --> User should not open file by mistake during interaction with checkbox
        if column != 0:
            item: QListWidgetItem = self.view.load_files_tab.list_loaded_filenames.item(
                row, column
            )
            file_name = item.text()
            file = self.model.current_project.get_file(file_name)
            self.view.load_files_tab.show_file_content(file.name, file.content)

    def on_remove_selected_files_clicked(self):
        """
        Removes the selected files from the list of loaded files in the view.
        """
        # TODO: Update Model
        self.view.load_files_tab.remove_selected_values()
        files = self.model.current_project.get_files()
        self.view.analysis_settings_tab.add_all_files(files)
        self.view.home_menu_tab.update_loaded_files(len(files))

    def on_load_files_finished_clicked(self):
        """
        Is called when the user clicks the "load files" button in the file-loading section. Starts the detection process for the loaded files.
        """
        # ANNOTATION DETECTION CASE 2: If a file is added and the user has already defined annotation formats, the annotations are detected automatically again
        if (
            len(self.model.current_project.get_annotation_formats_printable()) > 0
        ):  # TODO: Make async
            self.model.current_project.detect_annotations()
        # Save the current status of files in the model
        self.model.current_project.save_file_data()
        self.on_home_section_button_clicked(Tab.HOME_TAB)

    def on_error_occurred(self, error: str) -> None:
        """
        Is called when an error occurs in the model. Opens an error dialog in the view.
        """
        logging.critical(error)  # Log the error in a logging file
        self.view.display_error_message(error)

    def on_annotation_formats_changed(
        self, annotation_formats: Dict[str, Tuple[str, str]]
    ) -> None:
        """
        Is called when the annotation formats have changed in the model. Updates the annotation formats in the view.

        An example for the variable annotation_formats could be:
        { "[$TOKEN.IDENTIFIER]": (""\\[(?P<token>.*?)\\.(?P<identifier>.*?)\\]", "_")}
        """
        self.view.annotation_format_tab.clear_table()
        annotation_regex = self.model.current_project.get_annotation_regex()
        for annotation_name, separators in annotation_formats.items():
            regex = annotation_regex[annotation_name]
            self.view.annotation_format_tab.add_format_to_table(annotation_name, regex)

        # Invoke updates for changed DVs
        self.on_metadata_dv_values_changed()

        # Home Tab Anpassung
        self.view.home_menu_tab.update_annotations(
            len(self.model.current_project.get_detected_annotations())
        )
        self.view.home_menu_tab.update_annotation_formats(len(annotation_formats))

        # => UI-Updates: 1. Format Tabelle 2. DV Metadata Tree + Tabelle 3. Analysis Settings angezeigte DV Variants 4. Analysis Settings refreshen von annotation highlights
        pass

    def on_metadata_iv_changed(self):
        """
        Is called when the user changes the IVs.
        """
        # => UI-Updates: 1. IV-Metadata-Tree 2. Infos im Home-Tab anpassen
        ivs = self.model.current_project.get_iv_printable()
        self.view.variable_management_tab.add_all_ivs(ivs)
        # Home Tab Anpassung
        self.view.home_menu_tab.update_ivs(len(ivs))
        value_counter = 0
        for iv in ivs:
            value_counter += len(ivs[iv])
        self.view.home_menu_tab.update_iv_values(value_counter)
        pass

    def on_metadata_dv_changed(self):
        """
        Is called when the user changes the DVs.
        """
        # => UI-Updates: 1. DV-Metadata-Tree 2. DV-Metadata-Tabelle 3. Analysis Settings angezeigte DVs 4. Bei Farbänderungen highlighted Annotations anpassen 5. Infos im Home-Tab anpassen
        dvs = self.model.current_project.get_dv_printable()
        variants = self.model.current_project.get_dv_values_printable()
        detected_annos = self.model.current_project.get_detected_annotations()
        self.view.variable_management_tab.add_all_dvs(dvs)
        self.view.variable_management_tab.fill_detected_variants_fully(
            detected_annos, variants
        )
        self.view.analysis_settings_tab.add_all_dvs(dvs)
        if self.view.analysis_settings_tab.checkBox_showannotations.isChecked():
            self.view.analysis_settings_tab.highlight_dvs(
                True, variants, detected_annos
            )
        # Home Tab Anpassung
        self.view.home_menu_tab.update_dvs(len(dvs))
        self.view.home_menu_tab.update_dv_variants(len(variants))
        pass

    def on_metadata_dv_values_changed(self):
        """
        Is called when the user changes the DV values.
        """
        # => UI-Updates: 1. DV-Metadata-Tree 2. DV-Metadata-Tabelle 3. Analysis Settings angezeigte DVs 4. Bei Farbänderungen highlighted Annotations anpassen 5. Infos im Home-Tab anpassen
        dvs = self.model.current_project.get_dv_printable()
        variants = self.model.current_project.get_dv_values_printable()
        detected_annos = self.model.current_project.get_detected_annotations()
        self.view.variable_management_tab.add_all_dvs(dvs)
        self.view.variable_management_tab.fill_detected_variants_fully(
            detected_annos, variants
        )
        self.view.analysis_settings_tab.add_all_dvs(dvs)
        if self.view.analysis_settings_tab.checkBox_showannotations.isChecked():
            self.view.analysis_settings_tab.highlight_dvs(
                True, variants, detected_annos
            )
        # Home Tab Anpassung
        self.view.home_menu_tab.update_dvs(len(dvs))
        self.view.home_menu_tab.update_dv_variants(len(variants))
        pass

    def on_metadata_speaker_changed(self):
        """
        Is called when the user changes the speakers.
        """
        # => UI-Updates: 1. Speaker-Metadata-Tree 2. Speaker Ident-Tabellen 3. Analysis Settings angezeigte Speakers 4. Bei Farbänderungen underlined speakers anpassen 5. Infos im Home-Tab anpassen
        speakers = self.model.current_project.get_speakers_printable()
        self.view.variable_management_tab.add_all_speakers(speakers)
        # self.view.speaker_tab.add_all_speakers_to_table(None) # TODO: Wie Daten von Carsten
        # self.view.speaker_tab.add_all_words_to_table(None) # TODO: Wie Daten von Carsten
        self.view.analysis_settings_tab.add_all_speakers(speakers)
        if self.view.analysis_settings_tab.checkBox_showspeakers.isChecked():
            self.view.analysis_settings_tab.underline_speakers(
                True, speakers, self.model.current_project.get_detected_speakers()
            )
        # Home Tab Anpassung
        self.view.home_menu_tab.update_speakers(len(speakers))
        pass

    # SUPPORT FUNCTIONS (TODO: LATER IN OWN FILE)

    def get_tree_item_parent(self, tree_item: QTreeWidgetItem):
        """
        Returns the root item of the tree widget based on the given item. Used for the IVs, DVs, and speakers tree widgets to get
        the overarching item if a variant is double-clicked.
        """
        while tree_item.parent() is not None:
            tree_item = tree_item.parent()
        return tree_item
