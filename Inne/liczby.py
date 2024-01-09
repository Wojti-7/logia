n = [321, 152, 2141, 4211]

def suma_cyfr(a):
    suma = 0
    b = str(a)
    for i in range(0, len(b), 1):
        suma = suma + int(b[i])
    return suma

def iloczyn_cyfr(c):
    iloczyn = 1
    d = str(c)
    for i in range(0, len(d), 1):
        iloczyn = iloczyn * int(d[i])
    return iloczyn

def ile(n):
    licznik = 0
    for i in range(0, len(n), 1):
        e = str(n[i])
        if (suma_cyfr(e) == iloczyn_cyfr(e)):
            licznik = licznik + 1
    return licznik


print(ile(n))