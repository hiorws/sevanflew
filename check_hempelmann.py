import xml.etree.ElementTree as et
import csv

tree = et.parse('sample_data/subtask1-heterographic-test.xml')  # parse edilecek xml adi
root = tree.getroot()

# to generate a python dict to collect all keywords of hempelmann entry
hempelmann_dict = dict()
with open('sample_data/hempelmann_main_corpus.tsv', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        hempelmann_dict[str(row[1]).lower()] = row
        # print(row[1])


for texts in root:
    if texts.tag == 'text':
        sentence = ""
        for item in texts:
            if item.tag == 'word':
                sentence= sentence + item.text + ' '
        words_of_sentence = sentence.lower().split()
        # print(words_of_sentence)
        for word in words_of_sentence:
            if word in hempelmann_dict.keys():
                print("WORD: " + str(word) + "\n" + str(hempelmann_dict[word]))
                pass



