from typing import Dict
from PySide6.QtWidgets import (
    QWidget,
)

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QHeaderView,
    QTableWidgetItem,
)
from corpuscompass.view.generated.ui_annotation_format_table_tab import (
    Ui_AnnotationFormatTableTab,
)


class AnnotationFormatTableTab(QWidget, Ui_AnnotationFormatTableTab):
    """
    Class for the annotation-format-tab. This window serves for
    checking and managing the specified annotation formats for a
    project.
    """

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

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
