from tkinter import filedialog


def load_corpus():
    corpus_files = filedialog.askopenfilenames(
        title="Select Corpus Files", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    print("Selected Corpus Files:", corpus_files)

def load_annotation_info():
    annotation_info = filedialog.askopenfilename(
        title="Select Annotation Info CSV", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    print("Selected Annotation Info:", annotation_info)

