from Chap03_020 import load_wiki_data
import re


re_section = re.compile(r"(^\=+)(.+?)(\=+\=$)")
for line in load_wiki_data().split("\n"):
    m = re.match(re_section, line)
    if m:
        section_title = m.group(2)
        section_level = len(m.group(1))-1
        print("{0}: {1}".format(section_level, section_title))