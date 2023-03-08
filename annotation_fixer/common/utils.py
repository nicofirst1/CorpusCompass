import json
import os.path
import re
from collections import OrderedDict
from typing import Dict, List, Tuple, Any, Optional

import pandas as pd


def corpus_dict2text(corpus_list: Dict[str, str], skip_last=False) -> str:
    corpus_text = ""
    rep = 20

    idx = 0
    max_len = len(corpus_list)
    for key, value in corpus_list.items():
        corpus_text += f"{'#' * rep}\n {key} \n{'#' * rep}\n"

        if skip_last and idx == max_len - 1:
            continue
        value="\n".join(value.split("\n"))
        corpus_text += f"{value}\n\n\n"

        idx += 1

    return corpus_text


class CustomMatch:

    def __init__(self, start: int, end: int, token: str, full_corpus: str, match: Optional[re.Match] = None):
        self.match = match
        fc_len = len(full_corpus)

        # add all the attributes of the match

        self.start = start
        self.end = end
        self.fc_start = start + fc_len
        self.fc_end = end + fc_len
        self.token = token


def find_annotation_context(corpus: Dict[str, str], token: str, contexts: List[str]) -> \
        List[Tuple[CustomMatch]]:
    def save_match(word_idx):
        start = context_idx + word_idx
        end = start + len(token)

        ft = corpus_dict2text(full_text, skip_last=True)
        m = CustomMatch(start, end, token, ft)
        found.append((k, m))

    found = []
    found_context = []
    # for all the lines in the corpus find the annotation  with the regex
    full_text = OrderedDict()
    for k, line in corpus.items():
        full_text[k] = line

        contexts = [c for c in contexts if c not in found_context]

        idx = 0
        while idx < len(contexts):
            c = contexts[idx]
            if c not in line:
                idx += 1
                continue

            context_idx = line.index(c)

            token_present = sum([token in x for x in c.split(" ")])
            if token_present <= 1:
                word_idx = c.index(token)
                save_match(word_idx)
                found_context.append(c)

            else:
                prev_idx = 0
                for i in range(token_present):
                    word_idx = c.index(token, prev_idx)
                    save_match(word_idx)

                    prev_idx = word_idx + len(token)
                    found_context.append(contexts[idx + i])
                idx += token_present - 1
            idx += 1

    return found


def find_annotation_regex(corpus: Dict[str, str], token: str, annotation_regex: re.Pattern,
                          use_strict_rule: bool = True) -> \
        List[Tuple[CustomMatch]]:
    found = []
    # for all the lines in the corpus find the annotation  with the regex
    full_text = OrderedDict()
    for k, line in corpus.items():
        full_text[k] = line
        matches = annotation_regex.finditer(line)
        matches = list(matches)
        matches = [m for m in matches if token in m.group()]

        if use_strict_rule:
            matches = [m for m in matches if m.group().split(".")[-1].replace("]", "") == token]

        if len(matches) > 0:
            for m in matches:
                ft = corpus_dict2text(full_text, skip_last=True)
                m = CustomMatch(m.start(), m.end(), token, ft, m)
                found.append((k, m))

    return found


def open_postprocess(paths: List[str], encoding: str, separator: str) -> Tuple[List[Any], Optional[str]]:
    """
    Open the file and return the content
    :param paths: list of paths
    :return: the content of the file
    """
    content = {}
    encoding = encoding.lower()
    for path in paths:
        file_name = os.path.basename(path).split(".")[0]
        try:
            content[file_name] = pd.read_csv(path, encoding=encoding, on_bad_lines="skip", sep=separator)
        except UnicodeError as e:
            if encoding == "utf-8":
                encoding = "utf-16"
            elif encoding == "utf-16":
                encoding = "utf-8"
            else:
                error = f"Error while opening the file {path}\n{repr(e)}"
                return content, error

            content[file_name] = pd.read_csv(path, encoding=encoding, on_bad_lines="skip", sep=separator)
        except Exception as e:
            error = f"Error while opening the file {path}\n{repr(e)}"
            return content, error

    return content, None


def open_variables(paths: List[str], encoding: str) -> Tuple[List[Any], Optional[str]]:
    """
    Open the file and return the content
    :param paths: list of paths
    :return: the content of the file
    """
    content = {}
    encoding = encoding.lower()
    for path in paths:
        file_name = os.path.basename(path).split(".")[0]
        try:
            with open(path, encoding=encoding) as f:
                content[file_name] = json.load(f)

        except UnicodeError as e:
            if encoding == "utf-8":
                encoding = "utf-16"
            elif encoding == "utf-16":
                encoding = "utf-8"
            else:
                error = f"Error while opening the file {path}\n{repr(e)}"
                return content, error

            with open(path, encoding=encoding) as f:
                content[file_name] = json.load(f)
        except Exception as e:
            error = f"Error while opening the file {path}\n{repr(e)}"
            return content, error

    return content, None


def remove_independent_vars(dependent: Dict[str, Any], independent: Dict[str, Any]):
    """
    Remove the independent variables from the dependent variables.
    check if the values of the independent variables are the same as the dependent variables,
    if so remove the independent
    :param dependent: the dependent variables
    :param independent: the independent variables
    :return:
    """

    for k, v in independent.items():
        # check if any of the values are present in the dependent variables, if so remove from dependent

        v = [v] if not isinstance(v, list) else v
        for v2 in v:
            for k2, v3 in dependent.items():
                if v2 in v3:
                    del dependent[k2]
                    break

    return dependent


def multi_corpus_upload(corpus_list: Dict[str, bytes], encoding: Optional[str] = "utf-16") -> Tuple[
    Dict[str, str], List[str]]:
    """
    Upload multiple corpus
    """

    alternative_encodings = [encoding] + ["utf-8", "utf-16", "latin-1", "ascii", "cp1252", "cp1250", "cp1251",
                                          "cp1253", ]

    def decode(to_decode) -> Tuple[str, str]:
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

                dec = re.sub(r'[^\S\n]+', ' ', dec)


            except UnicodeDecodeError as e:
                print(f"Could not decode the corpus {k} with the encoding {encoding}.\n"
                      f"The error is: {e}\n")
                idx += 1
                continue
            success = True
            break

        if not success:
            msg = f"Could not decode the corpus {k} with any of the encodings {alternative_encodings}.\n"
            f"Please check the encoding of the corpus and try again."
            return "", msg
        else:
            print(f"The corpus {k} has been read with the encoding {encoding}.")
        return dec, ""

    corpus = {}
    errs = []
    for k, v in corpus_list.items():
        corpus[k], err = decode(v)
        errs.append(err)

    errs = [e for e in errs if e != ""]

    return corpus, errs
