# coding=utf-8

import re

def open_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def get_chars_between_body(m):
    s = re.search(r'<body>([\s\S]*?)</body>', m)
    st = ''.join(s.group(1))
    return st

xml = open_file('mystem.xml')
info = get_chars_between_body(xml)
with open('count.txt', 'w', encoding = 'utf-8') as f:
    f.write('количество символов внутри тега body = ' + str(len(info)))
print('количество символов внутри тега body = ' + str(len(info)))
input('Для продолжения введите любую клавишу. . .')
