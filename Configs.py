import re


class Configs:

    ############################
    # CSV file
    ############################

    # separator for csv file, default is tab , you can also use: semicolon: ; , comma: , , tab : \t
    separator = '\t'

    # It can be useful to add the previous paragraph in the final csv file.
    # For example, when examining an annotation, you want to know what the previous speaker
    # said before the current one. If you are interested in this information being
    # in the final output set `previous_line` to `True`, else leave it `False`

    previous_line = False


    ############################
    # REGEX
    ############################
    name_regex = re.compile(r"(^[A-Z]) ")  # regex to find the name of the speaker, should match the name only

    # regex to find the features in the corpus, should match the whole feature
    square_regex = re.compile(r"(\[\$[\S ]*?\])")
    feat_regex = re.compile(r'\[\$([\S ]*?)\]')
    sequence_regex = re.compile(r"({[\S ]+})")


