import sys

from qtpy import QtWidgets

from annotation_fixer.common import Memory
from annotation_fixer.windows import AnnotationFixer, AskLoading, LoadFilesPopup


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
        loader = LoadFilesPopup(mem)
        loader.show()
        app.exec_()

        if not loader.has_finished:
            raise Exception("The user closed the window without loading the files")

        # save the loader values
        preloaded = dict(
            corpus_text=loader.corpus_text,
            annotation_info_csv=loader.annotation_info_csv,
            missing_annotations_csv=loader.missing_annotations_csv
        )
        mem.save_preloaded(preloaded)


    else:
        preloaded = mem.load_all_preloaded()

    corpus_text = preloaded["corpus_text"]
    annotation_info_csv = preloaded["annotation_info_csv"]
    missing_annotations_csv = preloaded["missing_annotations_csv"]

    # open new window
    window2 = AnnotationFixer(mem, corpus_text, annotation_info_csv, missing_annotations_csv)
    window2.show()

    app.exec_()


if __name__ == "__main__":
    main()
