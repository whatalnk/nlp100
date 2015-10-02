import sys
lines = [line.rstrip("\n") for line in sys.stdin]
for line in lines:
    print(line.replace("\t", " "))