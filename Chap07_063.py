# coding:utf-8
import sys
import os.path
import gzip
import json
import redis
import msgpack

db = redis.Redis(host='localhost', port=6379, db=1)

with gzip.open(os.path.normpath('data/artist.json.gz'), 'rt', encoding='utf-8') as f:
    for line in f.readlines():
        d = json.loads(line)
        name = d["name"]
        if "tags" in d.keys():
            tags = msgpack.packb(d["tags"])
        else:
            tags = msgpack.packb([])
        db.set(name, tags)


# tags = db.unpackb(db.get(name), encoding="utf-8")
# for tag in tags:
#     print(tag["value"], tag["count"])
