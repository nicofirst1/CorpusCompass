import csv
import os
import sys
from typing import List, Dict, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import chi2_contingency, pointbiserialr, ttest_ind
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm

from data_analyzer.da_utils import catch_exception


@catch_exception
def proportions_analysis(df, dependent_variables, custom_path):
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)

    results = {}
    for var in dependent_variables:
        results[var] = df[var].mean()

    # save results to csv
    df = pd.DataFrame(results, index=["proportion in dataset"]).T
    df.to_csv(f"{custom_path}/proportions.csv")

    return results


@catch_exception
def t_test(df, dependent_variables, independent_variables, custom_path):
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)
    results = {}
    csv_header = ["dependent_variable", "independent_variable", "t_statistic", "pvalue"]
    csv_lines = [csv_header]
    for dep_var in dependent_variables:
        for ind_var in independent_variables:
            t_statistic, pvalue = ttest_ind(
                df[dep_var],
                df[ind_var],
            )
            csv_lines.append([dep_var, ind_var, t_statistic, pvalue])

    # save results to csv
    with open(f"{custom_path}/t_test.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv_lines)

    return results


@catch_exception
def cross_tabulation(df, dependent_variables, independent_variables, custom_path=None):
    results = {}
    for dep_var in dependent_variables:
        for ind_var in independent_variables:
            # todo: add row,col names
            results[(dep_var, ind_var)] = pd.crosstab(
                df[dep_var],
                df[ind_var],
                margins=True,
                margins_name="Total",
                rownames=[dep_var],
                colnames=[ind_var],
            )

    # save results to csv
    if custom_path:
        for key, table in results.items():
            file_name = f"{key[1]}~~{key[0]}.csv"
            file_name = file_name.replace(" ", "_").replace("/", "_")
            file_name = os.path.join(custom_path, file_name)
            table.to_csv(file_name)

    return results


@catch_exception
def chi_square_test(df, dependent_variables, independent_variables, custom_path):
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)
    results = {}
    crosstab_results = cross_tabulation(
        df,
        dependent_variables,
        independent_variables,
    )
    for key, table in crosstab_results.items():
        chi2, p, _, _ = chi2_contingency(table)
        results[key] = (chi2, p)

    # save results to csv
    df = pd.DataFrame(results, index=["chi2", "p"]).T
    df.to_csv(f"{custom_path}/chi_square.csv")

    return results


@catch_exception
def logistic_regression(df, dependent_variables, independent_variables, custom_path):
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)
    results = {}
    for ind_var in independent_variables:
        try:
            X = sm.add_constant(df[dependent_variables])
            y = df[ind_var]
            model = sm.Logit(y, X).fit()
            results[ind_var] = model.summary()

        except KeyError as e:
            print(f"KeyError: {e}")

        except Exception as e:
            print(f"Exception: {e}")

    # save results to csv
    for key, table in results.items():
        csv = table.as_csv()
        file_name = f"{key}.csv"
        file_name = file_name.replace(" ", "_")
        file_name = os.path.join(custom_path, file_name)

        # make sure the directory exists
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        with open(file_name, "w") as f:
            f.write(csv)

    return results


@catch_exception
def point_biserial_correlation(
    df, dependent_variables, independent_variables, custom_path
):
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)

    results = {}
    for dep_var in dependent_variables:
        for ind_var in independent_variables:
            try:
                corr, p = pointbiserialr(df[dep_var], df[ind_var])
                results[(dep_var, ind_var)] = (corr, p)
            except KeyError as e:
                print(f"KeyError: {e}")
                results[(dep_var, ind_var)] = None

    # save results to csv
    df = pd.DataFrame(results, index=["corr", "p"]).T
    df.to_csv(f"{custom_path}/point_biserial_correlation.csv")

    return results


@catch_exception
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

        pbar.close()

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
        # remove non string elements
        clusters[i] = [x for x in clusters[i] if isinstance(x, str)]

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


@catch_exception
def pair_wise_frequency(
    df: pd.DataFrame,
    dependent_variables: List[str],
    independent_variables: List[str],
    speakers: List[str],
    custom_path: str,
    speakers_properties: Optional[Dict[str, List[str]]] = None,
    normalization_dict: Optional[Dict[str, int]] = None,
) -> Dict[str, Dict[str, int]]:
    # make directory for the variables
    if not os.path.exists(custom_path):
        os.mkdir(custom_path)

    other_columns = independent_variables + speakers

    # get all the other columns in the df
    csv_lines = ["speaker/independent variable"] + dependent_variables
    csv_lines = [csv_lines]

    for c in other_columns:
        csv_row = [c]

        # get a subset of the dataframe with only the dependent variable
        df_subset = df[df[c] == 1]

        for oc in dependent_variables:
            rep = int(df_subset[oc].sum())

            # normalize the count
            if normalization_dict is not None:
                rep = rep / normalization_dict[c]

            csv_row.append(rep)

        # add the repetition to the dictionary
        csv_lines.append(csv_row)

    # get the total number of repetitions for other columns
    total_repetitions = df[dependent_variables].sum().to_dict()
    csv_row = ["total"] + [total_repetitions[oc] for oc in dependent_variables]
    csv_lines.append(csv_row)

    file_name = f"{custom_path}/dependent_variable_count"
    if normalization_dict is not None:
        file_name += "_normalized"

    # load the csv lines into a dataframe with rows and columns names

    df = pd.DataFrame(csv_lines[1:], columns=csv_lines[0])

    # drop all rows that do not contain "speaker" in the first column
    df = df[df["speaker/independent variable"].str.contains("speaker")]

    indep_vars = [v for v in other_columns if "speaker" not in v]

    for prp in indep_vars:
        bool_l = []
        v = prp.split(":")[1]
        for sp in df["speaker/independent variable"]:
            sp = sp.split(":")[1]
            props = speakers_properties[sp]
            bool_l.append(v in props)

        # make a new column with the boolean values
        df[prp] = bool_l

    # save the dataframe as a csv
    df.to_csv(file_name + "_for_model.csv", index=False)

    file_name += ".csv"

    # save the csv
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv_lines)


@catch_exception
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
        cat_val = c.split(":")[1]
        if any([x in c for x in independent_vars]) or cat_val in speakers:
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
        .replace(",", "_")
        .replace(".", "_")
        .replace("+", "_")
    )

    # replace the spaces in the column names with underscores
    df.columns = [fix_name(c) for c in df.columns]
    # do the same for the independent variables and dependent variables
    independent_variables = [fix_name(c) for c in independent_variables]
    dependent_variables = [fix_name(c) for c in dependent_variables]

    for dv in independent_variables:
        # get the poisson regression results
        try:
            formula = f"{dv} ~ {' + '.join(dependent_variables)}"
            poisson_results = smf.glm(
                formula=formula,
                data=df,
                family=sm.families.Poisson(),
            ).fit()
            # save the results
            csv_file = poisson_results.summary().as_csv()

            with open(f"{custom_path}/{dv}.csv", "w") as f:
                f.write(csv_file)

            print(f"Finished poisson regression for {dv}")
        except Exception as e:
            print(f"Error in poisson regression for {dv}:\n {e}", file=sys.stderr)

            with open(f"{custom_path}/error_{dv}.csv", "w") as f:
                f.write(f"Error in poisson regression for {dv}:\n {e}")
