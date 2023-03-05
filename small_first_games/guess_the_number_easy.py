from random import randint
mynum = randint(1, 100)
print("Я загадал число от 1 до 100. Угадай его!")
yournum = -1
count = 0
while yournum != mynum:
    yournum = int(input("Твой вариант?"))
    if yournum > mynum:
        print("Попробуй меньше")
    elif yournum < mynum:
        print("Попробуй больше")
    count = count + 1
print("Точно, молодец!")
print("Это число ", str(mynum))
print("Ты использовал " + str(count)+ " попыток!")