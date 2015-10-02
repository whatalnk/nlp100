import os.path
import sys
with open(os.path.normcase(sys.argv[1]), "r", encoding='utf-8') as f:
    col1 = [line.strip("\n") for line in f.readlines()]
with open(os.path.normcase(sys.argv[2]), "r", encoding='utf-8') as f:
    col2 = [line.strip("\n") for line in f.readlines()]

for(c1, c2) in zip(col1, col2):
    print("\t".join([c1, c2]))

