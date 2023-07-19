import os

from src.data_analyzer.da_analysis_functions import (
    kmeans_analysis,
    poisson_regression,
    pair_wise_frequency,
    proportions_analysis,
    cross_tabulation,
    chi_square_test,
    logistic_regression,
    point_biserial_correlation, t_test,
)
from src.data_analyzer.da_utils import load_all, to_df_names

if __name__ == "__main__":
    setting, custom_paths, variables, data, nomalization_num = load_all()

    dependent_variables, independent_variables, speakers = variables
    binary_df, tokens, context = data

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

    if setting["poisson_regression_analysis"]:
        # todo: check if correct
        print("Analyzing the variables with regression...")
        os.makedirs(custom_paths["poisson_regression"], exist_ok=True)
        poisson_regression(
            binary_df.copy(),
            independent_variables,
            speakers,
            custom_paths["poisson_regression"],
        )
        print("Done!")

        # transform dict of list to list of string
    independent_variables = to_df_names(binary_df, independent_variables)
    dependent_variables = to_df_names(binary_df, dependent_variables)
    speakers = [f"speaker:{s}" for s in speakers.keys()]
    speakers = [s for s in speakers if s in binary_df.columns]

    missing = [c for c in binary_df.columns if c not in independent_variables + dependent_variables + speakers]
    if len(missing) > 0:
        print(f"Missing columns: {missing}")

    # sort alphabetically
    independent_variables.sort()
    dependent_variables.sort()
    speakers.sort()

    if setting["t_test_analysis"]:
        print("Analyzing the variables with t-test...")
        os.makedirs(custom_paths["t_test"], exist_ok=True)
        t_test(binary_df, dependent_variables, independent_variables, custom_paths["t_test"])
        print("Done!")

    # analyze the dependent variables
    if setting["pair_wise_frequency_analysis"]:
        print("Analyzing the dependent variables...")
        os.makedirs(custom_paths["pair_wise_frequency_analysis"], exist_ok=True)
        pair_wise_frequency(
            binary_df,
            dependent_variables,
            independent_variables,
            speakers,
            custom_paths["pair_wise_frequency_analysis"],
            speakers_properties=variables[2],

        )
        print("Done!")

        print("Analyzing the dependent variables with normalized values...")
        os.makedirs(custom_paths["pair_wise_frequency_analysis"], exist_ok=True)
        pair_wise_frequency(
            binary_df,
            dependent_variables,
            independent_variables,
            speakers,

            custom_paths["pair_wise_frequency_analysis"],
            normalization_dict=nomalization_num,
            speakers_properties=variables[2],

        )
        print("Done!")

    if setting["proportions_analysis"]:
        print("Analyzing the proportions...")
        os.makedirs(custom_paths["proportions_analysis"], exist_ok=True)

        # Perform the analysis
        proportions_analysis(
            binary_df, dependent_variables, custom_paths["proportions_analysis"]
        )
        print("Done!")

    if setting["cross_tabulation_analysis"]:
        print("Analyzing the cross_tabulation...")
        os.makedirs(custom_paths["cross_tabulation_analysis"], exist_ok=True)

        cross_tabulation(
            binary_df,
            dependent_variables,
            independent_variables,
            custom_paths["cross_tabulation_analysis"],
        )

        print("Done!")

    if setting["chi_square_analysis"]:
        print("Analyzing the chi_square...")
        os.makedirs(custom_paths["chi_square_analysis"], exist_ok=True)

        chi_square_test(
            binary_df,
            dependent_variables,
            independent_variables,
            custom_paths["chi_square_analysis"],
        )
        print("Done!")

    if setting["logistic_regression_analysis"]:
        print("Analyzing the logistic_regression...")
        os.makedirs(custom_paths["logistic_regression_analysis"], exist_ok=True)

        logistic_regression(
            binary_df,
            dependent_variables,
            independent_variables,
            custom_paths["logistic_regression_analysis"],
        )
        print("Done!")

    if setting["point_biserial_analysis"]:
        print("Analyzing the point_biserial...")
        os.makedirs(custom_paths["point_biserial_analysis"], exist_ok=True)
        point_biserial_correlation(
            binary_df,
            dependent_variables,
            independent_variables,
            custom_paths["point_biserial_analysis"],
        )
        print("Done!")
