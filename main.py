import sys

from PySide6 import QtWidgets

from src.common import Memory
from src.other_windows import Main


def main():
    mem = Memory()

    app = QtWidgets.QApplication(sys.argv)

    # set  the application params
    app.setApplicationVersion("1.0")
    app.setOrganizationName("University of Sapienza")
    app.setDesktopFileName("Corpus Compass")
    app.setApplicationDisplayName("Corpus Compass")

    main = Main(mem)
    main.show()
    app.exec()


if __name__ == "__main__":
    main()
