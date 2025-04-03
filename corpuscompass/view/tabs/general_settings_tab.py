

from corpuscompass.view.generated.ui_settings_tab import Ui_SettingsTab

from PySide6.QtWidgets import (

    QWidget,

)

class GeneralSettingsTab(QWidget, Ui_SettingsTab):
    """
    Class for the general-settings-tab. This window contains control-
    elements to change settings for the current project, use of the
    tool etc.
    """

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view = parent