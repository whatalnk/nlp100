# coding: utf-8
from Chap03_025 import extract_country_data
import io
import sys
import re

dic_country_data = extract_country_data()
def remove_emph(dic):
    re_emph = re.compile(r"(?P<rec>'{2,5})(.+)(?P=rec)")
    for k, v in dic.items():
        m = re.search(re_emph, v)
        if m:
            dic[k] = re_emph.sub(r"\2", v)
    return dic

if __name__ == '__main__':
    dic_emph_removed = remove_emph(dic_country_data)
    for k, v in dic_emph_removed.items():
        print(k, ": ", v)