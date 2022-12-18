# TranscriptionTagger
Are you a linguist working with annotated corpora?

Did it take you 3 years to annotate and need to have it all nice and clean in a sharable format?

Well, despair no more, this is the tool for you!

TranscriptionTagger is a tool for converting between different formats of transcriptions. 
It is designed to be used with [ELAN](https://tla.mpi.nl/tools/tla-tools/elan/) and [Praat](https://www.fon.hum.uva.nl/praat/) annotation tools,
but can be used with any other tool that uses a similar format.


![example image](./includes/example.png)

## Error reporting and feature requests
If you find a bug or have a feature request, please open an issue on the [issue tracker](https://github.com/nicofirst1/TranscriptionTagger/issues/new/choose)


## Notebook
This tool is designed to be used with a Jupyter notebook.
If you are not familiar with colab, check this tutorial on [how to use colab](https://colab.research.google.com/notebooks/intro.ipynb).

We have different notebooks for different tasks:

- [Converting a transcription to a csv dataset](https://colab.research.google.com/github/nicofirst1/TranscriptionTagger/blob/main/dataset_creation.ipynb).
- An experimental [corpus analyzer](https://colab.research.google.com/github/nicofirst1/TranscriptionTagger/blob/main/corpus_analysis.ipynb) (may have some unresolved issues).



## Python code
If you don't like notebooks for some reason, you can also convert the notebook to a python file.
To do this, install nbconvert with `pip install nbconvert` and run `jupyter nbconvert --to python notebook.ipynb` in the directory of the notebook.

On the other hand, if you want to convert python code to a notebook, you need to install `p2j` with `pip install p2j` 
and run `p2j notebook.py` in the directory of the python file.

# TODO

List of todos:
- Bugs and errors:
  - [x] add default start of paragraph regex (without speaker at start)
  - [x] check for paragraph separators such as '\r' 
  - [ ] debug on more data
- Features and extensions:
  - [X] replace interviewer/interviewee with interested speakers (or something similar)
  - [ ] independent variables, connected to speakers
  - [X] add more infos during program execution