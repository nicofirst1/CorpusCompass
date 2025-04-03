"""
The module contains classes for the gui of CorpussCompass. The main class is
"CorpusCompassView".
"""

import inspect
from typing import Any, Dict, List, Tuple

import PySide6
from corpuscompass.view.dialogs import (
    AddSymbolDialog,
    AnalysisSettingsConfirmationDialog,
    AnalysisSuccessDialog,AnnotationFormatEditorDialog,AnnotationHelpDialog,AnnotationRemovalDialog,
    CreateProjectDialog,DetectVariantsDialog,DVEditorDialog,ExportMetadataDialog,ImportMetadataDialog,
    InvalidInputWarningDialog,IVEditorDialog,MetadataDeletionWarningDialog,OpenProjectDialog,
    ProjectInformationDialog,SpeakerEditorDialog,VariableDetectionHelpDialog
)

from corpuscompass.view.tabs import (
    AnalysisSettingsTab,AnnotationFormatTableTab,GeneralSettingsTab,HomeMenuTab,
    LazySignalTab,LoadFilesTab,SpeakerIdentificationTab,StartScreenTab,Tab,VariableManagementTab
)

from corpuscompass.view.font_configs import FontColors, FontConfig
from corpuscompass.view.tabs.annotation_format_table_tab import AnnotationFormatTableTab
from corpuscompass.view.tabs.general_settings_tab import GeneralSettingsTab
from corpuscompass.view.tabs.load_files_tab import LoadFilesTab
from corpuscompass.view.tabs.speaker_identification_tab import SpeakerIdentificationTab
from corpuscompass.view.tabs.start_screen_tab import StartScreenTab
from corpuscompass.view.tabs.tab import Tab
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
        self.annotationformat_editor_dialog = AnnotationFormatEditorDialog(self)
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
        self.annotationformat_editor_dialog = AnnotationFormatEditorDialog(self)
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





from corpuscompass.model.variables_speaker_detection import (
    SpeakerFormats,
    SpeakerDetector,
    AnnotationDetector,
)
from corpuscompass.model.files import (
    File,
)  # TODO: Files and Table with detected annotations should be handed over from controller

