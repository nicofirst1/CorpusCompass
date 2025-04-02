import re
from typing import Optional, Tuple
import json
import os


def decode_txt_file(
    file_path: str, encoding: Optional[str] = "utf-16", print_messages: bool = False
) -> Tuple[str, str, str]:
    buffered_file = open(file_path, "rb")
    file_binary = buffered_file.read()
    buffered_file.close()

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

            if idx > 0 and print_messages:
                print(f"Trying with the encoding {encoding}.")

            try:
                dec = to_decode.decode(encoding) + "\n"

                if " " not in dec:
                    if print_messages:
                        print(
                            f"The corpus {file_path} has been read with the encoding {encoding}, but it seems that it did not work."
                        )
                    idx += 1
                    continue

                dec = re.sub(r"[^\S\n]+", " ", dec)

            except UnicodeDecodeError as e:
                if print_messages:
                    print(
                        f"Could not decode the corpus {file_path} with the encoding {encoding}.\n"
                        f"The error is: {e}\n"
                    )
                idx += 1
                continue
            success = True
            break

        if not success:
            msg = f"Could not decode the corpus {file_path} with any of the encodings {alternative_encodings}.\n"
            f"Please check the encoding of the corpus and try again."
            return "", "", msg
        elif print_messages:
            print(f"The corpus {file_path} has been read with the encoding {encoding}.")
        return dec, encoding, ""

    corpus, used_encoding, err = decode(file_binary)
    return corpus, used_encoding, err


def save_json_file(
    filepath: str,
    data: dict,
) -> None:
    with open(filepath, "w") as outfile:
        json.dump(data, outfile, indent=4)


def load_json_file(filepath: str) -> dict:
    with open(filepath, "r") as infile:
        return json.load(infile)
