def silnia(n):
    if (n == 1):
        return 1
    return n * silnia(n-1)

def dostaw(l, s):
    wynik = ['']*(len(s) + 1)
    for i in range(0, len(s)+1, 1):
        wynik[i] = s[0:i] + l + s[i:]
    return wynik

def dostaw2(l, s):
    wynik = []
    for i in range(0, len(s)+1, 1):
        wynik = wynik + [s[0:i] + l + s[i:]]
    return wynik

def permutuj(s):
    if (len(s) == 1):
        return [s]
    if (len(s) == 2):
        return [s, s[1] + s[0]]
    wynik = []
    pierwsza = s[0]
    reszta = s[1:]
    mniejsza = permutuj(reszta)
    for i in range(0, len(mniejsza), 1):
        wynik = wynik + dostaw(pierwsza, mniejsza[i])
    return wynik
    
d = dostaw('b', 'aaaa')
print(d)
p = permutuj('pwlk')
print(p)
# print(len(p))

