word = input('Введите английское слово или фразу: ')
new_word = ''

for ch in word: 
    new_word += ch
    if ch in 'bcdfghjklmnpqrstvwxz' or ch in 'BCDFGHJKLMNPQRSTVWXZ':
        new_word += 'aig'
        
print ('Перевод на Aigy Paigy: ', new_word)
input('Введите любую клавишу, чтобы продолжить... ')
