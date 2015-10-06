import os.path
import sys
from Chap05_040 import Morph
from Chap05_041 import Chunk, cabocha_to_chunk_list

with open(os.path.normcase("output/Chapter5/neko.txt.cabocha"), "r", encoding='utf-8') as f:
    cabocha = [l.rstrip("\n") for l in f.readlines()]

sentences = cabocha_to_chunk_list(cabocha)

node_list = []
chunk_list = sentences[int(sys.argv[1])]
for chunk in chunk_list:
    dst = int(chunk.dst.rstrip("D"))
    if dst != -1:
        str_srcs = "".join([m.surface for m in chunk.morphs if m.pos != "記号"])
        str_dst = "".join([m.surface for m in chunk_list[dst].morphs if m.pos != "記号"])
        node_list.append([str_srcs, str_dst])

with open(os.path.normcase("output/Chapter5/_044.dot"), "w", encoding='utf-8') as f:
    f.write('digraph graphname {\nnode [fontname="IPAexGothic"];\n')
    for nodes in node_list:
        f.write('"{0}" -> "{1}";\n'.format(nodes[0], nodes[1]))
    f.write("}\n")
