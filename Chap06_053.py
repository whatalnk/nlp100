import os.path
import xml.etree.ElementTree as etree

# java -cp stanford-corenlp-3.5.2.jar;stanford-corenlp-3.5.2-models.jar;xom.jar;joda-time.jar;jollyday.jar;ejml-0.23.jar -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -file path\to\nlp.txt

tree = etree.parse(os.path.normcase("output/Chapter6/nlp.txt.xml"))
root = tree.getroot()
for e in root.findall(".//word"):
    print(e.text)