import os.path
import xml.etree.ElementTree as etree

tree = etree.parse(os.path.normcase("output/Chapter6/nlp.txt.xml"))
root = tree.getroot()
for e in root.findall(".//token"):
    word = e.find("./word").text
    lemma = e.find("./lemma").text
    pos = e.find("./POS").text
    print("{}\t{}\t{}".format(word, lemma, pos))