# coding:utf-8
import sys
import os.path
import gzip
import json
import redis

db = redis.Redis(host='localhost', port=6379, db=0)

res = 0
for name in db.keys():
    area = db.get(name)
    if area == "Japan":
        res += 1

print(res)