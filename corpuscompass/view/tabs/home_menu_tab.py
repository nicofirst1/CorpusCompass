
from corpuscompass.view.utils import   set_abbreviate_label
from corpuscompass.view.generated.ui_home_menu_tab import Ui_HomeMenuTab
from corpuscompass.view.tabs.tabs import Tab
from corpuscompass.view.tabs.lazy_signal_tab import LazySignalTab


class HomeMenuTab(LazySignalTab, Ui_HomeMenuTab):
    """
    Class for the home-menu tab. This window contains information about the
    current project and shows diffent options for the analysis of a corpus.
    """

    
    def connect_signals(self, controller: "Controller"):
        print("📍 HomeMenuTab now visible, connecting signals.")
        self.btn_home_managecorpus_sect.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.LOAD_FILES_TAB)
        )
        self.btn_home_speaker_sect.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.SPEAKER_TAB)
        )
        self.btn_home_annotformat_sect.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.ANNOTATIONFORMAT_TAB)
        )
        self.btn_home_varmanag_sect.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.VARMANAGEMENT_TAB)
        )
        self.btn_home_analysissettings_sect.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.ANALYSIS_SETTINGS_TAB)
        )
        self.btn_settings.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.GENERAL_SETTINGS_TAB)
        )
        self.btn_closeproject.clicked.connect(controller.on_project_closed_clicked)
        self.btn_projectinformation.clicked.connect(controller.on_projectinformation_clicked)
        self.btn_home_analysecorpus.clicked.connect(controller.on_analyse_corpus_button_clicked)

   

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent

        # Connect Signals from the main view to Slots
        self.view.proj_name_changed.connect(self.on_proj_name_changed)

    def on_proj_name_changed(self, proj_name: str) -> None:
        """
        Updates the displayed project name

        Args:
            proj_name (str): The project name, which should be displayed
        """
        # shorten name in view if it is too long, but add tooltip as compensation
        set_abbreviate_label(self.proj_name_label, "Project: <" + proj_name + ">", 30)

    def update_loaded_files(self, length: int) -> None:
        """
        Updates the displayed number of loaded files in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_loadedfiles_content.setText(str(length))
        if length == 0:
            self.label_warning_loaded_files.show()
            self.label_loadedfiles.setStyleSheet("color: black;")
        else:
            self.label_warning_loaded_files.hide()
            self.label_loadedfiles.setStyleSheet("color: green;")

    def update_speakers(self, length: int) -> None:
        """
        Updates the displayed number of detected speakers in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_uniquespeakers_content.setText(str(length))
        if length == 0:
            self.label_warning_speakers.show()
            self.label_uniquespeakers.setStyleSheet("color: black;")
        else:
            self.label_warning_speakers.hide()
            self.label_uniquespeakers.setStyleSheet("color: green;")

    def update_dvs(self, length: int) -> None:
        """
        Updates the displayed number of detected dependent variables in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_dvs_content.setText(str(length))
        if length == 0:
            self.label_warning_dvs.show()
            self.label_dvs.setStyleSheet("color: black;")
        else:
            self.label_warning_dvs.hide()
            self.label_dvs.setStyleSheet("color: green;")

    def update_dv_variants(self, length: int) -> None:
        """
        Updates the displayed number of detected dependent variable variants in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_dv_variants_content.setText(str(length))
        if length == 0:
            self.label_warning_dv_variants.show()
            self.label_dv_variants.setStyleSheet("color: black;")
        else:
            self.label_warning_dv_variants.hide()
            self.label_dv_variants.setStyleSheet("color: green;")

    def update_ivs(self, length: int) -> None:
        """
        Updates the displayed number of detected independent variables in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_ivs_contents.setText(str(length))
        if length == 0:
            self.label_warning_ivs.show()
            self.label_ivs.setStyleSheet("color: black;")
        else:
            self.label_warning_ivs.hide()
            self.label_ivs.setStyleSheet("color: green;")

    def update_iv_values(self, length: int) -> None:
        """
        Updates the displayed number of detected independent variable values in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_iv_values_content.setText(str(length))
        if length == 0:
            self.label_warning_iv_values.show()
            self.label_iv_values.setStyleSheet("color: black;")
        else:
            self.label_warning_iv_values.hide()
            self.label_iv_values.setStyleSheet("color: green;")

    def update_annotations(self, length: int) -> None:
        """
        Updates the displayed number of detected annotations in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_annotations_content.setText(str(length))
        if length == 0:
            self.label_warning_annotations.show()
            self.label_annotations.setStyleSheet("color: black;")
        else:
            self.label_warning_annotations.hide()
            self.label_annotations.setStyleSheet("color: green;")

    def update_annotation_formats(self, length: int) -> None:
        """
        Updates the displayed number of specified annotation formats in the home-menu tab. Also hides/shows the warning label if necessary.
        """
        self.label_annotationformat_contents.setText(str(length))
        if length == 0:
            self.label_warning_annotationformats.show()
            self.label_annotationformat.setStyleSheet("color: black;")
        else:
            self.label_warning_annotationformats.hide()
            self.label_annotationformat.setStyleSheet("color: green;")

