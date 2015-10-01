import random
def typoglycemia(s):
    words = s.split(" ")
    res = []
    for word in words:
        if len(word) <= 4:
            res.append(word)
        else:
            new_word = word[0] + "".join(random.sample(word[1:-1], len(word)-2)) + word[-1]
            res.append(new_word)
    return " ".join(res)


if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(s))