# coding: utf-8
from Chap03_020 import load_wiki_data
import io
import sys
import re
import regex
# from collections import OrderedDict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extract_country_data():
    re_curly_brackets = r"(?<rec>\{\{(?:[^{}]+|(?&rec))*\}\})"
    country_data = [data for data in regex.findall(re_curly_brackets,load_wiki_data(), regex.VERBOSE) if re.match(r"^\{\{基礎情報 国", data)][0].split("\n")[1:-1]
#    dic_country_data = OrderedDict()
    dic_country_data = {}
    for e in country_data:
        m = re.match(r"^\|(.+) \= (.+)", e)
        if m:
            current_key = m.group(1)
            dic_country_data[current_key] = m.group(2)
        else:
            dic_country_data[current_key] += "\n"+e
    return dic_country_data

if __name__ == '__main__':
    dic_country_data = extract_country_data()
    for k, v in dic_country_data.items():
        print(k, "-->", v)

# regex が漢字にマッチしなかった
# [Pythonの正規表現で入れ子括弧内をうまくマッチさせる方法 | NKNK](http://blog.ni-ken.net/2015/04/python-regex-tips/)
