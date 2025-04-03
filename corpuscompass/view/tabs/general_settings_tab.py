from typing import TYPE_CHECKING
from corpuscompass.view.generated.ui_settings_tab import Ui_SettingsTab


from corpuscompass.view.tabs.lazy_signal_tab import LazySignalTab
from corpuscompass.view.tabs.tab import Tab

if TYPE_CHECKING:
    from corpuscompass.view.corpus_compass_view import CorpusCompassView
    from corpuscompass.controllers import Controller


class GeneralSettingsTab(LazySignalTab, Ui_SettingsTab):
    """
    Class for the general-settings-tab. This window contains control-
    elements to change settings for the current project, use of the
    tool etc.
    """

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view: "CorpusCompassView" = parent

    def connect_signals(self, controller: "Controller"):
        self.btn_back.clicked.connect(
            lambda: controller.on_home_section_button_clicked(Tab.HOME_TAB)
        )
