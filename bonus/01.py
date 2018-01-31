num = input('Введите число: ')
k = 0
s = 0
if len(num) > 0:
    max_val = float(num)
    min_val = float(num)
    while len(num) > 0:
        k += 1
        a = float(num)
        s += a
        if a > max_val:
            max_val = a
        if a < min_val:
            min_val = a
        num = input('Введите число: ')
    print('Среднее арифметическое значение: ', s / k)   
    print('Минимальное среди введенных чисел: ', min_val)
    print('Максимальное среди введенных чисел: ', max_val)
else:
    print('Числа не были введены...')
input('Введите любую клавишу, чтобы продолжить...')

