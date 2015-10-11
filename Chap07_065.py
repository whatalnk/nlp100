# coding:utf-8
import sys
import os.path
import gzip
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artists
collection = db.tags

info_oasis = collection.find({"name":"Oasis"})
# print(info_oasis.count()) # 3
for i in info_oasis:
  print(i)
