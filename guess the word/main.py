from tkinter import *
from tkinter import messagebox
from random import randint


def pressKey(event):
    # print(f"Клавиша: {event.keycode}, символ {event.char.upper()}")
    # CTRL - показываем слово
    if event.keycode == 17:
        wordLabel["text"] = wordComp

        # Показываем на 1 сек
        def do_sth():
            wordLabel["text"] = len(wordComp) * "*"

        root.after(1000, do_sth)
        root.update()
    ch = event.char.upper()
    if len(ch) == 0:
        return 0

    codeBtn = ord(ch) - st
    # print(codeBtn)
    if codeBtn >= 0 and codeBtn <= 32 or codeBtn == -15:
        # Буква Ё
        if codeBtn == -15:
            pressLetter(-15)
        else:
            pressLetter(codeBtn)
    else:
        messagebox.showinfo("Хм...", "Проверь раскладку, возможно ты пишешь не русскими буквами")


def updateInfo():
    scoreLabel["text"] = f"Ваши очки: {score}"
    topScoreLabel["text"] = f"Лучший результат: {topScore}"
    userTryLabel["text"] = f"осталось попыток: {userTry}"


# Взять новое слово и расположить на экране
def startNewRound():
    global wordStar, wordComp, dictionary, userTry

    # Загадываем слово
    x = randint(0, len(dictionary) - 1)
    wordComp = dictionary[x]
    dictionary.remove(dictionary[x])
    if len(dictionary) == 0:
        messagebox.showinfo("Упс...", "Слова закончились")
    # Формируем строку из "*
    wordStar = "*" * len(wordComp)

    # Устанавливаем текст в метку
    wordLabel['text'] = wordStar

    # Устанавливаем метку по центру для вывода слова
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)

    count = 0
    # Сбрасываем кнопки
    for i in range(33):
        if count == 32:
            btn[i]["text"] = chr(st - 15)
            btn[i]["state"] = "normal"
            break
        btn[i]["text"] = chr(st + i)
        btn[i]["state"] = "normal"
        count += 1
    userTry = 10
    updateInfo()


# Загружает слова в список
def getWordsFromFile():
    ret = []
    try:
        f = open("words.dat", "r", encoding="utf-8")
        for line in f.readlines():
            line = line.replace("\n", "")
            ret.append(line)
        f.close()
    except FileNotFoundError:
        print("Проблема с файлом. Программа прекращает работу.")
        quit(0)
    return ret


# Сохраняет в файл очки пользователя
def saveTopScore():
    global topScore
    topScore = score
    try:
        f = open("topscore.dat", 'w', encoding="utf-8")
        f.write(str(topScore))
        f.close()
    except FileNotFoundError:
        messagebox.showinfo("Ошибка", "Возникла проблема с файлом при сохранении очков")


# Возвращает максимальное значение очков из файла
def getTopScore():
    try:
        f = open("topscore.dat", 'r', encoding="utf-8")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        m = 0
    return m


# Сравниваем строки и считаем, сколько символов отличается
def compareWord(s1, s2):
    res = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res += 1
    return res


# Возвращаем слово с открытыми символами
def getWordStar(ch):
    ret = ""
    for i in range(len(wordComp)):
        if wordComp[i] == ch:
            ret += ch
        else:
            ret += wordStar[i]
    return ret


def pressLetter(n):
    global score, wordStar, userTry
    # Буква Ё
    if btn[n]["text"] == '.':
        return 0

    if n == -15:
        n += 14
        btn[n]["text"] = "."
        btn[n]["state"] = "disabled"
    else:
        btn[n]["text"] = "."
        btn[n]["state"] = "disabled"

    # Временная переменная, хранящая нынешнее количество звезд до преобразования букв
    oldWordStar = wordStar

    # Получаем строку с открытыми символами
    wordStar = getWordStar(chr(st + n))

    # Находим различие между старой и новой строкой
    count = compareWord(wordStar, oldWordStar)

    wordLabel["text"] = wordStar

    if count > 0:
        score += count * 5
    else:
        score -= 20
        if score < 0:
            score = 0

        # Уменьшаем колво попыток
        userTry -= 1
    updateInfo()

    if wordComp == wordStar:
        score += score // 2
        updateInfo()
        if score > topScore:
            messagebox.showinfo("Поздравляю!", f"Вы - топчик! Угадано слово: {wordComp}! Нажмите ОК для продолжения "
                                               f"игры.")
            saveTopScore()
        else:
            messagebox.showinfo("Отлично", f"Слово угадано: {wordComp}! Продолжаем играть дальше!")
        startNewRound()
    elif userTry <= 0:
        messagebox.showinfo("Бу!", "Количество попыток закончилось...")
        quit(0)


# Создание окна
root = Tk()  # Храним ссылку на окно в памяти
root.bind("<Key>", pressKey)
root.resizable(False, False)  # Запрещаем изменение размеров
root.title("Угадай слово")

# Настройка геометрии окна
WIDTH = 810
HEIGHT = 320

SCR_WIDTH = root.winfo_screenwidth()  # Ширина экрана в пикселях
SCR_HEIGHT = root.winfo_screenheight()

POS_X = SCR_WIDTH // 2 - WIDTH // 2  # Координата по X
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2  # Координата по Y

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Метка для вывода слова, которое человек угадывает в текущем раунде
wordLabel = Label(font='consolas 35')

# Метки для отображения текущих очков и рекорда
scoreLabel = Label(font=', 12')
topScoreLabel = Label(font=', 12')

# Метка для оставшихся попыток
userTryLabel = Label(font=', 12')

# Метки в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# Переменные для хранения значений
score = 0  # Текущие очки
topScore = getTopScore()  # Рекорд игры
userTry = 10  # Количество попыток

st = ord("А")  # Для определения символа на кнопке по коду
btn = []  # Список кнопок

# Переменная счетчика для Ё
count = 0
# Алфавит
for i in range(33):
    # if count == 32:
    #     # Работа с буквой Ё. -15 нужно тк у буквы А ord=1040, а у Ё-1025
    #     btn.append(Button(text="Ё", width=2, font="consolas 15"))
    #     btn[count].place(x=565, y=250)
    #     btn[32]["command"] = lambda x=-15: pressLetter(x)
    #     break
    btn.append(Button(text=chr(st + i), width=2, font="consolas 15"))
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)
    btn[i]["command"] = lambda x=i: pressLetter(x)
    count += 1

# "загаданное слово"
wordComp = ""
# "слово со звёздочками"
wordStar = ""

dictionary = getWordsFromFile()
# Метода, отвечающий за старт каждого раунда
startNewRound()

root.mainloop()
