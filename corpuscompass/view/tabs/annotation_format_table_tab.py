from typing import TYPE_CHECKING, Dict


from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidgetItem,
)
from corpuscompass.view.generated.ui_annotation_format_table_tab import (
    Ui_AnnotationFormatTableTab,
)
from corpuscompass.view.tabs.lazy_signal_tab import LazySignalTab

if TYPE_CHECKING:
    from corpuscompass.view.corpus_compass_view import CorpusCompassView


class AnnotationFormatTableTab(LazySignalTab, Ui_AnnotationFormatTableTab):
    """
    Class for the annotation-format-tab. This window serves for
    checking and managing the specified annotation formats for a
    project.
    """

    def connect_signals(self, controller) -> None:
        """
        Connect signals from the annotation format tab to the corresponding controller methods.
        Called lazily when the tab is first shown.
        """

        self.btn_annotformat_save.clicked.connect(
            controller.on_annotformat_section_saved_clicked
        )
        # self.btn_annotformat_removerows.clicked.connect(controller.on_annotformat_section_removeformats_clicked)

        self.btn_help.clicked.connect(controller.on_annotformat_help_button_clicked)
        self.btn_annotformat_cancel.clicked.connect(
            controller.on_annotformat_cancel_button_clicked
        )

        self.btn_annotformat_addnew.clicked.connect(
            lambda: controller.on_open_annotation_format_editor(
                row=-1, column=-1, called_for_add=True
            )
        )
        self.btn_annotformat_edit.clicked.connect(
            lambda: controller.on_open_annotation_format_editor(
                row=-1, column=-1, called_for_add=False
            )
        )

        # Automatically passes (row, column) when double-clicked
        self.tableWidget_annotformats.cellDoubleClicked.connect(
            controller.on_open_annotation_format_editor
        )

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view: "CorpusCompassView" = parent

        # show/hide
        self.btn_annotformat_cancel.hide()  # Hide Cancel button for now to make workflow more clear

        # Fix column size
        for column in range(self.tableWidget_annotformats.columnCount()):
            self.tableWidget_annotformats.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

    def add_format_to_table(self, format: str, regex: str):
        """
        Adds a new annotation format to the table widget.

        Parameters:
        - format (str): The annotation format.
        - regex (str): The regular expression associated with the format.
        """
        str_annot_format = format
        str_regex = regex

        format_item = QTableWidgetItem(str_annot_format)
        format_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        regex_item = QTableWidgetItem(str_regex)
        regex_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        current_row_count = self.tableWidget_annotformats.rowCount()
        self.tableWidget_annotformats.insertRow(current_row_count)

        self.tableWidget_annotformats.setItem(current_row_count, 0, format_item)
        self.tableWidget_annotformats.setItem(current_row_count, 1, regex_item)

    def remove_format_item_from_table(self, remove_row_formats):
        """
        Removes the selected annotation-format-items from the
        table widget that contains all annotation formats.

        Parameters:
        - remove_row_formats (List[str]): A list of annotation formats to be removed.
        """
        for row in range(self.tableWidget_annotformats.rowCount() - 1, -1, -1):
            if self.tableWidget_annotformats.item(row, 0).text() in remove_row_formats:
                self.tableWidget_annotformats.removeRow(row)

    def clear_table(self):
        """
        Clears the table widget that contains all annotation formats.
        """
        self.tableWidget_annotformats.setRowCount(0)

    def fill_table(self, formats: Dict[str, str]):
        """
        Fills the table widget with the specified annotation formats.

        Parameters:
        - formats (Dict[str, str]): A dictionary containing the annotation formats and their associated regular expressions.
        """
        self.clear_table()
        for format, regex in formats.items():
            self.add_format_to_table(format, regex)
