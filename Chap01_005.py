def ngram(s, n):
    res = []
    for i in range(len(s) - n + 1):
        res.append(s[i:i+2])
    return res

if __name__ == '__main__':
    s = "I am an NLPer"
    w = s.split(" ")
    print(ngram(w, 2))
    print(ngram(s, 2))