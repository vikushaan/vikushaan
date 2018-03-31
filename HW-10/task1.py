# coding=utf-8

import re

def open_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def get_research_field(m):
    s = re.search(r'Научная сфера[\s\S]*?title="(.*)"', m)
    st = ''.join(s.group(1))
    return st

html = open_file('einstein.html')
info = get_research_field(html)
with open('einstein.txt', 'w', encoding = 'utf-8') as f:
    f.write(info)
print(info)
input('Для продолжения введите любую клавишу. . .')
