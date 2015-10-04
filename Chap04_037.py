from Chap04_030 import parse_mecab_output
from Chap04_036 import get_word_freqency
import os.path
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fpJ = FontProperties(fname=r'C:\WINDOWS\Fonts\ipaexg.ttf', size=14)
fpE = FontProperties(fname=r'C:\WINDOWS\Fonts\arial.ttf', size=14)

neko = parse_mecab_output("output/Chapter4/neko.txt.mecab")

dic_freq = get_word_freqency(neko)

diq_freq_sorted = sorted(dic_freq.items(), key=lambda x:x[1], reverse=True)[0:10]

x = range(1, 11)
x_label = [i[0] for i in diq_freq_sorted]
y = [i[1] for i in diq_freq_sorted]

plt.bar(x, y, align="center")
plt.xticks(x, x_label, fontproperties=fpJ)
plt.yticks(fontproperties=fpE)
plt.xlabel("Word", fontproperties=fpE)
plt.ylabel("Frequency", fontproperties=fpE)
plt.savefig(os.path.normcase("output/Chapter4/fig_037.png"))
