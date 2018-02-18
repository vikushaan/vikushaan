def read_words():
    dic = {}
    with open('words.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            words = line.strip().split()
            dic[words[0]] = words[1]
    return dic

d = read_words()
guessed = 0
for k, v in d.items():
    l = ['.' for i in range(len(v))]
    print('Угадайте слово по подсказке: ', k, end = ' ')
    print(*l, sep = '')
    if input().lower() == v:
        print('Вы выиграли!')
        guessed += 1
    else:
        print('Вы проиграли!')
    print()
percent = guessed / len(d.items()) * 100
print('Угаданных слов: {0:.0f}%'.format(percent))
input('Введите любую клавишу, чтобы продолжить... ')

