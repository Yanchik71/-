def hem():
    chisla = '0123456789'
    chisla_spisok = list(chisla)
    print(chisla_spisok)
    haming = '0000000 0001111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100 '
    haming_spisok = haming.split()
    print(haming_spisok)

    def distance(x, y):
        k = 7
        for i in range(7):
            if x % 10 == y % 10:
                k = k - 1
            x = x // 10
            y = y // 10
        return k
    cod = int(input("код= "))
    min = distance(cod, int(haming_spisok[0]))
    imin = 0
    for i in range(10):
        D = distance(cod, int(haming_spisok[i]))
        if D < min:
            min = D
        imin = i
    print(min)
    if min == 0:
        print(f"код верный: символ {chisla_spisok[imin]}")
    elif min == 1:
        print(f"код исправлен: символ {chisla_spisok[imin]}")
    else:
        print("код неверный")


def menu0():
    print("Что ты хочешь?")
    print("1. Морзе")
    print("2. код Хемминга")
    print("3. Из n-ой в 10")
    print("4. Из 10 в n-ую")
    print("5. Таблица умножения")
    n = int(input())
    if n == 1:
        morz()
    elif n == 2:
        hem()
    elif n == 3:
        izn()
    elif n == 4:
        vnn()
    elif n == 5:
        tabl()


def vnn():
    N10 = int(input(f"Введите число в десятичной системе счисления >>> "))
    Np = int(0)
    k = int(1)
    p = int(input(
        f"Введите основание системы счисления, в которую нужно перевести число >>> "))
    while N10 != 0:
        Np = Np+(N10 % p)*k
        k = k*10
        N10 = N10//p
    print(f"Число {N10} в {p}-ичной системе счисления равно {Np}")


def morz():
    a = "abwgdevijklmnoprstufhcqx"
    abc = list(a)
    print(abc)
    b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
    abcm = b.split()
    print(abcm)
    abcm = b.split()
    text = input("Введите текст на английском: ")
    indm = ""
    for i in range(len(text)):
        ind = abc.index(text[i])
        indm = indm + abcm[ind]
    print(f"{indm}строка  в азбуке морзе")


def izn():
    p = int(input("p="))
    Np = int(input(f"N{p}="))
    k = 1
    N10 = int(0)
    while not Np == 10:
        N10 = (N10+Np % 10)*k
        k = k*p
        Np = Np//10
    print(f"N10={N10}")


def tabl():
    p = int(input("Введите p (2<p<=10):"))
    x, y = int(1), int(1)
    for x in range(1, p):
        a = []
    for y in range(1, p):
        z = (x*y//p)*10 + (x*y) % p
        a.append(z)
    print(a)


menu0()
