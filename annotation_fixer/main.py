import sys

from qtpy import QtWidgets

from annotation_fixer.common import Memory
from annotation_fixer.windows import AnnotationFixer, AskLoading, LoadFiles
from annotation_fixer.windows.Settings import AskSettings


def main():
    mem = Memory()

    app = QtWidgets.QApplication(sys.argv)

    # set  the application params
    app.setApplicationName("Annotation Fixer")
    app.setApplicationVersion("0.1")
    app.setOrganizationName("University of Sapienza")
    app.setDesktopFileName("Annotation Fixer")
    app.setApplicationDisplayName("Annotation Fixer")

    if mem.exist_preloaded():
        ask = AskLoading(mem)
        ask.show()
        app.exec_()
        load = ask.load
    else:
        load = False

    # if the user wants to load the files
    if not load:
        loader = LoadFiles(mem)
        loader.show()
        app.exec_()

        if not loader.has_finished:
            raise Exception("The user closed the window without loading the files")

        # save the loader values
        postprocess_data = dict(
            corpus_text=loader.corpus_text,
        )
        postprocess_data.update(loader.annotation_info_csv)
        postprocess_data.update(loader.variables_csv)
        mem.save_preloaded(postprocess_data)


    else:
        postprocess_data = mem.load_all_preloaded()

    # ask for settings
    window = AskSettings(mem)
    window.show()
    app.exec_()

    # open new window
    window2 = AnnotationFixer(mem, postprocess_data)
    window2.show()

    app.exec_()


if __name__ == "__main__":
    main()
