from Chap03_021 import extract_category
import re

categories = extract_category()
re_category_content = re.compile(r'\[\[Category:(.+)\]\]')
for line in categories:
    m = re.match(re_category_content, line)
    if m:
        print(m.group(1))
