import os.path
import sys
from Chap05_040 import Morph
from Chap05_041 import Chunk, cabocha_to_chunk_list

with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
    cabocha = [l.rstrip("\n") for l in f.readlines()]

sentences = cabocha_to_chunk_list(cabocha)
with open(os.path.normcase("output/Chapter5/_046.txt"), "w", encoding='utf-8') as f:
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
                    phrase = "".join([m.surface for m in chunk.morphs if m.pos != "記号"])
                    if verb in d.keys():
                        d[verb][0] += adverbs
                        d[verb][1] += [phrase]
                    else:
                        d[verb] = [adverbs, [phrase]]
        for k, v in d.items():
            verb = k
            adverbs = " ".join(sorted(v[0]))
            phrase = " ".join(sorted(v[1]))
            f.write("{}\t{}\t{}\n".format(verb, adverbs, phrase))
