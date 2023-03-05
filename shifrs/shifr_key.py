import random


def crypt(s, key):
    lenKey = len(key)
    start = 0
    p1 = 0

    if len(s) % lenKey != 0:
        for i in range(lenKey - len(s) % lenKey):
            s += chr(random.randint(ord('!'), ord('=')))

    lenS = len(s)
    sEncrypt = ""

    while start + lenKey < lenS + 1:
        sEncrypt += s[start + key[p1] - 1]
        p1 += 1
        if p1 == lenKey:
            p1 = 0
            start += lenKey

    return sEncrypt


encryptKey = [3, 6, 4, 2, 1, 5]

decryptKey = [5, 4, 1, 3, 6, 2]

stringCrypt = crypt("На мели мы налимов лениво ломили, это зашифровано", encryptKey)
print("Зашифровано:", stringCrypt)

stringCrypt = crypt(stringCrypt, decryptKey)
print("Расшифровано:", stringCrypt)