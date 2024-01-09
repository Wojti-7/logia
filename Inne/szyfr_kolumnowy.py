dane = input().split()
wiadomosc = dane[0]
klucz = dane[1]
# print(wiadomosc)
# print(klucz)

def nawin(w, k):
    tab = ['']*len(k)
    j = 0
    for i in range(0, len(w), 1):
        tab[j] = tab[j] + w[i]
        j = (j + 1) % len(k)
    return tab

def koduj(k):
    d = list(k)
    for i in range(0, len(d), 1):
        d[i] = (d[i], i+1)
    # print(d)
    d.sort()
    # print(d)
    for i in range(0, len(d), 1):
        x, y = d[i]
        d[i] = (y, x, i+1)
    # print(d)
    d.sort()
    # print(d)
    for i in range(0, len(d), 1):
        x, y, z = d[i]
        d[i] = z
    return d

wynik = nawin(wiadomosc, klucz)
# print(wynik)

kod = koduj(klucz)
# print(kod)

zakodowane = ''
for i in range(0, len(kod), 1):
    zakodowane = zakodowane + wynik[ kod[i]-1 ]

print(zakodowane)
