# CorpusCompass

CorpusCompass is a tool for researchers in the field of Corpus Linguistics that helps them efficiently extract and analyze data from annotated corpora. 
By defining variables and annotation rules using JSON files and specifying how to find them in the corpus using regular expressions (REGEX), 
researchers can tailor the tool to their specific research questions and needs. 
CorpusCompass also includes features for debugging missing annotations and identifying unexpected correlations in the data.

It is designed to be used with [ELAN](https://tla.mpi.nl/tools/tla-tools/elan/) and [Praat](https://www.fon.hum.uva.nl/praat/) annotation tools,
but can be used with any other tool that uses a similar format.


![example image](./includes/example.png)

### Error reporting and feature requests
If you find a bug or have a feature request, please open an issue on the [issue tracker](https://github.com/nicofirst1/CorpusCompass/issues/new/choose)

## Getting started

### Online Notebook
This tool is designed to be used with a Jupyter notebook in an online environment.
If you are not familiar with colab, check this tutorial on [how to use colab](https://colab.research.google.com/notebooks/intro.ipynb).

We have a [notebook for creating the dataset](https://colab.research.google.com/github/nicofirst1/CorpusCompass/blob/main/dataset_creation.ipynb), 
and a python file for [dataset analysis](./data_analysis.py) (check the local installation section for more info on how to use it).

### Using CorpusCompass

To use CorpusCompass, you will need to define your own variables and annotation rules using JSON files. 
Detailed instructions for customizing the tool to your specific needs are provided in the Jupyter notebook.

Once you have defined your variables and annotation rules, you can use CorpusCompass to extract and analyze data from your annotated corpus. 
The tool provides various functions for debugging missing annotations and identifying unexpected correlations in the data, 
which can be helpful for refining your research questions and hypotheses.


### Additional Resources

CorpusCompass can be used in conjunction with statistical analysis or visualization tools (such as Excel or R) to gain 
further insights into the factors that are affecting language use. More information on using these tools with CorpusCompass 
is provided in the Jupyter notebook.



## Local installation 

If you wish to install the tool locally, you can do so by cloning the repository and 
installing the requirements:
- Python (should be already installed on your system)
- Jupyter Notebook

You can install these dependencies by running the following command:

`pip install jupyter`

Next, clone the CorpusCompass repository and install the package:

```
git clone https://github.com/nicofirst1/CorpusCompass
pip install -e CorpusCompass/
```

Now that you have all the necessary dependencies installed, you can open the Jupyter notebook and start using CorpusCompass.

### Data analysis
We provide a python file for automatic data analysis. This analysis is based on the dataset we created previously (`binary_dataset.csv`).
The analysis provided are the following:
- Correlation between the variables
- Covariance between the variables
- Pearson's correlation coefficient
- Spearman's correlation coefficient
- K-means clustering of the data

#### Running the analysis
To run the analysis you need to specify the path to the dataset you want to analyze, with:
```
python data_analysis.py /path/to/binary_dataset.csv
```
A new folder will be created in the same directory as the dataset, with the name `analysis`, and the analysis will be saved there.

### Python code
If you don't like notebooks for some reason, you can also convert the notebook to a python file.
To do this, install nbconvert with `pip install nbconvert` and run `jupyter nbconvert --to python notebook.ipynb` in the directory of the notebook.

On the other hand, if you want to convert python code to a notebook, you need to install `p2j` with `pip install p2j` 
and run `p2j notebook.py` in the directory of the python file.
