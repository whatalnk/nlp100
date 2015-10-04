from Chap04_030 import parse_mecab_output

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

def extract_verbs(f):
    return [i for i in f if i['pos'] == "動詞"]

if __name__ == '__main__':
    verbs = extract_verbs(neko)
    print(set([v['surfaces'] for v in verbs]))