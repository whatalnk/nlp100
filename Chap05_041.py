import os.path
from Chap05_040 import Morph

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def cabocha_to_chunk_list(cabocha):
    sentences = []
    sentence = []
    chunks = []
    morphs = []
    for line in cabocha:
        if line == "EOS":
            if len(morphs) != 0:
                sentence.append(Chunk(morphs, dst, srcs))
                sentences.append(sentence)
                sentence = []
                morphs = []
        else:
            if line[0] == "*":
                if len(morphs) == 0:
                    out = line.rstrip("\n").split(" ")
                    dst = out[2]
                    srcs = out[1]
                else:
                    sentence.append(Chunk(morphs, dst, srcs))
                    out = line.rstrip("\n").split(" ")
                    dst = out[2]
                    srcs = out[1]
                    morphs = []
            else:
                out1 = line.rstrip("\n").split("\t")
                out2 = out1[1].split(",")
                surface = out1[0]
                base = out2[6]
                pos = out2[0]
                pos1 = out2[1]
                morphs.append(Morph(surface, base, pos, pos1))
    return sentences

if __name__ == '__main__':
    with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
        cabocha = [l.rstrip("\n") for l in f.readlines()]
    sentences = cabocha_to_chunk_list(cabocha)
    for chunk in sentences[7]:
        string = "".join([m.surface for m in chunk.morphs])
        print(string, "-->", chunk.dst)
