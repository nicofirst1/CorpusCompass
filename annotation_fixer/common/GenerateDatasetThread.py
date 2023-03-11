import csv
import itertools
import os
import re
from collections import Counter
from copy import copy

import pandas as pd
from PySide6 import QtCore
from tqdm import tqdm

from .AppLogger import DataCreatorLogger
from .data_creator_utils import get_name, check_correct_annotations, find_repetitions, remove_features, get_ngram, \
    preprocess_corpus


def generate_dataset(inputs: list, logger: DataCreatorLogger, corpus_dict: dict, speakers: dict, independent_variables,
                     dependent_variables, separator:str):
    # extract input values
    square_regex, feat_regex, name_regex, previous_line, ngram_prev, ngram_next = inputs

    # compile regex
    square_regex = re.compile(square_regex)
    feat_regex = re.compile(feat_regex)
    name_regex = re.compile(name_regex)

    logger.info("Starting dataset generation")
    corpus_dict = {k: preprocess_corpus(v, k, name_regex, logger) for k, v in corpus_dict.items()}
    corpus = list(corpus_dict.values())
    corpus = list(itertools.chain(*corpus))

    # get speaker of interest
    speakers_of_interest = speakers.keys()
    # remove spaces
    speakers_of_interest = [x.strip() for x in speakers_of_interest]

    logger.info(f"The selected speakers of interest are: {', '.join(speakers_of_interest)}")

    # get interviewer/interviewees names
    all_speakers = [get_name(x, name_regex) for x in corpus]
    all_speakers = set(all_speakers)
    # filter out empty all_speakers
    all_speakers = [x for x in all_speakers if x != '']

    all_speakers_dict = {k: set([get_name(x, name_regex) for x in v]) for k, v in corpus_dict.items()}
    all_speakers_dict = {k: sorted(v) for k, v in all_speakers_dict.items() if len(v) > 0}

    # notify user about names
    logger.info(f"I found the following speakers names: {', '.join(all_speakers)}")

    # notify some of the speakers are not in the list of all speakers
    if len(speakers_of_interest) > 0:
        not_in_list = set(all_speakers) - set(speakers_of_interest)
        if len(not_in_list) > 0:
            logger.warning(
                f"Warning: the following speakers are not in the list of speakers of interest: {', '.join(not_in_list)}")

    # merge the two dictionaries into a new one and warn on duplicates
    # order the keys so that the dependent variables are first
    variable_dict = {**independent_variables, **dependent_variables}
    if len(variable_dict) != len(independent_variables) + len(dependent_variables):
        logger.warning("Warning: I have found duplicate variables. I will take the first one")
        # warning the duplicates
        logger.warning("Duplicates are:")
        for token, v in variable_dict.items():
            if token in independent_variables and token in dependent_variables:
                logger.warning(f"{token}: {v}")

    # get an inverse of the dependent variable
    idv = {}
    for token, v in variable_dict.items():
        if isinstance(v, list):
            for i in v:
                idv[i] = token
        else:
            idv[v] = token

    # Output file settings
    # Now it's time to create the output files.
    #
    # There are different outputs and here we specify their names.


    # get the name of the output path
    output_dir = "postprocessed"
    # create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # define the output file names
    dataset_path = os.path.join(output_dir, "dataset.csv")
    binary_dataset_path = os.path.join(output_dir, "binary_dataset.csv")
    annotation_info_path = os.path.join(output_dir, "annotation_info.csv")
    not_annotated_path = os.path.join(output_dir, "missed_annotations.csv")

    # compile regex to find features
    csv_header = sorted(dependent_variables.keys())

    # define the end of the csv
    csv_end = ["speaker", "interlocutor/s", "file", 'context', 'unk']
    if previous_line:
        csv_end.insert(0, 'previous line')
    csv_header = ["token"] + csv_header + csv_end
    csv_file = [csv_header]
    unk_categories = []

    print(f"The csv header looks like this")
    csv_header

    # Finding all the annotated words
    whole_corpus = "\n".join(corpus)

    annotations = []
    for pt, crp in corpus_dict.items():
        crp = "\n".join(crp)
        anns = feat_regex.finditer(crp)

        # check correctness of all annotations
        anns, _ = check_correct_annotations(anns, crp, pt, verbose=True)

        annotations.extend(anns)

    annotations = [x.split(".")[-1] for x in annotations]
    # remove square brackets
    annotations = [x.replace("[", "").replace("]", "") for x in annotations]

    # count the number of annotations
    annotation_counter = Counter(annotations)
    annotation_counter = {k: dict(annotated=v) for k, v in annotation_counter.items()}

    print(f"The total number of annotated words is {len(annotation_counter)}")

    # Now, we check the number of times the token appears annotated (following the REGEX rule) vs not, we do this for each annotated token.


    # check if there are any annotations not annotated

    for token, v in tqdm(annotation_counter.items(), desc="Checking annotations", file=logger.text_edit_stream):
        # check for annotation repetitions
        wild_rep, wild_rep_interest, ann_rep, _ = find_repetitions(whole_corpus, token, feat_regex, name_regex,
                                                                   speakers_of_interest)
        total_rep = wild_rep + ann_rep
        not_annotated = total_rep - v['annotated']
        annotation_counter[token]['not annotated'] = not_annotated
        annotation_counter[token]['not_annotated_interest'] = wild_rep_interest

    logger.info(
        f"The total repetitions of annotated words is {sum([x['annotated'] for x in annotation_counter.values()])}")
    logger.info(
        f"The total repetitions of not annotated words is {sum([x['not annotated'] for x in annotation_counter.values()])}")
    logger.info(
        f"The total repetitions of not annotated words from speaker of interest is {sum([x['not_annotated_interest'] for x in annotation_counter.values()])}")


    # While the previous cell, counts all the tokens in the whole corpus, we probably want to differentiate between speakers.
    # For this reason, here we need to specify where we want to look for the missed tokens.
    #
    # You have the following options:
    #
    # - Choose all the speakers found in your corpus with: `speakers=all_speakers`
    # - Choose only the speakers you are interested in (defined previously):
    # `speakers=speakers_of_interest`
    # - Choose other speakers you are interested in, by manually enumerating them: `speakers= ["name1","name2",...,"nameN"]`
    #
    # By default, we check for all the speakers


    # choose which speaker to check for annotations, you can uncomment one of the following lines:
    speakers = all_speakers

    # Now it's time to find those missing annotations


    not_annotated_log = {}

    for path, crp in tqdm(corpus_dict.items(), desc="Finding not annotated words"):

        # filter out the speakers of interest
        crp = [x for x in crp if get_name(x, name_regex) in speakers]

        # join the corpus
        crp = "\n".join(crp)
        not_annotated_log[path] = {}
        # for all the tokens
        for token, _ in annotation_counter.items():
            # find the annotations
            _, _, _, wna = find_repetitions(crp, token, feat_regex, name_regex, speakers_of_interest,
                                            check_annotated=False)
            if len(wna) > 0:
                if token not in not_annotated_log[path]:
                    not_annotated_log[path][token] = []
                not_annotated_log[path][token] += wna

    logger.info(f"\nThe total number of not annotated words is {len(not_annotated_log)}")

    # Finally, some pre-processing


    for sp in tqdm(speakers, desc="Finding speakers for not annotated words"):
        sp_corpus = [c for c in corpus if get_name(c, name_regex) == sp]
        sp_corpus = "\n".join(sp_corpus)
        for token, v in annotation_counter.items():
            # check for annotation repetitions
            wild_rep, wild_rep_interest, ann_rep, _ = find_repetitions(sp_corpus, token, feat_regex, name_regex,
                                                                       speakers_of_interest)

            if sp + ' not annotated' not in annotation_counter[token]:
                annotation_counter[token][sp + ' not annotated'] = 0
            if sp + ' annotated' not in annotation_counter[token]:
                annotation_counter[token][sp + ' annotated'] = 0

            annotation_counter[token][sp + ' not annotated'] = wild_rep
            annotation_counter[token][sp + ' annotated'] = ann_rep

    # augment annotation_counter with speakers and add total number
    for token in annotation_counter.keys():
        annotation_counter[token]['total'] = annotation_counter[token]['annotated'] + annotation_counter[token][
            'not annotated']
        for speaker in speakers_of_interest:
            annotation_counter[token][speaker + " annotated"] = 0
            annotation_counter[token][speaker + " not annotated"] = 0

    # Starting the main loop
    # This part starts the main loop. You don't need to change anything here, if you are interested check out the comments.


    # for every paragraph in the transcript
    logger.info(f"Starting the main loop")
    for file_path, corpus in tqdm(corpus_dict.items(), desc="Files"):
        file_speakers = all_speakers_dict[file_path]
        for idx in range(len(corpus)):
            c = corpus[idx]
            cur_speaker = get_name(c, name_regex)

            # get the paragraph without features
            if cur_speaker in speakers_of_interest:
                sp = corpus[idx - 1]
            else:
                continue

            clean_p, wrong_tags = remove_features(c, square_regex)

            # get the features
            tags = feat_regex.finditer(c)

            # for every tags with features in the paragraph
            for t in tags:
                # get index of result + tag
                index = t.start()
                org_t = t.group(0)
                t = t.group(1)

                # skip annotations that are not valid
                if t.split(".")[-1] not in annotation_counter.keys():
                    logger.waring(f"\nSkipping '{t}' because it is not valid")
                    continue

                # skip any tags that are wrongly formatted
                if any([t in wt for wt in wrong_tags]):
                    logger.waring(f"\nSkipping '{t}' because it is wrongly formatted")
                    continue

                # initialize empty row
                csv_line = ["" for _ in range(len(csv_header))]

                # get independent variable information
                for token, v in independent_variables.items():
                    if cur_speaker != token:
                        continue
                    for var in v:
                        category = idv[var]
                        cat_idx = csv_header.index(category)
                        csv_line[cat_idx] = var

                # get the features
                feats = t.rsplit(".", 1)
                text = feats[1]
                feats = feats[0]

                context = get_ngram(c, (ngram_prev, ngram_next), index, square_regex)

                # for every feature in the word
                for f in feats.split("."):
                    # if the category is not present in the dict, then add to unk
                    if f not in idv.keys():
                        unk_categories.append(f)
                        csv_line[-1] = csv_line[-1] + f + ","
                    else:
                        category = idv[f]
                        cat_idx = csv_header.index(category)
                        csv_line[cat_idx] = f

                # add initial infos and final unk to the line
                # ["speaker", "interlocutor/s", "file", 'context', 'unk']

                speakers = copy(file_speakers)
                speakers.remove(cur_speaker)

                csv_line[0] = text
                csv_line[-2] = context
                csv_line[-3] = file_path
                csv_line[-4] = speakers
                csv_line[-5] = cur_speaker
                if previous_line:
                    csv_line[-6] = sp

                csv_line[-1] = csv_line[-1].strip(",")
                csv_file.append(csv_line)

    # Saving the output
    # Finally, we need to save the output in the csv file for all our results


    # write the csv
    with open(dataset_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerows(csv_file)

    # generate the annotation info file
    header = ["token"] + list(list(annotation_counter.values())[0].keys())

    with open(annotation_info_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerow(header)

        for token, v in annotation_counter.items():
            writer.writerow([token] + list(v.values()))

    # save the not annotated log
    if len(not_annotated_log) > 0:
        header = ["file", "token"]

        # count the maximum length for all the values of the values of the dict
        max_lens = max([len(x) for sub in not_annotated_log.values() for x in sub.values()])
        header += [f"context {i}" for i in range(1, max_lens + 1)]

        with open(not_annotated_path, "w", newline="", encoding="utf16") as f:
            writer = csv.writer(f, delimiter=separator)
            writer.writerow(header)
            for path, vals in not_annotated_log.items():
                for token, context in vals.items():
                    writer.writerow([path, token] + context)

    # If you want to download it right away run this cell:


    # Binary Dataset
    # The original dataset likely had categorical variables with multiple possible values represented as text or numbers. In order to perform certain types of analysis or feed the data into a machine learning model, it's often helpful to convert these categorical variables into a numerical format. One way to do this is through one-hot encoding, where a new binary column is created for each possible value of a categorical variable. This new dataset will differ from the original in that it will have more columns, one for each possible value of the categorical variables. Additionally, each row will now contain only 0's and 1's. The benefit of having the dataset encoded in this format is that it allows for the data to be easily processed by many machine learning algorithms, since they often expect numerical data as input. Additionally, one-hot encoding can help improve the performance of certain types of models, such as decision trees, by allowing them to make splits on categorical variables without having to convert them to numerical values first.


    # create the binary dataset file
    # read the csv file to pandas dataframe
    df = pd.read_csv(dataset_path, sep=separator, encoding="utf16")

    to_drop = ["context", "token", "unk", "file"]

    tokens = df["token"]
    context = df['context']

    # drop first and last two columns
    df = df.drop(to_drop, axis=1)
    df_encoded = pd.get_dummies(df, columns=df.columns, prefix_sep=":")
    df_encoded["token"] = tokens
    df_encoded["context"] = context

    df_encoded.to_csv(binary_dataset_path, index=False)

    # Finally to download it run

    #


    # Unknown categories
    # Here, we show the unknown category, if any could be found.


    if len(unk_categories) > 0:
        unk_categories = set(unk_categories)
        unk_categories = sorted(unk_categories)
        logger.warning(
            f"I have found several categories not listed in your variable file.\n"
            f"Following in alphabetical order:")
        for idx, c in enumerate(unk_categories):
            logger.warning(f"{idx} - '{c}'")


class GenerateDatasetThread(QtCore.QThread):
    log = QtCore.Signal(str)

    def __init__(self, inputs, corpus_dict, independent_variables, dependent_variables, speakers,
                 logger, separator):
        super().__init__()

        self.corpus_dict = corpus_dict
        self.independent_variables = independent_variables
        self.dependent_variables = dependent_variables
        self.speakers = speakers
        self.inputs = inputs
        self.logger = logger
        self.separator = separator

    def run(self):
        try:
            # Call the generate_dataset() method here
            dataset = generate_dataset(self.inputs, self.logger, self.corpus_dict, self.speakers,
                                       self.independent_variables,
                                       self.dependent_variables, self.separator)
            # ...
        except Exception as e:
            self.log.emit(f"Error generating dataset: {e}")
        finally:
            self.finished.emit()
