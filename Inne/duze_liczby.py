def iloczyn_cyfr(l):
    wynik = 1
    j = str(l)
    f = len(j)
    t = int(l)
    for i in range(0, f, 1):
        wynik = wynik * int(j[i])
    return wynik

def czy_jest_pierwsza(n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        pierw = int(n**0.5) + 1
        for dzielnik in range(3, pierw, 2):
            if n % dzielnik == 0:
                return False
        return True

def ICP(x):
    p = iloczyn_cyfr(x)
    if (czy_jest_pierwsza(p) == True):
        return 'prawda'
    return 'fałsz'
    
x = input('Podaj x: ')
c = ICP(x)
print(c)

