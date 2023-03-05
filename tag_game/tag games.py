from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
from winsound import Beep
from time import sleep


# freq = [440, 330, 440, 330, 440, 415, 415, 415, 330, 415, 330, 415, 440, 440]
# duration = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
# pause = [0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0]
#
# for i in range(len(freq)):
#     try:
#         Beep(freq[i], duration[i])
#         sleep(pause[i])
#     except:
#         print("Не проигрывается")

def music():
    Beep(100, 100)
    Beep(200, 200)
    Beep(300, 300)


# Обновляем надписи
def refreshText():
    textSteps["text"] = f"Сделано ходов: {steps[diffCombobox.current()]}"
    textRecord["text"] = f"Рекорд ходов: {record[diffCombobox.current()]}"


# Сохраняет в файл рекорды пользвоателя
def saveRecords():
    global record
    try:
        with open("steps.dat", 'w', encoding="utf-8") as f:
            for i in range(len(steps)):
                # Проверяем: чтобы побить рекорд , количество шагов для каждого уровня должно быть больше нуля,
                # но не меньше предыдущего рекорда
                if steps[i] > 0 and steps[i] < record[i]:
                    record[i] = steps[i]
                f.write(str(record[i]) + "\n")
    except FileNotFoundError:
        messagebox.showinfo("Ошибка", "Возникла проблема с файлом при сохранении очков")


# Возвращает рекорды ходов
def getRecordSteps():
    try:
        m = []
        with open("steps.dat", 'r', encoding="utf-8") as f:
            for line in f.readlines():
                m.append(int(line))

    except FileNotFoundError:
        m = []

    if len(m) != 6:
        for i in range(6):
            m.append(1000 + 1000 * i)

    return m


def seeEnd(event):
    global dataImage
    Beep(1082, 25)
    for i in range(n):
        for j in range(m):
            # Восстанавливаем изображения
            dataImage[i][j] = copyData[i][j]
    updatePictures()


# Кнопка просмотра собранного нажата
def seeStart(event):
    global copyData, dataImage
    Beep(1632, 25)
    for i in range(n):
        for j in range(m):
            # копирую значения
            copyData[i][j] = dataImage[i][j]

            dataImage[i][j] = i * n + j

    updatePictures()


def isCheckImage():
    global imageBackground
    # Если в переменной image содержится True
    if image.get():
        # то ставим imageBackground01
        imageBackground = imageBackground01
        Beep(1000, 25)
    else:
        imageBackground = imageBackground02
        Beep(1000, 25)

    updatePictures()


# # Обновление всех изображений
def updatePictures():
    # Проход по labelImage и установка исображений
    for i in range(n):
        for j in range(m):
            # Устанавливаем изображение
            labelImage[i][j]["image"] = imageBackground[dataImage[i][j]]
    # Обновление экрана
    root.update()


# # Сброс игрового поля
def resetPictures():
    global dataImage, steps, playGame
    steps[diffCombobox.current()] = 0
    playGame = False

    # Настраиваем состояни виджетов
    startButton["state"] = NORMAL
    resetButton["state"] = DISABLED
    diffCombobox["state"] = "readonly"
    radio01["state"] = NORMAL
    radio02["state"] = NORMAL

    # Заполняем dataImage первоначальными значениями
    # for i in range(n):
    #     for j in range(m):
    #         dataImage[i][j] = i * n + j
    dataImage = [[i * n + j for j in range(m)] for i in range(n)]

    # Задаем ПУСТОЕ ПОЛЕ
    dataImage[n - 1][m - 1] = blackImage

    # Звук
    Beep(800, 50)
    Beep(800, 35)

    # Перерисовка экрана
    updatePictures()
    refreshText()


# Обмен изображений
def exchangeImage(x1, y1, x2, y2):
    global dataImage, labelImage

    # Меняем мат модель
    dataImage[x1][y1], dataImage[x2][y2] = dataImage[x2][y2], dataImage[x1][y1]

    # Получаем изображение по номеру из dataImage и устанавливаем его в labelImage
    labelImage[x1][y1]["image"] = imageBackground[dataImage[x1][y1]]
    labelImage[x2][y2]["image"] = imageBackground[dataImage[x2][y2]]

    root.update()
    sleep(0.1)


def shufflePictures(x, y):
    if diffCombobox.current() < 5:
        # Количество перемешиваний в зависимости от уровня сложности
        count = (5 + diffCombobox.current()) ** 2
        # Запрет направления
        noDirection = 0
        i = 0
        # Повтрение перемешиваний
        while i < count:
        # for i in range(count):
            # Задаём заведомо истинную комбинацию для while
            direction = noDirection

            # Получаем число, ТОЧНО не повторяющее предыдущее
            while direction == noDirection:
                direction = randint(0, 3)
                # Вниз
                if direction == 0 and x + 1 < n:
                    # Обмениваем текущую и спрайт ниже
                    exchangeImage(x, y, x + 1, y)

                    # Увеличиваем x, т.к. пустое место переместилось в новую позицию x + 1
                    x += 1
                    # Запрещаем направление. След direction не должен равняться 1.
                    noDirection = 1
                    i += 1
                # Вверх
                elif direction == 1 and x + 1 >= 0:
                    exchangeImage(x, y, x - 1, y)
                    x -= 1
                    noDirection = 0
                    i += 1
                # Вправо
                elif direction == 2 and y + 1 < m:
                    exchangeImage(x, y, x, y + 1)
                    y += 1
                    noDirection = 3
                    i += 1
                # Вверх
                elif direction == 3 and y - 1 >= 0:
                    exchangeImage(x, y, x, y - 1)
                    y -= 1
                    noDirection = 2
                    i += 1
    else:
        exchangeImage(n - 1, m - 3, n - 1, m - 2)

    Beep(1750, 50)
    resetButton['state'] = NORMAL


def startNewRound():
    global steps, playGame
    playGame = True

    # Обнуление количества шагов для текущего уровня
    steps[diffCombobox.current()] = 0

    # Сбрасываем состояние кнопок и радиопереключателей
    diffCombobox["state"] = DISABLED
    radio01["state"] = DISABLED
    radio02["state"] = DISABLED
    startButton["state"] = DISABLED

    # Проигрываем звуковой сигнал
    Beep(750, 50)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!Подумать над неиспльзованием циклов(Глава 6 - где-то в 30% чтения);
    # Так же подумать над реализацией запоминания последней игры
    # Находим координаты пустого поля простым перебором каждого элемента двумерного списка dataImage[][]
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            # При совпадении числа в dataImage с номером "пустого поля", передаем в
            # в x и y счётчики циклов, тк их значения и будуи искомыми координатами
            if dataImage[i][j] == blackImage:
                x = i
                y = j
                break
    # Запускаем метод и перемешиваем
    shufflePictures(x, y)


def go(x, y):
    global steps, playGame

    if x + 1 < n and dataImage[x + 1][y] == blackImage:
        exchangeImage(x, y, x + 1, y)
    elif x - 1 >= 0 and dataImage[x - 1][y] == blackImage:
        exchangeImage(x, y, x - 1, y)
    elif y - 1 >= 0 and dataImage[x][y - 1] == blackImage:
        exchangeImage(x, y, x, y - 1)
    elif y + 1 < m and dataImage[x][y + 1] == blackImage:
        exchangeImage(x, y, x, y + 1)
    else:
        Beep(500, 100)
        return 0

    Beep(1400, 5)

    # Если игра идёт и метод продолжает выполняться
    if playGame:
        steps[diffCombobox.current()] += 1
        refreshText()

        win = True
        for i in range(n):
            for j in range(m):
                # Если няжняя правая клетка - сравниваем с blackimage
                if i == n - 1 and j == m - 1:
                    win = win and dataImage[i][j] == blackImage
                # иначе сравниваем с числовым рядом от 0 до 14
                else:
                    win = win and dataImage[i][j] == i * n + j

        if win:
            # Устанавливаем вместо свободного поля спрайт правого нижнего угла для целостности изображения
            dataImage[n - 1][m - 1] = blackImage - 1

            # Обновляем содержимое Label
            updatePictures()

            messagebox.showinfo("Браво!", "Вы победили в этой сложной игре!")

            # Победная мелодия
            music()
            # Сохраняем рекорды
            saveRecords()
            playGame = False
            refreshText()


# Цвета
back = "#373737"
fore = "#AFAFAF"
root = Tk()
root.resizable(False, False)
root.title("Пятнашки")

root.iconbitmap("images/icon/1.ico")

WIDTH = 422
HEIGHT = 710

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Задаем ширину, высоту и позицию окна по центру
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Установка фонового цвета
root["bg"] = back

# Кнопка ПОСМОТРЕТЬ ИЗБРАННОЕ
seeButton = Button(root, text="Посмотреть, как должно быть", width=56)
seeButton.place(x=10, y=600)
seeButton.bind("<Button-1>", seeStart)
seeButton.bind("<ButtonRelease>", seeEnd)

# Кнопка СТАРТ
startButton = Button(root, text="СТАРТ", width=56)
startButton.place(x=10, y=630)
startButton["command"] = startNewRound

# Кнопка СБРОС
resetButton = Button(root, text="Сброс", width=56)
resetButton.place(x=10, y=660)
resetButton["command"] = resetPictures

# Метка для вывода текста с количеством сделанных ходов и рекордом текущего уровня
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
textRecord = Label(root, bg=back, fg=fore)
textRecord.place(x=10, y=570)

# Метка сложности
Label(root, bg=back, fg=fore, text="Сложность:").place(x=267, y=550)

# Названия степеней сложности перемешивания
itemDiff = ["Junior", "Middle", "Senior", "Lead", "Mega genius", "sent a donation"]
diffCombobox = ttk.Combobox(root, width=20, values=itemDiff, state="readonly")
diffCombobox.place(x=270, y=570)

diffCombobox.bind("<<ComboboxSelected>>", lambda e: refreshText())
# Выбираем нулевой пункт: сложность Джун
diffCombobox.current(0)

# Радиопереключатели
# Создаем переменную
image = BooleanVar()
# Устанавливаем значение
image.set(True)

# Создаем радио-кнопку и привязываем к ней переменную image
radio01 = Radiobutton(root, text="Космос", variable=image, value=True, activebackground=back, bg=back, fg=fore)
radio02 = Radiobutton(root, text="Природа", variable=image, value=False, activebackground=back, bg=back, fg=fore)
radio01["command"] = isCheckImage
radio02["command"] = isCheckImage
radio01.place(x=150, y=548)
radio02.place(x=150, y=568)

# ----------------------Работа с изображениями----------------------

# Размер поля
n = 4
m = 4

# Размер "полного" изображения
pictureWidth = 400
pictureHeight = 532

# Ширина и высота одного спрайта
widthPic = pictureWidth / n
heightPic = pictureHeight / m

fileName = ["img01.png",
            "img02.png",
            "img03.png",
            "img04.png",
            "img05.png",
            "img06.png",
            "img07.png",
            "img08.png",
            "img09.png",
            "img10.png",
            "img11.png",
            "img12.png",
            "img13.png",
            "img14.png",
            "img15.png",
            "img16.png",
            "black.png"]

imageBackground = []  # Активное изображени
imageBackground01 = []  # Природа
imageBackground02 = []  # Космос

# Добавляем в списки элементы и загружаем в них объекты PhotoImage
for name in fileName:
    imageBackground01.append(PhotoImage(file="images/image01/" + name))
    imageBackground02.append(PhotoImage(file="images/image02/" + name))

# Номер излображения "пустого поля"
blackImage = 16
# Устанавливаем набор спрайтов "Космос"
imageBackground = imageBackground01

# Метки Label
labelImage = []

# Мат модель игрового поля
dataImage = []

# Для создания копии модели игрового поля при просмотре по кнопке
# "Посмотреть, как должно быть"
copyData = []

for i in range(n):
    # Начинаем заполнять списки
    labelImage.append([])
    dataImage.append([])
    copyData.append([])

    for j in range(m):
        # Формула i * n + j сгенерирует ряд чисел 0, 1, 2, 3, 4 и тд
        # Это и есть номера "собранной" версии изображения
        dataImage[i].append(i * n + j)
        copyData[i].append(i * n + j)

        # Создаем и настраиваем Label, в который будем выводить PhotoImage из imageBackground
        labelImage[i].append(Label(root, bg=back))
        # Граница между картинками
        labelImage[i][j]['bd'] = 1
        labelImage[i][j].place(x=10 + j * widthPic, y=10 + i * heightPic)

        # Что произойдет при нажатии на Label
        labelImage[i][j].bind("<Button-1>", lambda e, x=i, y=j: go(x, y))

        # Устанавливаем изображение
        labelImage[i][j]["image"] = imageBackground[dataImage[i][j]]

# !!!Ходы
steps = [0, 0, 0, 0, 0, 0]
playGame = False

# Рекорд
record = getRecordSteps()

# Обновляем текст
refreshText()

# Обновляем изображение
resetPictures()
root.mainloop()
