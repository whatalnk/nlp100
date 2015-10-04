from Chap04_030 import parse_mecab_output
from Chap04_036 import get_word_freqency
import os.path
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fpJ = FontProperties(fname=r'C:\WINDOWS\Fonts\ipaexg.ttf', size=14)
fpE = FontProperties(fname=r'C:\WINDOWS\Fonts\arial.ttf', size=14)

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

dic_freq = get_word_freqency(neko)

x = list(dic_freq.values())

plt.hist(x)
plt.xticks(fontproperties=fpE)
plt.yticks(fontproperties=fpE)
plt.xlabel("Frequency", fontproperties=fpE)
plt.ylabel("Number of words", fontproperties=fpE)
# plt.show()
plt.savefig(os.path.normcase("output/Chapter4/fig_038.png"))
