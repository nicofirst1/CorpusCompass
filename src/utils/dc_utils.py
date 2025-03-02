import re
import string
from collections import Counter
from copy import copy
from typing import Tuple, List, Optional

import nltk

nltk.download("punkt")

from nltk import word_tokenize


def preprocess_corpus(corpus_text, path, name_regex, logger):
    # step 1: split the whole corpus in different elements every new line, creating a list of paragraphs. For us this means splitting interviewer and interviewee in different paragraphs
    corpus = split_paragraphs(corpus_text)
    # step 2: remove spaces at the start and end of each paragraph
    corpus = [x.strip() for x in corpus]
    # remove extra spaces in the middle of the paragraph
    corpus = [re.sub(r"\s+", " ", x) for x in corpus]
    # step 3 : remove empty paragraphs from the list
    corpus = [x for x in corpus if x != ""]
    # step 4 : filter out all the paragraphs that do not have any DETECTED speaker
    prev_c = copy(corpus)
    corpus = [x for x in corpus if get_name(x, name_regex)]

    removed_sentences = len(prev_c) - len(corpus)
    if removed_sentences > 0:
        logger.warning(
            f"I removed {removed_sentences} (out of {len(prev_c)}, {len(corpus)} left) paragraphs from the '{path}' file, since I could not detect a speaker\n"
            f"I will show it over here, sorted by the their line:"
        )
        diff = set(prev_c) - set(corpus)
        diff = sorted(diff, key=lambda x: prev_c.index(x))
        msg = ""
        for i in diff:
            msg += f"{prev_c.index(i)}: {i}\n\n"

        logger.warning(
            f"{msg}"
            f"\n\n"
            "If you see paragraphs you are interested in, consider manually changing them in the corpus, or expanding the 'name_regex' rule"
        )

    return corpus


def check_correct_annotations(
    annotations: List[re.Match],
    corpus: str,
    corpus_path: str,
    verbose: bool = True,
) -> Tuple[List[str], List[Tuple[str, str]], str]:
    """
    Check if the annotations are correct

    :param annotations: the annotations to check
    :param corpus: the corpus
    :return: a tuple with the correct annotations and the incorrect ones
    """

    def get_context(match: re.Match, ngram_params: Tuple[int, int]) -> str:
        """
        Get the context of a match
        """
        lower_bound = match.start() - ngram_params[0]
        upper_bound = match.end() + ngram_params[1]

        # Check if the ngram is out of the corpus
        lower_bound = lower_bound if lower_bound > 0 else 0
        upper_bound = upper_bound if upper_bound < len(corpus) else len(corpus)

        result = " ".join(corpus.split(" ")[lower_bound:upper_bound])

        return result

    def custom_print(to_print):
        err_msg = ""
        if verbose:
            err_msg = f"\nError in the corpus {corpus_path}: \n" f"{to_print}\n"
        return err_msg

    ngram_params = (+50, 50)
    new_annotations = []
    incorrect_annotations = []

    error_msg = ""

    for ann in annotations:
        group = ann.group(0)
        # check if there are parenthesis
        if "(" in group or ")" in group:
            error_msg += custom_print(
                f"The annotation '{group}' contains parenthesis . Please remove them and try again."
            )
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue
        else:
            new_annotations.append(ann.group("token"))

    return new_annotations, incorrect_annotations, error_msg


def remove_features(corpus: str, feat_regex_dict: dict, logger):
    """
    Remove the features from the corpus
    """
    corpus = copy(corpus)
    for _, content in feat_regex_dict.items():
        feat_regex, _ = content
        words = re.finditer(feat_regex, corpus)
        wrong_tags = []
        for w in words:
            try:
                text = w.group("token")
                corpus = corpus.replace(w.group(0), text)
            except IndexError:
                logger.error(
                    f"I found an error for the tag '{w}'. Please check the tag and try again.")
                wrong_tags.append(w)
                continue

    return corpus, wrong_tags


def get_name(line: str, regex):
    """
    Use the regex to find the name of the speaker
    :param line:
    :return:
    """

    name = regex.findall(line)
    if len(name) > 0:
        if type(name) == tuple:
            return name[0].strip()
        elif type(name) == list:
            return name[0][0].strip()

    return ""


def get_ngram(
    corpus: str,
    ngram_params: Tuple[int, int],
    index: int,
    feat_regex: re.Pattern,
    logger,
):
    """
    Get the ngram of a word in a corpus
    """

    prev = corpus[:index]
    next = corpus[index:]

    prev = prev.split(" ")
    next = next.split(" ")

    lower_bound = ngram_params[0]
    upper_bound = ngram_params[1]
    # Check if the ngram is out of the corpus
    lower_bound = lower_bound if lower_bound > 0 else 0
    upper_bound = upper_bound if upper_bound < len(corpus) else len(corpus)

    prev = prev[-lower_bound:]
    next = next[:upper_bound]

    result = prev + next
    result = " ".join(result)
    result, _ = remove_features(result, feat_regex, logger)

    return result


def split_paragraphs(corpus: str) -> List[str]:
    """
    Split the corpus into paragraphs
    :param corpus:
    :return:
    """

    res = corpus.split("\n")
    if len(res) == 1:
        res = corpus.split("\r")

    if len(res) == 1:
        raise ValueError(
            "Could not split the corpus into paragraphs. Please check the format of the corpus."
        )

    return res


def find_repetitions(
    corpus: str,
    token: str,
    feat_regex_dict: re.Pattern,
    name_regex: re.Pattern,
    speaker_of_interest: List[str],
    check_annotated: Optional[bool] = True,
) -> Tuple[int, int, int, List[str]]:
    """
    Find the repetitions of a token in a corpus
    :param corpus: the corpus
    :param token: the token to look for
    :param feat_regex_dict: dict containing the regex to use
    :param name_regex: the regex to use to find the name of the speaker
    :param speaker_of_interest: a list of speaker of interest
    :return: Tuple with :
    - the repetitions of all not-annotated tokens
    - the repetitions of not-annotated tokens of the speaker of interest
    - the repetitions of annotated tokens
    - the context of non-annotated tokens
    """

    # context n-gram
    char_ngram = (+50, 50)

    custom_token_regex = re.compile(rf"( {token})[^\][A-z][.,]?")

    wild_rep = list(re.finditer(custom_token_regex, corpus))
    total_wild_rep = len(wild_rep)
    interested_wild_rep = 0

    # total_wild_rep = corpus.count(f" {token} ")
    for _, content in feat_regex_dict.items():
        feat_regex, _ = content
        if check_annotated:
            ann_rep = re.finditer(feat_regex, corpus)

            ann_rep = [a.group("token") for a in ann_rep]
            ann_rep = [a for a in ann_rep if token == a]
            ann_rep = len(ann_rep)
        else:
            ann_rep = 0

        wild_index = []
        speakers = []
        for w in wild_rep:
            lower_bound = w.start() - char_ngram[0]
            upper_bound = w.end() + char_ngram[1]

            lower_bound = lower_bound if lower_bound > 0 else 0
            upper_bound = upper_bound if upper_bound < len(corpus) else len(corpus)

            wild_index.append(corpus[lower_bound:upper_bound])

            # find the speaker based on match location
            speak = corpus[: w.start()].split("\n")
            speak = speak[-1]
            speak = get_name(speak, name_regex)

            if speak in speaker_of_interest:
                interested_wild_rep += 1
                speakers.append(speak)

    return total_wild_rep, interested_wild_rep, ann_rep, wild_index


def count_tokens(corpus: str, remove_punctuation=True):
    """
    Count the number of tokens in a corpus
    :param corpus:
    :param remove_punctuation:
    :return:
    """
    corpus_words = word_tokenize(corpus)

    corpus_words = Counter(corpus_words)

    # exclude punctuation
    if remove_punctuation:
        corpus_words = {
            k: v for k, v in corpus_words.items() if k not in string.punctuation
        }

    return corpus_words
