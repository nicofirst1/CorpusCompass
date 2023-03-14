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
            f"I removed {removed_sentences} (out of {len(corpus)}) paragraphs from the '{path}' file, since I could not detect a speaker\n"
            f"I will show it over here, sorted by the their line:"
        )
        diff = set(prev_c) - set(corpus)
        diff = sorted(diff, key=lambda x: prev_c.index(x))
        for i in diff:
            logger.warning(f"{prev_c.index(i)}: {i}")
        logger.warning("\n\n")
        logger.warning(
            "If you see paragraphs you are interested in, consider manually changing them in the corpus, or expanding the 'name_regex' rule"
        )

    if len(corpus) == 0:
        logger.error(
            "All the paragraphs in the corpus have been deleted! You should review your regex rules"
        )

    return corpus


def check_correct_annotations(
    annotations: List[re.Match],
    corpus: str,
    corpus_path: str,
    logger,
    verbose: bool = True,
) -> Tuple[List[str], List[Tuple[str, str]]]:
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

    def custom_print(*args, **kwargs):
        if verbose:
            logger.error(f"\nError in the corpus {corpus_path}: ")
            logger.error(*args, **kwargs)

    ngram_params = (+50, 50)
    new_annotations = []
    incorrect_annotations = []
    for ann in annotations:
        group = ann.group()
        # check if there are parenthesis
        if "(" in group or ")" in group:
            custom_print(
                f"The annotation '{group}' contains parenthesis . Please remove them and try again."
            )
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue
        # elif if the number of square brackets is greater than 1
        elif len(re.findall(r"\[|\]", group)) > 2:
            custom_print(
                f"The annotation '{group}' contains more than one square bracket. Please remove them and try again."
            )
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue
        # elif there is no point in the annotation
        elif "." not in group:
            custom_print(
                f"The annotation '{group}' does not contain a point. Please add it and try again."
            )
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue

        else:
            new_annotations.append(group)

    return new_annotations, incorrect_annotations


def remove_features(corpus, square_regex, logger):
    """
    Remove the features from the corpus
    """
    corpus = copy(corpus)
    words = square_regex.findall(corpus)
    wrong_tags = []
    for w in words:
        try:
            text = w.rsplit(".", 1)[1][:-1] + " "
            corpus = corpus.replace(w, text)
        except IndexError:
            logger.error(
                f"I found an error for the tag '{w}'. Maybe it does not have a point in it?\n"
                f"Please check the tag and try again."
            )
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
        return name[0].strip()
    else:
        return ""


def get_ngram(
    corpus: str, ngram_params: Tuple[int, int], index: int, square_regex: re.Pattern
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
    result, _ = remove_features(result, square_regex)

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
    annotation_regex: re.Pattern,
    name_regex: re.Pattern,
    speaker_of_interest: List[str],
    check_annotated: Optional[bool] = True,
) -> Tuple[int, int, int, List[str]]:
    """
    Find the repetitions of a token in a corpus
    :param corpus: the corpus
    :param token: the token to look for
    :param annotation_regex: the regex to use
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
    if check_annotated:
        ann_rep = annotation_regex.findall(corpus)

        ann_rep = [a.split(".")[-1] for a in ann_rep]
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
