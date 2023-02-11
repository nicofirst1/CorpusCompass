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

        corpus_text += f"{value}\n\n\n"

        idx += 1

    return corpus_text


class CustomMatch:

    def __init__(self, match: re.Match, full_corpus: str):
        self.match = match
        fc_len = len(full_corpus)

        # add all the attributes of the match

        self.start = match.start()
        self.end = match.end()
        self.fc_start = match.start() + fc_len
        self.fc_end = match.end() + fc_len


def find_annotation(corpus: Dict[str, str], token: str, annotation_regex: re.Pattern, use_strict_rule: bool = True) -> \
        List[Tuple[CustomMatch, str]]:
    global warned_strict_rule

    found = []
    # for all the lines in the corpus find the annotation  with the regex
    full_text = OrderedDict()
    for k, line in corpus.items():
        full_text[k] = line
        matches = annotation_regex.finditer(line)
        matches = [m for m in matches if token in m.group()]

        if use_strict_rule:
            matches = [m for m in matches if m.group().split(".")[-1].replace("]", "") == token]

        if len(matches) > 0:
            for m in matches:
                ft = corpus_dict2text(full_text, skip_last=True)
                m = CustomMatch(m, ft)
                found.append((k, m))

    return found


def open_postprocess(paths: List[str], encoding: str, separator: str) -> Tuple[List[Any], Optional[str]]:
    """
    Open the file and return the content
    :param paths: list of paths
    :return: the content of the file
    """
    content = {}
    encoding= encoding.lower()
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
