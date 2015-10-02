from Chap03_020 import load_wiki_data
import re


re_media = re.compile(r"(ファイル|File):(.+?)\|", re.I)
for line in load_wiki_data().split("\n"):
    m = re.search(re_media, line)
    if m:
        print(m.group(2))
