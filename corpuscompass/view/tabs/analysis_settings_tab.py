from corpuscompass.model.files import File
from corpuscompass.model.variables_speaker_detection import (
    AnnotationDetector,
    SpeakerDetector,
)
from corpuscompass.view.generated.ui_analysis_settings_tab import Ui_AnalysisSettingsTab

from typing import Dict, List, Tuple

from PySide6.QtWidgets import (
    QPushButton,
    QGridLayout,
    QSizePolicy,
    QWidget,
    QCheckBox,
    QPlainTextEdit,
    QLabel,
    QScrollArea,
)
from PySide6.QtGui import (
    QTextCharFormat,
    QColor,
    QTextCursor,
)

from PySide6.QtCore import Qt, QRect

from corpuscompass.view.utils import (
    expand_button_clicked,
    set_abbreviate_label,
    set_checkbox_stylesheet,
    set_expand_button_stylesheet,
)


class AnalysisSettingsTab(QWidget, Ui_AnalysisSettingsTab):
    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

        self.file_name_text_edit_mapping: Dict[str, QPlainTextEdit] = {}
        self.dv_checkbox_mapping: Dict[str, QCheckBox] = {}
        self.speaker_checkbox_mapping: Dict[str, QCheckBox] = {}

        self.checkBox_selectall_dvs.toggled.connect(
            lambda: self.check_all(
                self.scrollArea_dvcontents, self.checkBox_selectall_dvs
            )
        )
        self.checkBox_selectall_speakers.toggled.connect(
            lambda: self.check_all(
                self.scrollArea_speakercontents, self.checkBox_selectall_speakers
            )
        )

        # ALL BELOW IN INIT IS JUST FOR TESTING (REMOVE LATER)
        # self.add_file_text_edit("Testfile1", "A: This is a file!", 5)
        # self.add_file_text_edit("Testfile2", "B: This is another file!", 6)
        # self.add_file_text_edit("Testfile3", "C: This is a third one!", 7)
        # self.add_file_text_edit("Testfile4", "A: Last File!", 8)

        annotation_detector = AnnotationDetector()
        #speaker_detector = SpeakerDetector()

        # Check if the detector generates a correct re from the following string:
        annotation_format_str = "[$TOKEN.IDENTIFIER]"
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str=annotation_format_str, token=(2, 6), identifier=(8, 17)
        )

        # filetext = self.corpusPlainTextEdit.toPlainText()
        # f1 = File("File1", "utf8", "./file1.txt", 1.0, filetext)

        # self.detected_speakers = None #speaker_detector.detect_speakers([f1])
        # self.detected_annotations = None #annotation_detector.detect_annotations([f1])

        # self.add_dv_container("DV1", ["var1", "var2", "var3"], ["#123123", "#777888", "#341231"], 0)
        # self.add_dv_container("DV2", ["var1", "var1.5", "var2", "var3"], ["#123123", "#777888", "#341231", "#987654"], 1)

        # self.add_single_metadata_row_to_container(self.scrollArea_speakercontents, 0, "A", "#023132")
        # self.add_single_metadata_row_to_container(self.scrollArea_speakercontents, 1, "B", "#033332")
        # self.add_single_metadata_row_to_container(self.scrollArea_speakercontents, 2, "C", "#015738")

        # TEST END

    def add_all_dvs(self, model_dvs: Dict[str, Tuple[List[str], List[str]]]):
        """
        Adds all DVs to the scroll area that displays the DVs. Clears the scroll area before adding the new DVs.
        """
        self.clear_scroll_area_dvs()
        dv_id = 0
        for dv_name, dv_data in model_dvs.items():
            self.add_dv_container(dv_name, dv_data[0], dv_data[1], dv_id)
            dv_id += 1

    def add_all_speakers(self, model_speakers: Dict[str, Tuple[Dict[str, str], str]]):
        """
        Adds all speakers to the scroll area that displays the speakers. Clears the scroll area before adding the new speakers.
        """
        self.clear_scroll_area_speakers()
        speaker_id = 0
        for speaker_name, speaker_data in model_speakers.items():
            self.add_single_metadata_row_to_container(
                self.scrollArea_speakercontents,
                speaker_id,
                speaker_name,
                speaker_data[1],
            )
            speaker_id += 1

    def add_all_files(self, model_files: List[File]):
        """
        Adds all files to the scroll area that displays the files. Clears the scroll area before adding the new files.
        """
        self.clear_scroll_area_files()
        file_id = 0
        for file in model_files:
            file_name = file.get_file_name()
            file_text = file.get_file_content()
            self.add_file_text_edit(file_name, file_text, file_id)
            file_id += 1

    def clear_all_contents(self):
        """
        Clears all scroll areas that display content (DV variants, Speakers, etc.). This function is called whenever there are changes to the content
        or to the underlyign data that require a complete refresh of the content.
        """
        self.clear_scroll_area_dvs()
        self.clear_scroll_area_speakers()
        self.clear_scroll_area_files()

    def clear_scroll_area_dvs(self):
        """
        Clears all items from the scroll area layout that displays the DV variants.
        """
        # Remove all items from the scroll area layout
        layout = self.scrollArea_dvcontents.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget safely
        # clear the dv checkbox mapping
        self.dv_checkbox_mapping.clear()

    def clear_scroll_area_speakers(self):
        """
        Clears all items from the scroll area layout that displays the speakers.
        """
        # Remove all items from the scroll area layout
        layout = self.scrollArea_speakercontents.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget safely
        # clear the speaker checkbox mapping
        self.speaker_checkbox_mapping.clear()

    def clear_scroll_area_files(self):
        """
        Clears all items from the scroll area layout that displays the files.
        """
        # Remove all items from the scroll area layout
        layout = self.scrollAreaWidgetContents_contentdisplay.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        # Clear the file name to text edit mapping
        self.file_name_text_edit_mapping.clear()

    def highlight_dvs(
        self,
        toggle,
        dv_values: Dict[str, Tuple[int, str, str]] = None,
        detected_annotations=None,
    ):
        """
        This function is called, when the user wants to highlight the detected DVs in the text. Calls the function that executes the highlighting
        for all files/text-edits.
        """
        # for each textedit
        for file in self.file_name_text_edit_mapping.keys():
            text_edit = self.get_text_edit_by_file_name(file)
            self.highlight_dvs_in_text_edit(
                toggle, file, text_edit, dv_values, detected_annotations
            )

    def underline_speakers(
        self,
        toggle,
        speakers: Dict[str, Tuple[Dict[str, str], str]] = None,
        detected_speakers=None,
    ):
        """
        This function is called, when the user wants to underline the speakers in the text. Calls the function that executes the underlining
        for all files/text-edits.
        """
        for file in self.file_name_text_edit_mapping.keys():
            text_edit = self.get_text_edit_by_file_name(file)
            self.underline_speakers_in_text_edit(
                toggle, file, text_edit, speakers, detected_speakers
            )

    def highlight_dvs_in_text_edit(
        self,
        toggle,
        file_name,
        file_textEdit: QPlainTextEdit,
        dv_values: Dict[str, Tuple[int, str, str]] = None,
        detected_annotations=None,
    ):
        """
        Highlight the correct words with the correct colors for all text-edits.

        Args:
            toggle (bool): A boolean value indicating whether to enable or disable the highlighting.
            file_textEdit (QPlainTextEdit): The text edit widget to apply the highlighting to.
        """
        # get the annotations for the file

        if detected_annotations is not None:
            detected_annotations_for_file = detected_annotations[
                detected_annotations["file_name"] == file_name
            ]
        else:
            return

        cursor = file_textEdit.textCursor()
        format = QTextCharFormat()
        default_color = QColor("yellow") if toggle else QColor("white")
        format.setBackground(
            default_color
        )  # "default color"/gets changed for each interrow entry

        for index, row in detected_annotations_for_file.iterrows():
            start = row["annotation_start"]
            end = row["annotation_end"]

            identifiers = row["identifier"]
            first_identifier = identifiers[0]
            color = dv_values[first_identifier][2]
            if color is None:  # default color if user didnt choose a color
                color = "yellow"

            format.setBackground(QColor(color)) if toggle else format.setBackground(
                QColor("white")
            )

            cursor.clearSelection()
            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
            cursor.mergeCharFormat(format)

    def underline_speakers_in_text_edit(
        self,
        toggle,
        file_name,
        file_textEdit: QPlainTextEdit,
        speakers: Dict[str, Tuple[Dict[str, str], str]] = None,
        detected_speakers=None,
    ):
        """
        Underlining the speakers with the correct colors for all text-edits.

        Args:
            toggle (bool): A boolean value indicating whether to enable or disable the underlining.
            file_textEdit (QPlainTextEdit): The text edit widget to apply the underlining to.
        """
        # get the speakers for the file
        if detected_speakers is not None:
            detected_speakers_for_file = detected_speakers[
                detected_speakers["file_name"] == file_name
            ]
        else:
            return

        cursor = file_textEdit.textCursor()
        format = QTextCharFormat()
        cursor.setPosition(0)

        for index, row in detected_speakers_for_file.iterrows():
            start = row["speaker_start"]
            end = row["spoken_text_end"]
            speaker_name = row["speaker_name"]
            color = speakers[speaker_name][1]
            if color is None:  # default color if user didnt choose a color
                color = "blue"

            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
            if toggle:
                format.setFontUnderline(True)
                format.setUnderlineColor(QColor(color))
                format.setUnderlineStyle(QTextCharFormat.UnderlineStyle.SingleUnderline)
            else:
                format.setFontUnderline(False)
            cursor.mergeCharFormat(format)

    def get_text_edit_by_file_name(self, file_name: str) -> QPlainTextEdit:
        """
        Get the text edit widget by the file name.

        Args:
            file_name (str): The name of the file.

        Returns:
            QPlainTextEdit: The text edit widget that corresponds to the file name.
        """
        if file_name in self.file_name_text_edit_mapping.keys():
            return self.file_name_text_edit_mapping[file_name]
        else:
            return None

    def get_list_of_selected_dvs(self) -> List[str]:
        """
        Get the list of selected DVs.

        Returns:
            List[str]: The list of selected DVs.
        """
        selected_dvs = []
        for dv_name, checkbox in self.dv_checkbox_mapping.items():
            if checkbox.isChecked():
                selected_dvs.append(dv_name)
        return selected_dvs

    def get_list_of_selected_speakers(self) -> List[str]:
        """
        Get the list of selected speakers.

        Returns:
            List[str]: The list of selected speakers.
        """
        selected_speakers = []
        for speaker_name, checkbox in self.speaker_checkbox_mapping.items():
            if checkbox.isChecked():
                selected_speakers.append(speaker_name)
        return selected_speakers

    def add_file_text_edit(self, file_name: str, file_text: str, row: int):
        """
        Add a new text edit widget to the view that represents a file.

        Args:
            file_name (str): The name of the file.
            file_text (str): The text content of the file.
            row (int): The row index where the file text edit should be added.

        """
        text_container = self.scrollAreaWidgetContents_contentdisplay

        new_text_edit = QPlainTextEdit()
        new_text_edit.setPlainText(file_text)
        new_text_edit.setStyleSheet(
            "QPlainTextEdit {font-size: 16px; min-height: 200px; max-height: 200px}"
        )
        new_text_edit.setReadOnly(True)
        new_text_edit.setBackgroundVisible(False)
        new_text_edit.setCenterOnScroll(False)

        # add the text edit to the mapping so it can be accessed later
        self.file_name_text_edit_mapping[file_name] = new_text_edit
        new_text_edit.setObjectName(file_name)

        file_label = QLabel("")
        set_abbreviate_label(file_label, file_name, 15, True)
        file_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        layout = text_container.layout()
        layout.addWidget(file_label, row, 0)
        layout.addWidget(new_text_edit, row, 2)

    def add_dv_container(
        self, dv_name: str, variants_names, variants_colors, dv_id: int
    ):
        """
        Add a container for a dependent variable to the view. This container includes the dependent variable name and the information about its variants.
        It calls another function to add all these variants to the container, which includes the variant name, color, and a checkbox.

        Args:
            dv_name (str): The name of the data variant.
            variants_names: The names of the variants.
            variants_colors: The colors of the variants.
            dv_id (int): The ID of the data variant.

        Returns:
            None
        """
        # Create the inner scroll-area
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QGridLayout()
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_widget.setLayout(scroll_layout)
        scroll_widget.setGeometry(QRect(0, 0, 262, 180))
        # scroll_widget.setMinimumWidth(262)
        # Rows will have same ordering as the variants in the data structure
        for variant_id in range(len(variants_names)):
            self.add_single_metadata_row_to_container(
                scroll_widget,
                variant_id,
                variants_names[variant_id],
                variants_colors[variant_id],
                False,
            )
        scroll_area.setWidget(scroll_widget)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Create the outer items (expand-button, label and check-all-box)
        data_name_label = QLabel("")
        set_abbreviate_label(data_name_label, dv_name, 30, True)
        data_name_label.setStyleSheet("font-weight: bold; font-size: 11pt;")

        # Add checkbox and connect toggle to (de-)selecting all inner checkboxes
        checkbox = QCheckBox()
        set_checkbox_stylesheet(checkbox)
        checkbox.setChecked(True)
        checkbox.toggled.connect(lambda: self.check_all(scroll_widget, checkbox))

        expand_button = QPushButton("▼")
        set_expand_button_stylesheet(expand_button=expand_button, init_expanded=True)
        expand_button.toggled.connect(
            lambda: expand_button_clicked(scroll_area, expand_button)
        )

        # Add items/widgets to main dv-container
        container_layout = self.scrollArea_dvcontents.layout()
        # Add the outer items to the main dv-layout
        container_layout.addWidget(expand_button, dv_id * 2, 0)
        container_layout.addWidget(data_name_label, dv_id * 2, 1)
        container_layout.addWidget(checkbox, dv_id * 2, 2)

        # Add the scroll area to the main dv-layout
        container_layout.addWidget(scroll_area, dv_id * 2 + 1, 0, 1, 3)

    def add_single_metadata_row_to_container(
        self,
        scroll_area_container: QWidget,
        row: int,
        metadata_name: str,
        color_code: str,
        for_speaker: bool = True,
    ):
        """
        Adds a single metadata row (dependent variable variant or speaker) to the given scroll area container.

        Args:
            scroll_area_container (QWidget): The container widget where the metadata row will be added.
            row (int): The row index where the metadata row will be inserted.
            metadata_name (str): The name of the metadata.
            color_code (str): The color code for the metadata color box.

        Returns:
            None
        """
        # Create the labels and checkbox
        data_name_label = QLabel("")
        set_abbreviate_label(data_name_label, metadata_name, 27, True)

        colorbox_label = QLabel("")
        if color_code is None:
            color_code = "#FFFFFF"
        colorbox_label.setStyleSheet(
            "QLabel { background-color:"
            + color_code
            + "; border: 3px solid black; max-height: 20px; max-width: 20px; min-height: 20px; min-width: 20px; }"
        )
        colorbox_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        checkbox = QCheckBox()
        checkbox.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )  # Set size policy to fixed
        checkbox.setMaximumWidth(32)  # Set maximum width to 32
        checkbox.setChecked(True)

        # map the metadata name to the checkbox so it can be accessed later
        if for_speaker:
            self.speaker_checkbox_mapping[metadata_name] = checkbox
        else:
            self.dv_checkbox_mapping[metadata_name] = checkbox

        set_checkbox_stylesheet(checkbox)

        # Create a grid layout
        layout = scroll_area_container.layout()

        # Add widgets to the layout
        layout.addWidget(data_name_label, row, 0)
        layout.addWidget(colorbox_label, row, 1)
        layout.addWidget(checkbox, row, 2)

        layout.setAlignment(colorbox_label, Qt.AlignmentFlag.AlignRight)
        layout.setAlignment(checkbox, Qt.AlignmentFlag.AlignRight)

        # Set the layout to the widget
        scroll_area_container.setLayout(layout)

    def check_all(self, target_widget: QWidget, checkbox_checkall: QCheckBox):
        """
        Iterates over all elements in a widget and (un-)checks all checkboxes
        that are direct children of the widget (so not contained as part of
        an inner widget), based on the selection of a "select-all" checkbox.
        """
        for checkbox in target_widget.findChildren(QWidget):
            if isinstance(checkbox, QCheckBox) and checkbox.parent() == target_widget:
                # if selectall is now false, then also deselect all inner checkboxes
                checkbox.setChecked(checkbox_checkall.isChecked())

    def toggle_file_indicator(self, toggle):
        """
        Toggles if the file name is shown next to each text edit.
        """
        for label_widget in self.scrollAreaWidgetContents_contentdisplay.findChildren(
            QWidget
        ):
            if (
                isinstance(label_widget, QLabel)
                and label_widget.parent()
                == self.scrollAreaWidgetContents_contentdisplay
            ):
                label_widget.setVisible(toggle)
