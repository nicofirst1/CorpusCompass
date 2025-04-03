from typing import TYPE_CHECKING, Dict
from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidgetItem,
)
from PySide6.QtGui import (
    QColor,
)

from PySide6.QtCore import Qt

from corpuscompass.view.font_configs import FontConfig
from corpuscompass.view.generated.ui_speaker_format_tab import Ui_SpeakerIdTab
from corpuscompass.view.tabs.lazy_signal_tab import LazySignalTab
from corpuscompass.view.utils import expand_button_clicked

if TYPE_CHECKING:
    from corpuscompass.view.corpus_compass_view import CorpusCompassView


class SpeakerIdentificationTab(LazySignalTab, Ui_SpeakerIdTab):
    """
    Class for the speaker-identification tab. This window allows the user to
    specify the transcription format in order to detect speakers and associate
    them with their spoken text.
    """

    def connect_signals(self, controller) -> None:
        """
        Connect signals from the speaker tab to the corresponding controller methods.
        Called lazily when the tab is first shown.
        """

        self.btn_sp_save.clicked.connect(controller.on_speaker_format_saved_clicked)
        self.btn_sp_cancel.clicked.connect(controller.on_speaker_cancel_button_clicked)

        self.btn_expand_speakerinfo.clicked.connect(self.on_speaker_expand_clicked)
        self.btn_expand_wordinfo.clicked.connect(self.on_words_expand_clicked)

        self.radbtn_sp_standard.toggled.connect(
            lambda: controller.on_speaker_format_changed(self.radbtn_sp_standard)
        )
        self.radbtn_sp_praat.toggled.connect(
            lambda: controller.on_speaker_format_changed(self.radbtn_sp_praat)
        )
        self.radbtn_sp_flex.toggled.connect(
            lambda: controller.on_speaker_format_changed(self.radbtn_sp_flex)
        )
        self.radbtn_sp_elan.toggled.connect(
            lambda: controller.on_speaker_format_changed(self.radbtn_sp_elan)
        )

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view: "CorpusCompassView" = parent

        # show/hide elements
        self.tableWidget_distinctspeakers.hide()
        self.tableWidget_unassignedwords.hide()

        # self.add_speaker_table_row("Speaker 1", 10)
        # self.add_speaker_table_row("Speaker 2", 5)

        # self.add_words_table_row("File 1", 11)
        # self.add_words_table_row("File 2", 2)
        self.add_all_speakers_to_table({"Speaker 1": 10, "Speaker 2": 5})
        self.add_all_words_to_table({"File 1": 11, "File 2": 2})
        self.update_labels(2, 13)

        for column in range(self.tableWidget_distinctspeakers.columnCount()):
            self.tableWidget_distinctspeakers.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )
            self.tableWidget_unassignedwords.horizontalHeader().setSectionResizeMode(
                column, QHeaderView.ResizeMode.Fixed
            )

    def get_selected_format(self) -> str:
        """
        Returns the selected speaker format. Currently supported formats are
        "STANDARD", "PRAAT", "ELAN", "FLEX"

        Returns:
        - str: The selected transcription format.
        """
        if self.radbtn_sp_standard.isChecked():
            return "STANDARD"
        if self.radbtn_sp_praat.isChecked():
            return "PRAAT"
        if self.radbtn_sp_elan.isChecked():
            return "ELAN"
        if self.radbtn_sp_flex.isChecked():
            return "FLEX"

    def update_labels(self, speaker_count: int, word_count: int):
        """
        Updates the labels of the speaker-identification tab with the current speaker and word count.

        Parameters:
        - speaker_count (int): The total number of detected speakers.
        - word_count (int): The total number of undetected words.
        """
        self.label_distinctspeakercount.setText(str(speaker_count))
        self.label_unassignedwordcount.setText(str(word_count))

    def on_speaker_expand_clicked(self):
        """
        Is called when the user clicks on the expand button for showing more information about the detected speakers.
        """
        expand_button_clicked(
            self.tableWidget_distinctspeakers, self.btn_expand_speakerinfo
        )

    def on_words_expand_clicked(self):
        """
        Is called when the user clicks on the expand button for showing more information about undetected words in the corpus.
        """
        expand_button_clicked(
            self.tableWidget_unassignedwords, self.btn_expand_wordinfo
        )

    def add_all_speakers_to_table(self, speakers: Dict[str, int]):
        """
        Adds all detected speakers to the table widget.

        Parameters:
        - speakers (Dict[str, int]): A dictionary containing the detected speakers and the number of occurrences.
        """
        # clear the table before adding all speakers
        self.clear_speaker_table()
        for speaker, occurrences in speakers.items():
            self.add_speaker_table_row(speaker, occurrences)

    def add_speaker_table_row(self, left_column_data: str, right_column_data: int):
        """
        Adds a new row to the table widget containing the detected speakers.

        Parameters:
        - left_column_data (str): The data for the left column of the new row.
        - right_column_data (int): The data for the right column of the new row.
        """

        font_size = 10

        current_row_count = self.tableWidget_distinctspeakers.rowCount()
        self.tableWidget_distinctspeakers.insertRow(current_row_count)

        left_item = QTableWidgetItem(left_column_data)
        left_item.setFont(FontConfig.get_standardized_font(font_size, False))
        left_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_distinctspeakers.setItem(current_row_count, 0, left_item)

        right_item = QTableWidgetItem(str(right_column_data))
        right_item.setFont(FontConfig.get_standardized_font(font_size, False))
        right_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_distinctspeakers.setItem(current_row_count, 1, right_item)

    def add_all_words_to_table(self, words: Dict[str, int]):
        """
        Adds all undetected words for each file to the table widget.

        Parameters:
        - words (Dict[str, int]): A dictionary containing the undetected words and the number of occurrences.
        """
        # clear the table before adding all words
        self.clear_words_table()
        for word, occurrences in words.items():
            self.add_words_table_row(word, occurrences)

    def add_words_table_row(self, left_column_data: str, right_column_data: int):
        """
        Adds a new row to the table widget containing the undetected words. Used explicit function as
        this table may differ in style from the speaker table.

        Parameters:
        - left_column_data (str): The data for the left column of the new row.
        - right_column_data (str): The data for the right column of the new row.
        """

        font_size = 10

        current_row_count = self.tableWidget_unassignedwords.rowCount()
        self.tableWidget_unassignedwords.insertRow(current_row_count)

        left_item = QTableWidgetItem(left_column_data)
        left_item.setFont(FontConfig.get_standardized_font(font_size, False))
        # TODO: Change color depending on the amount of undetected words (second column value) in a meaningful way only once as well
        if right_column_data > 5:
            left_item.setForeground(QColor(255, 0, 0))
        left_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_unassignedwords.setItem(current_row_count, 0, left_item)

        right_item = QTableWidgetItem(str(right_column_data))
        right_item.setFont(FontConfig.get_standardized_font(font_size, False))
        # TODO: Change color depending on the amount of undetected words (second column value) in a meaningful way only once as well
        if right_column_data > 5:
            right_item.setForeground(QColor(255, 0, 0))
        right_item.setTextAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.tableWidget_unassignedwords.setItem(current_row_count, 1, right_item)

    def clear_words_table(self):
        """
        Clears the table widget that contains the undetected words.
        """
        self.tableWidget_distinctspeakers.setRowCount(0)

    def clear_speaker_table(self):
        """
        Clears the table widget that contains the detected speakers.
        """
        self.tableWidget_distinctspeakers.setRowCount(0)
