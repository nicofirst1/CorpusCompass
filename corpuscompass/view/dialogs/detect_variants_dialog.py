from typing import Dict, Tuple
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QHeaderView,
    QTableWidgetItem,
)
from PySide6.QtCore import Qt


from corpuscompass.view.font_configs import FontConfig
from corpuscompass.view.generated.ui_detecting_dvvariants_dialog import (
    Ui_DetectVariantsDialog,
)


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
