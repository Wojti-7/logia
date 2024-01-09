def odwroc(x):
    wynik = ''
    k = str(x)
    for i in range(0, len(k), 1):
        wynik = wynik + k[len(k) - i -1]
    return int(wynik)

def czy_palindromiczna(x):
    d = str(x)
    for i in range(0, len(d), 1):
        if (d[i] != d[len(d) - i - 1]):
            return False
    return True

def lustro(x, n):
    for i in range(0, n, 1):
        x = x + odwroc(x)
        if (czy_palindromiczna(x) == True):
            return x
    return -1

x = int(input("Podaj x: "))
n = int(input("Podaj n: "))
print(lustro(x, n))
