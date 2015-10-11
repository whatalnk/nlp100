# coding:utf-8
import sys
import os.path
import gzip
import json
from pymongo import MongoClient, IndexModel


# client > artists > tags > ...
client = MongoClient('localhost', 27017)
db = client.artists
collection = db.tags

with gzip.open(os.path.normpath('data/artist.json.gz'), 'rt', encoding='utf-8') as f:
    for line in f.readlines():
        d = json.loads(line)
        collection.insert_one(d)

i_name = IndexModel("name")
i_aliases_name = IndexModel("aliases.name")
i_tags_value = IndexModel("tags.value")
i_rating_value = IndexModel("rating.value")

collection.create_indexes([i_name, i_aliases_name, i_tags_value, i_rating_value])
