from Chap04_030 import parse_mecab_output

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

nouns = [i['base'] for i in neko if i['pos'] == "名詞" and i['pos1'] == "サ変接続"]
print(len(set(nouns)))