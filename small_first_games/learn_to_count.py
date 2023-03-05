from random import randint

lowDiapazon = 10
highDiapazon = 1000
sign = 0  # знак
playGame = True
count = 0  # количество примеров
right = 0  # количество правильных ответов
score = 0
x, y, z = 0, 0, 0
znak = ''

while playGame:
    print("""Компьютер составляет пример. Введите ответ.
    Для завершения работы нажмите STOP""")
    print("*" * 40)
    print(f"Ваши очки: {score}")
    print(f"Обработано задач: {count}")
    print(f"Правильных ответов: {right}")
    print("*" * 20)
    sign = randint(0, 3)
    if sign == 0:
        znak = '+'
    elif sign == 1:
        znak = '-'
    elif sign == 2:
        znak = '*'
    elif sign == 3:
        znak = '/'

    # сложение
    if sign == 0:
        z = randint(lowDiapazon, highDiapazon)
        x = randint(lowDiapazon, z)
        y = z - x

        if randint(0, 1) == 0:
            print(f'{x} + {y} = ?')
        else:
            print(f'{y} + {x} = ?')
    elif sign == 1:
        # вычитание
        x = randint(lowDiapazon, highDiapazon)
        y = randint(0, x - lowDiapazon)

        z = x - y
        print(f'{x} - {y} = ?')
    elif sign == 2:
        # умножение

        x = randint(1, (highDiapazon - lowDiapazon) // 10 + 1)
        y = randint(lowDiapazon, highDiapazon) // x

        z = x * y
        print(f'{x} * {y} = ?')
    elif sign == 3:
        # деление

        x = randint(1, (highDiapazon - lowDiapazon) // 20 + 1)
        y = randint(lowDiapazon, highDiapazon) // x
        if y == 0:
            y = 1

        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")

    user = ''
    while not user.isdigit() and user.upper() != "STOP" and user.upper() != "ЫЕЩЗ":
        user = input("Ваш ответ?")
        while not user.isdigit() and user.upper() != "STOP" and user.upper() != "ЫЕЩЗ" and user.upper() != "HELP" and user.upper() != "РУДЗ":
            user = input("Нужно писать либо числа, либо 'STOP', либо 'HELP'")
        if user.upper() == "HELP" or user.upper() == "РУДЗ":
            if z > 9:
                print(f"Последняя цифра ответа: {z % 10}")
            else:
                print(f"Ответ состоит из одной цифры, подсказка невозможна")
            score -= 10
        elif user.upper() == "STOP" or user.upper() == "ЫЕЩЗ":
            playGame = False
        else:
            count += 1
            if int(user) == z:
                print(f'\nПравильно!\n')
                right += 1
                score += 10
            else:
                print(f'\n Ответ неправильный... Правильно {z}')
                print(f"Вы можете ввести команду HELP, чтобы увидеть последнюю цифру ответа(-10 очков)\n")
                score -= 20
print("*" * 45)
print("СТАТИСТИКА ИГРЫ")
print(f'Всего примеров: {count}')
print(f"Правильных ответов: {right}")
print(f"Неправильных ответов: {count - right}")
if count > 0:
    print(f"Процент правильных ответов: {int(right / count * 100)}%")
else:
    print(f"Процент правильных ответов: 0%")
