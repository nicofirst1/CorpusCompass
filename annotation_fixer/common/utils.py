import re
from collections import OrderedDict
from typing import Dict, List, Tuple


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
                ft = corpus_dict2text(full_text,skip_last=True)
                m = CustomMatch(m, ft)
                found.append((k, m))

    return found
