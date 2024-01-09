def suma(a, b):
    s = 0
    for i in range(a, b+1, 1):
        s = s+i
    return s

def sumaparzystych(a, b):
    s = 0
    for i in range(a, b+1, 1):
        if (i%2 == 0):
            s = s+i
        else:
            s = s+0
    return s

def sumanieparzystych(a, b):
    s = 0
    for i in range(a, b+1, 1):
        if (i%2 == 1):
            s = s+i
    return s

def silnia(n):
    z = 1
    for i in range(1, n+1, 1):
        z = z*i
    return z


poczatek = int(input("podaj liczbe poczatkowa: "))
koniec   = int(input("podaj liczbe koncowa   : "))

print("suma: ", suma(poczatek, koniec))
print("suma parzystych: ", sumaparzystych(poczatek, koniec))
print("suma nieparzystych: ", sumanieparzystych(poczatek, koniec))
print("silnia:", silnia(koniec))