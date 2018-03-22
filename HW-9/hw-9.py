import re

def open_file(filename):
    words = []
    with open (filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        for i in range(len(words)):
            words[i] = words[i].strip('.,:;!''?-""1234567890*()«»')
    return words

def get_verbs(filename):
    verbs = []
    text = open_file(filename)
    for word in text:
        if re.search(r"""\bвып((ил[аио]?)               # выпил; выпила; выпило; выпили
                           |(ь(ю|ют|е(шь|т|м|те|мте)))  # выпью; выпьют; выпьешь; выпьет; выпьем; выпьете; выпьемте
                           |(ей(те)?)                   # выпей; выпейте
                           |(ит(((ь|а|о|ы)?)            # выпит; выпить; выпита; выпито; выпиты
                           (ая|о(е|й|ю|м|му|го)         # выпитая; выпитое; выпитой; выпитою; выпитом; выпитому; выпитого 
                           |ы(й|х|м|ми|е)|ую)?))        # выпитый; выпитых; выпитым; выпитыми; выпитые; выпитую
                           |(ив(ши(й|е|х|м|ми)?         # выпив; выпивши; выпивший; выпившие; выпивших; выпившим; выпившими 
                           |ше(го|му|м|й|ю|е)           # выпившего; выпившему; выпившем; выпившей; выпившею; выпившее  
                           |шую|шая)?))                 # выпившую; выпившая   
                           \b""", word, re.X):
            if word not in verbs:
                verbs.append(word)
    return verbs

v = get_verbs('verbs.txt')
print(*v, sep = '\n')
input('Введите любую клавишу, чтобы продолжить... ')
