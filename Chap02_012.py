import sys
lines = [line.rstrip("\n") for line in sys.stdin]
n = int(sys.argv[1])
for line in lines:
    print(line.split("\t")[n - 1])