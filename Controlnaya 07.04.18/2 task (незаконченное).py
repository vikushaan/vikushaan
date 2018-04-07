
import re

def open_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def get_dict(m):
    grkeys = re.findall(r'gr="(.*)"', m)
    d = {}
    for i in grkeys:
        d[i] = m.count(i)
    return d

xml = open_file('mystem.xml')
d = get_dict(xml)

Я не знаю что дальше, не получается :(
