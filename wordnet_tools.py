# documentation of nltk wordnet interface
# http://www.nltk.org/howto/wordnet.html

from nltk.corpus import wordnet as wn


def get_a_words_synsets(word, pos_tag=None):
    """
    if pos tag is given, then you can constrain part of speech of the word
    pos_tag's can be wn.VERB wn.NOUN wn.ADJ wn.ADV
    """

    if pos_tag:
        synsets = wn.synsets(word, pos=pos_tag)
    else:
        synsets = wn.synsets(word)
    return synsets


def get_pos_tag_of_a_synset(synset):
    """
    the function which returns the pos tag of an synset object
    """

    pos_tag = synset.name().split(".")[1]

    return pos_tag
