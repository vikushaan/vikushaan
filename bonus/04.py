word = input('Введите слово или фразу на русском: ')
new_word = ''

for ch in word: 
    new_word += ch
    if ch in 'аеёиоуыэюя':
        new_word += 'с' + ch
    if ch in 'АЕЁИОУЫЭЮЯ':
        new_word += 'С' + ch
        
print ('Перевод введенного текста на кирпичный язык: ', new_word)
input('Введите любую клавишу, чтобы продолжить... ')
