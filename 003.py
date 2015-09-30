def get_pi(s):
  l = s.replace(",", "").replace(".", "").split(" ")
  return [len(i) for i in l]
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(get_pi(s))