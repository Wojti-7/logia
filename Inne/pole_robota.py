def poler(n):
    wynik1 = 0
    wynik2 = 0
    g = n.count('g')
    d = n.count('d')
    if (g > d):
        wynik1 = g
    else:
        wynik1 = d
    p = n.count('p')
    l = n.count('l')
    if (l > p):
        wynik2 = l
    else:
        wynik2 = p
    w = wynik1 * wynik2
    return w

n = input('Podaj n: ')
f = poler(n)
print(f)



