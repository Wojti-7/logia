def suma(liczba):
    s = str(liczba)
    wynik1 = 0
    for i in range(0, len(s), 1):
        wynik1 = wynik1 + int(s[i])
    return wynik1

def iloczyn(liczba):
    w = str(liczba)
    wynik2 = 1
    for i in range(0, len(w), 1):
        wynik2 = wynik2 * int(w[i])
    return wynik2
   
def irs(n):
    licznik = 0
    j = 1
    while (licznik < n):
        if (suma(j) == iloczyn(j)):
            licznik = licznik + 1
        j = j + 1
    return j-1

n = int(input("Podaj n: "))
print(irs(n))
