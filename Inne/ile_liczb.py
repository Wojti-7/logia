def potegi(x, y):
    wynik = 1
    for i in range(1, y+1, 1):
        wynik = wynik*x
    return wynik

def ile(z, c):
    wynik = 0
    p = potegi(10, z-1)
    g = potegi(10, z)
    d = str(c)
    for i in  range(p, g, 1):
        s = str(i)
        if ((s.count(d)) > 0):
            wynik = wynik + 1        
    return wynik

z = int(input("Podaj z: "))
c = int(input("Podaj c: "))
l = ile(z, c)
print(l)