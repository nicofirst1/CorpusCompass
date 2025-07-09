from PySide6.QtWidgets import QProxyStyle, QStyle
from PySide6.QtGui import QPalette, QColor


class CustomProxyStyle(QProxyStyle):
    """
    A custom proxy style to override specific drawing behavior, like the
    hover color of QComboBox items, which can be problematic on some OSes.
    """

    def drawControl(self, element, option, painter, widget=None):
        """
        Overrides the drawing of specific controls. We use this to fix the
        QComboBox item text color on hover.
        """
        # This handles the text color of items in the ComboBox's POPUP/DROPDOWN list
        if element == QStyle.CE_MenuItem:
            # Check if the item is being hovered over/selected
            if option.state & QStyle.State_Selected:
                # When hovering, the OS theme might set the text color to white.
                # We force it to be black to ensure it's always readable against
                # the highlight background.
                option.palette.setColor(QPalette.HighlightedText, QColor("gray"))

        # Call the base class's method to do the actual drawing with our modified option
        super().drawControl(element, option, painter, widget)
