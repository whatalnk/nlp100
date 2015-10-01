def cipher(s):
    res = []
    alphabets = list(map(chr, range(ord("a"), ord("z")+1)))
    for i in s:
        if i in alphabets:
            res.append(chr(219 - ord(i)))
        else:
            res.append(i)
    return "".join(res)

if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    s1 = cipher(s)
    s2 = cipher(s1)
    print(s1)
    print(s == s2)


