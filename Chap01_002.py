def concat_s1_s2(s1, s2):
  res = ""
  for (i, j) in zip(s1, s2):
    res += i+j
  return res

s1 = "パトカー"
s2 = "タクシー"
print(concat_s1_s2(s1, s2))