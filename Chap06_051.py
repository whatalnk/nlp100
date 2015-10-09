import os.path


with open(os.path.normcase("output/Chapter6/_050.txt"), "r", encoding="utf-8") as f:
    for line in f.readlines():
        words = line.rstrip("\n").split(" ")
        for word in words:
            print(word)
        if words[-1] != "":
            print()
