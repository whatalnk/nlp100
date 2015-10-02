# encoding:utf-8
import io
import sys

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
lines = [line.rstrip() for line in input_stream]
col1 = [line.split("\t")[0] for line in lines]
print(set(col1))
