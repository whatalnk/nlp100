from Chap03_020 import load_wiki_data
import re

def extract_category():
    re_category = re.compile(r'\[\[Category:.+\]\]')
    res = []
    for line in load_wiki_data().split("\n"):
        m = re.match(re_category, line)
        if m:
            res.append(line)
    return res

if __name__ == '__main__':
    for l in extract_category():
        print(l)
