import re
import string
from collections import Counter
from copy import copy
from typing import Tuple, List, Dict, Optional

import nltk

nltk.download('punkt')

from nltk import word_tokenize


def check_correct_annotations(annotations: List[re.Match], corpus: str, verbose: bool = True) -> Tuple[
    List[str], List[Tuple[str, str]]]:
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
            print(*args, **kwargs)

    ngram_params = (+50, 50)
    new_annotations = []
    incorrect_annotations = []
    for ann in annotations:
        group = ann.group()
        # check if there are parenthesis
        if "(" in group or ")" in group:
            custom_print(f"The annotation '{group}' contains parenthesis . Please remove them and try again.")
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue
        # elif if the number of square brackets is greater than 1
        elif len(re.findall(r"\[|\]", group)) > 2:
            custom_print(
                f"The annotation '{group}' contains more than one square bracket. Please remove them and try again.")
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue
        # elif there is no point in the annotation
        elif "." not in group:
            custom_print(f"The annotation '{group}' does not contain a point. Please add it and try again.")
            incorrect_annotations.append((group, get_context(ann, ngram_params)))
            continue


        else:
            new_annotations.append(group)

    return new_annotations, incorrect_annotations


def remove_features(corpus, square_regex):
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
            print(f"I found an error for the tag '{w}'. Maybe it does not have a point in it?\n"
                  f"Please check the tag and try again.")
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
        return name[0].lower().strip()
    else:
        return ""


def get_ngram(corpus: str, ngram_params: Tuple[int, int], index: int, square_regex: re.Pattern):
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
    result,_ = remove_features(result, square_regex)

    return result


def multi_corpus_upload(corpus_list: Dict[str, bytes], encoding: Optional[str] = "utf-16") -> Dict[str, str]:
    """
    Upload multiple corpus
    """

    alternative_encodings = [encoding] + ["utf-8", "utf-16", "latin-1", "ascii", "cp1252", "cp1250", "cp1251",
                                          "cp1253", ]

    def decode(to_decode) -> str:
        idx = 0
        dec = ""
        success = False
        while idx < len(alternative_encodings):
            encoding = alternative_encodings[idx]

            if idx > 0:
                print(f"Trying with the encoding {encoding}.")

            try:
                dec = to_decode.decode(encoding) + "\n"

                if " " not in dec:
                    print(
                        f"The corpus {k} has been read with the encoding {encoding}, but it seems that it did not work.")
                    idx += 1
                    continue

            except UnicodeDecodeError as e:
                print(f"Could not decode the corpus {k} with the encoding {encoding}.\n"
                      f"The error is: {e}\n")
                idx += 1
                continue
            success = True
            break

        if not success:
            raise ValueError(f"Could not decode the corpus {k} with any of the encodings {alternative_encodings}.\n"
                             f"Please check the encoding of the corpus and try again.")
        else:
            print(f"The corpus {k} has been read with the encoding {encoding}.")
        return dec

    corpus = {}

    for k, v in corpus_list.items():
        corpus[k] = decode(v)

    return corpus


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
        raise ValueError("Could not split the corpus into paragraphs. Please check the format of the corpus.")

    return res


def find_repetitions(corpus: str, token: str, annotation_regex: re.Pattern, name_regex: re.Pattern,
                     speaker_of_interest: List[str]) -> Tuple[int, int, int, List[str]]:
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

    for w in wild_rep:
        # find the speaker based on match location
        speaker = ""
        speak = corpus[:w.start()].split("\n")
        speak = speak[-1]
        speak = get_name(speak, name_regex)

        if speak in speaker_of_interest:
            interested_wild_rep += 1

    # total_wild_rep = corpus.count(f" {token} ")
    ann_rep = annotation_regex.findall(corpus)

    ann_rep = [a.split(".")[-1] for a in ann_rep]
    ann_rep = [a for a in ann_rep if token == a]
    ann_rep = len(ann_rep)

    wild_index = []
    for group in re.finditer(custom_token_regex, corpus):
        lower_bound = group.start() - char_ngram[0]
        upper_bound = group.end() + char_ngram[1]

        lower_bound = lower_bound if lower_bound > 0 else 0
        upper_bound = upper_bound if upper_bound < len(corpus) else len(corpus)

        wild_index.append(corpus[lower_bound:upper_bound])

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
        corpus_words = {k: v for k, v in corpus_words.items() if k not in string.punctuation}

    return corpus_words
