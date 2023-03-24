import argparse
import json
import os

import pandas as pd


def load_all():
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

    variables = dependent_variables, independent_variables, speaker
    data = binary_df, tokens, context

    return setting, custom_paths, variables, data


def to_df_names(df, variables, sep=":"):
    res = []
    for k, v in variables.items():
        if not isinstance(v, list):
            v = [v]

        for i in v:
            name = f"{k}{sep}{i}"
            if name in df.columns:
                res.append(name)

    return res


# decorator to catch exception and print them to stderr

