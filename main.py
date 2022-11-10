import csv
import json
import re
from copy import copy

dependent_variable_path = './dependent_variables.json'
independent_variable_path = './independent_variables.json'
square_regex=re.compile(r"(\[\$[\S ]*?\])")

def remove_features(corpus):

    corpus=copy(corpus)

    words = square_regex.findall(corpus)

    for w in words:
        try:
            text = w.rsplit(".", 1)[1][:-1]
            corpus=corpus.replace(w, text)
        except IndexError:
            print(f"I found an error for the text '{text}'.\n"
                  f"The complete tag is '{w}'. Myabe it does not have a point in it?\n"
                  f"Please check the tag and try again.")
            exit()
            continue

    return corpus



if __name__ == '__main__':

    # Load the dependent variable
    with open(dependent_variable_path, 'r') as f:
        dependent_variable = json.load(f)

        # Load the dependent variable
    with open(dependent_variable_path, 'r') as f:
        independent_variable = json.load(f)

    dependent_variable.update(independent_variable)
    # get an inverse of the dependent variable
    idv={}
    for k,v in dependent_variable.items():
        if isinstance(v, list):
            for i in v:
                idv[i]=k
        else:
            idv[v]=k


   # ask user for path input
    transcription_path="/Users/giulia/Downloads/Somaya.txt"
    path = input(f'Enter transcription path, or leave blank if "{transcription_path}" is correct: ')
    print("\n")
    if len(path) > 0:
        transcription_path = path

    output_path = transcription_path.replace('.txt', '_output.csv')

    # opend the file
    with open(transcription_path, 'r+',encoding="utf16") as f:
        trans = f.readlines()

    date=trans[1]
    trans=trans[2:]
    trans=[x.strip() for x in trans]
    trans=[x for x in trans if x != '']

    # get speak/list names
    speaker=trans[0][0]
    listener=trans[1][0]

    # compile regex to find features
    feat_regex = re.compile(r'\[\$([\S ]*?)\]')

    csv_header=list(dependent_variable.keys())
    csv_header=["text"] +csv_header +["unk"]

    csv_file=[csv_header]


    unk_categories=[]

    # for every paragraph in the transcript
    for idx in range(len(trans)):
        c=trans[idx]

        # get the paragraph without features

        if c[0] == listener:
            sp=trans[idx-1]
        else:
            continue

        clean_p=remove_features(c)

        # get the features
        words=feat_regex.findall(c)

        # for every words with features in the paragraph
        for w in words:

            csv_line=["" for _ in range(len(csv_header))]

            feats=w.rsplit(".",1)
            text=feats[1]
            feats=feats[0]

            # for every feature in the word
            for f in feats.split("."):
                # if the category is not present in the dict, then add to unk
                if f not in idv.keys():
                    unk_categories.append(f)
                    csv_line[-1]=csv_line[-1]+f+","
                else:
                    category=idv[f]
                    cat_idx=csv_header.index(category)
                    csv_line[cat_idx]=f

            # add initial infos and final unk to the line
            csv_line[0]=text
            # csv_line[1]=clean_p
            # csv_line[2]=sp
            csv_line[-1]=csv_line[-1].strip(",")



            csv_file.append(csv_line)



    # write the csv
    with open(output_path, "w", newline="", encoding="utf16") as f:
        writer = csv.writer(f)
        writer.writerows(csv_file)

    print(f"Done!\nFile has been saved in '{output_path}'")
    if len(unk_categories)>0:
        unk_categories=set(unk_categories)
        unk_categories=sorted(unk_categories)
        print(f"I have found several categories not listed in '{independent_variable_path}' or in '{dependent_variable_path}'.\n"
              f"Following in alphabetical order:")
        for c in unk_categories:
            print(c)
