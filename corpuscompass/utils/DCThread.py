import itertools
import re
import threading
import traceback
from collections import Counter
from copy import copy
from typing import Dict, Tuple

import pandas as pd
from PySide6 import QtCore
from tqdm import tqdm

from corpuscompass.utils.QTextLogger import QTextLogger
from corpuscompass.utils.dc_utils import (
    preprocess_corpus,
    get_name,
    check_correct_annotations,
    find_repetitions,
    remove_features,
    get_ngram,
)


def generate_dataset(
    inputs: Tuple,
    logger: QTextLogger,
    corpus_dict: Dict,
    speakers_variables: Dict,
    independent_variables: Dict,
    dependent_variables: Dict,
    stop_flag: threading.Event,
):
    # extract input values
    feat_regex_dict, name_regex, previous_line, ngram_prev, ngram_next = inputs

    # compile regex
    name_regex = re.compile(name_regex)

    logger.info("Starting dataset generation")
    corpus_dict = {
        k: preprocess_corpus(v, k, name_regex, logger) for k, v in corpus_dict.items()
    }
    corpus = list(corpus_dict.values())
    corpus = list(itertools.chain(*corpus))

    if len(corpus) == 0:
        logger.error(
            "All the paragraphs in the corpus have been deleted! You should review your regex rules"
        )
        raise ValueError("The corpus is empty!")

    corpus_statitstics = {}

    # add statistics about corpus
    corpus_statitstics["paragraphs"] = len(corpus)

    # get speaker of interest
    speakers_of_interest = speakers_variables.keys()
    # remove spaces
    speakers_of_interest = [x.strip() for x in speakers_of_interest]

    logger.info(
        f"The selected speakers of interest are: {', '.join(speakers_of_interest)}"
    )

    corpus_statitstics["speakers_of_interest"] = len(speakers_of_interest)

    # get interviewer/interviewees names
    all_speakers = [get_name(x, name_regex) for x in corpus]
    all_speakers = set(all_speakers)
    # filter out empty all_speakers
    all_speakers = [x for x in all_speakers if x != ""]

    corpus_statitstics["all_speakers"] = len(all_speakers)

    all_speakers_dict = {
        k: set([get_name(x, name_regex) for x in v]) for k, v in corpus_dict.items()
    }
    all_speakers_dict = {
        k: sorted(v) for k, v in all_speakers_dict.items() if len(v) > 0
    }

    # notify user about names
    logger.info(f"I found the following speakers names: {', '.join(all_speakers)}")

    # notify some of the speakers are not in the list of all speakers
    if len(speakers_of_interest) > 0:
        not_in_list = set(all_speakers) - set(speakers_of_interest)
        if len(not_in_list) > 0:
            logger.warning(
                f"Warning: the following speakers are not in the list of speakers of interest: {', '.join(not_in_list)}"
            )

    # merge the two dictionaries into a new one and warn on duplicates
    # order the keys so that the dependent variables are first
    variable_dict = {**independent_variables, **dependent_variables}
    if len(variable_dict) != len(independent_variables) + len(dependent_variables):
        msg = (
            "Warning: I have found duplicate variables. I will take the first one\n"
            "Duplicates are:\n"
        )

        for token, v in variable_dict.items():
            if token in independent_variables and token in dependent_variables:
                msg += f"{token}: {v}\n"

        logger.warning(msg)

    # get an inverse of the dependent variable
    idv = {}
    for token, v in variable_dict.items():
        if isinstance(v, list):
            for i in v:
                idv[i] = token
        else:
            idv[v] = token

    del variable_dict

    # get statistics about the number of variables
    corpus_statitstics["dependent_variables"] = len(dependent_variables)
    corpus_statitstics["independent_variables"] = len(independent_variables)
    corpus_statitstics["variables"] = len(dependent_variables) + len(
        independent_variables
    )

    # get the number of values for each variable
    corpus_statitstics["variables_values"] = len(idv)
    corpus_statitstics["dependent_variable_values"] = sum(
        [len(x) for x in dependent_variables.values()]
    )
    corpus_statitstics["independent_variable_values"] = sum(
        [len(x) for x in independent_variables.values()]
    )

    # Output file settings
    # Now it's time to create the output files.
    #
    # There are different outputs and here we specify their names.

    # compile regex to find features
    csv_header = sorted(dependent_variables.keys()) + sorted(
        independent_variables.keys()
    )

    # define the end of the csv
    csv_end = ["speaker", "interlocutor/s", "file", "context", "unk"]
    if previous_line:
        csv_end.insert(0, "previous line")
    csv_header = ["token"] + csv_header + csv_end
    csv_file = [csv_header]

    if stop_flag.is_set():
        logger.info("Dataset generation stopped.")
        return None

    # Finding all the annotated words
    whole_corpus = "\n".join(corpus)
    wc_clean, _ = remove_features(whole_corpus, feat_regex_dict, logger)

    corpus_statitstics["words"] = len(wc_clean.split())
    corpus_statitstics["characters"] = len(wc_clean)

    annotations = []
    err_msg = ""

    for _, content in feat_regex_dict.items():
        feat_regex, _ = content
        for pt, crp in corpus_dict.items():
            crp = "\n".join(crp)
            anns = re.finditer(feat_regex, crp)
            # check correctness of all annotations
            anns, _, msg = check_correct_annotations(
                anns, crp, pt, verbose=True
            )  # TODO: Problem: Diese Methode ist speziell für die alte Version der Annotation zugeschnitten
            err_msg += msg + "\n\n"

            annotations.extend(anns)

    # check if err_msg is not just newlines
    err_msg = err_msg.strip()
    if err_msg:
        logger.error(err_msg)

    # count the number of annotations
    annotation_counter = Counter(annotations)
    annotation_counter = {k: dict(annotated=v) for k, v in annotation_counter.items()}

    logger.info(f"There is a total of  {len(annotation_counter)} unique annotations")
    corpus_statitstics["unique_annotations"] = len(annotation_counter)

    # Now, we check the number of times the token appears annotated (following the REGEX rule) vs not, we do this for each annotated token.

    # check if there are any annotations not annotated
    pbar = tqdm(
        annotation_counter.items(),
        desc="Checking annotations...",
        file=logger.text_edit_stream,
    )
    for token, v in pbar:
        # check for annotation repetitions
        wild_rep, wild_rep_interest, ann_rep, _ = find_repetitions(
            whole_corpus, token, feat_regex_dict, name_regex, speakers_of_interest
        )
        total_rep = wild_rep + ann_rep
        not_annotated = total_rep - v["annotated"]
        annotation_counter[token]["not annotated"] = not_annotated
        annotation_counter[token]["not_annotated_interest"] = wild_rep_interest
        if stop_flag.is_set():
            pbar.close()
            logger.info("Dataset generation stopped.")
            return None

    annotated = sum([x["annotated"] for x in annotation_counter.values()])
    not_annotated = sum([x["not annotated"] for x in annotation_counter.values()])
    not_annotated_interest = sum(
        [x["not_annotated_interest"] for x in annotation_counter.values()]
    )

    logger.info(
        f"There is a total of {annotated} annotations in the corpus ({annotated / len(whole_corpus.split(' ')) * 100:.2f}% "
        f"of the corpus).\n"
        f"I found {not_annotated} not annotated words that were previously annotated.\n"
        f"Of those {not_annotated_interest} ({not_annotated_interest / (not_annotated + 1e-10) * 100:.2f}%) "
        f"are produced by a speakers of interest"
    )

    corpus_statitstics["annotated_tokens"] = annotated

    # While the previous cell, counts all the tokens in the whole corpus, we probably want to differentiate between speakers.
    # For this reason, here we need to specify where we want to look for the missed tokens.
    # Now it's time to find those missing annotations

    not_annotated_log = {}
    pbar = tqdm(
        corpus_dict.items(),
        desc="Finding not annotated words",
        file=logger.text_edit_stream,
    )

    for path, crp in pbar:
        # filter out the speakers of interest
        crp = [x for x in crp if get_name(x, name_regex) in speakers_of_interest]

        # join the corpus
        crp = "\n".join(crp)
        not_annotated_log[path] = {}
        # for all the tokens
        for token, _ in annotation_counter.items():
            # find the annotations
            _, _, _, wna = find_repetitions(
                crp,
                token,
                feat_regex_dict,
                name_regex,
                speakers_of_interest,
                check_annotated=False,
            )
            if len(wna) > 0:
                if token not in not_annotated_log[path]:
                    not_annotated_log[path][token] = []
                not_annotated_log[path][token] += wna
            if stop_flag.is_set():
                pbar.close()
                logger.info("Dataset generation stopped.")
                return None

    # Finally, some pre-processing

    pbar = tqdm(
        speakers_variables,
        desc="Finding speakers for not annotated words",
        file=logger.text_edit_stream,
    )

    for sp in pbar:
        sp_corpus = [c for c in corpus if get_name(c, name_regex) == sp]
        sp_corpus = "\n".join(sp_corpus)
        for token, v in annotation_counter.items():
            # check for annotation repetitions
            wild_rep, wild_rep_interest, ann_rep, _ = find_repetitions(
                sp_corpus, token, feat_regex_dict, name_regex, speakers_of_interest
            )

            if sp + " not annotated" not in annotation_counter[token]:
                annotation_counter[token][sp + " not annotated"] = 0
            if sp + " annotated" not in annotation_counter[token]:
                annotation_counter[token][sp + " annotated"] = 0

            annotation_counter[token][sp + " not annotated"] = wild_rep
            annotation_counter[token][sp + " annotated"] = ann_rep

            if stop_flag.is_set():
                pbar.close()
                logger.info("Dataset generation stopped.")
                return None

    # augment annotation_counter with speakers and add total number
    for token in annotation_counter.keys():
        annotation_counter[token]["total"] = (
            annotation_counter[token]["annotated"]
            + annotation_counter[token]["not annotated"]
        )
        for speaker in speakers_of_interest:
            if speaker + " annotated" not in annotation_counter[token]:
                annotation_counter[token][speaker + " annotated"] = 0
                annotation_counter[token][speaker + " not annotated"] = 0

            if stop_flag.is_set():
                logger.info("Dataset generation stopped.")
                return None

    # Starting the main loop
    # This part starts the main loop. You don't need to change anything here, if you are interested check out the comments.

    unk_variables = {}
    used_dep_vars = {cat: {v1: 0 for v1 in v} for cat, v in dependent_variables.items()}
    speaker_n_words = {sp: 0 for sp in all_speakers}
    not_found_vars = []

    # for every paragraph in the transcript
    logger.info(f"Starting the main loop")
    pbar = tqdm(
        corpus_dict.items(), desc="Building dataset... ", file=logger.text_edit_stream
    )
    for file_path, corpus in pbar:
        file_speakers = all_speakers_dict[file_path]
        for idx in range(len(corpus)):
            if stop_flag.is_set():
                pbar.close()
                logger.info("Dataset generation stopped.")
                return None

            c = corpus[idx]
            cur_speaker = get_name(c, name_regex)
            clean_p, wrong_tags = remove_features(c, feat_regex_dict, logger)

            # get number of words for each speaker
            speaker_n_words[cur_speaker] += len(clean_p.split(" "))

            # get the paragraph without features
            if cur_speaker in speakers_of_interest:
                sp = corpus[idx - 1]
            else:
                continue

            for _, content in feat_regex_dict.items():
                feat_regex, multiple_identifier_seperator = content
                # get the features
                tags = re.finditer(feat_regex, c)

                # for every tags with features in the paragraph
                for t in tags:
                    # get index of result + tag
                    index = t.start()
                    org_t = t.group(0)
                    token = t.group("token")

                    # skip annotations that are not valid
                    if token not in annotation_counter.keys():
                        logger.warning(f"\nSkipping '{t}' because it is not valid")
                        continue

                    # skip any tags that are wrongly formatted
                    if any([token in wt for wt in wrong_tags]):
                        logger.warning(
                            f"\nSkipping '{token}' because it is wrongly formatted"
                        )
                        continue

                    # initialize empty row
                    csv_line = ["" for _ in range(len(csv_header))]

                    # get independent variable information
                    cur_speaker_var = speakers_variables.get(cur_speaker, [])
                    for var in cur_speaker_var:
                        try:
                            category = idv[var]
                            cat_idx = csv_header.index(category)
                            csv_line[cat_idx] = var
                        except KeyError:
                            not_found_vars.append(var)
                            continue

                    # get the features
                    feats = t.group("identifier").split(multiple_identifier_seperator)

                    context = get_ngram(
                        c, (ngram_prev, ngram_next), index, feat_regex_dict, logger
                    )

                    # for every feature in the word
                    for f in feats:
                        # if the category is not present in the dict, then add to unk
                        if f not in idv.keys():
                            if f not in unk_variables:
                                unk_variables[f] = []
                            unk_d = dict(
                                file=file_path,
                                speaker=cur_speaker,
                                context=context,
                                token=token,
                                tag=org_t,
                            )

                            unk_variables[f].append(unk_d)

                            csv_line[-1] = csv_line[-1] + f + ","
                        else:
                            category = idv[f]
                            cat_idx = csv_header.index(category)
                            csv_line[cat_idx] = f
                            used_dep_vars[category][f] += 1

                    # add initial infos and final unk to the line
                    # ["speaker", "interlocutor/s", "file", 'context', 'unk']

                    speakers = copy(file_speakers)
                    speakers.remove(cur_speaker)

                    csv_line[0] = token
                    csv_line[-2] = context
                    csv_line[-3] = file_path
                    csv_line[-4] = ",".join(speakers)
                    csv_line[-5] = cur_speaker
                    if previous_line:
                        csv_line[-6] = sp

                    csv_line[-1] = csv_line[-1].strip(",")
                    csv_file.append(csv_line)

    not_found_vars = list(set(not_found_vars))
    if len(not_found_vars) > 0:
        logger.warning(
            f"\n\nThe following variables were not found in the independent variables file: {not_found_vars}"
        )
    # Saving the output
    corpus_statitstics["speaker_n_words"] = speaker_n_words

    # Finally, we need to save the output in the csv file for all our results

    # generate the annotation info file
    header = ["token"] + list(list(annotation_counter.values())[0].keys())
    annotation_info = [header]
    for token, v in annotation_counter.items():
        annotation_info.append([token] + list(v.values()))

    # save the not annotated log
    if any([len(x) > 0 for x in not_annotated_log.values()]):
        header = ["file", "token"]

        # count the maximum length for all the values of the values of the dict
        max_lens = max(
            [len(x) for sub in not_annotated_log.values() for x in sub.values()]
        )
        header += [f"context {i}" for i in range(1, max_lens + 1)]

        missing_annotations = [header]

        for path, vals in not_annotated_log.items():
            for token, context in vals.items():
                missing_annotations.append([path, token] + context)
    else:
        missing_annotations = [["No missing annotations"]]

    # Binary Dataset
    # The original dataset likely had categorical variables with multiple possible values represented as text or numbers. In order to perform certain types of analysis or feed the data into a machine learning model, it's often helpful to convert these categorical variables into a numerical format. One way to do this is through one-hot encoding, where a new binary column is created for each possible value of a categorical variable. This new dataset will differ from the original in that it will have more columns, one for each possible value of the categorical variables. Additionally, each row will now contain only 0's and 1's. The benefit of having the dataset encoded in this format is that it allows for the data to be easily processed by many machine learning algorithms, since they often expect numerical data as input. Additionally, one-hot encoding can help improve the performance of certain types of models, such as decision trees, by allowing them to make splits on categorical variables without having to convert them to numerical values first.

    # create the binary dataset file
    # read the csv file to pandas dataframe
    df = pd.DataFrame(data=csv_file[1:], columns=csv_file[0])

    to_drop = ["context", "token", "unk", "file"]

    tokens = df["token"]
    context = df["context"]

    # drop first and last two columns
    df = df.drop(to_drop, axis=1)
    sep = ":"
    df_encoded = pd.get_dummies(df, columns=df.columns, prefix_sep=sep)

    if df_encoded.size != 0:
        # drop all columns that have nothing after : in name
        df_encoded = df_encoded.loc[:, ~df_encoded.columns.str.contains(f"{sep}$")]

        df_encoded["token"] = tokens
        df_encoded["context"] = context

    # todo: add check for values that are not used in the corpus but appear in the variable file
    # todo: add number of annotations per speaker

    # Unknown categories
    # Here, we show the unknown category, if any could be found.

    if len(unk_variables) > 0:
        header = ["variable", "file", "speaker", "context", "token", "tag"]

        body = []

        for var, vals in unk_variables.items():
            for val in vals:
                body.append(
                    [
                        var,
                        val["file"],
                        val["speaker"],
                        val["context"],
                        val["token"],
                        val["tag"],
                    ]
                )

        unk_df = pd.DataFrame(data=body, columns=header)

        # warn the user
        logger.warning(
            f"Unknown dependent variables found in the corpus. Please check the unknown_vars.csv file for more information."
        )
    else:
        unk_df = [["No unknown variables found"]]
        unk_df = pd.DataFrame(data=unk_df, columns=["No unknown variables found"])

    to_return = dict(
        dataset=pd.DataFrame(data=csv_file[1:], columns=csv_file[0]),
        annotation_info=pd.DataFrame(
            data=annotation_info[1:], columns=annotation_info[0]
        ),
        missed_annotations=pd.DataFrame(
            data=missing_annotations[1:], columns=missing_annotations[0]
        ),
        binary_dataset=df_encoded,
        unk_variables=unk_df,
        corpus_stats=corpus_statitstics,
    )

    return to_return


class DCThread(QtCore.QThread):
    def __init__(
        self, inputs, corpus_dict, independent_variables, dependent_variables, speakers
    ):
        super().__init__()

        self.corpus_dict = corpus_dict
        self.independent_variables = independent_variables
        self.dependent_variables = dependent_variables
        self.speakers = speakers
        self.inputs = inputs
        self.logger = QTextLogger()
        # define the flag to stop the thread
        self.stop_event = threading.Event()
        self.results = None

    def stop(self) -> None:
        self.stop_event.set()

    def run(self):
        try:
            # Call the generate_dataset() method here
            results = generate_dataset(
                self.inputs,
                self.logger,
                self.corpus_dict,
                self.speakers,
                self.independent_variables,
                self.dependent_variables,
                self.stop_event,
            )

            self.results = results
        except Exception as e:
            err_msg = (
                f"An error occurred while generating the dataset: {e}\n"
                f"{traceback.format_exc()}"
            )

            self.results = err_msg

        finally:
            self.finished.emit()


class CustomThread(QtCore.QThread):
    """Runs a method in a separate thread and emits a signal with the result when done."""

    def __init__(
        self, method2run: callable, signal: QtCore.Signal = None, *args, **kwargs
    ):
        """Initializes the thread with the method to run and the signal to emit the result.

        Args:
            method2run (callable): The method to run in the thread.
            signal (QtCore.Signal): The signal to emit the result.
        """
        super().__init__()
        self.method2run = method2run
        self.args = args
        self.kwargs = kwargs
        self.signal = signal

    def run(self):
        """Runs the method and emits the signal with the result when done."""
        result = self.method2run(*self.args, **self.kwargs)
        if self.signal:
            self.signal.emit(result)
        self.finished.emit()
