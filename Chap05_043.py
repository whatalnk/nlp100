import os.path
from Chap05_040 import Morph
from Chap05_041 import Chunk, cabocha_to_chunk_list

with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
    cabocha = [l.rstrip("\n") for l in f.readlines()]

sentences = cabocha_to_chunk_list(cabocha)
with open(os.path.normcase("output/Chapter5/_043.tsv"), "w", encoding='utf-8') as f:
    for chunk_list in sentences:
        for chunk in chunk_list:
            dst = int(chunk.dst.rstrip("D"))
            if dst != -1:
                pos_from = [m.pos for m in chunk.morphs]
                pos_to = [m.pos for m in chunk_list[dst].morphs]
                if "名詞" in pos_from and "動詞" in pos_to:
                    str_from = "".join([m.surface for m in chunk.morphs if m.pos != "記号"])
                    str_to = "".join([m.surface for m in chunk_list[dst].morphs if m.pos != "記号"])
                    f.write("\t".join([str_from, str_to])+"\n")