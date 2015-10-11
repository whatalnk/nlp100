# coding:utf-8
import sys
import os.path
import gzip
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artists
collection = db.tags

info_japan = collection.find({"area":"Japan"})
print(info_oasis.count()) # 22886
