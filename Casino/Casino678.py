from random import randint
import time

valuta = '₽'
money = 0
startMoney = 0
defaultMoney = 10000
playGame = True

COLORS = {"white": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35, "cyan": 36, "lightgray": 37,
          "darkgray": 90, "lightred": 91, "lightgreen": 92,
          "lightyellow": 93, "lightblue": 94, "lightmagenta": 95, "lightcyan": 96}


# функция изменения цвета
def color(c):
    c = COLORS[c]
    print(f"\033[{c}m")


# Вывод на экран цветного, обрамлённого звёздочками текста
def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))


# Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color("white")
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("    Введи целое число!")
    return ret


# Функция ввода значения
def getInput(digit, message):
    color("white")
    ret = ""
    while ret == "" or not ret in digit:
        ret = input(message)
    return ret


# Вывод сообщения о выигрыше
def win(result):
    color("yellow")
    print(f"    Победа за тобой! Выигрыш составил: {result}{valuta}")
    print(f"    У тебя на счету: {money}")


# Вывод сообщения о проигрыше
def lose(result):
    color("red")
    print(f"    К сожалению, проигрыш: {result}{valuta}")
    print(f"    У тебя на счету: {money}")
    print("    Обязательно нужно отыграться!")


# Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open('money.dat', "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney}{valuta}")
        m = defaultMoney
    return m


# Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except FileNotFoundError:
        print("Ошибка создания файла, наше Казино закрывается")
        quit(0)


# функция получения случайного числа и отображение рулетки
def getRoulette(visible):
    tickTime = randint(100, 200) / 10000
    mainTime = 0
    number = randint(0, 38)
    increaseTickTime = randint(100, 110) / 100
    # i = randint(30, 38)
    i = 30
    while mainTime < 0.7:
        if i > 95:
            i = 30
        elif 37 < i < 90:
            i = 90

        mainTime += tickTime
        tickTime *= increaseTickTime
        print(f"\033[{i}m")
        number += 1
        i += 1
        if number > 38:
            number = 0
            print()
        printNumber = number

        if number == 37:
            printNumber = "00"
        elif number == 38:
            printNumber = "000"

        print(" Число >",
              printNumber,
              "*" * number,
              " " * (78 - number * 2),
              "*" * number)

        if visible:
            time.sleep(mainTime)

    return number


# Начало рулетки
def roulette():
    global money
    playGame = True

    while playGame and money > 0:
        colorLine("cyan", "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ")
        color("lightmagenta")
        print(f"\n У тебя на счету {money}{valuta} \n")
        color("lightgreen")
        print(" Ставлю на...")
        print("    1. Чётное (выигрыш 1:1)")
        print("    2. Нечётное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        x = getInput("01234", "    Твой выбор?")

        playRoulette = True
        if x == "3":
            color("lightgreen")
            print()
            print(" Выбери числа...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")

            duzhina = getInput("1230", "    Твой выбор?")
            if duzhina == "1":
                textDuzhina = "От 1 до 12"
            elif duzhina == "2":
                textDuzhina = "От 13 до 24"
            elif duzhina == "3":
                textDuzhina = "От 25 до 36"
            elif duzhina == "0":
                playRoulette = False
        elif x == "4":
            chislo = getIntInput(0, 36, "    На какое число стваишь? (0..36):")

        color('white')
        if x == "0":
            return 0

        if playRoulette:
            loadMoney()
            stavka = getIntInput(0, money, f"    Сколько поставишь? (не больше {money}{valuta}): ")
            if stavka == 0:
                return 0
            number = getRoulette(True)

            print()
            color("cyan")

            if number < 37:
                print(f"    Выпало число {number}! " + "*" * number)
            else:
                if number == 37:
                    printNumber = '00'
                elif number == 38:
                    printNumber = '000'
                print(f"    Выпало число {printNumber}!")

            if x == "1":
                print("    Ты ставил на ЧЁТНОЕ!")
                if number < 37 and number % 2 == 0:
                    money += stavka
                    win(stavka)
                else:
                    money -= stavka
                    lose(stavka)
            elif x == "2":
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if number < 37 and number % 2 == 1:
                    money += stavka
                    win(stavka)
                else:
                    money -= stavka
                    lose(stavka)
            elif x == "3":
                print(f"    Ставка сделана на диапазон числе {textDuzhina}")
                winDuzhina = ""
                if 0 < number < 13:
                    winDuzhina = "1"
                elif 12 < number < 25:
                    winDuzhina = "2"
                elif 24 < number < 37:
                    winDuzhina = "3"

                if winDuzhina == duzhina:
                    money += stavka * 2
                    win(stavka * 3)
                else:
                    money -= stavka
                    lose(stavka)
            elif x == "4":
                print(f"    Ставка сделана на число {chislo}")
                if number == chislo:
                    money += stavka * 35
                    win(stavka * 36)
                else:
                    money -= stavka
                    lose(stavka)
            saveMoney(money)
            color("lightyellow")
            print()
            input("\nНажми Enter, чтобы продолжить...")


# Анимация костей
def getDice():
    count = randint(3, 8)
    sleep = 0
    i = randint(30, 38)
    while count > 0:
        if i > 95:
            i = randint(30, 38)
        elif 37 < i < 90:
            i = randint(90, 95)
        print(f"\033[{i}m")
        i += 1
        x = randint(1, 6)
        y = randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y


# Кости
def dice():
    global money
    playGame = True

    while playGame:
        print()
        colorLine("lightred", "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color("lightmagenta")
        print(f"\n У тебя на счету {money}{valuta} \n")
        color("lightyellow")
        print(" Правила игры: ")
        print("    1. Делаешь ставку. Выигрыш 1/5 от суммы, проигрыш - вся сумма целиком ")
        print("    2. Стартовый раунд: выбрасываются 2 кубика. Делаешь прогноз на следующий ход.")
        print("    3. Если уходишь на 1 этапе, спишется сумма ставки. После 1 раунда можно забирать свои деньги.")
        print("    4. Каждая победа дает + 1/5 от ставки.")
        print("""    5. Пример игры: 
                        Ставим 500 руб. 
                        Выпадает 2:3. 
                        Делаем прогноз 'больше'. 
                        Выпадает 6:1.
                        Выигрываем 100 руб.
                        Прогнозируем 'меньше' 
                        Выпадает 1:1.
                        Выигрываем 120 рублей(1/5 от 600 руб. 
                        Можем забрать 700 руб.""")
        print("    0. Ставка 0 для завершения игры. \n")
        color("white")
        stavka = getIntInput(0, money, f"    Сделай ставку в пределах {money}{valuta}:")
        if stavka == 0:
            return 0

        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while playRound and stavka > 0 and money > 0:
            loadMoney()
            if stavka > money:
                stavka = money
            color("lightyellow")
            print(f"\n    В твоём распоряжении {stavka}{valuta}")
            color("red")
            print(f"\n    Текущая сумма чисел на костях: {oldResult}")
            color("lightgreen")
            print("\n Сумма чисел на гранях будет больше, меньше или равно предыдущей?")
            color("white")
            x = getInput("0123", "    Введи 1 - больше, 2 - меньше, 3 - равна или 0 - выход:")

            if x != '0':
                firstPlay = False
                if stavka > money:
                    stavka = money

                money -= stavka
                diceResult = getDice()

                # win1 = (oldResult > diceResult and x == "2") or (oldResult < diceResult and x == '1')
                win1 = False

                if oldResult > diceResult:
                    if x == '2':
                        win1 = True
                elif oldResult < diceResult:
                    if x == '1':
                        win1 = True

                if not x == '3':
                    if win1:
                        money += stavka + stavka // 5
                        win(stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        lose(stavka)
                elif x == "3":
                    if oldResult == diceResult:
                        money += stavka * 3
                        win(stavka * 2)
                        stavka *= 3
                    else:
                        stavka = control
                        lose(stavka)

                oldResult = diceResult
                saveMoney(money)
                color("lightyellow")
                print()
                input("\nНажми Enter, чтобы продолжить...")
            else:
                if firstPlay:
                    money -= stavka
                playRound = False
                saveMoney(money)
                color("lightyellow")
                print()
                input("\nНажми Enter, чтобы продолжить...")


def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if digit == v1:
        ret += 1
    if digit == v2:
        ret += 1
    if digit == v3:
        ret += 1
    if digit == v4:
        ret += 1
    if digit == v5:
        ret += 1
    return ret


def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True

    i = randint(30, 38)
    while (getD1
           or getD2
           or getD3
           or getD4
           or getD5):
        if i > 95:
            i = randint(30, 38)
        elif 37 < i < 90:
            i = randint(90, 95)
        print(f"\033[{i}m")

        if getD1:
            d1 += 1
        if getD2:
            d2 -= 1
        if getD3:
            d3 += 1
        if getD4:
            d4 -= 1
        if getD5:
            d5 += 1

        if d1 > 9:
            d1 = 0
        if d2 < 0:
            d2 = 9
        if d3 > 9:
            d3 = 0
        if d4 < 0:
            d4 = 9
        if d5 > 9:
            d5 = 0

        if randint(0, 20) == 1:
            getD1 = False
        if randint(0, 20) == 1:
            getD2 = False
        if randint(0, 20) == 1:
            getD3 = False
        if randint(0, 20) == 1:
            getD4 = False
        if randint(0, 20) == 1:
            getD5 = False

        time.sleep(0.1)
        i += 1

        print("    " + "%" * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if maxCount < getMaxCount(d2, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d3, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d4, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d5, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color("lightblue")
    if maxCount == 2:
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res}")
    elif maxCount == 3:
        res *= 2
        print(f" Совпадение трех чисел! Твой выигрыш 2:1: {res}")
    elif maxCount == 4:
        res *= 5
        print(f" Совпадение четырёх чисел! Твой выигрыш 5:1: {res}")
    elif maxCount == 5:
        res *= 10
        print(f" Совпадение ВСЕХ чисел! Твой выигрыш 10:1: {res}")
    else:
        saveMoney(money)
        lose(stavka)
        res = 0

    color("lightyellow")
    print()
    input("\nНажми Enter, чтобы продолжить...")

    return res


def oneHandBandit():
    global money
    playGame = True

    while playGame:
        loadMoney()
        colorLine("green", "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        color("lightmagenta")
        print(f"\n У тебя на счету {money}{valuta}\n")
        color("lightcyan")
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка не списывается.")
        print("    2. При совпадении 3-х чисел выигрыш 2:1.")
        print("    3. При совпадении 4-х чисел выигрыш 5:1.")
        print("    4. При совпадении 5-ти чисел выигрыш 10:1.")
        print("    0. Ставка 0 для завершения игры. \n")

        stavka = getIntInput(0, money, f"    Введите ставку от 0 до {money}.")
        if stavka == 0:
            return 0

        money -= stavka
        money += getOHBRes(stavka)
        saveMoney(money)
        if money <= 0:
            playGame = False


def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    while playGame and money > 0:
        colorLine("lightcyan", "ПРИВЕТСТВУЮ ТЕБЯ В НАШЕМ КАЗИНО, ДРУЖИЩЕ!")
        color("lightmagenta")
        print("У тебя на счету ", money, "рублей")
        color("blue")
        print("""Ты можешь сыграть в:
    1. Рулетку
    2. Кости
    3. Однорукого бандита
    0. Выход. Ставка 0 в играх - выход.""")
        color("white")

        x = getInput("0123", "    Твой выбор?")

        if x == "0":
            playGame = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            oneHandBandit()

    colorLine("red", "Жаль, что ты покидаешь нас! Возвращайся скорей!")
    color("magenta")
    if money <= 0:
        print("Упс, ты остался без денег. Возми микрокредит и возвращайся!")

    color("cyan")
    if money > startMoney:
        print("Ну что ж, поздравляем с прибылью!")
        print(f"На начало игры у тебя было {startMoney}{valuta}")
        print(f"Сейчас же {money}{valuta}! Играй ещё и приумножай накопления!")
    elif money == startMoney:
        print("Ты сегодня и не выиграл, и не проиграл!")
        print("Ты остался при своём.")
    else:
        print(f"К сожалению, ты проиграл {startMoney - money}{valuta}")
        print("В следующий раз всё обязательно получится!")

    saveMoney(money)

    color("white")
    time.sleep(10)

    quit(0)


main()
