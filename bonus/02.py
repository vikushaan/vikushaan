s = input('Введите градусы Цельсия: ')
if s != '':
    t = float(s)
    print(t, 'градусов по Цельсию составляют', round((9/5 * t + 32), 2), 'градусов по Фаренгейту')
    print(t, 'градусов по Цельсию составляют', round((t + 273.15), 2), 'градусов по Кельвину')
else:
    print('Значение температуры не было введено!')
input('Введите любую клавишу, чтобы продолжить... ')