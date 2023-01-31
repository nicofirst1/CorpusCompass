import os
import re
from datetime import datetime
from typing import Dict

import pandas as pd

global warned_strict_rule


def find_annotation(corpus: Dict[str, str], token: str, annotation_regex: re.Pattern, use_strict_rule: bool = True) -> \
        Dict[str, str]:
    global warned_strict_rule

    if not warned_strict_rule and use_strict_rule:
        print(
            "Using strict rule, this works specifically for the annotation of the CorpusCompass example corpus.\n"
            "Consider using the non-strict rule if you are using a different corpus.")
        warned_strict_rule = True

    found = {}
    # for all the lines in the corpus find the annotation  with the regex
    for k, line in corpus.items():
        matches = annotation_regex.findall(line)
        matches = [m for m in matches if token in m]

        if use_strict_rule:
            matches = [m for m in matches if m.split(".")[-1].replace("]", "") == token]

        if len(matches) > 0:
            for m in matches:
                found[k] = m

    return found


def remove_annotation(corpus: Dict[str, str], token: str, annotation_regex: re.Pattern, use_strict_rule: bool = True):
    """
    Remove the annotation from the corpus
    :param corpus: the corpus
    :param token: the annotation to remove
    :param annotation_regex: the regex to use
    :return: the corpus without the annotation
    """
    found = find_annotation(corpus, token, annotation_regex, use_strict_rule)
    for k, v in found.items():
        corpus[k] = corpus[k].replace(v, token)
        print(f"Removed annotation {v} from file {k}")


def input_loop(low_reps: pd.DataFrame, annotation_r: re.Pattern, ann_info: pd.DataFrame, corpus: Dict[str, str]):
    """
    Loop over the rows of the dataframe and ask the user for the annotation
    :param low_reps: the dataframe with the low repetitions
    :param annotation_r: the regex to use
    :param ann_info: the dataframe with the annotation info
    :param corpus: the corpus
    :return: None
    """
    t = datetime.now()
    print("\n\n")
    index = 0
    # iterate over the rows and print the info
    for _, row in low_reps.iterrows():

        # print number of rows left and estimated time of completion
        print(
            f"\n{index} of {len(low_reps)} rows left ({index / len(low_reps) * 100:2f}%), estimated time of completion: {t + (datetime.now() - t) * (len(low_reps) - index)}")
        t = datetime.now()
        index += 1

        # get the token, the 'not annotated' columns
        token = row['token']
        annotated = row['annotated']
        not_annotated = row['not annotated']
        not_annotated_interest = row['not_annotated_interest']

        # find the name of the columns where the cell is greater than 0
        speaker = [col for col in low_reps.columns[5:] if row[col] > 0]
        speaker = set(speaker)

        found = find_annotation(corpus, token, annotation_r)

        # print the info in one line
        print(f"{token=} - {annotated=} - {not_annotated=} - {not_annotated_interest=} - {speaker=} - {found=}")

        # ask the user if they want to keep it
        keep = input("Do you want to keep it? (y/n): ")

        # if they want to keep it, add it to the annotation info
        if keep == "y":
            ann_info = ann_info.append(row, ignore_index=True)

        # if they don't want to keep it, remove it from the corpus
        else:
            remove_annotation(corpus, token, annotation_r)


if __name__ == '__main__':

    warned_strict_rule = False

    corpus_path = ["/Users/giulia/Desktop/cc_corpora/group1/Adnan.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Ali.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Aya.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Bashar.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Dunya.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Mohanad.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Myasar.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Somaya.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Suadad.txt",
                   "/Users/giulia/Desktop/cc_corpora/group1/Suham.txt"]

    # ask the user for the dir in which the corpus is
    corpus_dir = input("Insert the path to the directory containing the corpus: ")

    # check all the files in the dir that end with .txt
    if os.path.exists(corpus_dir):
        corpus_path = [os.path.join(corpus_dir, f) for f in os.listdir(corpus_dir) if f.endswith(".txt")]
        print("The path is correct, using the files in the directory: ", corpus_path)
    else:
        print("The path is not correct, using the default one: ", corpus_path)

    # make a dict with open rb files
    corpus_path_f = {os.path.basename(path): open(path, "rb").read() for path in corpus_path}
    corpus = {}
    for k, v in corpus_path_f.items():
        corpus[k] = v.decode("utf-16")

    # as the user to the path to the csv annotation info file
    annotation_path = input("Insert the path to the csv file with the annotation info: ")

    # if the path is not correct, use the default one
    if not os.path.exists(annotation_path):
        annotation_path = "/Users/giulia/Desktop/cc_corpora/group1/annotation_info.csv"
        print("The path is not correct, using the default one: ", annotation_path)

    # ask the user for the  annotation to regex
    annotation_r = input("Insert the annotation to regex, (use X for the token): ")

    # if the annotation is not correct, use the default one
    if annotation_r == "":
        annotation_r = r"(\[\$[\S ]*?\])"
        print("The annotation is not correct, using the default one: ", annotation_r)

    # compile the regex
    annotation_r = re.compile(annotation_r)

    # open the csv file with pandas, encode with utf-16
    ann_info = pd.read_csv(annotation_path, encoding="utf-16", on_bad_lines='skip', sep=";")

    # ask user what is the lowest value of the annotation repetition to consider
    min_repetition = input("Insert the minimum number of annotation repetition to consider: ")

    # if the value is not correct, use the default one
    if min_repetition == "":
        min_repetition = 1
        print("The value is not correct, using the default one: ", min_repetition)
    else:
        min_repetition = int(min_repetition)

    # get the rows where 'annotated' is less than the minimum repetition
    low_reps = ann_info[ann_info['annotated'] <= min_repetition]

    # drop the rows where 'annotated' is less than the minimum repetition
    ann_info = ann_info[ann_info['annotated'] > min_repetition]

    # if keybord interrupt, save the new annotation info and corpus
    try:
        input_loop(low_reps, annotation_r, ann_info, corpus)
    except KeyboardInterrupt:
        # ask if they want to save the new annotation info and corpus
        save = input("\nKeyboard interrupt,Do you want to save the new annotation info and corpus? (y/n): ")
        if save == "n":
            exit(0)

    # save the new annotation info
    # modify the path to save the new annotation info
    annotation_path_new = annotation_path.replace(".csv", "_new.csv")
    ann_info.to_csv(annotation_path_new, encoding="utf-16", sep=";", index=False)

    # save the new corpus
    # modify the path to save the new corpus
    corpus_path_new = [path.replace(".txt", "_new.txt") for path in corpus_path]

    for path, text in zip(corpus_path_new, corpus.values()):
        with open(path, "w", encoding="utf-16") as f:
            f.write(text)
