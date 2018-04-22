import os
import re

count = 0
unique_dirs = []
unique_files = []

for root, dirs, files in os.walk('.'):
    for directory in dirs:
        if directory not in unique_dirs:
            unique_dirs.append(directory)

    for file in files:
        if file not in unique_files:
            unique_files.append(file)
        if re.search(r'^[a-zA-Z]+$', os.path.splitext(file)[0]):
            count += 1

print('Список найденных папок: ')
print(*unique_dirs, sep = '\n')
print('\nСписок найденных файлов: ')
print(*unique_files, sep = '\n')
print('\nКоличество найденных по условию задачи файлов:', count)
input('Введите любую клавишу, чтобы продолжить. . . ')
