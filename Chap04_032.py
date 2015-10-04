from Chap04_030 import parse_mecab_output
from Chap04_031 import extract_verbs

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

if __name__ == '__main__':
    verbs = extract_verbs(neko)
    print(set([i['base'] for i in verbs]))