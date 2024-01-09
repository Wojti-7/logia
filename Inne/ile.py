def potegi(p, w):
    wynik = 1
    for i in range(0, w, 1):
        wynik = wynik*p
    return wynik

def odwroc(napis):
    wynik = ""
    for i in range(0, len(napis), 1):
        wynik = napis[i] + wynik
    return wynik

def wartosc(n, p):
    m = odwroc(n)
    wynik = 0
    for i in range(0, len(m), 1):
        wynik = wynik + int(m[i])*potegi(p, i)
    return wynik

def napis(w, p):
    wynik = ""
    while (w > 0):
        x = w%p 
        wynik = wynik + str(x)
        w = int((w-x)/p)
    return odwroc(wynik)

def ile(liczba):
    z = napis(liczba, 3)
    wynik = 0
    for i in range(0, len(z), 1):
        wynik = wynik + int(z[i])
    return wynik   

liczba = int(input("Podaj: "))
print(ile(liczba))
