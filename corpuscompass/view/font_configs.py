from PySide6.QtGui import (
    QFont,
    QColor,
)


# TODO: CONSTANT VALUE FUNCTIONS -> In own class
class FontColors:
    """
    A class that defines the font colors used in the application.
    """

    TOKEN = QColor(58, 60, 202)
    IDENTIFIER = QColor(185, 68, 185)


class FontConfig:
    """
    Class that returns the used fonts for the different text formats in the application.
    """

    @staticmethod
    def get_standardized_font(font_size: int, set_bold: bool) -> QFont:
        """
        Returns the font for token text format.
        """
        font = QFont()
        font.setBold(set_bold)
        font.setPointSize(font_size)
        font.setFamily("Segoe UI")
        return font

    # Alternative (but could be worse as font sizes could vary a lot in the application)
    # standardized_font = None

    # @classmethod
    # def get_standardized_font(cls, font_size: int, set_bold: bool) -> QFont:
    #     """
    #     Returns the font for token text format.
    #     """
    #     if cls.standardized_font is None:
    #         cls.standardized_font = QFont()
    #         cls.standardized_font.setFamily("Segoe UI")
    #     cls.standardized_font.setBold(set_bold)
    #     cls.standardized_font.setPointSize(font_size)
    #     return cls.standardized_font
