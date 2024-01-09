def zawiera3(liczba):
    napis = str(liczba)
    for i in range(0, len(napis), 1):
        if (int(napis[i]) == 3):
            return True
    return False

def kolejna(p, w):
    licznik = 0
    i = p+1
    while True:
        if not zawiera3(i):
            licznik = licznik + 1
            if (licznik == w):
                return i
        i = i+1
    return 0

def kolejna1(p, w):
    licznik = 0
    for i in range(p+1, 1000000, 1):
        if not zawiera3(i):
            licznik = licznik + 1
            if (licznik == w):
                return i
    return 0

def kolejna2(p, w):
    licznik = 0
    wynik = -1
    i = p+1
    while (wynik == -1):
        if not zawiera3(i):
            licznik = licznik + 1
            if (licznik == w):
                wynik = i
        i = i+1
    return wynik

poczatkowa = int(input("Poczatkowa: "))
wypisywana = int(input("Wypisywana: "))
print(kolejna(poczatkowa, wypisywana))
print(kolejna1(poczatkowa, wypisywana))
print(kolejna2(poczatkowa, wypisywana))
