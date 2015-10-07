import os.path
import sys
from Chap05_040 import Morph
from Chap05_041 import Chunk, cabocha_to_chunk_list

with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
    cabocha = [l.rstrip("\n") for l in f.readlines()]

sentences = cabocha_to_chunk_list(cabocha)
with open(os.path.normcase("output/Chapter5/_045.txt"), "w", encoding='utf-8') as f:
    for chunk_list in sentences:
        d = {}
        for chunk in chunk_list:
            dst = chunk.dst
            if dst != -1:
                pos_from = [m.pos for m in chunk.morphs]
                pos_to = [m.pos for m in chunk_list[dst].morphs]
                if "助詞" in pos_from and "動詞" in pos_to:
                    adverbs = [m.base for m in chunk.morphs if m.pos == "助詞"]
                    verb = [m.base for m in chunk_list[dst].morphs if m.pos == "動詞"][0]
                    if verb in d.keys():
                        d[verb] += adverbs
                    else:
                        d[verb] = adverbs
        for k, v in d.items():
            f.write("{}\t{}\n".format(k, " ".join(sorted(v))))