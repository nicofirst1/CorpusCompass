"""
The module contains classes for the gui of CorpussCompass. The main class is
"CorpusCompassView".
"""

import inspect
from typing import Any, Dict, List, Tuple

import PySide6
from corpuscompass.view.font_configs import FontColors, FontConfig
from corpuscompass.view.tabs.analysis_settings_tab import AnalysisSettingsTab
from corpuscompass.view.tabs.annotation_format_tab import AnnotationFormatTableTab
from corpuscompass.view.tabs.general_settings_tab import GeneralSettingsTab
from corpuscompass.view.tabs.load_files_tab import LoadFilesTab
from corpuscompass.view.tabs.speaker_identification_tab import SpeakerIdentificationTab
from corpuscompass.view.tabs.start_screen_tab import StartScreenTab
from corpuscompass.view.tabs.tabs import Tab
from corpuscompass.model.variables_speakers import Variable, Speaker, VariableValue
from corpuscompass.view.tabs.home_menu_tab import HomeMenuTab
from corpuscompass.view.tabs.variable_management_tab import VariableManagementTab
from corpuscompass.view.utils import (
    split_string_with_token_and_identifier,
    set_checkbox_stylesheet,
    set_expand_button_stylesheet,
    expand_button_clicked,
    set_abbreviate_label)

from corpuscompass.view.generated.ui_start_screen_tab import Ui_StartScreenTab
from corpuscompass.view.generated.ui_create_project_dialog import Ui_CreateProjectDialog
from corpuscompass.view.generated.ui_home_menu_tab import Ui_HomeMenuTab
from corpuscompass.view.generated.ui_main_window import Ui_MainWindow
from corpuscompass.view.generated.ui_settings_tab import Ui_SettingsTab
from corpuscompass.view.generated.ui_project_information_dialog import Ui_ProjectInformationDialog
from corpuscompass.view.generated.ui_speaker_format_tab import Ui_SpeakerIdTab
from corpuscompass.view.generated.ui_annotation_format_table_tab import (
    Ui_AnnotationFormatTableTab,
)
from corpuscompass.view.generated.ui_load_files_tab import Ui_LoadFilesTab
from corpuscompass.view.generated.ui_variable_management_tab import Ui_VariableManagementTab
from corpuscompass.view.generated.ui_analysis_settings_tab import Ui_AnalysisSettingsTab
from corpuscompass.view.generated.ui_annotationformat_editor_dialog import (
    Ui_EditorAnnotationformatDialog,
)
from corpuscompass.view.generated.ui_annotformat_deletion_dialog import (
    Ui_AnnotationFormatRemoveDialog,
)
from corpuscompass.view.generated.ui_iv_editor_dialog import Ui_IVEditorDialog
from corpuscompass.view.generated.ui_dv_editor_dialog import Ui_DVEditorDialog
from corpuscompass.view.generated.ui_speaker_editor_dialog import Ui_SpeakerEditorDialog
from corpuscompass.view.generated.ui_add_symbol_dialog import Ui_AddSymbolsDialog
from corpuscompass.view.generated.ui_detecting_dvvariants_dialog import Ui_DetectVariantsDialog
from corpuscompass.view.generated.ui_open_project_dialog import Ui_OpenProjectDialog
from corpuscompass.view.generated.ui_generic_warning_dialog import Ui_GenericWarningDialog
from corpuscompass.view.generated.ui_analysis_success_dialog import Ui_AnalysisSuccessDialog
from corpuscompass.view.generated.ui_analysis_settings_confirmation_dialog import (
    Ui_AnalysisSettingsConfirmationDialog,
)
from corpuscompass.view.generated.ui_annotation_help_dialog import Ui_AnnotationHelpDialog
from corpuscompass.view.generated.ui_import_metadata_dialog import Ui_ImportMetadataDialog
from corpuscompass.view.generated.ui_export_metadata_dialog import Ui_ExportMetadataDialog
from corpuscompass.view.generated.ui_metadata_deletion_warning_dialog import (
    Ui_MetadataDeletionWarningDialog,
)
from corpuscompass.view.generated.ui_variable_detection_help_dialog import (
    Ui_VariableDetectionHelpDialog,
)
from corpuscompass.view.generated.ui_invalid_input_warning_dialog import (
    Ui_InvalidInputWarningDialog,
)


from PySide6.QtWidgets import (
    QPushButton,
    QGridLayout,
    QSizePolicy,
    QMainWindow,
    QWidget,
    QDialog,
    QFileDialog,
    QTextEdit,
    QComboBox,
    QMessageBox,
    QHeaderView,
    QTableWidgetItem,
    QColorDialog,
    QTableWidgetItem,
    QListWidget,
    QListWidgetItem,
    QTreeWidgetItem,
    QTableWidget,
    QDialogButtonBox,
    QCheckBox,
    QPlainTextEdit,
    QLabel,
    QToolTip,
    QScrollArea,
    QLayoutItem,
)
from PySide6.QtCore import Signal, Slot, Qt, QModelIndex, QSize, QRect, QTimer, QEvent
from PySide6.QtGui import (
    QFont,
    QKeyEvent,
    QTextCharFormat,
    QColor,
    QTextCursor,
    QStandardItemModel,
    QDragEnterEvent,
    QDropEvent,
)

import re
import random
import logging


# TODO: SUPPORT FUNCTIONS -> In own class
# def split_string_with_token_and_identifier(input_string):
#     # Define the regular expression pattern to capture arbitrary characters before and after "token" and "identifier"
#     pattern = r'(.*?)((token)|(identifier))(.*?)((token)|(identifier))(.*)'
#     match = re.match(pattern, input_string)
#     parts = [match.group(1), match.group(2), match.group(5), match.group(8), match.group(9)]  # Include match.group(9) to capture the remaining characters
#     parts = [part for part in parts if part]

#     return parts



def print_function_decorator(cls):
    for name, method in cls.__dict__.items():
        if callable(method) and name != '__init__' and not isinstance(method, PySide6.QtCore.Signal):  # Exclude __init__
            def create_wrapper(method):
                def wrapper(*args, **kwargs):
                    method_name=inspect.stack()[1][3]
                    print(f"Calling {method_name} with args: {args}, kwargs: {kwargs}")
                    return method(*args, **kwargs)
                return wrapper
            setattr(cls, name, create_wrapper(method))
    return cls


@print_function_decorator
class CorpusCompassView(QMainWindow, Ui_MainWindow):
    """
    The Main Window of the Corpus Compass application. Initializes all Tabs and
    Dialog windows
    """

    # Catching Signals from Controller
    proj_name_changed = Signal(str)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        # Initialize Tabs
        self.start_screen_tab = StartScreenTab(self)
        self.home_menu_tab = HomeMenuTab(self)
        self.speaker_tab = SpeakerIdentificationTab(self)
        self.annotation_format_tab = AnnotationFormatTableTab(self)
        self.load_files_tab = LoadFilesTab(self)
        self.variable_management_tab = VariableManagementTab(self)
        self.analysis_settings_tab = AnalysisSettingsTab(self)
        self.general_settings_tab = GeneralSettingsTab(self)

        # Add Tabs to Main Window so they can be displayed
        # --> Order of adding tabs must match the order of the Tab Enum (See Tab Enum for more information)
        self.stackedWidget.addWidget(self.start_screen_tab)
        self.stackedWidget.addWidget(self.home_menu_tab)
        self.stackedWidget.addWidget(self.speaker_tab)
        self.stackedWidget.addWidget(self.annotation_format_tab)
        self.stackedWidget.addWidget(self.load_files_tab)
        self.stackedWidget.addWidget(self.variable_management_tab)
        self.stackedWidget.addWidget(self.analysis_settings_tab)
        self.stackedWidget.addWidget(self.general_settings_tab)

        # Initialize Dialogs (None for initialization, as they are later created on demand)
        # --> Dialogs are created dynamically when needed and stored in instance variables of the view, as they are not needed all the time and should be deleted when not needed anymore
        # --> Implication for the controller: All signals from the dialogs must be connected in the controller, as the view does not know when the dialogs are created
        self.create_proj_dialog = None
        self.project_information_dialog = None
        # self.annotation_specify_dialog = None
        self.annotationformat_editor_dialog = None
        self.annotation_removal_dialog = None
        self.iv_editor_dialog = None
        self.dv_editor_dialog = None
        self.speaker_editor_dialog = None
        self.add_symbol_dialog = None
        self.detect_variants_dialog = None
        self.open_project_dialog = None
        self.generic_warning_dialog = None
        self.analysis_success_dialog = None
        self.analysis_settings_confirmation_dialog = None
        self.annotation_help_dialog = None
        self.import_metadata_dialog = None
        self.export_metadata_dialog = None
        self.dv_detection_help_dialog = None
        self.metadata_deletion_warning_dialog = None
        self.invalid_input_warning_dialog = None

    def switch_to_tab(self, tab: Tab):
        """
        Switches to a new tab. For this method to work properly, the order in
        which the tabs are added in the __init__ method must match the order of
        the assigned indices in the Tab-Enum (See description of Tab Enum for
        more information).


        Args:
            tab (Tab): The tab the view should change to
        """
        self.stackedWidget.setCurrentIndex(tab.value)

    def open_file_explorer(self, dir: str) -> list:
        corpus_files = QFileDialog.getOpenFileNames(
            self, "Select Corpus Files", dir, "Text Files (*.txt);;All Files (*.*)"
        )[0]
        return corpus_files

    def display_error_message(self, message: str):
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Icon.Critical)
        error_message.setText(message)
        error_message.setWindowTitle("Error")
        error_message.exec()

    # Functions for creating dialogs "on demand" dynamically
    # --> Each function creates a dialog window object, stores it in an instance variable of the view and sets initial properties of the object (what to show/hide, what elements to fill lists with, ...)
    # --> Delete functions just remove the reference from the instance variables to the objects so that the garbage collector can delete them

    def create_addsymbol_dialog(self, current_symbol_list):
        """
        Creates a new instance of the addsymbol_dialog and sets initial properties of the object.

        Args:
            current_symbol_list (list): The list of symbols to populate the dialog with.
        """
        self.add_symbol_dialog = AddSymbolDialog(self)

        # Set initial data --> Add all symbols to the list
        self.add_symbol_dialog.add_all_symbols_to_list(current_symbol_list)

        # show/hide initial elements
        self.add_symbol_dialog.label_symbolalreadyadded.hide()

    def delete_addsymbol_dialog(self):
        """
        Deletes the addsymbol_dialog instance.
        """
        self.add_symbol_dialog = None

    def create_create_proj_dialog(self):
        """
        Creates a new instance of the create_proj_dialog.
        """
        self.create_proj_dialog = CreateProjectDialog(self)

    def delete_create_proj_dialog(self):
        """
        Deletes the create_proj_dialog instance.
        """
        self.create_proj_dialog = None

    def create_project_information_dialog(
        self, proj_name: str = "My Name", proj_descr: str = "My Description"
    ):
        """
        Creates a new instance of the project_information_dialog
        """
        self.project_information_dialog = ProjectInformationDialog(self)
        self.project_information_dialog.lineEdit_pname.setText(proj_name)
        self.project_information_dialog.plainTextEdit_pdescr.setPlainText(proj_descr)

    def delete_project_information_dialog(self):
        """
        Deletes the project_information_dialog instance.
        """
        self.project_information_dialog = None

    def create_annotation_specify_dialog(
        self, symbols: List[str], formats: Dict[str, List[str]] = None
    ):  # Formats needed to check if a newly added format is a duplicate
        """
        Creates a dialog for adding a new annotation format.

        Parameters:
        - symbols (List[str]): The list of symbols to populate the dialog with.
        - formats (Dict[str, List[str]]): A dictionary containing the current annotation formats and their symbols, where each key is the format and the value is a list of symbols.

        This function initializes and configures the annotation editor dialog
        for adding a new annotation format. It hides unnecessary elements, enables
        necessary elements, and sets default values for certain fields.
        """
        self.annotationformat_editor_dialog = AnnotationformatEditorDialog(self)
        self.annotationformat_editor_dialog.comboBox_selectformat.hide()
        self.annotationformat_editor_dialog.label_ivselect.hide()
        self.annotationformat_editor_dialog.btn_delete_annotformat.hide()
        self.annotationformat_editor_dialog.widget_specificationcontents.setEnabled(
            True
        )
        # self.annotationformat_editor_dialog.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)

        # formats = {
        #     "[token.identifier]": ["@", "#", "$"],
        #     "[&token.identifier]": []
        # }

        self.annotationformat_editor_dialog.current_formats_temp = formats

        for format_name, format_symbols in formats.items():
            # check if multiple separator symbols are stored, if so, set an entry in the list that tracks the state of the checkbox
            if len(format_symbols) >= 1:
                self.annotationformat_editor_dialog.current_format_checkboxes_temp[
                    format_name
                ] = True
            else:
                self.annotationformat_editor_dialog.current_format_checkboxes_temp[
                    format_name
                ] = False

        # Fill the symbol list with the symbols from the model
        self.annotationformat_editor_dialog.fill_symbol_list(symbols)

    def delete_annotation_specify_dialog(self):
        """
        Deletes the annotation_specify_dialog instance.
        """
        self.annotationformat_editor_dialog = None

    def create_annotationformat_editor_dialog(
        self,
        row: int,
        column: int,
        symbols: List[str],
        formats: Dict[str, List[str]] = None,
    ):  # TODO: Needs: List of current annotation formats from Model
        """
        Creates and displays the annotation format editor dialog.

        Parameters:
        - row (int): The row index of the item in the table that was double-clicked.
        - column (int): The column index of the item in the table that was double-clicked.
        - formats (Dict[str, List[str]]): A dictionary containing the current annotation formats and their symbols, where each key is the format and the value is a list of symbols.

        Description:
        - This function is called when the user double-clicks on an item in the table or clicks the edit-button to edit
        existing annotation formats.
        - It creates an instance of the AnnotationformatEditorDialog class and displays it.
        - If the row and column indices are not -1, it means that the function was called by double clicking the table.
        Therefore the function sets the selected item in the dialog's combobox based on the text of the selected item in the table.
        - It then manually triggers the combobox reactions, as the signals are only connected after the create function is finished.
        """
        self.annotationformat_editor_dialog = AnnotationformatEditorDialog(self)
        # NOTE: Testing temporary storage of changes in the dialog object

        self.annotationformat_editor_dialog.current_formats_temp = formats

        for format_name, format_symbols in formats.items():
            # add all formats to the combobox
            self.annotationformat_editor_dialog.comboBox_selectformat.addItem(
                format_name
            )

        for format_name, format_symbols in formats.items():
            # check if multiple separator symbols are stored, if so, set an entry in the list that tracks the state of the checkbox
            if len(format_symbols) >= 1:
                self.annotationformat_editor_dialog.current_format_checkboxes_temp[
                    format_name
                ] = True
            else:
                self.annotationformat_editor_dialog.current_format_checkboxes_temp[
                    format_name
                ] = False

        # if row/column != -1 --> Edit-Dialog was called by double clicking on an item in the table
        if row != -1 and column != -1:
            annotation_format_text = (
                self.annotation_format_tab.tableWidget_annotformats.item(row, 0).text()
            )
            for index in range(
                self.annotationformat_editor_dialog.comboBox_selectformat.count()
            ):
                combobox_text = (
                    self.annotationformat_editor_dialog.comboBox_selectformat.itemText(
                        index
                    )
                )
                if annotation_format_text == combobox_text:
                    self.annotationformat_editor_dialog.comboBox_selectformat.setCurrentIndex(
                        index
                    )
                    break

            # manually trigger combobox-reactions, as signals are only connected after create-function is finished
            self.annotationformat_editor_dialog.on_combobox_activated()
            self.annotationformat_editor_dialog.on_multiple_annot_checked()

        # Fill the symbol list with the symbols from the model
        self.annotationformat_editor_dialog.fill_symbol_list(symbols)

    def delete_annotationformat_editor_dialog(self):
        """
        Deletes the annotationformat_editor_dialog instance.
        """
        self.annotationformat_editor_dialog = None

    def create_annotation_removal_dialog(self):
        """
        Creates a new instance of the annotation_removal_dialog.
        """
        self.annotation_removal_dialog = AnnotationRemovalDialog(self)

    def delete_annotation_removal_dialog(self):
        """
        Deletes the annotation_removal_dialog instance.
        """
        self.annotation_removal_dialog = None

    def create_add_iv_dialog(self, current_variables: Dict[str, List[str]] = None):
        """
        Creates a dialog for adding a new IV (Independent Variable).

        Parameters:
        - current_variables (List[Variable]): The list of current IVs to check for duplicates.

        This function initializes and configures the IV editor dialog
        for adding a new IV. It hides unnecessary elements, enables
        necessary elements, and sets default values for certain fields.
        """
        self.iv_editor_dialog = IVEditorDialog(self)
        self.iv_editor_dialog.current_ivs_temp = current_variables
        self.iv_editor_dialog.comboBox_selectiv.hide()
        self.iv_editor_dialog.btn_editconfirm.hide()
        self.iv_editor_dialog.btn_delete_iv.hide()
        self.iv_editor_dialog.label_ivselect.hide()
        self.iv_editor_dialog.label_ivname.setText("Input IV-Name:")
        self.iv_editor_dialog.lineEdit_nameinput.setPlaceholderText(
            "Input Variable-Name..."
        )
        self.iv_editor_dialog.lineEdit_nameinput.setEnabled(True)
        self.iv_editor_dialog.lineEdit_valueinput.setEnabled(True)
        self.iv_editor_dialog.btn_addvalue.setEnabled(True)
        # Disable Save-Button initially if "Add IV" is pressed -> Cannot save "empty" variable directly after the editor is opened
        self.iv_editor_dialog.buttonBox.button(
            QDialogButtonBox.StandardButton.Save
        ).setEnabled(False)

    def delete_add_iv_dialog(self):
        """
        Deletes the add_iv_dialog instance.
        """
        self.iv_editor_dialog = None

    def create_edit_iv_dialog(
        self,
        clicked_item: QTreeWidgetItem,
        column,
        current_variables: Dict[str, List[str]] = None,
    ):
        """
        Opens a dialog for editing or deleting an independent variable (IV).

        Parameters:
        - clicked_item (QTreeWidgetItem): The item that was clicked in the tree widget.
        - column (int): The column index of the clicked item.
        - current_variables (Dict[str, List[str]]): The list of current IVs to check for duplicates and to know which IVs are editable.

        Description:
        - This function creates an instance of the IVEditorDialog class.
        - If a clicked_item is provided, the function sets the current index of the comboBox_selectiv
            in the iv_editor_dialog to match the text of the clicked_item. This scenario happens when
            the user double-clicks an IV in the tree widget to edit it. If no clicked_item is provided,
            the function opens the dialog for the IV editor with its default settings, as it was opened
            by the user clicking the edit-button.
        - The function then manually triggers the on_combobox_activated() function of the iv_editor_dialog
            to update the dialog based on the selected IV.
        """
        self.iv_editor_dialog = IVEditorDialog(self)

        # populate dialog with current variables

        # current_variables = {"IV1": ["Value1", "Value2", "Value3"], "IV2": ["Value4", "Value5", "Value6"]}

        self.iv_editor_dialog.current_ivs_temp = current_variables
        # add variable text to combobox
        self.iv_editor_dialog.comboBox_selectiv.addItems(
            [var for var in current_variables.keys()]
        )

        if clicked_item is not None:
            item_text = clicked_item.text(column)
            for index in range(self.iv_editor_dialog.comboBox_selectiv.count()):
                combobox_text = self.iv_editor_dialog.comboBox_selectiv.itemText(index)
                if item_text == combobox_text:
                    # select correct item in combobox
                    self.iv_editor_dialog.comboBox_selectiv.setCurrentIndex(index)
                    break
            # manually trigger combobox-reactions, as signals are only connected after create-function is finished
            self.iv_editor_dialog.on_combobox_activated()

    def delete_edit_iv_dialog(self):
        """
        Deletes the edit_iv_dialog instance.
        """
        self.iv_editor_dialog = None

    def create_add_dv_dialog(
        self,
        detected_variants: Dict[str, Tuple[int, str, str]] = None,
        current_variables: Dict[str, Tuple[List[str], List[str]]] = None,
    ):  # TODO: Needs: List of DVs Variants with Colors and their current associated DV from Model. ALSO NEEDS: List of all current DVs to check for duplicates
        """
        Creates a dialog for adding a new DV (Dependent Variable).

        This function initializes and configures the DV editor dialog
        for adding a new DV. It hides unnecessary elements, enables
        necessary elements, and sets default values for certain fields.

        - detected_variants (List[Dict[str, Any]]): A list of detected variants for the DV.
        - current_variables (Dict[str, List[Dict[str, Any]]]): The list of current DVs to update the view with according to the model.
        """
        self.dv_editor_dialog = DVEditorDialog(self)

        # current_variables = {"DV1": (["Val1", "Val2"], ["#FF0000", "#00FF00"]), "DV2": (["Val3"], ["#0000FF"])}
        self.dv_editor_dialog.current_dvs_temp = current_variables

        # detected_variants = {"Var1": (2, "DV1", "#FF0000"), "Var2": (4, "DV1", "#00FF00"), "Val3": (3, "DV2", "#0000FF")}
        self.dv_editor_dialog.detected_variants_temp = detected_variants

        # manually add variants to the table as the combobox trigger for adding variants for a DV cannot be called for adding a DV as the combobox is hidden
        # set the stored values for the selected IV
        self.dv_editor_dialog.tableWidget_dialog_dvaddvariants.setRowCount(
            0
        )  # clear the table widget to load all variants of the selected DV again

        # disconnect the cellChanged signal to prevent that the filling of the table triggers any changes in the model
        self.dv_editor_dialog.tableWidget_dialog_dvaddvariants.cellChanged.disconnect(
            self.dv_editor_dialog.update_dv_grouping
        )
        for (
            variant,
            variant_data,
        ) in self.dv_editor_dialog.detected_variants_temp.items():
            # add all variants of the selected DV to the table with "False" as the default value for the checkbox, as new DVs have no variants selected by default
            self.dv_editor_dialog.add_item_to_variant_list(
                item_text=variant, is_grouped_to_dv=False, variant_color=variant_data[2]
            )
        self.dv_editor_dialog.tableWidget_dialog_dvaddvariants.cellChanged.connect(
            self.dv_editor_dialog.update_dv_grouping
        )

        # Show/Hide elements, as generic editor dialog holds elements
        self.dv_editor_dialog.comboBox_selectdv.hide()
        self.dv_editor_dialog.btn_editconfirm.hide()
        self.dv_editor_dialog.btn_delete_dv.hide()
        self.dv_editor_dialog.label_selectdv.hide()
        self.dv_editor_dialog.label_dvname.setText("Input DV-Name:")
        self.dv_editor_dialog.lineEdit_nameinput.setPlaceholderText(
            "Input Variable-Name..."
        )
        self.dv_editor_dialog.lineEdit_nameinput.setEnabled(True)
        self.dv_editor_dialog.tableWidget_dialog_dvaddvariants.setEnabled(True)
        self.dv_editor_dialog.buttonBox.button(
            QDialogButtonBox.StandardButton.Save
        ).setEnabled(False)

    def delete_add_dv_dialog(self):
        """
        Deletes the dv_editor_dialog instance.
        """
        self.dv_editor_dialog = None

    def create_edit_dv_dialog(
        self,
        clicked_item: QTreeWidgetItem,
        column,
        detected_variants: Dict[str, Tuple[int, str, str]] = None,
        current_variables: Dict[str, Tuple[List[str], List[str]]] = None,
    ):  # TODO: Needs: List of DVs Variants with Colors and their current associated DV from Model, as well as list of all current DVs and their grouped variants
        """
        Opens a dialog for editing or deleting a dependent variable (DV).

        Parameters:
        - clicked_item (QTreeWidgetItem): The item that was clicked in the tree widget.
        - column (int): The column index of the clicked item.
        - detected_variants (List[Dict[str, Any]]): A list of detected variants for the DV.
        - current_variables (Dict[str, List[Dict[str, Any]]]): The list of current DVs to update the view with according to the model.

        Description:
        - This function creates an instance of the DVEditorDialog class.
        - If a clicked_item is provided, the function sets the current index of the comboBox_selectdv
            in the dv_editor_dialog to match the text of the clicked_item. This scenario happens when
            the user double-clicks a DV in the tree widget to edit it. If no clicked_item is provided,
            the function opens the dialog for the DV editor with its default settings, as it was opened
            by the user clicking the edit-button.
        - The function then manually triggers the on_combobox_activated() function of the dv_editor_dialog
            to update the dialog based on the selected DV.
        """
        self.dv_editor_dialog = DVEditorDialog(self)

        # current_variables = {"DV1": (["Val1", "Val2"], ["#FF0000", "#00FF00"]), "DV2": (["Val3"], ["#0000FF"])}
        self.dv_editor_dialog.current_dvs_temp = current_variables

        # detected_variants = {"Var1": (2, "DV1", "#FF0000"), "Var2": (4, "DV1", "#00FF00"), "Val3": (3, "DV2", "#0000FF")}
        self.dv_editor_dialog.detected_variants_temp = detected_variants

        self.dv_editor_dialog.comboBox_selectdv.addItems(
            [var for var in current_variables.keys()]
        )

        if (
            clicked_item is not None
        ):  # is not None == method called from double-clicking the item -> Open edit for item directly, otherwise disable buttons and start with item selection
            item_text = clicked_item.text(column)
            for index in range(self.dv_editor_dialog.comboBox_selectdv.count()):
                combobox_text = self.dv_editor_dialog.comboBox_selectdv.itemText(index)
                if item_text == combobox_text:
                    self.dv_editor_dialog.comboBox_selectdv.setCurrentIndex(index)
                    break
            # TODO: Check model conformance etc.
            # manually trigger combobox-reactions, as signals are only connected after create-function is finished
            self.dv_editor_dialog.on_combobox_activated()

    def delete_edit_dv_dialog(self):
        """
        Deletes the dv_editor_dialog instance.
        """
        self.dv_editor_dialog = None

    def create_add_speaker_dialog(
        self,
        current_speakers: Dict[str, Tuple[Dict[str, str], str]] = None,
        current_ivs: Dict[str, List[str]] = None,
    ):
        """
        Creates a dialog for adding a new speaker.

        This function initializes and configures the speaker editor dialog
        for adding a new speaker. It hides unnecessary elements, enables
        necessary elements, and sets default values for certain fields.
        """
        self.speaker_editor_dialog = SpeakerEditorDialog(self)

        # current_speakers = {"Speaker1": ({"IV1":"Val1", "IV2":"Val3"}, "#FF0000"), "Speaker2": ({"IV1":"Val2", "IV2":"Val4", "IV3":"Val5"}, "#00FF00")}
        self.speaker_editor_dialog.current_speakers_temp = current_speakers

        # current_ivs = {"IV1": ["Val1", "Val2"], "IV2": ["Val3", "Val4"], "IV3": ["Val5", "Val6"], "IV4": ["Val7", "Val8"], "IV5": ["Val9", "Val10"], "IV6": ["Val11", "Val12"], "IV7": ["Val13", "Val14"], "IV8": ["Val15", "Val16"], "IV9": ["Val17", "Val18"], "IV10": ["Val19", "Val20"]}
        self.speaker_editor_dialog.current_ivs_temp = current_ivs

        for iv_name, iv_values in current_ivs.items():
            # get the all selected values for each iv for the current speaker --> Set default values as the user needs to select them for a newly added speaker
            self.speaker_editor_dialog.add_iv_item_row(iv_name, iv_values)

        self.speaker_editor_dialog.comboBox_selectspeaker.hide()
        self.speaker_editor_dialog.btn_delete_speaker.hide()
        self.speaker_editor_dialog.lineEdit_nameinput.setEnabled(True)
        self.speaker_editor_dialog.label_speakerselect.hide()
        self.speaker_editor_dialog.label_speakername.setText("Input Speaker-Name:")
        self.speaker_editor_dialog.btn_changecolor.setEnabled(True)
        self.speaker_editor_dialog.scrollArea_ivscontents.setEnabled(True)
        self.speaker_editor_dialog.buttonBox.button(
            QDialogButtonBox.StandardButton.Save
        ).setEnabled(False)

    def delete_add_speaker_dialog(self):
        """
        Deletes the speaker_editor_dialog instance.
        """
        self.speaker_editor_dialog = None

    def create_edit_speaker_dialog(
        self,
        clicked_item: QTreeWidgetItem,
        column,
        current_speakers: Dict[str, Tuple[Dict[str, str], str]] = None,
        current_ivs: Dict[str, List[str]] = None,
    ):  # TODO: Needs: List of IVs and their values so that the editor can display Ivs and their values for the user to select for a speaker. List of all current speakers and their set attributes
        """
        Opens a dialog for editing or deleting a speaker.

        Parameters:
        - clicked_item (QTreeWidgetItem): The item that was clicked in the tree widget.
        - column (int): The column index of the clicked item.

        Description:
        - This function creates an instance of the SpeakerEditorDialog class.
        - If a clicked_item is provided, the function sets the current index of the comboBox_selectspeaker
            in the speaker_editor_dialog to match the text of the clicked_item. This scenario happens when
            the user double-clicks a speaker in the tree widget to edit it. If no clicked_item is provided,
            the function opens the dialog for the speaker editor with its default settings, as it was opened
            by the user clicking the edit-button.
        - The function then manually triggers the on_combobox_activated() function of the speaker_editor_dialog
            to update the dialog based on the selected speaker.
        """
        self.speaker_editor_dialog = SpeakerEditorDialog(self)

        # current_speakers = {"Speaker1": ({"IV1":"Val1", "IV2":"Val3"}, "#FF0000"), "Speaker2": ({"IV1":"Val2", "IV2":"Val4", "IV3":"Val5"}, "#00FF00")}
        self.speaker_editor_dialog.current_speakers_temp = current_speakers

        # current_ivs = {"IV1": ["Val1", "Val2"], "IV2": ["Val3", "Val4"], "IV3": ["Val5", "Val6"], "IV4": ["Val7", "Val8"], "IV5": ["Val9", "Val10"], "IV6": ["Val11", "Val12"], "IV7": ["Val13", "Val14"], "IV8": ["Val15", "Val16"], "IV9": ["Val17", "Val18"], "IV10": ["Val19", "Val20"]}
        self.speaker_editor_dialog.current_ivs_temp = current_ivs

        # add all items to combobox
        self.speaker_editor_dialog.comboBox_selectspeaker.addItems(
            [var for var in current_speakers.keys()]
        )

        # add all iv comboboxes to the scroll area
        for iv_name, iv_values in current_ivs.items():
            # get the all selected values for each iv for the current speaker --> Initially set default values for each, as on_combobox_activated will be called if the user selects a speaker initially and on each change
            self.speaker_editor_dialog.add_iv_item_row(iv_name, iv_values)

        if clicked_item is not None:
            item_text = clicked_item.text(column)
            for index in range(
                self.speaker_editor_dialog.comboBox_selectspeaker.count()
            ):
                combobox_text = (
                    self.speaker_editor_dialog.comboBox_selectspeaker.itemText(index)
                )
                if item_text == combobox_text:
                    self.speaker_editor_dialog.comboBox_selectspeaker.setCurrentIndex(
                        index
                    )
                    break
            # manually trigger combobox-reactions, as signals are only connected after create-function is finished
            self.speaker_editor_dialog.on_combobox_activated()

    def delete_edit_speaker_dialog(self):
        """
        Deletes the speaker_editor_dialog instance.

        Currently a copy the delete_add_speaker_dialog function, as different behaviour may be implemented in the future.
        """
        self.speaker_editor_dialog = None

    def create_detect_variants_dialog(
        self, detected_variants: Dict[str, Tuple[int, str, str]] = None
    ):
        """
        Creates a new instance of the detect_variants_dialog and fills it with the correct data, which in this case are the detected variants.

        Parameters:
        - detected_variants (List[Dict[str, Any]]): A list of detected variants for the DV, which includes the variant name, the number of occurrences, the DV it is associated with, and the color of the variant.
        """
        self.detect_variants_dialog = DetectVariantsDialog(self)
        if detected_variants is not None:
            # update the label
            self.detect_variants_dialog.update_label(detected_variants)
            # fill the table with the detected variants
            self.detect_variants_dialog.add_all_to_table(detected_variants)

    def delete_detect_variants_dialog(self):
        """
        Deletes the detect_variants_dialog instance.
        """
        self.detect_variants_dialog = None

    def create_open_project_dialog(self):
        """
        Creates a new instance of the open_project_dialog.
        """
        self.open_project_dialog = OpenProjectDialog(self)

    def delete_open_project_dialog(self):
        """
        Deletes the open_project_dialog instance.
        """
        self.open_project_dialog = None

    def create_generic_warning_dialog(self):
        """
        Creates a new instance of the generic_warning_dialog.
        """
        self.generic_warning_dialog = GenericWarningDialog(self)

    def delete_generic_warning_dialog(self):
        """
        Deletes the generic_warning_dialog instance.
        """
        self.generic_warning_dialog = None

    def create_analysis_success_dialog(self):
        """
        Creates a new instance of the analysis_success_dialog.
        """
        self.analysis_success_dialog = AnalysisSuccessDialog(self)

    def delete_analysis_success_dialog(self):
        """
        Deletes the analysis_success_dialog instance.
        """
        self.analysis_success_dialog = None

    def create_analysis_settings_confirmation_dialog(
        self, selected_dvs: List[str], selected_speakers: List[str]
    ):
        """
        Creates a new instance of the analysis_settings_confirmation_dialog.
        """
        self.analysis_settings_confirmation_dialog = AnalysisSettingsConfirmationDialog(
            self
        )
        self.analysis_settings_confirmation_dialog.add_all_dvs_to_list(selected_dvs)
        self.analysis_settings_confirmation_dialog.add_all_speakers_to_list(
            selected_speakers
        )

    def delete_analysis_settings_confirmation_dialog(self):
        """
        Deletes the analysis_settings_confirmation_dialog instance.
        """
        self.analysis_settings_confirmation_dialog = None

    def create_annotation_help_dialog(self):
        """
        Creates a new instance of the annotation_help_dialog.
        """
        self.annotation_help_dialog = AnnotationHelpDialog(self)

    def delete_annotation_help_dialog(self):
        """
        Deletes the annotation_help_dialog instance.
        """
        self.annotation_help_dialog = None

    def create_import_metadata_dialog(self):
        """
        Creates a new instance of the import_metadata_dialog.
        """
        self.import_metadata_dialog = ImportMetadataDialog(self)

    def delete_import_metadata_dialog(self):
        """
        Deletes the import_metadata_dialog instance.
        """
        self.import_metadata_dialog = None

    def create_export_metadata_dialog(self):
        """
        Creates a new instance of the export_metadata_dialog.
        """
        self.export_metadata_dialog = ExportMetadataDialog(self)

    def delete_export_metadata_dialog(self):
        """
        Deletes the export_metadata_dialog instance.
        """
        self.export_metadata_dialog = None

    def create_dv_detection_help_dialog(self):
        """
        Creates a new instance of the dv_detection_help_dialog.
        """
        self.dv_detection_help_dialog = VariableDetectionHelpDialog(self)

    def delete_dv_detection_help_dialog(self):
        """
        Deletes the dv_detection_help_dialog instance.
        """
        self.dv_detection_help_dialog = None

    def create_metadata_deletion_warning_dialog(self, called_from: str):
        """
        Creates a new instance of the metadata_deletion_warning_dialog.
        """
        self.metadata_deletion_warning_dialog = MetadataDeletionWarningDialog(self)

        if called_from == "IV":
            self.metadata_deletion_warning_dialog.label_effect.setText(
                "Speakers will lose their attributes for this IV"
            )
        elif called_from == "DV":
            self.metadata_deletion_warning_dialog.label_effect.setText(
                "Analysis results will be lost for this DV"
            )
        else:
            self.metadata_deletion_warning_dialog.label_effect.setText(
                "Words that are mapped to this speaker will not be considered in the analysis anymore"
            )

    def delete_metadata_deletion_warning_dialog(self):
        """
        Deletes the metadata_deletion_warning_dialog instance.
        """
        self.metadata_deletion_warning_dialog = None

    def create_invalid_input_warning_dialog(self):
        """
        Creates a new instance of the invalid_input_warning_dialog.
        """
        self.invalid_input_warning_dialog = InvalidInputWarningDialog(self)

    def delete_invalid_input_warning_dialog(self):
        """
        Deletes the invalid_input_warning_dialog instance.
        """
        self.invalid_input_warning_dialog = None





class ProjectInformationDialog(QDialog, Ui_ProjectInformationDialog):
    """
    Class for the project-information-dialog. This window allows the user to
    check and specify the project name and description, alongside other project related information.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Project Information")



class AnnotationformatEditorDialog(QDialog, Ui_EditorAnnotationformatDialog):
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
            item_text = source_item.item(0, 0).text()

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


class AnnotationRemovalDialog(QDialog, Ui_AnnotationFormatRemoveDialog):
    """
    Class for the annotation-specification-dialog. This window informs user
    about the irreversibility of deleting a format.
    """

    remove_format_accepted = Signal(bool)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Warning: Deletion of Annotation Format")

    def accept(self) -> None:
        """
        Accepts the deletion of the annotation format and closes the dialog.
        """

        # Check if the user provided a project name
        dont_show_again = self.checkBox_showagain.isChecked()

        # Send a signal to the controller
        self.remove_format_accepted.emit(dont_show_again)

        # Close the Window
        self.done(0)


class DetectVariantsDialog(QDialog, Ui_DetectVariantsDialog):
    """
    Class for the detected-variants-dialog. Opens a dialog window that displays
    all detected variants for the selected annotation formats.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Detected Variants")

        # last column smaller
        self.tableWidget_variants.setColumnWidth(0, 500)
        self.tableWidget_variants.setColumnWidth(1, 200)

        # Fix column size
        for column in range(self.tableWidget_variants.columnCount()):
            self.tableWidget_variants.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

        # NOTE: Hide for simplicity, can be removed if features need to be included later
        self.btn_extractlater.hide()
        self.widget_recommendation.hide()

        self.update_label(
            {"Variant 1": (5, "asdasd", "dddasd"), "Variant2": (3, "asdasd", "dddasd")}
        )
        self.add_all_to_table(
            {"Variant 1": (5, "asdasd", "dddasd"), "Variant2": (3, "asdasd", "dddasd")}
        )
        # self.add_row_to_table("Variant 1", "5")
        # self.add_row_to_table("Variant 2", "3")
        # self.add_row_to_table("Variant 3", "2")
        # self.add_row_to_table("Variant 4", "1")
        # self.add_row_to_table("Variant 5", "1")
        # self.add_row_to_table("Variant 6", "1")
        # self.add_row_to_table("Variant 7", "1")
        # self.add_row_to_table("Variant 8", "1")
        # self.add_row_to_table("Variant 9", "1")
        # self.add_row_to_table("Variant 10", "1")
        # self.add_row_to_table("Variant 11", "5")

    def update_label(self, detected_variants: Dict[str, Tuple[int, str, str]]):
        """
        Updates the label that displays the number of detected variants.

        Parameters:
        - detected_variants (Dict[str, Tuple[int, str, str]]): A dictionary containing the detected variants and their occurences.
        """
        # calculate the number of detected annotations and variants based on the detected variants
        num_detected_annotations = 0
        for variant in detected_variants:
            num_detected_annotations += detected_variants[variant][0]
        num_detected_variants = len(detected_variants)

        text = (
            f"With the specified annotation format(s), <i>CorpusCompass</i> was able to detect "
            f"<b>{num_detected_annotations}</b> annotations and <b>{num_detected_variants}</b> Dependent Variable - Variants for these annotations."
        )
        self.label_detectionsummary.setText(text)

    def add_row_to_table(self, detected_variant: str, occurences: str):
        """
        Adds a new row to the table widget in the detected variants dialog.

        Parameters:
        - left_column_data: The data for the left column of the new row.
        - right_column_data: The data for the right column of the new row.
        """
        font_size = 12

        current_row_count = self.tableWidget_variants.rowCount()
        self.tableWidget_variants.insertRow(current_row_count)

        left_item = QTableWidgetItem(detected_variant)
        left_item.setFont(FontConfig.get_standardized_font(font_size, True))
        left_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_variants.setItem(current_row_count, 0, left_item)

        right_item = QTableWidgetItem(occurences)
        right_item.setFont(FontConfig.get_standardized_font(font_size, True))
        right_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_variants.setItem(current_row_count, 1, right_item)

    def reject(self) -> None:
        """
        Rejects the detection of variants and closes the dialog.
        """
        # TODO: Remove this later when possibility exists for user to not extract variants immediately
        self.accept()

    def clear_table(self):
        """
        Clears the table widget in the detected variants dialog.
        """
        self.tableWidget_variants.clearContents()
        self.tableWidget_variants.setRowCount(0)

    def add_all_to_table(self, detected_variants: Dict[str, Tuple[int, str, str]]):
        """
        Adds all detected variants to the table widget in the detected variants dialog.

        Parameters:
        - data_list (List[Tuple[str, str]]): A list of tuples containing the detected variants and their occurences.
        """
        self.clear_table()
        for dv_name, dv_data in detected_variants.items():
            self.add_row_to_table(dv_name, str(dv_data[0]))


class AddSymbolDialog(QDialog, Ui_AddSymbolsDialog):
    """
    Class for the annotation-specification-dialog. Opens a further dialog window
    in which symbols for the annotation format builder can be added.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Add Symbols")

    # TODO: Check if symbol was already in current symbols before adding, Propagate Changes

    def add_symbol_to_list_old_symbols(self, symbol):
        """
        Adds a new symbol to the list widget in the dialog that contains all symbols for the annotation format builder.
        """
        new_item = QListWidgetItem(symbol)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listwidget_annotformat_oldsymbols.addItem(new_item)

    def add_symbol_to_list_new_symbols(self, symbol):
        """
        Adds a new symbol to the list widget in the dialog that contains all symbols for the annotation format builder.
        """
        new_item = QListWidgetItem(symbol)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listwidget_annotformat_symbolcontainer.addItem(new_item)

    def on_add_symbol_clicked(self):
        """
        Is called when the "add symbol"-button is clicked in the
        dialog adding symbols in the annotation builder. Checks if
        1. there is no input 2. the input is not a character
        3. the input is not already in the model. If none of
        the above apply, then the character can be added
        to the list of symbols in the model and the view.
        """
        new_symbol = self.lineEdit_newsymbol.text()
        self.lineEdit_newsymbol.setText("")
        if new_symbol == "" or new_symbol == " ":
            self.label_symbolalreadyadded.setText("No symbol input!")
            self.label_symbolalreadyadded.show()
        elif new_symbol.isalpha() or new_symbol.isdigit():
            self.label_symbolalreadyadded.setText(
                "Alphabetic symbols and digits should not be used for marking annotations!"
            )
            self.label_symbolalreadyadded.show()
        elif (
            len(
                self.listwidget_annotformat_oldsymbols.findItems(
                    new_symbol, Qt.MatchFlag.MatchCaseSensitive
                )
            )
            > 0
            or len(
                self.listwidget_annotformat_symbolcontainer.findItems(
                    new_symbol, Qt.MatchFlag.MatchCaseSensitive
                )
            )
            > 0
        ):
            self.label_symbolalreadyadded.setText("Symbol already added!")
            self.label_symbolalreadyadded.show()
        else:
            self.add_symbol_to_list_new_symbols(new_symbol)
            self.label_symbolalreadyadded.hide()

    def add_all_symbols_to_list(self, current_symbol_list):
        """
        Adds all symbols from the current symbol list to the list widget in the dialog that contains all symbols for the annotation format builder.
        Called after initializing the dialog.
        """
        for symbol in current_symbol_list:
            self.add_symbol_to_list_old_symbols(symbol)
        self.listwidget_annotformat_oldsymbols.sortItems(
            order=Qt.SortOrder.DescendingOrder
        )


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


class GenericWarningDialog(QDialog, Ui_GenericWarningDialog):
    """
    Class for a generic warning dialog. Text inside the dialog
    can be changed as required. Serves no purpose to the
    model, but is just feedback for the user.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Warning")


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


class AnnotationHelpDialog(QDialog, Ui_AnnotationHelpDialog):
    """
    Class for a the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Help: Annotation Format")


class ImportMetadataDialog(QDialog, Ui_ImportMetadataDialog):
    """
    Class for a the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Import Metadata")


class ExportMetadataDialog(QDialog, Ui_ExportMetadataDialog):
    """
    Class for the help-dialog that explains the idea and process
    of specifying an annotation format.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Export Metadata")


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
            and self.comboBox_selectiv.isVisible() == True
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
            and self.comboBox_selectdv.isVisible() == True
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
            and self.comboBox_selectspeaker.isVisible() == True
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


class MetadataDeletionWarningDialog(QDialog, Ui_MetadataDeletionWarningDialog):
    """
    Dialog for displaying a warning message when deleting metadata.

    This dialog is used to display a warning message when the user tries to delete metadata.
    It inherits from QDialog and Ui_MetadataDeletionWarningDialog.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Warning: Deleting Metadata")


class VariableDetectionHelpDialog(QDialog, Ui_VariableDetectionHelpDialog):
    """
    Dialog that holds information about how the detection of variable variants works.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Help: Detected DV-Variants")


class InvalidInputWarningDialog(QDialog, Ui_InvalidInputWarningDialog):
    """
    Dialog that displays a warning message when the user tries to confirm an invalid input.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Warning: Invalid Input")



from corpuscompass.model.variables_speaker_detection import (
    SpeakerFormats,
    SpeakerDetector,
    AnnotationDetector,
)
from corpuscompass.model.files import (
    File,
)  # TODO: Files and Table with detected annotations should be handed over from controller



class CreateProjectDialog(QDialog, Ui_CreateProjectDialog):
    """
    The dialog is opened, if a new project should be created.
    """

    create_proj_accepted = Signal(str)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

    def accept(self) -> None:
        """
        Method is called, if the user clicks on "OK" in the dialog window. The
        Method checks first, if the necessary informations are provided by the
        user before sending a signal to the controller.
        """
        proj_name = self.proj_name_lineedit.text()

        # Check if the user provided a project name
        if len(proj_name) == 0:
            self.display_error_message("The project name cannot be empty!")
            return

        print("emitting signal")
        # Send a signal to the controller
        self.create_proj_accepted.emit(proj_name)

        # Close the Window
        self.done(0)

    def reject(self) -> None:
        """
        Method is called, if the user clickes on "Cancel" in the dialog window.
        Closes the window.
        """
        self.done(0)

    def display_error_message(self, text: str) -> None:
        """
        Method displays a red error message at the bottom of the dialog window.

        Args:
            text (str): The error-message, that should be displayed.
        """
        self.error_message_label.setText(text)
