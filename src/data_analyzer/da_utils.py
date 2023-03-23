import argparse
import csv
import json
import os
import sys
from typing import List, Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm


def kmeans_analysis(
    df: pd.DataFrame,
    tokens: pd.Series,
    custom_path: str,
    num_clusters: int,
    max_clusters: int,
):
    """
    Perform a k-means analysis on the data
    :param df: the data
    :param custom_path: the path where to save the results
    :param num_clusters: the number of clusters to use. If -1, the number of clusters is estimated

    """

    # scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # estimate the number of clusters
    scores = []
    if num_clusters == -1:
        pbar = tqdm(
            range(2, max_clusters),
            desc="Estimating the number of clusters",
        )
        for i in pbar:
            kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
            kmeans.fit(scaled_data)
            scores.append(silhouette_score(scaled_data, kmeans.labels_))

        # plot the scores
        plt.plot(range(2, max_clusters), scores)
        plt.xlabel("Number of clusters")
        plt.ylabel("Silhouette score")
        plt.savefig(f"{custom_path}/cluster_scores.png")
        plt.clf()

        # get the best number of clusters
        best_n_clusters = np.argmax(scores) + 2
        print(
            f"Best number of clusters: {best_n_clusters}.\n"
            f" You should use this number for the clustering in future runs"
        )

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
    cluster_path = f"{custom_path}/clusters"

    # create the output directory if it does not exist
    if not os.path.exists(cluster_path):
        os.mkdir(cluster_path)

    for i in range(num_clusters):
        with open(f"{cluster_path}/cluster_{i}.txt", "w") as f:
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
        plt.scatter(
            pca_data[labels == i, 0], pca_data[labels == i, 1], label=f"Cluster {i}"
        )
    plt.legend()
    plt.savefig(f"{custom_path}/clusters_2d.png")
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
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(pca_data[:, 0], pca_data[:, 1], pca_data[:, 2], c=labels, cmap="viridis")
    plt.savefig(f"{custom_path}/clusters_3d.png")
    plt.clf()


def dependent_variable_count(
    df: pd.DataFrame,
    dependent_variables: List[str],
    speakers: List[str],
    custom_path: str,
) -> Dict[str, Dict[str, int]]:
    # make directory for the variables
    if not os.path.exists(custom_path):
        os.mkdir(custom_path)

    columns = []
    for c in df.columns:
        c1 = c.split("_")[1]
        if any([x in c for x in dependent_variables]) or c1 in speakers:
            columns.append(c)

    # get all the other columns in the df
    other_columns = sorted([c for c in df.columns if c not in columns])
    csv_lines = ["speaker/independent variable"] + other_columns
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


def variable_analysis(df, custom_path: str, dependent_variables: Dict[str,List]  ):
    """
    This function performs an analysis of the variables in the dataframe.
    It saves the covariance matrix, the correlation matrix, the highest and lowest covariance and correlation.

    :param df: the dataframe to analyze
    :param custom_path: the path where to save the results
    """
    # make directory for the variables
    if not os.path.exists(custom_path):
        os.mkdir(custom_path)

    cov = df.cov()


    # drop the rows that are not in the list
    rows = [r for r in cov.index if any([x in r for x in dependent_variables.keys()])]
    cols= [c for c in cov.columns if c not in rows]
    cov = cov.loc[rows,cols]


    # save the covariance matrix
    cov.to_csv(f"{custom_path}/covariance_matrix.csv")

    # get top 10 highest and lowest covariance not in diagonal
    cov = cov.where(np.triu(np.ones(cov.shape), k=1).astype(bool))
    cov = cov.stack()
    cov = cov.sort_values(ascending=False)
    cov.to_csv(f"{custom_path}/highest_covariance.csv")
    # get the lowest covariance
    cov = cov.sort_values(ascending=True)
    cov.to_csv(f"{custom_path}/lowest_covariance.csv")

    # do the same for correlation matrix
    corr = df.corr()
    corr = corr.loc[rows,cols]
    corr.to_csv(f"{custom_path}/correlation_matrix.csv")
    corr = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    corr = corr.stack()
    corr = corr.sort_values(ascending=False)
    corr.to_csv(f"{custom_path}/highest_correlation.csv")
    corr.sort_values(ascending=True)
    corr.to_csv(f"{custom_path}/lowest_correlation.csv")

    # do the same for the pearson correlation matrix
    pearson = df.corr(method="pearson")
    pearson = pearson.loc[rows,cols]
    pearson.to_csv(f"{custom_path}/pearson_correlation_matrix.csv")
    pearson = pearson.where(np.triu(np.ones(pearson.shape), k=1).astype(bool))
    pearson = pearson.stack()
    pearson = pearson.sort_values(ascending=False)
    pearson.to_csv(f"{custom_path}/highest_pearson_correlation.csv")
    pearson.sort_values(ascending=True)
    pearson.to_csv(f"{custom_path}/lowest_pearson_correlation.csv")

    # do the same for the spearman correlation matrix
    spearman = df.corr(method="spearman")
    spearman = spearman.loc[rows,cols]
    spearman.to_csv(f"{custom_path}/spearman_correlation_matrix.csv")
    spearman = spearman.where(np.triu(np.ones(spearman.shape), k=1).astype(bool))
    spearman = spearman.stack()
    spearman = spearman.sort_values(ascending=False)
    spearman.to_csv(f"{custom_path}/highest_spearman_correlation.csv")
    spearman.sort_values(ascending=True)
    spearman.to_csv(f"{custom_path}/lowest_spearman_correlation.csv")


def poisson_regression(
    df: pd.DataFrame, independent_vars: List[str], speakers: List[str], custom_path: str
):
    """
    This function performs a poisson regression on the dataframe.

    :param df: the dataframe to analyze
    :param independent_vars: the independent variables to use
    :param speakers: the speakers to use
    """

    # make directory for the variables
    if not os.path.exists(custom_path):
        os.mkdir(custom_path)

    independent_variables = []
    for c in df.columns:
        c1 = c.split(":")[1]
        if any([x in c for x in independent_vars]) or c1 in speakers:
            independent_variables.append(c)

    # get all the other columns in the df
    dependent_variables = sorted(
        [c for c in df.columns if c not in independent_variables]
    )

    fix_name = (
        lambda x: x.replace(" ", "_")
        .replace(":", "_")
        .replace("-", "_")
        .replace("/", "_")
    )

    # replace the spaces in the column names with underscores
    df.columns = [fix_name(c) for c in df.columns]
    # do the same for the independent variables and dependent variables
    independent_variables = [fix_name(c) for c in independent_variables]
    dependent_variables = [fix_name(c) for c in dependent_variables]

    for dv in dependent_variables:
        # get the poisson regression results
        try:
            poisson_results = smf.glm(
                formula=f"{dv} ~ {' + '.join(independent_variables)}",
                data=df,
                family=sm.families.Poisson(),
            ).fit()
            # save the results
            csv_file = poisson_results.summary().as_csv()

            with open(f"{custom_path}/poisson_regression_results_{dv}.csv", "w") as f:
                f.write(csv_file)
        except Exception as e:
            print(f"Error in poisson regression for {dv}: {e}", file=sys.stderr)


if __name__ == "__main__":
    # define argparse
    parser = argparse.ArgumentParser(
        description="This script performs an analysis of the data in the csv file."
    )
    parser.add_argument("preloaded_dir", help="The path to the preloaded dir")
    parser.add_argument(
        "binary_dataset_path", help="The path to the binary dataset pandas csv"
    )
    parser.add_argument("setting_file", help="The path to the setting file")
    parser.add_argument("custom_paths", help="The path to the paths file")

    args = parser.parse_args()

    # open the setting file
    with open(args.setting_file, "r") as f:
        setting = json.load(f)

    encoding = setting["encoding"]
    separator = setting["separator"]
    # get the binary dataset
    binary_df = pd.read_csv(args.binary_dataset_path, sep=separator, encoding=encoding)

    # from the preloaded dir load the dependent variables

    dependent_variables = []
    independent_variables = []
    speaker = []

    for file in os.listdir(args.preloaded_dir):
        if "independent_variables" in file:
            with open(f"{args.preloaded_dir}/{file}", "r") as f:
                independent_variables = json.load(f)
        elif "dependent_variables" in file:
            with open(f"{args.preloaded_dir}/{file}", "r") as f:
                dependent_variables = json.load(f)
        elif "speaker" in file:
            with open(f"{args.preloaded_dir}/{file}", "r") as f:
                speaker = json.load(f)

    # open the custom paths
    with open(args.custom_paths, "r") as f:
        custom_paths = json.load(f)

    # get the tokens and drop them from the dataframe
    tokens = binary_df["token"]
    context = binary_df["context"]
    binary_df = binary_df.drop(columns=["token", "context"])

    if setting["kmean_analysis"]:
        print("Starting cluster analysis...")
        os.makedirs(custom_paths["kmean"], exist_ok=True)
        kmeans_analysis(
            binary_df,
            tokens,
            custom_paths["kmean"],
            setting["kmean_n_clusters"],
            setting["kmean_max_clusters"],
        )
        print("Done!")

    # analyze the data
    if setting["variable_analysis"]:
        print("Analyzing the variables...")
        os.makedirs(custom_paths["variable_analysis"], exist_ok=True)
        variable_analysis(binary_df, custom_paths["variable_analysis"], dependent_variables)
        print("Done!")

    if setting["poisson_regression_analysis"]:
        print("Analyzing the variables with regression...")
        os.makedirs(custom_paths["poisson_regression"], exist_ok=True)
        poisson_regression(
            binary_df,
            independent_variables,
            speaker,
            custom_paths["poisson_regression"],
        )
        print("Done!")

    # analyze the dependent variables
    if setting["dependent_variable_analysis"]:
        print("Analyzing the dependent variables...")
        os.makedirs(custom_paths["dependent_variable_analysis"], exist_ok=True)
        dependent_variable_count(
            binary_df,
            dependent_variables,
            speaker,
            custom_paths["dependent_variable_analysis"],
        )
        print("Done!")
