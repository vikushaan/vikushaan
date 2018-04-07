
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
# для проверки:
#for k, v in d.items():
#    print('Ключ: ', k, '; Значение: ', v)
s_keys = sorted(d.items(), key=lambda x: x[1])
with open('gr.txt', 'w', encoding = 'utf-8') as f:
    for i in s_keys[::-1]:
        print(i[0])
        f.write(i[0] + '\n')
input('Для продолжения введите любую клавишу. . .')
