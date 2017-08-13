import nltk
from nltk import ngrams
from nltk.collocations import *

sentence = 'bu cumle, n-gram denemesi icin yazilmis bir deneme cumlesidir.'
tokens = nltk.word_tokenize(sentence)

# Create your bigrams
bgs = nltk.ngrams(tokens,2)

# compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    print (k,v)
