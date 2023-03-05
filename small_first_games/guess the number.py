from random import randint

lowDigit = 1
highDigit = 100
digit = 0
countInput = 0
win = False
playGame = True
x = 0
startScore = 100
score = 0
maxScore = 0


while playGame:
    digit = randint(lowDigit, highDigit)
    print("-" * 30)
    countInput = 0
    score = startScore
    print("Компьютер загадал число от 1 до 100, попробуй отгадать!")
    while not win and score > 0:
        print("-" * 30)
        print(f"заработано очков: {score}")
        print(f"Рекорд: {maxScore}")

        x = ""
        while not x.isdigit():
            x = input(f"Введите число от {lowDigit} до {highDigit}: ")
            if not x.isdigit():
                print("." * 27 + " Введите, пожалуйста, число.")
        x = int(x)

        if x == digit:
            win = True
        elif x > 100 or x < 0:
            print('Ошибка: нужно вводить числа от 0 до 100.')
        else:
            length = abs(x-digit)
            if length < 3:
                print("Очень горячо!")
            elif length < 5:
                print("Горячо!")
            elif length < 10:
                print("Тепло!")
            elif length < 15:
                print("Прохладно")
            elif length < 20:
                print("Холодно")
            else:
                print("Слишком холодно")
            if countInput == 7:
                score -= 10
                if digit % 2 == 0:
                    print("Число чётное")
                else:
                    print("Число нечётное")
            elif countInput == 6:
                score -= 8
                if digit % 3 == 0:
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif countInput == 5:
                score -= 4
                if digit % 4 == 0:
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif 2 < countInput < 5:
                score -= 2
                if x > digit:
                    print("Загаданное число меньше вашего")
                else:
                    print("Загаданное число больше вашего")
            score -= 5
        countInput += 1
    print("*" * 40)
    if x == digit:
        print("Победа! Поздравляю!")
    else:
        print("Ой, у вас закончились очки. Вы проиграли :(")

    if input("Enter - сыграть ещё, 0 - выход") == "0":
        playGame = False
    else:
        win = False

    if score > maxScore:
        maxScore = score
print("*" * 40)
print("""Спасибо, что сыграли в мою игру!
Возвращайтесь скорей! Буду ждать с нетерпением!
""")

