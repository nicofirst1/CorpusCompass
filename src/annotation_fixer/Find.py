from PySide6 import QtCore, QtWidgets, QtGui


class FindDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Find")
        self.setWindowModality(QtCore.Qt.NonModal)

        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.returnPressed.connect(self.on_find_next)

        self.next_button = QtWidgets.QPushButton("Next", self)
        self.next_button.clicked.connect(self.on_find_next)

        self.prev_button = QtWidgets.QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.on_find_previous)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.next_button)
        layout.addWidget(self.prev_button)

        self.setLayout(layout)

    def on_find_next(self):
        # disable the main app's window
        self.parent().setDisabled(True)

        # get the main window's text area
        text_area = self.parent().text_area

        # get the text to search for
        text = self.line_edit.text()

        # search for the next occurrence of the text
        cursor = text_area.textCursor()
        match = cursor.document().find(text, cursor)

        if not match.isNull():
            cursor.setPosition(match.position())
            cursor.movePosition(
                QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor, len(text)
            )
            text_area.setTextCursor(cursor)
        else:
            # wrap around to the beginning of the document
            cursor.setPosition(0)
            match = cursor.document().find(text, cursor)

            if not match.isNull():
                cursor.setPosition(match.position())
                cursor.movePosition(
                    QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor, len(text)
                )
                text_area.setTextCursor(cursor)
        # re-enable the main app's window
        self.parent().setEnabled(True)

    def on_find_previous(self):
        # get the main window's text area
        text_area = self.parent().text_area

        # get the text to search for
        text = self.line_edit.text()

        # search for the previous occurrence of the text
        cursor = text_area.textCursor()
        match = cursor.document().find(
            text,
            cursor,
            QtGui.QTextDocument.FindBackward | QtGui.QTextDocument.FindCaseSensitively,
        )

        if not match.isNull():
            cursor.setPosition(match.position())
            cursor.movePosition(
                QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor, len(text)
            )
            text_area.setTextCursor(cursor)
        else:
            # wrap around to the end of the document
            cursor.setPosition(cursor.document().characterCount() - 1)
            match = cursor.document().find(
                text,
                cursor,
                QtGui.QTextDocument.FindBackward
                | QtGui.QTextDocument.FindCaseSensitively,
            )

            if not match.isNull():
                cursor.setPosition(match.position())
                cursor.movePosition(
                    QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor, len(text)
                )
                text_area.setTextCursor(cursor)
