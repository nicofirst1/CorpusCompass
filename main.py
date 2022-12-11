import csv
import json
import re
from copy import copy
from colors import color_print, info, warning, error

# REGEX used to find the tags
square_regex = re.compile(r"(\[\$[\S ]*?\])")
feat_regex = re.compile(r'\[\$([\S ]*?)\]')
sequence_regex = re.compile(r"({[\S ]+})")

# variables paths
dependent_variable_path = './dependent_variables.json'
independent_variable_path = './independent_variables.json'

# path for the transcription file
transcription_path = ""

# separator for the csv file
# Alternatives are:
# semicolon: ';'
# comma: ','
separator = '\t'


def remove_features(corpus):
    """
    Remove the features from the corpus
    """

    corpus = copy(corpus)

    words = square_regex.findall(corpus)

    for w in words:
        try:
            text = w.rsplit(".", 1)[1][:-1]
            corpus = corpus.replace(w, text)
        except IndexError:

            color_print(f"I found an error for the tag '{w}'. Myabe it does not have a point in it?\n"
                        f"Please check the tag and try again.", "error")

            exit()
            continue

    return corpus


def get_name(line):
    return line.split(" ")[0]


def main(transcription_path):
    # Load the dependent variable
    with open(dependent_variable_path, 'r') as f:
        dependent_variable = json.load(f)

    # Load the dependent variable
    with open(independent_variable_path, 'r') as f:
        independent_variable = json.load(f)

    dependent_variable.update(independent_variable)
    # get an inverse of the dependent variable
    idv = {}
    for k, v in dependent_variable.items():
        if isinstance(v, list):
            for i in v:
                idv[i] = k
        else:
            idv[v] = k

    # ask user for path input
    path = input(info(f'Drag and drop the transcription file (.txt), or leave blank if "{transcription_path}" '
                      f'is correct: '))
    print("\n")
    if len(path) > 0:
        transcription_path = path.strip()

    output_path = transcription_path.replace('.txt', '_output.csv')

    # opend the file
    with open(transcription_path, 'r+', encoding="utf16") as f:
        trans = f.readlines()

    trans = trans[2:]
    trans = [x.strip() for x in trans]
    trans = [x for x in trans if x != '']

    # ask for interviwers name
    interviewers = input(info(f'Add the name(s) of the interviewer(s) (separated by comma), '
                              f'leave empty for classical interviewer-interviewees structure: '))
    print("\n")
    if len(interviewers) > 0:
        interviewers = interviewers.split(',')
    else:
        interviewers = trans[0][0]

    # ask for previous line
    previous_line = input(info(f'When generating the final cvs file, I can also include the speaker utterance.'
                               f' Do you want me to include it? (y/n): '))
    print("\n")
    if previous_line == 'y':
        previous_line = True
    else:
        previous_line = False

    # get speak/list names
    names = [get_name(x).strip() for x in trans]
    names = set(names)

    # remove all mention of interviwers in names
    for i in interviewers:
        names = [x for x in names if i not in x]

    interviewees = list(names)

    # notify user about names
    print(warning(f"I found the following names: {', '.join(interviewees)}"))

    # compile regex to find features
    csv_header = list(dependent_variable.keys())

    # define the end of the csv
    csv_end = ['sequence in sentence', 'unk']

    if previous_line:
        csv_end.insert(0, 'previous line')

    csv_header = ["text"] + csv_header + csv_end

    csv_file = [csv_header]

    unk_categories = []

    # for every paragraph in the transcript
    for idx in range(len(trans)):
        c = trans[idx]

        # get the paragraph without features

        if get_name(c) in interviewees:
            sp = trans[idx - 1]
        else:
            continue

        clean_p = remove_features(c)

        # capture all the sequences
        sequences = sequence_regex.finditer(clean_p)
        sequences = [(x.start(), x.end(), x.group()) for x in sequences]

        # get the features
        tags = feat_regex.finditer(c)

        # for every tags with features in the paragraph
        for t in tags:
            # get index of result + tag
            index = t.start()
            t = t.group(1)

            # initialize empty row
            csv_line = ["" for _ in range(len(csv_header))]

            # get the features
            feats = t.rsplit(".", 1)
            text = feats[1]
            feats = feats[0]

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
            csv_line[0] = text
            if previous_line:
                csv_line[-3] = sp

            # add the sequence to the line
            if len(sequences) != 0:
                for s in sequences:
                    seq_start, seq_end, seq = sequences[0]
                    if seq_start < index < seq_end:
                        seq = seq.replace("{", "").replace("}", "")
                        csv_line[-2] = seq

            csv_line[-1] = csv_line[-1].strip(",")
            csv_file.append(csv_line)

    # write the csv
    with open(output_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f, delimiter=separator)
        writer.writerows(csv_file)

    color_print(f"Done!\nFile has been saved in '{output_path}'","ok")
    if len(unk_categories) > 0:
        unk_categories = set(unk_categories)
        unk_categories = sorted(unk_categories)
        print(warning(
            f"I have found several categories not listed in '{independent_variable_path}' or in '{dependent_variable_path}'.\n"
            f"Following in alphabetical order:"))
        for c in unk_categories:
            print(warning(c.strip()))


if __name__ == '__main__':

    try:
        main(transcription_path)
    except Exception as e:
        print(error(f"An error occured: {e}"))
        exit(1)
