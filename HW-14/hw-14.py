def split_sentence(s):
    return [w.strip('«"\',;:-»') for w in s.split() if w.strip('«"\',;:-»') != '']

f = open('text.txt', 'r', encoding = 'utf-8')
text = ''.join(f.readlines())
f.close()
clean_text = text.replace('\n', '').replace('!', '.').replace('?','.').split('.')
sentences = {s: {w:len(w) for w in split_sentence(s)} for s in clean_text}
for k, v in sentences.items():
    print('\nПредложение: \'{0}\'\nдлины слов: {1}\n'.format(k.lstrip(), v))
input('Введите любую клавишу, чтобы продолжить. . . ')
