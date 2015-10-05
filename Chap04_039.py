from Chap04_030 import parse_mecab_output
from Chap04_036 import get_word_freqency
import os.path
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

fpJ = FontProperties(fname=r'C:\WINDOWS\Fonts\ipaexg.ttf', size=14)
fpE = FontProperties(fname=r'C:\WINDOWS\Fonts\arial.ttf', size=14)

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

dic_freq = get_word_freqency(neko)

y = sorted(list(dic_freq.values()), reverse=True)
# x = range(1, len(y)+1)
x = pd.Series(y).rank(ascending=False)

plt.plot(x, y)
plt.xscale("log")
plt.yscale("log")
plt.xticks(fontproperties=fpE)
plt.yticks(fontproperties=fpE)
plt.xlabel("Rank", fontproperties=fpE)
plt.ylabel("Frequency", fontproperties=fpE)
# plt.show()
# plt.savefig(os.path.normcase("output/Chapter4/fig_039.png")) # range()
plt.savefig(os.path.normcase("output/Chapter4/fig_039-2.png")) # pd.Seriese.rank()
