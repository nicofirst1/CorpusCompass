from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QListWidgetItem,
)
from PySide6.QtCore import Qt


from corpuscompass.view.font_configs import FontConfig
from corpuscompass.view.generated.ui_add_symbol_dialog import Ui_AddSymbolsDialog


class AddSymbolDialog(QDialog, Ui_AddSymbolsDialog):
    """
    Class for the annotation-specification-dialog. Opens a further dialog window
    in which symbols for the annotation format builder can be added.
    """

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Add Symbols")

    # TODO: Check if symbol was already in current symbols before adding, Propagate Changes

    def add_symbol_to_list_old_symbols(self, symbol):
        """
        Adds a new symbol to the list widget in the dialog that contains all symbols for the annotation format builder.
        """
        new_item = QListWidgetItem(symbol)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listwidget_annotformat_oldsymbols.addItem(new_item)

    def add_symbol_to_list_new_symbols(self, symbol):
        """
        Adds a new symbol to the list widget in the dialog that contains all symbols for the annotation format builder.
        """
        new_item = QListWidgetItem(symbol)
        new_item.setFont(FontConfig.get_standardized_font(16, True))
        self.listwidget_annotformat_symbolcontainer.addItem(new_item)

    def on_add_symbol_clicked(self):
        """
        Is called when the "add symbol"-button is clicked in the
        dialog adding symbols in the annotation builder. Checks if
        1. there is no input 2. the input is not a character
        3. the input is not already in the model. If none of
        the above apply, then the character can be added
        to the list of symbols in the model and the view.
        """
        new_symbol = self.lineEdit_newsymbol.text()
        self.lineEdit_newsymbol.setText("")
        if new_symbol == "" or new_symbol == " ":
            self.label_symbolalreadyadded.setText("No symbol input!")
            self.label_symbolalreadyadded.show()
        elif new_symbol.isalpha() or new_symbol.isdigit():
            self.label_symbolalreadyadded.setText(
                "Alphabetic symbols and digits should not be used for marking annotations!"
            )
            self.label_symbolalreadyadded.show()
        elif (
            len(
                self.listwidget_annotformat_oldsymbols.findItems(
                    new_symbol, Qt.MatchFlag.MatchCaseSensitive
                )
            )
            > 0
            or len(
                self.listwidget_annotformat_symbolcontainer.findItems(
                    new_symbol, Qt.MatchFlag.MatchCaseSensitive
                )
            )
            > 0
        ):
            self.label_symbolalreadyadded.setText("Symbol already added!")
            self.label_symbolalreadyadded.show()
        else:
            self.add_symbol_to_list_new_symbols(new_symbol)
            self.label_symbolalreadyadded.hide()

    def add_all_symbols_to_list(self, current_symbol_list):
        """
        Adds all symbols from the current symbol list to the list widget in the dialog that contains all symbols for the annotation format builder.
        Called after initializing the dialog.
        """
        for symbol in current_symbol_list:
            self.add_symbol_to_list_old_symbols(symbol)
        self.listwidget_annotformat_oldsymbols.sortItems(
            order=Qt.SortOrder.DescendingOrder
        )
