# encoding:utf-8
import io
import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 10
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
lines = [line.rstrip() for line in input_stream]
for line in lines[-n:]:
    print(line)
