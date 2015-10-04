# coding: utf-8
import os.path

def parse_mecab_output(f):
    with open(os.path.normcase(f), "r", encoding='utf-8') as f:
        lines = f.readlines()

    dic_list = []
    for l in lines:
        ll = l.rstrip("\n")
        if ll != "EOS":
            out1 = ll.split("\t")
            out2 = out1[1].split(",")
            dic = {'surface': out1[0], 'base': out2[6], 'pos': out2[0], 'pos1': out2[1]}
            dic_list.append(dic)
    return dic_list

if __name__ == '__main__':
    print(parse_mecab_output("output/Chapter4/neko.txt.mecab")[0:10])