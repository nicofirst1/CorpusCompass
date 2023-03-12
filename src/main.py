import sys

from PySide6 import QtWidgets

from annotation_fixer import AnnotationFixer
from common import Memory
from dataset_creator import DatasetCreator
from other_windows import AskLoading, LoadFiles


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
        app.exec()
        load = ask.load
    else:
        load = False

    # if the user wants to load the files
    if not load:
        loader = LoadFiles(mem)
        loader.show()
        app.exec()

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

    if "dataset" not in postprocess_data.keys():
        window1 = DatasetCreator(mem, postprocess_data)
        window1.show()
    else:
        # open new window
        window2 = AnnotationFixer(mem, postprocess_data)
        window2.show()

    app.exec()


if __name__ == "__main__":
    main()
