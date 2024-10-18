"""
Contains the Enum "Tab", which includes the names of all different tabs that exist in the view.
"""
from enum import Enum


class Tab(Enum):
    """
    Lists each existing tab in the view. IMPORTANT: The index of the tabs does 
    matter! The tabs inices should be ordered in the same way, like how they are added 
    in the class "CorpusCompassView" inside the __init__-method. (e.g. the start-tab
    is added first so it's index should be zero here, the home tab is added 
    second, so it gets the 1, etc.)
    """
    START_TAB = 0
    HOME_TAB = 1
    SPEAKER_TAB = 2
    ANNOTATIONFORMAT_TAB = 3
    LOAD_FILES_TAB = 4
    VARMANAGEMENT_TAB = 5
    ANALYSIS_SETTINGS_TAB = 6
    GENERAL_SETTINGS_TAB = 7
