import tkinter as tk

from annotation_fixer.utils import load_corpus, load_annotation_info

class App:
    def __init__(self, master, text, annotations):
        self.master = master
        self.text = text
        self.annotations = annotations
        self.current_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.text_widget = tk.Text(self.master, wrap='word', height=10, width=40)
        self.text_widget.pack(side='left')
        self.text_widget.insert('1.0', self.text[self.current_index])
        self.highlight_annotation(self.annotations[self.current_index])

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(side='right')

        self.next_button = tk.Button(self.buttons_frame, text='Next', command=self.next_annotation)
        self.next_button.pack()

        self.skip_button = tk.Button(self.buttons_frame, text='Skip', command=self.skip_annotation)
        self.skip_button.pack()

    def highlight_annotation(self, annotation):
        start_index = self.text_widget.search(annotation, '1.0', stopindex='end')
        end_index = f'{start_index}+{len(annotation)}c'
        self.text_widget.tag_add('highlight', start_index, end_index)
        self.text_widget.tag_config('highlight', background='yellow')

    def next_annotation(self):
        self.current_index += 1
        if self.current_index >= len(self.text):
            self.master.quit()
        else:
            self.text_widget.delete('1.0', 'end')
            self.text_widget.insert('1.0', self.text[self.current_index])
            self.highlight_annotation(self.annotations[self.current_index])

    def skip_annotation(self):
        self.current_index += 1
        if self.current_index >= len(self.text):
            self.master.quit()
        else:
            self.text_widget.delete('1.0', 'end')
            self.text_widget.insert('1.0', self.text[self.current_index])
            self.highlight_annotation(self.annotations[self.current_index])


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Corpus Annotation Fixer")
    corpus_button = tk.Button(root, text="Load Corpus Files", command=load_corpus)
    corpus_button.pack()

    annotation_info_button = tk.Button(root, text="Load Annotation Info", command=load_annotation_info)
    annotation_info_button.pack()

    app = App(root, text, annotations)




    root.mainloop()
