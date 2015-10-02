# encoding:utf-8
import io
import sys

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
lines = [line.rstrip().split("\t") for line in input_stream]
dic = {}
for line in lines:
    col1 = line[0]
    if col1 in dic:
        dic[col1] += 1
    else:
        dic[col1] = 1
for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
    print(v, k)