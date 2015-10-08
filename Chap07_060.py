# coding:utf-8
import sys
import os.path
import gzip
import json
import redis

db = redis.Redis(host='localhost', port=6379, db=0)

with gzip.open(os.path.normpath('data/artist.json.gz'), 'rt', encoding='utf-8') as f:
    for line in f.readlines():
        d = json.loads(line)
        name = d["name"]
        if "area" in d.keys():
            area = d["area"]
        else:
            area = ""
        db.set(name, area)

