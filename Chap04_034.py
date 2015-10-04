from Chap04_030 import parse_mecab_output

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

list_noun_no_noun = []
for i in range(len(neko)-2):
    if neko[i]['pos'] == "名詞" and neko[i+1]['surface'] == "の" and neko[i+2]['pos'] == "名詞":
        noun_no_noun = neko[i]['surface'] + "の" + neko[i+2]['surface']
        list_noun_no_noun.append(noun_no_noun)

for i in list_noun_no_noun:
    print(i)
