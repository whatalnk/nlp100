# coding:utf-8
import sys
import os.path
import gzip
import json
from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient('localhost', 27017)
db = client.artists
collection = db.tags
info_tags_dance = collection.find({"tags.value": "dance"})
print("Name\tRating\tCount")
for i in info_tags_dance.sort("rating.value", DESCENDING).limit(10):
    name = i["name"]
    rating = i["rating"]["value"]
    count = i["rating"]["count"]
    print("{}\t{}\t{}".format(name, rating, count))
