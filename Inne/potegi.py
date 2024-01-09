def potegi(x, y):
    wynik = 1
    for i in range(1, y+1, 1):
        wynik = wynik*x
    return wynik

def odwroc(s):
    wynik = ''
    # to_do
    return wynik

x = int(input("Podstawa: "))
y = int(input("Wykładnik: "))
print((potegi(x, y)))