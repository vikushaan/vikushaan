with open ("/Users/victoriagevorkyan/Desktop/Ozhegov.txt", encoding="utf-8") as f:
    for line in f:

        d = line.find('|')
        word = line[0:d].strip()


        ind = word.find('-')
        if (ind == 0):
            word = word[ind + 1 :]
        elif (ind == len(word)-1):
            word = word[:ind]
        if (word.count('...') != 0):
            word = word[:word.find('...')]
        if (word.count('.') != 0):
            word = word[:word.find('.')]

        if (len(word) >= 20):
            print(line)
