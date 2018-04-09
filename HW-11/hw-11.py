
import re

def open_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def change_article(s):
    s1 = re.sub('философи(я|и|й|ю|ей|ях|ям|ами)?([^а-я])', 'астрологи\\1\\2', s)
    s2 = re.sub('Философи(я|и|й|ю|ей|ях|ям|ами)?([^а-я])', 'Астрологи\\1\\2', s1)
    return s2

html = open_file('philosophy.txt')
info = change_article(html)
with open('astrology.txt', 'w', encoding = 'utf-8') as f:
    f.write(info)
print(info)
input('Для продолжения введите любую клавишу. . .')
