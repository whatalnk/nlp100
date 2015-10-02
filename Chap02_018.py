# encoding:utf-8
import io
import sys

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
lines = [line.rstrip().split("\t") for line in input_stream]
lines_sorted = sorted(lines, key=lambda x:x[2])
for line in lines_sorted:
    print("\t".join(line))