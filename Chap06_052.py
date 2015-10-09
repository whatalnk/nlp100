import os.path
from stemming.porter2 import stem


with open(os.path.normcase("output/Chapter6/_051.txt"), "r", encoding="utf-8") as f:
    for word in f.readlines():
        word = word.rstrip("\n")
        if word == "":
            print(word)
        else:
            print("{}\t{}".format(word, stem(word)))