from Chap01_005 import ngram

x = set(ngram("paraparaparadise", 2))
y = set(ngram("paragraph", 2))

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print("se" in x)
print("se" in y)