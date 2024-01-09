def odwroc(x):
    wynik = ''
    k = str(x)
    for i in range(0, len(k), 1):
        wynik = wynik + k[len(k) - i -1]
    return wynik

print(odwroc(125))