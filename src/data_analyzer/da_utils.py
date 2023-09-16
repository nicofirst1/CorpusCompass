import argparse
import json
import os
import sys
import traceback

import pandas as pd


def load_all():
    # define argparse
    parser = argparse.ArgumentParser(
        description="This script performs an analysis of the data in the csv file."
    )
    parser.add_argument("variable_dir", help="The path to the variable directory")
    parser.add_argument("postprocess_paths", help="The path to the file containing the post process paths")

    parser.add_argument("setting_file", help="The path to the setting file")
    parser.add_argument("custom_paths", help="The path to the paths file")

    args = parser.parse_args()

    # open the setting file
    with open(args.setting_file, "r") as f:
        setting = json.load(f)

    encoding = setting["encoding"]
    separator = setting["separator"]

    # open postprocess paths
    with open(args.postprocess_paths, "r") as f:
        postprocess_paths = json.load(f)

    # get the corpus stats
    with open(postprocess_paths['corpus_stats'], "r", encoding=encoding) as f:
        corpus_stats = json.load(f)

    # get the binary dataset
    binary_df = pd.read_csv(postprocess_paths['binary_dataset'], sep=separator, encoding=encoding)

    # replace \ufeff with nothing
    binary_df = binary_df.replace("\ufeff", "", regex=True)

    # convert all strings to int
    binary_df = binary_df.apply(pd.to_numeric, errors="ignore")

    # from the preloaded dir load the dependent variables

    dependent_variables = []
    independent_variables = []
    speaker = []

    for file in os.listdir(args.variable_dir):
        if file == "independent_variables.json":
            with open(f"{args.variable_dir}/{file}", "r") as f:
                independent_variables = json.load(f)
        elif file == "dependent_variables.json":
            with open(f"{args.variable_dir}/{file}", "r") as f:
                dependent_variables = json.load(f)
        elif file == "speakers.json":
            with open(f"{args.variable_dir}/{file}", "r") as f:
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

    # for every speaker and independnt variable , get the number of words
    speaker_words = corpus_stats["speaker_n_words"]
    normalization_num = {f"speaker:{k}": v for k, v in speaker_words.items()}

    # for every independent variable
    for iv_k, iv_list in independent_variables.items():

        # for every value of the independent variable
        for iv_v in iv_list:
            normalization_num[f"{iv_k}:{iv_v}"] = 0

            # for every speaker
            for sp_k, sp_v in speaker.items():

                # if the value of the independent variable is in the speaker
                if iv_v in sp_v and sp_k in speaker_words.keys():
                    # add the number of words of the speaker to the normalization number
                    normalization_num[f"{iv_k}:{iv_v}"] += speaker_words[sp_k]


    #divide all for the multiplier
    normalization_num={k:v/setting['pair_wise_frequency_normalizer_multiplier'] for k,v in normalization_num.items()}

    return setting, custom_paths, variables, data, normalization_num


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
def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(repr(e), file=sys.stderr)
            # print the traceback
            traceback.print_exc(file=sys.stderr)

    return wrapper
