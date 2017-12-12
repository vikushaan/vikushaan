search = []

wordList = []
senseList = []
exampleList = []

while True:
    inp = input('Введите слово: ')
    if (inp != ''):
        search.append(inp)
    else:
        break;

with open ("/Users/victoriagevorkyan/Desktop/Ozhegov.txt", encoding="utf-8") as f:
    for line in f:
        tmp = line

        # Слово
        d = tmp.find('|')
        word = tmp[0:d].strip()
        tmp = tmp[d+1:]

        # Определение
        d = tmp.find('|')
        sense = tmp[:d].strip()
        tmp = tmp[d+1:]

        # Антоним
        d = tmp.find('|')
        ant = tmp[:d].strip()
        tmp = tmp[d+1:]

        # Пример
        d = tmp.find('|')
        example = tmp[:d].strip()
        tmp = tmp[d+1:]

        # Избавимся от лишних символов
        # Из особых символов может быть '...','.' в конце и '-' в конце/в начале
        ind = word.find('-')
        if (ind == 0):
            word = word[ind + 1 :]
        elif (ind == len(word)-1):
            word = word[:ind]
        if (word.count('...') != 0):
            word = word[:word.find('...')]
        if (word.count('.') != 0):
            word = word[:word.find('.')]

        wordList.append(word)
        senseList.append(sense)
        exampleList.append(example)

    print()
    for word in search:
        wordFound = False
        print('Слово "' + word + '"')
        for i in range(len(wordList)):
            # Если слово для поиска строго равно слову в словаре
            if (word.upper() == wordList[i].upper()):
                wordFound = True
                print('Совпадение в словаре: ' + wordList[i])
                print('Пример употребления: ' + exampleList[i])
                print('Определение: ' + senseList[i])
                print()
        if (wordFound == False):
            print('Значения для слова "' + word + '" не найдено.')
        print()
