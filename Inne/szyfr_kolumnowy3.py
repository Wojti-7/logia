wiadomosc, klucz = input().split()

def nawin(w, k):
    wynik = ['']*len(k)
    for i in range(0, len(w), 1):
        wynik[i%len(k)] = wynik[i%len(k)] + w[i]
    return wynik

def kod(k):
    d = list(k)
    for i in range(0, len(k), 1):
        d[i] = d[i], i
    d.sort()
    for i in range(0, len(k), 1):
        x, y = d[i]
        d[i] = y, x, i
    d.sort()
    for i in range(0, len(k), 1):
        x, y, z = d[i]
        d[i] = z
    return d

w = wiadomosc
k = klucz
n = nawin(w, k)
r = kod(k)
l = ''
for i in range(0, len(k), 1):
    l = l + n[r[i]]
print(l)