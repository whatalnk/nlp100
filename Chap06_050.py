import os.path
import re

re_sentence = re.compile(r"[.:;!?]( )[A-Z]")
with open(os.path.normcase("data/nlp.txt"), "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        m = re.search(re_sentence, line)
        if m:
            i = 0
            for mm in re.finditer(re_sentence, line):
                print(line[i:mm.start()+2:])
                i = mm.start()+2
            print(line[i:])
        else:
            print(line)