import argparse
import csv
import os
from typing import List, Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm

analysis_path = "analysis"


def kmeans_analysis(df, kmeans_path=f"{analysis_path}/clusters", num_clusters=-1):
    """
    Perform a k-means analysis on the data
    :param df: the data
    :param kmeans_path: the path where to save the results
    :param num_clusters: the number of clusters to use. If -1, the number of clusters is estimated

    """
    # make directory for the clusters
    if not os.path.exists(kmeans_path):
        os.mkdir(kmeans_path)

    # scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # estimate the number of clusters
    scores = []
    if num_clusters == -1:
        max_clusters = 100
        print("Estimating the number of clusters...")
        for i in tqdm(range(2, max_clusters)):
            kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
            kmeans.fit(scaled_data)
            scores.append(silhouette_score(scaled_data, kmeans.labels_))

        # plot the scores
        plt.plot(range(2, max_clusters), scores)
        plt.xlabel("Number of clusters")
        plt.ylabel("Silhouette score")
        plt.savefig(f"{kmeans_path}/cluster_scores.png")
        plt.clf()

        # get the best number of clusters
        best_n_clusters = np.argmax(scores) + 2
        print(f"Best number of clusters: {best_n_clusters}")

        num_clusters = best_n_clusters

    # perform the clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(scaled_data)
    labels = kmeans.labels_

    # cluster the tokens
    clusters = {}
    for i in range(num_clusters):
        clusters[i] = []
    for i, token in enumerate(tokens):
        clusters[labels[i]].append(token)

    # remove duplicates from clusters
    for i in range(num_clusters):
        clusters[i] = list(set(clusters[i]))

    # save the clusters
    for i in range(num_clusters):
        with open(f"{kmeans_path}/cluster_{i}.txt", "w") as f:
            f.write("\n".join(clusters[i]))

    # plot the clusters in 2D using PCA add legend with color and cluster number
    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(scaled_data)

    # print pca information for the user
    print("PCA 2d information:")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Explained variance: {pca.explained_variance_}")
    print(f"Singular values: {pca.singular_values_}")

    for i in range(num_clusters):
        plt.scatter(pca_data[labels == i, 0], pca_data[labels == i, 1], label=f"Cluster {i}")
    plt.legend()
    plt.savefig(f"{kmeans_path}/clusters_2d.png")
    plt.clf()

    # plot the clusters in 3D using PCA add legend with color and cluster number
    pca = PCA(n_components=3)
    pca_data = pca.fit_transform(scaled_data)

    # print pca information for the user
    print("PCA 3d information:")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Explained variance: {pca.explained_variance_}")
    print(f"Singular values: {pca.singular_values_}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(pca_data[:, 0], pca_data[:, 1], pca_data[:, 2], c=labels, cmap='viridis')
    plt.savefig(f"{kmeans_path}/clusters_3d.png")
    plt.clf()


def dependent_variable_count(df: pd.DataFrame, dependent_variables: List[str], speakers: List[str],
                             custom_path: str = f"{analysis_path}/dependent_variables") -> Dict[str, Dict[str, int]]:
    # make directory for the variables
    if not os.path.exists(custom_path):
        os.mkdir(custom_path)

    columns = []
    for c in df.columns:
        c1 = c.split(":")[1]
        if any([x in c for x in dependent_variables]) or c1 in speakers:
            columns.append(c)

    # get all the other columns in the df
    other_columns = sorted([c for c in df.columns if c not in columns])
    csv_lines = ['speaker/independent variable'] + other_columns
    csv_lines = [csv_lines]

    for c in columns:

        csv_row = [c]

        # get a subset of the dataframe with only the dependent variable
        df_subset = df[df[c] == 1]

        for oc in other_columns:
            rep = int(df_subset[oc].sum())
            csv_row.append(rep)

        # add the repetition to the dictionary
        csv_lines.append(csv_row)

    # get the total number of repetitions for other columns
    total_repetitions = df[other_columns].sum().to_dict()
    csv_row = ["total"] + [total_repetitions[oc] for oc in other_columns]
    csv_lines.append(csv_row)

    # save the csv
    with open(f"{custom_path}/dependent_variable_count.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv_lines)


def variable_analysis(df, variable_path=f"{analysis_path}/variables"):
    """
    This function performs an analysis of the variables in the dataframe.
    It saves the covariance matrix, the correlation matrix, the highest and lowest covariance and correlation.

    :param df: the dataframe to analyze
    :param variable_path: the path where to save the results
    """
    # make directory for the variables
    if not os.path.exists(variable_path):
        os.mkdir(variable_path)

    cov = df.cov()

    # save the covariance matrix
    cov.to_csv(f"{variable_path}/covariance_matrix.csv")

    # get top 10 highest and lowest covariance not in diagonal
    cov = cov.where(np.triu(np.ones(cov.shape), k=1).astype(bool))
    cov = cov.stack()
    cov = cov.sort_values(ascending=False)
    cov.to_csv(f"{variable_path}/highest_covariance.csv")
    # get the lowest covariance
    cov = cov.sort_values(ascending=True)
    cov.to_csv(f"{variable_path}/lowest_covariance.csv")

    # do the same for correlation matrix
    corr = df.corr()
    corr.to_csv(f"{variable_path}/correlation_matrix.csv")
    corr = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    corr = corr.stack()
    corr = corr.sort_values(ascending=False)
    corr.to_csv(f"{variable_path}/highest_correlation.csv")
    corr.sort_values(ascending=True)
    corr.to_csv(f"{variable_path}/lowest_correlation.csv")

    # do the same for the pearson correlation matrix
    pearson = df.corr(method="pearson")
    pearson.to_csv(f"{variable_path}/pearson_correlation_matrix.csv")
    pearson = pearson.where(np.triu(np.ones(pearson.shape), k=1).astype(bool))
    pearson = pearson.stack()
    pearson = pearson.sort_values(ascending=False)
    pearson.to_csv(f"{variable_path}/highest_pearson_correlation.csv")
    pearson.sort_values(ascending=True)
    pearson.to_csv(f"{variable_path}/lowest_pearson_correlation.csv")

    # do the same for the spearman correlation matrix
    spearman = df.corr(method="spearman")
    spearman.to_csv(f"{variable_path}/spearman_correlation_matrix.csv")
    spearman = spearman.where(np.triu(np.ones(spearman.shape), k=1).astype(bool))
    spearman = spearman.stack()
    spearman = spearman.sort_values(ascending=False)
    spearman.to_csv(f"{variable_path}/highest_spearman_correlation.csv")
    spearman.sort_values(ascending=True)
    spearman.to_csv(f"{variable_path}/lowest_spearman_correlation.csv")


if __name__ == '__main__':

    # define argparse
    parser = argparse.ArgumentParser(description="This script performs an analysis of the data in the csv file.")
    parser.add_argument("file_path", help="The path to the binary_dataset.csv file to analyze.")
    # optional argument for the dependent annotation
    parser.add_argument("-i", "--independent_variables",
                        help="The independent variables to use for the analysis. "
                             "They should be provided as a list of strings, e.g. [GENDER,AGE].")

    parser.add_argument("-s", "--speaker",
                        help="The speaker to use for the analysis. "
                             "They should be provided as a list of strings, e.g. [A,B,C,D].")

    args = parser.parse_args()

    # read the file path given as argument

    # read the dependent annotation given as argument to a list
    if args.independent_variables:
        args.independent_variables = args.independent_variables.strip("[]").split(",")
        args.independent_variables = [x.strip() for x in args.independent_variables]
    else:
        args.independent_variables = []

    if args.speaker:
        args.speaker = args.speaker.strip("[]").split(",")
        args.speaker = [x.strip() for x in args.speaker]
    else:
        args.speaker = []

    independent_variables = args.independent_variables

    # open the csv file with pandas
    df = pd.read_csv(args.file_path)

    # print the first 5 rows
    print("First 5 rows of the csv file:")
    print(df.head())

    # get the tokens and drop them from the dataframe
    tokens = df['token']
    context = df['context']
    df = df.drop(columns=['token', 'context'])

    # make directory for the output files
    if not os.path.exists(analysis_path):
        os.mkdir(analysis_path)

    # analyze the dependent variables
    if independent_variables or args.speaker:
        print("Analyzing the dependent variables...")
        dependent_variable_count(df, independent_variables, args.speaker)
        print("Done!")

    # analyze the data
    print("Analyzing the variables...")
    variable_analysis(df)
    print("Done!")

    print("Starting cluster analysis...")
    kmeans_analysis(df, num_clusters=10)
    print("Done!")
