from typing import TYPE_CHECKING
from PySide6.QtWidgets import (
    QWidget,
)

from corpuscompass.view.generated.ui_start_screen_tab import Ui_StartScreenTab

if TYPE_CHECKING:
    from corpuscompass.view.corpus_compass_view import CorpusCompassView
class StartScreenTab(QWidget, Ui_StartScreenTab):
    """
    Class for the start-screen tab. This is the first window the user sees and
    it contains the options to create or load a project
    """

    def __init__(self, parent: "CorpusCompassView") -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.view: "CorpusCompassView" = parent
