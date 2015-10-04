from Chap04_030 import parse_mecab_output

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

def get_word_freqency(f):
    dic_freq = {}
    for i in neko:
        if i['surface'] in dic_freq:
            dic_freq[i['surface']] += 1
        else:
            dic_freq[i['surface']] = 1
    return dic_freq

if __name__ == '__main__':
    dic_freq = get_word_freqency(neko)
    diq_freq_sorted = sorted(dic_freq.items(), key=lambda x:x[1], reverse=True)
    for i in diq_freq_sorted:
        print(i)