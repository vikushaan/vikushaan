import os

def get_freq_dict():
    start_with = {}
    for root, dirs, files in os.walk('.'):
        for dname in dirs:
            f_char = dname[0]
            start_with[f_char] = start_with.get(f_char, 0) + 1
    return start_with

d = get_freq_dict()
if d: print(max(d, key = d.get))
else: print('Дерево не содержит папок!')
input('Введите любую клавишу, чтобы продолжить. . . ')
