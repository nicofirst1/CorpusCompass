from corpuscompass.view.generated.ui_load_files_tab import Ui_LoadFilesTab


from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QTextEdit,
)

from PySide6.QtCore import Qt


class LoadFilesTab(QWidget, Ui_LoadFilesTab):
    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

        # Connect Signals
        self.tab_file_preview.tabCloseRequested.connect(self.closeTab)

    def add_file(self, file_name: str):
        self.add_item_to_stored_values(file_name, item_column=1, checkbox_column=0)
        # self.list_loaded_filenames.addItem(file_name)

    def show_file_content(self, file_name: str, file_content: str):
        already_open = False
        old_tab_count = self.tab_file_preview.tabBar().count()
        for index in range(old_tab_count):
            tab_text = self.tab_file_preview.tabBar().tabText(index)
            if tab_text == file_name:
                already_open = True
                tab_index = index
                break

        if not already_open:
            file_preview = QTextEdit()
            file_preview.setText(file_content)
            file_preview.setReadOnly(True)
            self.tab_file_preview.addTab(file_preview, file_name)
            self.tab_file_preview.setCurrentIndex(old_tab_count)
        else:
            self.tab_file_preview.setCurrentIndex(tab_index)

    def closeTab(self, id: int):
        self.tab_file_preview.removeTab(id)

    def remove_selected_values(self):
        """
        Removes selected files from the table-widget ("list") that
        contains all files. Also closes all opened tabs that
        showed files that are now removed.
        """
        removed_files = []
        for row in range(self.list_loaded_filenames.rowCount() - 1, -1, -1):
            if (
                self.list_loaded_filenames.item(row, 0).checkState()
                == Qt.CheckState.Checked
            ):
                removed_files.append(self.list_loaded_filenames.item(row, 1).text())
                self.list_loaded_filenames.removeRow(row)

        for index in range(self.tab_file_preview.tabBar().count() - 1, -1, -1):
            tab_text = self.tab_file_preview.tabBar().tabText(index)
            if tab_text in removed_files:
                self.tab_file_preview.removeTab(index)

    def add_item_to_stored_values(
        self, item_text: str, item_column: int, checkbox_column: int
    ):
        """
        Adds a checkbox with the correct style at the correct position and a new item at the correct position to the table widget.
        """
        self.list_loaded_filenames.insertRow(0)

        new_item = QTableWidgetItem(item_text)
        self.list_loaded_filenames.setItem(0, item_column, new_item)

        checkbox_item = QTableWidgetItem()
        checkbox_item.setFlags(
            Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled
        )
        checkbox_item.setCheckState(Qt.CheckState.Unchecked)
        self.list_loaded_filenames.setItem(0, checkbox_column, checkbox_item)
