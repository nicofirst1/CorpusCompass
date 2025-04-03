from typing import TYPE_CHECKING, Dict, List, Tuple
from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidgetItem,
    QTreeWidgetItem,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
)


from corpuscompass.view.generated.ui_variable_management_tab import (
    Ui_VariableManagementTab,
)
from corpuscompass.view.tabs.lazy_signal_tab import LazySignalTab


if TYPE_CHECKING:
    from corpuscompass.view.corpus_compass_view import CorpusCompassView


class VariableManagementTab(LazySignalTab, Ui_VariableManagementTab):
    def connect_signals(self, controller):
        self.btn_save_changes.clicked.connect(controller.on_metadata_saved_clicked)
        # self.btn_cancel.clicked.connect(controller.on_metadata_cancel_clicked)
        self.btn_help.clicked.connect(controller.on_metadata_help_clicked)

        self.btn_add_iv.clicked.connect(
            lambda: controller.on_open_metadata_iv_editor(
                item=None, column=0, called_for_add=True
            )
        )
        self.btn_edit_ivs.clicked.connect(
            lambda: controller.on_open_metadata_iv_editor(
                item=None, column=0, called_for_add=False
            )
        )
        self.treeWidget_ivs.itemDoubleClicked.connect(
            controller.on_open_metadata_iv_editor
        )

        self.btn_add_dv.clicked.connect(
            lambda: controller.on_open_metadata_dv_editor(
                item=None, column=0, called_for_add=True
            )
        )
        self.btn_edit_dvs.clicked.connect(
            lambda: controller.on_open_metadata_dv_editor(
                item=None, column=0, called_for_add=False
            )
        )
        self.treeWidget_dvs.itemDoubleClicked.connect(
            controller.on_open_metadata_dv_editor
        )

        self.btn_add_speaker.clicked.connect(
            lambda: controller.on_open_metadata_speaker_editor(
                item=None, column=0, called_for_add=True
            )
        )
        self.btn_edit_speakers.clicked.connect(
            lambda: controller.on_open_metadata_speaker_editor(
                item=None, column=0, called_for_add=False
            )
        )
        self.treeWidget_speakers.itemDoubleClicked.connect(
            controller.on_open_metadata_speaker_editor
        )

        self.btn_import_metadata.clicked.connect(
            controller.on_import_metadata_button_clicked
        )
        self.btn_export_metadata.clicked.connect(
            controller.on_export_metadata_button_clicked
        )
        self.btn_detectvariants.clicked.connect(controller.on_detect_variants_clicked)

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view: "CorpusCompassView" = parent
        self.switch_tab(0)

        # Connect signals
        self.btn_open_iv.clicked.connect(lambda: self.switch_tab(0))
        self.btn_open_dv.clicked.connect(lambda: self.switch_tab(1))
        self.btn_open_speakers.clicked.connect(lambda: self.switch_tab(2))

        # show/hide elements

        self.label_corpuswaschanged.hide()
        self.label_detectednewvariants.hide()

        # decrease size of 4th column (color-column)
        self.tableWidget_detectedinformation.setColumnWidth(3, 100)

        # Fix column size
        for column in range(self.tableWidget_detectedinformation.columnCount()):
            self.tableWidget_detectedinformation.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

        for column in range(self.treeWidget_dvs.columnCount()):
            self.treeWidget_dvs.header().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

        for column in range(self.treeWidget_ivs.columnCount()):
            self.treeWidget_ivs.header().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

        for column in range(self.treeWidget_speakers.columnCount()):
            self.treeWidget_speakers.header().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

    def switch_tab(self, tab_id):
        """
        Switches the tab to the specified tab.
        """
        self.stackedWidget.setCurrentIndex(tab_id)
        self.btn_open_iv.setChecked(True if tab_id == 0 else False)
        self.btn_open_dv.setChecked(True if tab_id == 1 else False)
        self.btn_open_speakers.setChecked(True if tab_id == 2 else False)

    def update_detected_data(self):
        """
        Updates the detected data in the variable management tab.
        """
        # TODO Add all new detected DV-Variants to the top of the list, based on the model
        self.label_detectednewvariants.show()

    def on_detect_all_variants(self, variants):
        # forall variants:
        #   self.add_detected_variant_row(variant.info)
        pass

    def fill_detected_variants_fully(
        self, detected_variants, dv_values: Dict[str, Tuple[int, str, str]]
    ):
        """
        Fills the detected variants table with the detected variants.

        Parameters:
        - detected_variants (List[DetectedVariant]): The detected variants to display.
        """
        self.clear_detected_variants_table()
        for index, row in detected_variants.iterrows():
            variant_name = row["identifier"][0]
            variant_data = dv_values[variant_name]
            self.add_detected_variant_row(
                variant_name, variant_data[0], variant_data[2], variant_data[1]
            )

    def add_detected_variant_row(
        self,
        variant_name: str,
        occurences: int,
        color_hex: str,
        corresponding_dv: str = "-",
    ):
        """
        Adds a new row to the detected variants table with the given variant name, occurences, color, and corresponding DV.

        Parameters:
        - variant_name (str): The name of the variant.
        - occurences (int): The number of occurences of the variant.
        - color_hex (str): The hexadecimal representation of the color of the variant.
        - corresponding_dv (str): The name of the corresponding DV. Defaults to '-'.
        """
        variant_item = QTableWidgetItem(variant_name)
        variant_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        occurences_item = QTableWidgetItem(str(occurences))
        occurences_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        dv_item = QTableWidgetItem(corresponding_dv)
        dv_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        color_item = QTableWidgetItem()
        if color_hex is not None:
            color_item.setBackground(QColor(color_hex))

        current_row_count = self.tableWidget_detectedinformation.rowCount()
        self.tableWidget_detectedinformation.insertRow(current_row_count)

        self.tableWidget_detectedinformation.setItem(current_row_count, 0, variant_item)
        self.tableWidget_detectedinformation.setItem(
            current_row_count, 1, occurences_item
        )
        self.tableWidget_detectedinformation.setItem(current_row_count, 2, dv_item)
        self.tableWidget_detectedinformation.setItem(current_row_count, 3, color_item)

    def update_detected_variants_table(
        self, updated_variants: Dict[str, Tuple[int, str, str]]
    ):
        """
        Updates the detected variants table with the changes made to the model after the dv editor was used to either add new DVs, remove DVs, change the grouping of DVs or changing the colors of certain variants.
        """
        for row in range(self.tableWidget_detectedinformation.rowCount()):
            # get the variant name
            variant_name = self.tableWidget_detectedinformation.item(row, 0).text()
            # get the occurences
            # occurences = self.tableWidget_detectedinformation.item(row, 1).text()
            # get the corresponding DV
            corresponding_dv = self.tableWidget_detectedinformation.item(row, 2).text()
            # get the color
            color = (
                self.tableWidget_detectedinformation.item(row, 3)
                .background()
                .color()
                .name()
            )
            # get the updated data for the variant and check if any of the data has changed --> if so update the table
            if (
                variant_name in updated_variants.keys()
            ):  # also check if the variant is in the updated table (has to be, as the table is the source of the updated data and variants cannot be deleted in the DV editor, only grouped to another DV)
                updated_variants_data = updated_variants[variant_name]
                new_grouped_var = updated_variants_data[1]
                # check if the group (DV) of the variant is None, which means that it is/was ungrouped from a DV --> in this case, the DV in the table has to be updated to "-"
                if new_grouped_var is None:
                    new_grouped_var = "-"
                if new_grouped_var != corresponding_dv:
                    self.tableWidget_detectedinformation.item(row, 2).setText(
                        new_grouped_var
                    )
                if updated_variants_data[2] != color:
                    self.tableWidget_detectedinformation.item(row, 3).setBackground(
                        QColor(updated_variants_data[2])
                    )

    def add_all_ivs(self, ivs: Dict[str, List[str]]):
        """
        Adds all IVs to the IVs tree widget.

        Parameters:
        - ivs (Dict[str, List[str]]): The IVs to add to the tree widget.
        """
        # clear the tree widget before adding the new IVs
        self.clear_ivs_tree()
        for iv_name, iv_values in ivs.items():
            self.add_iv_row(iv_name, iv_values)

    def add_iv_row(self, iv_name: str, iv_values: List[str]):
        """
        Adds a new row to the IVs tree widget with the given IV name and values.

        Parameters:
        - iv_name (str): The name of the IV.
        - iv_values (List[str]): The values of the IV.
        """
        iv_item = QTreeWidgetItem([iv_name])
        for value in iv_values:
            value_item = QTreeWidgetItem([value])
            iv_item.addChild(value_item)
        self.treeWidget_ivs.addTopLevelItem(iv_item)

    def add_all_dvs(self, dvs: Dict[str, Tuple[List[str], List[str]]]):
        """
        Adds all DVs to the DVs tree widget.

        Parameters:
        - dvs (Dict[str, Tuple[List[str], List[str]]): The DVs to add to the tree widget.
        """
        # clear the tree widget before adding the new DVs
        self.clear_dvs_tree()
        for dv_name, dv_data in dvs.items():
            self.add_dv_row(dv_name, dv_data[0])

    def add_dv_row(self, dv_name: str, dv_variants: List[str]):
        """
        Adds a new row to the DVs tree widget with the given DV name, variants, and colors.

        Parameters:
        - dv_name (str): The name of the DV.
        - dv_variants (List[str]): The variants of the DV.
        - dv_colors (List[str]): The colors of the DV.
        """
        dv_item = QTreeWidgetItem([dv_name])
        for variant in dv_variants:
            variant_item = QTreeWidgetItem([variant])
            dv_item.addChild(variant_item)
        self.treeWidget_dvs.addTopLevelItem(dv_item)

    def add_all_speakers(self, speakers: Dict[str, Tuple[Dict[str, str], str]]):
        """
        Adds all speakers to the speakers tree widget.

        Parameters:
        - speakers (Dict[str, Tuple[Dict[str, str], str]]): The speakers to add to the tree widget.
        """
        # clear the tree widget before adding the new speakers
        self.clear_speakers_tree()
        for speaker_name, speaker_data in speakers.items():
            self.add_speaker_row(speaker_name, speaker_data[0])

    def add_speaker_row(self, speaker_name: str, speaker_ivs: Dict[str, str]):
        """
        Adds a new row to the speakers tree widget with the given speaker name, IVs, and color.

        Parameters:
        - speaker_name (str): The name of the speaker.
        - speaker_ivs (Dict[str, str]): The IVs of the speaker.
        - speaker_color (str): The color of the speaker.
        """
        speaker_item = QTreeWidgetItem([speaker_name])
        for iv_name, iv_value in speaker_ivs.items():
            item_name = iv_name + " : " + iv_value
            iv_item = QTreeWidgetItem([item_name])
            speaker_item.addChild(iv_item)
        self.treeWidget_speakers.addTopLevelItem(speaker_item)

    def clear_all_contents(self):
        """
        Clears all content in the DV editor tab. This function is called whenever there are changes to the content or to the underlying data that require a complete refresh of the content.
        """
        self.clear_detected_variants_table()
        self.clear_ivs_tree()
        self.clear_dvs_tree()
        self.clear_speakers_tree()

    def clear_detected_variants_table(self):
        """
        Clears all detected variants from the table. Useful for refreshing the table after changes to the detected variants.
        """
        self.tableWidget_detectedinformation.setRowCount(0)

    def clear_ivs_tree(self):
        """
        Clears all IVs from the tree widget. Useful for refreshing the tree widget after changes to the IVs.
        """
        self.treeWidget_ivs.clear()

    def clear_dvs_tree(self):
        """
        Clears all DVs from the tree widget. Useful for refreshing the tree widget after changes to the DVs.
        """
        self.treeWidget_dvs.clear()

    def clear_speakers_tree(self):
        """
        Clears all speakers from the tree widget. Useful for refreshing the tree widget after changes to the speakers.
        """
        self.treeWidget_speakers.clear()
