count = 0
antList = []

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

        if (ant != ''):
            count += 1
            antList.append(ant)

print('Кол-во антонимов: ' + str(count))
print(antList)
