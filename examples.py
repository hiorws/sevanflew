from wordnet_tools import get_a_words_synsets, get_pos_tag_of_a_synset


def wordnet_samples():
    sample_word = "dog"
    synsets_list = get_a_words_synsets(sample_word)

    print("For word %s all synsets and their pos tag" % sample_word.upper())
    for syn in synsets_list:
        print(syn, str(get_pos_tag_of_a_synset(syn)).upper())


if __name__ == "__main__":
    wordnet_samples()
