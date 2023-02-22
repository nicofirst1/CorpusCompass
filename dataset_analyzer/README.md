# Binary Data Analysis Script

This script analyzes a binary dataset that is provided as a CSV file. The analysis includes several functions, which can be run with command-line arguments.
##  Installation and Requirements

The script requires the following libraries to be installed: argparse, csv, matplotlib, numpy, pandas, statsmodels, sklearn, tqdm.

To install the required libraries, use the following command:
```bash
pip install .[dataset_analyzer]
```

## Usage

To run the script, provide a path to the binary dataset CSV file as a required argument. The script also accepts optional command-line arguments for specifying the independent variables and speakers to use in the analysis.

Example command to run the script:

```bash
python binary_data_analysis.py data/binary_dataset.csv -i "GENDER, AGE" -s "A, B, C"
```

The above command runs the script on the data/binary_dataset.csv file, using the independent variables "GENDER" and "AGE" and the speakers "A", "B", and "C".
## Functions

The script includes the following functions:

    kmeans_analysis: Performs a K-means analysis on the data, estimating the number of clusters if it is not provided as an argument. It saves the resulting clusters to files and also generates 2D and 3D plots of the clusters.

    dependent_variable_count: Analyzes the independent and dependent variables in the dataset and generates a CSV file that counts the number of times each independent variable occurs with each dependent variable.

    variable_analysis: Performs an analysis of the variables in the dataset, generating covariance matrices, correlation matrices, and lists of the highest and lowest covariance and correlation.

    poisson_regression: Performs a Poisson regression on the dataset for each dependent variable, using the specified independent variables and speakers. It saves the results of each regression to a CSV file.

The script prints some information about the dataset and the analysis that was performed after the analysis is completed.


## Output

After running the analysis script, the following output files will be generated in the analysis_results directory:
- variables directory containing the covariance and correlation matrices, as well as the top highest and lowest covariances and correlations. 
- dependent_variable_count.csv file containing the count of each dependent variable for each speaker. 
- poisson directory containing the results of Poisson regression for each dependent variable. 
- clusters directory containing the clusters created using K-Means algorithm, including the tokens that belong to each cluster, and 2D and 3D plots of the clusters.

Note that the script may generate additional files depending on the options selected.
