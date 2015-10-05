import os.path

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def cabocha_to_morph_list(cabocha):
    sentences = []
    sentence = []
    for line in cabocha:
        if line == "EOS" and len(sentence) != 0:
            sentences.append(sentence)
            sentence = []
        elif line != "EOS" and line[0] != "*":
            out1 = line.rstrip("\n").split("\t")
            out2 = out1[1].split(",")
            surface = out1[0]
            base = out2[6]
            pos = out2[0]
            pos1 = out2[1]
            sentence.append(Morph(surface, base, pos, pos1))
    return sentences

if __name__ == '__main__':
    with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
        cabocha = [l.rstrip("\n") for l in f.readlines()]
    sentences = cabocha_to_morph_list(cabocha)
    print([e.surface for e in sentences[2]])
