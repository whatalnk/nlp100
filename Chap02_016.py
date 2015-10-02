# encoding:utf-8
import io
import sys

n = int(sys.argv[1])

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
lines = [line.rstrip() for line in input_stream]
n_lines = len(lines)
if n > n_lines:
    files = lines
else:
    files = []
    for i in range(n_lines // n):
        s = i*n
        e = (i+1)*n
        files.append(lines[s:e])
    files.append(lines[-(n_lines % n):])

i = 1
for f in files:
    f_name = "file" + str(i) + ".txt"
    with open(f_name, "w", encoding='utf-8') as ff:
        for l in f:
            ff.write(l + "\n") 
    i += 1
