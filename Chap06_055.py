import os.path
import xml.etree.ElementTree as etree

tree = etree.parse(os.path.normcase("output/Chapter6/nlp.txt.xml"))
root = tree.getroot()
for e in root.findall(".//token"):
    ner = e.find("./NER").text
    if ner == "PERSON":
        print(e.find("./word").text)