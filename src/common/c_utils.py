import csv
import json
import os
import re
from typing import Dict, Optional, Tuple, List, Any

import pandas as pd

from src.common.Memory import Memory


def multi_corpus_upload(
    corpus_list: Dict[str, bytes], encoding: Optional[str] = "utf-16"
) -> Tuple[Dict[str, str], List[str]]:
    """
    Upload multiple corpus
    """

    alternative_encodings = [encoding] + [
        "utf-8",
        "utf-16",
        "latin-1",
        "ascii",
        "cp1252",
        "cp1250",
        "cp1251",
        "cp1253",
    ]

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
                        f"The corpus {k} has been read with the encoding {encoding}, but it seems that it did not work."
                    )
                    idx += 1
                    continue

                dec = re.sub(r"[^\S\n]+", " ", dec)

            except UnicodeDecodeError as e:
                print(
                    f"Could not decode the corpus {k} with the encoding {encoding}.\n"
                    f"The error is: {e}\n"
                )
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


def load_postprocess(
    paths: List[str], encoding: str, separator: str
) -> Tuple[List[Any], Optional[str]]:
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
            content[file_name] = pd.read_csv(
                path, encoding=encoding, on_bad_lines="skip", sep=separator
            )
        except UnicodeError as e:
            if encoding == "utf-8":
                encoding = "utf-16"
            elif encoding == "utf-16":
                encoding = "utf-8"
            else:
                error = f"Error while opening the file {path}\n{repr(e)}"
                return content, error

            content[file_name] = pd.read_csv(
                path, encoding=encoding, on_bad_lines="skip", sep=separator
            )
        except Exception as e:
            error = f"Error while opening the file {path}\n{repr(e)}"
            return content, error

    return content, None


def save_postprocess(results: Dict, mem: Memory):
    separator = mem.settings.get("separator", ";")
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

    # write the csv
    with open(dataset_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerows(results["dataset"])

    with open(annotation_info_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerow(results["annotation_info"])

    with open(not_annotated_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerow(results["missed_annotations"])

    results["binary_dataset"].to_csv(binary_dataset_path, index=False)

    # save the new paths in the memory
    mem.postprocess_paths = dict(
        dataset=dataset_path,
        binary_dataset=binary_dataset_path,
        annotation_info=annotation_info_path,
        missed_annotations=not_annotated_path,
    )


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