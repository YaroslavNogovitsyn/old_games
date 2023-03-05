import random

toCode = "0123456789QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕКНЕГШШЩГХЗЪФЫВПРОЛЛДЖЭЯЧСМИМТЬ"
sIN = input("Введите строку для шифрования ").upper()
sOut = ""
for i in range(len(sIN)):
    count = random.randint(0, 10)
    for j in range(count):
        sOut += toCode[random.randint(0, len(toCode) - 1)]
    if random.randint(0, 1) == 1:
        sOut += "А"
    else:
        sOut += "Б"
    sOut += sIN[i]
print(f"Защифрованная строка: {sOut}")

sIn = input("Введите строку для дешифрования ")
sOut = ''

p1 = 0
while p1 < len(sIn):
    if sIn[p1] == "А" or sIn[p1] == "Б":
        sOut += sIn[p1 + 1]
        p1 += 2
    else:
        p1 += 1

print(sOut)
