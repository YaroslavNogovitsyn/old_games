from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

root = Tk()

# Размеры окна
WIDTH = 1024
HEIGHT = 600

x01 = 20
x02 = 20
x03 = 20
x04 = 20

nameHorse01 = "Кактус"
nameHorse02 = "Габриэлла"
nameHorse03 = "Бавария"
nameHorse04 = "Янис"

defaultMoney = 10000
valuta = '₽'
money = 0

# Переменная состояния погоды: 1 - ливень, 2 - моросит дождик, 3 - облачно, на горизонте тучи, 4 - безоблачно, ветер,
# 5 - безоблачно, прекрасная погода!
weather = randint(1, 5)
# Переменная состояния дня: 1- ночь, 2 - утро, 3 - день, 4 - вечер
timeDay = randint(1, 4)

# Случайное состояние лошадей 1 - отлично, 5 - ужасно плохо
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

# Высчитываем коэфф выигрыша для лошади
"""winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100  ВАРИАНТ ВИКТОРА
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100"""

winCoeff01 = int(100 + randint(state01 * 10, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(state02 * 10, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(state03 * 10, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(state04 * 10, 30 + state04 * 60)) / 100

# Маркеры ситуаций
# В какую сторону бежим
reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
# Бежим ли
play01 = True
play02 = True
play03 = True
play04 = True
# ускорение
fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False


def setupHorse():
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(state01 * 10, 30 + state01 * 60)) / 100
    winCoeff02 = int(100 + randint(state02 * 10, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(state03 * 10, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(state04 * 10, 30 + state04 * 60)) / 100

    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False


def winRound(horse):
    global x01, x02, x03, x04, money

    res = "К финишу пришла лошадь "
    if horse == 1:
        res += nameHorse01
        win = summ01.get() * winCoeff01
    elif horse == 2:
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif horse == 3:
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif horse == 4:
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if horse > 0:
        res += f" Вы выиграли {int(win)} {valuta}. "
        if win > 0:
            res += "Поздравляем! Средства уже зачислены на Ваш счёт!"
            insertText(f"Этот забег принёс Вам {int(win)} {valuta}.")
        else:
            res += "К сожалению, выбранная Вами лошадь не выиграла. Попробуйте ещё раз!"
            insertText("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо",
                            "До финиша не дошёл никто.Забег признан несостоявшимся. Все ставки возвращены.")
        insertText("Забег признан несостоявшимся.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))
    # Сброс данных
    setupHorse()

    # Сбрасываем виджеты
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    #  Сбрасываем координаты
    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceWindow()

    # Обновляем интерфейс
    refreshCombo(eventObject="")  # Обновляем выпадающие списки и чекбоксы
    viewWeather()  # вывод в чат погоды
    healthHorse()  # вывод в чат состояние лошадей
    insertText(f"Ваши средства: {int(money)} {valuta}.")

    if money < 1:
        messagebox.showinfo("Стоп! На ипподром без средств заходить нельзя!")
        quit(0)


# функция расположения начало лошадей
def horsePlaceWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)


# функция вставки текста в поле
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)


# функция загрузки денег из файла
def loadMoney():
    try:
        f = open('money.dat', "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney}{valuta}")
        m = defaultMoney
    return m


# функция сохранения денег в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наш Ипподром закрывается")
        quit(0)


# Функция для нахождения ставки(даем возможность пользователю поставить 10, 20 ... процентов от его средств
def getVAlues(summa):
    value = list()
    if summa > 9:
        for i in range(11):
            value.append((i * (int(summa) // 10)))
    else:
        value.append(0)
        if summa > 0:
            value.append(summa)

    return value


# Функция выполняет динамическую смену денег на счету, если изменится ставка
def refreshCombo(eventObject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    LabelAllMoney["text"] = f"У Вас на счету: {int(money - summ)} {valuta}."

    stavka01['values'] = getVAlues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02['values'] = getVAlues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03['values'] = getVAlues(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04['values'] = getVAlues(int(money - summ02.get() - summ03.get() - summ01.get()))

    if summ > 0:
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"
    if summ01.get() > 0:
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if summ02.get() > 0:
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if summ03.get() > 0:
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if summ04.get() > 0:
        horse04Game.set(True)
    else:
        horse04Game.set(False)


def problemHorse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04
    # Выбираем случайную лошадь для события
    horse = randint(1, 4)

    # Чем выше число, тем ниже вероятность события
    maxRand = 10000

    if horse == 1 and play01 and x01 > 0:
        if randint(0, maxRand) < state01 * 5:
            # Маркер движения в обрутную сторонуя
            reverse01 = not reverse01
            # Сообщение пользователю
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse01} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < state01 * 5:
            # Лошадь остановилась
            play01 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse01} заржала и скинула жокея!")
        elif randint(0, maxRand) < state01 * 5 and not fastSpeed01:
            messagebox.showinfo("Великолепно!", f"{nameHorse01} перестала притворяться и ускорилась!")
            # Задаем множитель ускорения.
            fastSpeed01 = True

    elif horse == 2 and play02 and x02 > 0:
        if randint(0, maxRand) < state02 * 5:
            reverse02 = not reverse02
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse02} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < state02 * 5:
            # Лошадь остановилась
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse02} заржала и скинула жокея!")
        elif randint(0, maxRand) < state02 * 5 and not fastSpeed02:
            messagebox.showinfo("Великолепно!", f"{nameHorse02} перестала притворяться и ускорилась!")
            # Задаем множитель ускорения.
            fastSpeed02 = True
    elif horse == 3 and play03 and x03 > 0:
        if randint(0, maxRand) < state03 * 5:
            reverse03 = not reverse03
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse03} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < state03 * 5:
            # Лошадь остановилась
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse03} заржала и скинула жокея!")
        elif randint(0, maxRand) < state03 * 5 and not fastSpeed03:
            messagebox.showinfo("Великолепно!", f"{nameHorse03} перестала притворяться и ускорилась!")
            # Задаем множитель ускорения.
            fastSpeed03 = True
    elif horse == 4 and play04 and x04 > 0:
        if randint(0, maxRand) < state04 * 5:
            reverse04 = not reverse04
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse04} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < state04 * 5:
            # Лошадь остановилась
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse04} заржала и скинула жокея!")
        elif randint(0, maxRand) < state04 * 5 and not fastSpeed04:
            messagebox.showinfo("Великолепно!", f"{nameHorse04} перестала притворяться и ускорилась!")
            # Задаем множитель ускорения.
            fastSpeed04 = True


# Движение лошадей
def moveHorse():
    global x01, x02, x03, x04

    if randint(0, 100) < 20:
        problemHorse()

    # Расчет скорости лошади
    speed01 = (randint(1, timeDay + weather) + randint(1, int(7 - state01) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int(7 - state02) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int(7 - state03) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int(7 - state04) * 3)) / randint(10, 175)

    multiple = 3
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    # В какую сторону бежит лошадь(вправо или влево)
    if play01:
        if not reverse01:
            x01 += speed01
        else:
            x01 -= speed01
    if play02:
        if not reverse02:
            x02 += speed02
        else:
            x02 -= speed02
    if play03:
        if not reverse03:
            x03 += speed03
        else:
            x03 -= speed03
    if play04:
        if not reverse04:
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceWindow()

    # Все ли бегут
    allPlay = play01 or play02 or play03 or play04  # Все True. Когда станут перестанут бежать будет False
    # Все ли лошади находятся за пределами левой границы
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0  # Когда все будут True - значит все находятся за левой границей
    # Все ли бегут в обратную сторону
    allReverse = reverse01 and reverse02 and reverse03 and reverse04  # Только когда все бегут в обратную сторону - получим True

    if not allPlay or allX or allReverse:
        winRound(0)
        return 0
    # Пока не дошли до финиша, вызываем функцию каждые 5 милисекунд
    if (x01 < 952 and
            x02 < 952 and
            x03 < 952 and
            x04 < 952):
        root.after(5, moveHorse)
    else:
        if x01 >= 952:
            winRound(1)
        elif x02 >= 952:
            winRound(2)
        elif x03 >= 952:
            winRound(3)
        elif x04 >= 952:
            winRound(4)


# Функция, запрещающая пользователю менять  ставки и нажиммать старт
def runHorse():
    global money
    startButton['state'] = 'disabled'
    stavka01['state'] = 'disabled'
    stavka02['state'] = 'disabled'
    stavka03['state'] = 'disabled'
    stavka04['state'] = 'disabled'
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()


# Функция изменения погоды
def viewWeather():
    s = "Сейчас на ипподроме "
    if timeDay == 1:
        s += "ночь, "
    elif timeDay == 2:
        s += "утро, "
    elif timeDay == 3:
        s += "день, "
    elif timeDay == 4:
        s += "вечер, "

    if weather == 1:
        s += "льёт сильный дождь."
    elif weather == 2:
        s += "моросит дождик."
    elif weather == 3:
        s += "облачно, на горизонте тучи."
    elif weather == 4:
        s += "безоблачно, ветер."
    elif weather == 5:
        s += "безоблачно, прекрасная погода!"
    insertText(s)


# Функция передает аргументы insertText на основании функции getHealth
def healthHorse():
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))


# Функция создает строку с описанием лошади перед забегом
def getHealth(name, state, win):
    s = f"Лошадь {name} "
    if state == 5:
        s += "мучается несварение мжелудка."
    if state == 4:
        s += "плохо спала. Подёргивается веко."
    if state == 3:
        s += "сурова и беспощадна."
    if state == 2:
        s += "в отличном настроении, покушала хорошо."
    if state == 1:
        s += "просто ракета!."

    s += f" ({win} : 1)"
    return s


# Координаты для размещения окна
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Задаем ширину, высоту и позицию окна по центру
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Устанвливаем заголовок
root.title("ИППОДРОМ")

# Запрет на изменение экрана
root.resizable(False, False)

# Загрузка фото ипподрома
road_image = PhotoImage(file='road.png')
road = Label(root, image=road_image)
road.place(x=0, y=17)
# os.path.abspath(os.curdir)

# Загрузка фото лошадей
horse01_image = PhotoImage(file='horse01.png')
horse01 = Label(root, image=horse01_image)

horse02_image = PhotoImage(file='horse02.png')
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file='horse03.png')
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file='horse04.png')
horse04 = Label(root, image=horse04_image)

# отрисовка лошадей
horsePlaceWindow()

# создание кнопки старт
startButton = Button(text='START', font='arial 20', width=61, background="#37AA37")
startButton.place(x=20, y=370)
startButton["state"] = "disable"

# создание текстового поля
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

# создание скрола
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary['yscrollcommand'] = scroll.set

# загрузка денег
money = loadMoney()

# Если нет денег - не играем
if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

# надписи про средства и ставки на лошадь
LabelAllMoney = Label(text=f"Осталось средств: {money} {valuta}.", font="Arial 12")
LabelAllMoney.place(x=20, y=565)

LabelHorse01 = Label(text="Ставка на лошадь №1")
LabelHorse01.place(x=20, y=450)

LabelHorse02 = Label(text="Ставка на лошадь №2")
LabelHorse02.place(x=20, y=480)

LabelHorse03 = Label(text="Ставка на лошадь №3")
LabelHorse03.place(x=20, y=510)

LabelHorse04 = Label(text="Ставка на лошадь №4")
LabelHorse04.place(x=20, y=540)

# Чекбоксы для выбора ставки
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)
horseCheck01["state"] = "disabled"

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)
horseCheck02["state"] = "disabled"

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)
horseCheck03["state"] = "disabled"

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)
horseCheck04["state"] = "disabled"

# Выпадающий список
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# атрибут - только чтение
stavka01["state"] = "readonly"
stavka01.place(x=260, y=450)

stavka02["state"] = "readonly"
stavka02.place(x=260, y=480)

stavka03["state"] = "readonly"
stavka03.place(x=260, y=510)

stavka04["state"] = "readonly"
stavka04.place(x=260, y=540)

# Создаем переменные, где будут храниться ставки для каждой лошади
summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# В чекбокс кладем сумму
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

# Если меняем значение бокса - вызвается refreshCombo
stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

# Обновляем значение в Combobox
refreshCombo("")

# Ставим в Combobox первое значени списка
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

startButton["command"] = runHorse

viewWeather()
healthHorse()
root.mainloop()
