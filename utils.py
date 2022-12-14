import re
import string
from collections import Counter
from copy import copy
from typing import Tuple, List, Dict

import nltk
nltk.download('punkt')

from nltk import RegexpTokenizer, word_tokenize

name_regex= re.compile(r"(^[A-Z]) ")

def remove_features(corpus,square_regex):
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
            print(f"I found an error for the tag '{w}'. Myabe it does not have a point in it?\n"
                        f"Please check the tag and try again.", "error")
            exit()

    return corpus

def get_name(line:str):
    """
    Use the regex to find the name of the speaker
    :param line:
    :return:
    """

    name = name_regex.findall(line)
    if len(name) > 0:
        return name[0]
    else:
        return ""

def get_ngram(word:str, corpus:str, ngram_params:Tuple[int, int]):
    """
    Get the ngram of a word in a corpus
    """

    tokenizer = RegexpTokenizer(r'\w+')

    words=tokenizer.tokenize(word)

    lookup_corpus=tokenizer.tokenize(corpus)

    try:
        words_idx=[lookup_corpus.index(word) for word in words]
    except ValueError:
        print(f"Could not find the word '{word}' in the corpus:\n {corpus}.\n\n Maybe there is a problem with the annotation?\nI'm going to skip this for now, but you should check it later!")
        return "Error"


    lower_bound=[w- ngram_params[0] for w in  words_idx]
    upper_bound=[w+ ngram_params[1] for w in  words_idx]

    # get min and max
    lower_bound=min(lower_bound)
    upper_bound=max(upper_bound)

    # Check if the ngram is out of the corpus
    lower_bound= lower_bound if lower_bound >0 else 0
    upper_bound= upper_bound if upper_bound < len(corpus) else len(corpus)

    result=" ".join( corpus.split(" ")[lower_bound:upper_bound])

    return result



def multi_corpus_upload(corpus_list:Dict[str,bytes])->str:
    """
    Upload multiple corpus
    """
    corpus=""
    for k,v in corpus_list.items():
        corpus+=v.decode("utf-16")+"\n"

    return corpus




def count_tokens(corpus:str, remove_punctuation=True):
    """
    Count the number of tokens in a corpus
    :param corpus:
    :param remove_punctuation:
    :return:
    """
    corpus_words=word_tokenize(corpus)


    corpus_words=Counter(corpus_words)

    # exclude punctuation
    if remove_punctuation:
        corpus_words={k:v for k,v in corpus_words.items() if k not in string.punctuation}


    return corpus_words