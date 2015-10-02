# coding:utf-8
import os.path
import gzip
import json

def load_wiki_data():
    with gzip.open(os.path.normpath('data/jawiki-country.json.gz'), 'rt', encoding='utf-8') as f:
        for line in f.readlines():
            d = json.loads(line)
            if d['title'] == "イギリス":
                return d['text']

