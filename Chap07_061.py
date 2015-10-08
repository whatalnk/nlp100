# coding:utf-8
import sys
import os.path
import gzip
import json
import redis

db = redis.Redis(host='localhost', port=6379, db=0)

def get_area(name):
    return db.get(name).decode('utf-8')

if __name__ == '__main__':
    name = sys.argv[1]
    print(get_area(name))