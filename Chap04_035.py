from Chap04_030 import parse_mecab_output

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

list_noun_seq = []
noun_seq = []
for i in neko:
    if i['pos'] == "名詞":
        noun_seq.append(i['surface'])
    else:
        if len(noun_seq) > 1:
            list_noun_seq.append(noun_seq)
        noun_seq = []

for i in list_noun_seq:
    print("".join(i))