def number_translation():
    number = int(input('Введите число: '))
    system = int(input('Введите систему счисления: '))
    result = ' '
    if system == 2:
        while number > 0:
            result = str(number%2) + result
            number = number // 2
        print('Результат: ',result)
    elif system == 8:
        while number > 0:
            result = str(number % 8) + result
            number = number // 8
        print('Результат: ',result)
    else:
        print('Данные некорректны, введите систему счисления 2 или 8 ')
number_translation()
