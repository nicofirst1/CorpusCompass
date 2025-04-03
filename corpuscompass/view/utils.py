


from PySide6.QtWidgets import (
    QPushButton,
    QSizePolicy,
    QWidget,
    
    QCheckBox,
    QLabel,
   
)


def split_string_with_token_and_identifier(input_string):
    substrings = ["token", "identifier"]
    result = []
    i = 0

    while i < len(input_string):
        # Check if the current position matches any of the special substrings
        matched = False
        for substring in substrings:
            if input_string[i : i + len(substring)] == substring:
                result.append(substring)
                i += len(substring)
                matched = True
                break
        if not matched:
            result.append(input_string[i])
            i += 1

    return result


def set_checkbox_stylesheet(checkbox: QCheckBox):
    """
    Is used as a standardized function to set the stylesheet of checkboxes in the application.
    """
    checkbox.setSizePolicy(
        QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
    )  # Set size policy to fixed
    checkbox.setMaximumWidth(32)  # Set maximum width to 32
    checkbox.setStyleSheet("""
                QCheckBox { 
                    width: 30px; 
                    height: 30px; 
                } 
                QCheckBox::indicator { 
                    width: 28px; 
                    height: 28px; 
                    margin: 2px; 
                } 
                QCheckBox::indicator:checked { 
                    image: url(:/images/images/checked_icon.png); 
                } 
                QCheckBox::indicator:unchecked { 
                    image: url(:/images/images/unchecked_icon.png); 
                } 
                QCheckBox::indicator:hover { 
                    background-color: lightgray; 
                } 
                QCheckBox::indicator:checked:hover { 
                    background-color: rgb(255, 166, 167); 
                } 
                QCheckBox::indicator:unchecked:hover { 
                    background-color: lightgreen; 
                }
            """)


def set_expand_button_stylesheet(expand_button: QPushButton, init_expanded: bool):
    """
    Is used as a standardized function to set the stylesheet of expand buttons in the application.
    """
    expand_button.setCheckable(True)
    if init_expanded:
        expand_button.setText("▼")
        expand_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid white;
                color: grey;
                font: 12pt;
                min-height: 25px;
                max-height: 25px;
                min-width: 25px;
                max-width: 25px;
                margin-bottom: 2px;
            }
            QPushButton:hover {
                color: black;
            }
            QPushButton:focus {
                border: 1px solid white;
            }
            QPushButton::menu-indicator {
                image: none;
            }
        """)
        expand_button.setChecked(True)
    else:
        expand_button.setText("▶")
        expand_button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border: 1px solid white;
                    color: grey;
                    font: 20pt "Segoe UI";
                    min-height: 25px;
                    max-height: 25px;
                    min-width: 25px;
                    max-width: 25px;
                    margin-bottom: 2px;
                }

                QPushButton:hover {
                    color: black; 
                }

                QPushButton:focus {
                    border: 1px solid white;
                }

                QPushButton::menu-indicator {
                    image: none;
                }
            """)
        expand_button.setChecked(False)


def expand_button_clicked(expand_target: QWidget, expand_button: QPushButton):
    """
    Handle the click event of the expand button.

    Parameters:
    - expand_target (QWidget): The widget to expand or collapse.
    - expand_button (QPushButton): The button that was clicked.
    """
    if expand_button.isChecked():
        expand_target.setHidden(False)
        expand_button.setText("▼")
        expand_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid white;
                color: grey;
                font: 12pt;
                min-height: 25px;
                max-height: 25px;
                min-width: 25px;
                max-width: 25px;
                margin-bottom: 2px;
            }
            QPushButton:hover {
                color: black;
            }
            QPushButton:focus {
                border: 1px solid white;
            }
            QPushButton::menu-indicator {
                image: none;
            }
        """)

    else:
        expand_target.setHidden(True)
        expand_button.setText("▶")
        expand_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid white;
                color: grey;
                font: 20pt;
                min-height: 25px;
                max-height: 25px;
                min-width: 25px;
                max-width: 25px;
                margin-bottom: 2px;
            }
            QPushButton:hover {
                color: black;
            }
            QPushButton:focus {
                border: 1px solid white;
            }
            QPushButton::menu-indicator {
                image: none;
            }
        """)


def set_abbreviate_label(
    label: QLabel, name: str, max_size: int, abbreviat_end: bool = True
):
    """
    Is used to abbreviate the text of a QLabel if it exceeds a certain length, in order to prevent the text from overflowing the label.
    Sets the text of the label and a tooltip that displays the full text when hovering over the label.

    Parameters:
    - label (QLabel): The label to set the text and tooltip for.
    - name (str): The text to set in the label.
    - max_size (int): The maximum number of characters to display in the label.
    - abbreviat_end (bool): If True, the text is abbreviated at the end, otherwise at the beginning.
    """
    if abbreviat_end:
        if len(name) > max_size:
            label.setText(name[: max_size - 3] + "...")
            label.setToolTip(name)
        else:
            label.setText(name)
    else:
        if len(name) > max_size:
            label.setText("..." + name[-max_size + 3 :])
            label.setToolTip(name)
        else:
            label.setText(name)
