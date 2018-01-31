def pig_latin(s):
    new_word = s
    if len(s) > 0 and s.isalpha():
        word = s.lower()
        if word[0] in 'aeiou':
            new_word = word + 'ay'
        else:
            part = ''
            k = 0
            for i in word:
                if i not in 'aeiou':
                    part += i
                    k += 1
                else: break
            new_word = word[k:] + part + 'ay'
    return new_word
    
text = input('Введите слово или фразу: ')
phrase = text.split(' ')
for w in phrase:
    print(pig_latin(w), end = ' ')
input('Введите любую клавишу, чтобы продолжить... ')
