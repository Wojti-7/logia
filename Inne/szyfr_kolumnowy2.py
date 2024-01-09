wiadomosc, klucz = input().split()
# print(wiadomosc)
# print(klucz)

def nawin(w, k):
    wynik = ['']*len(k)
    for i in range(0, len(w), 1):
        wynik[i%len(k)] = wynik[i%len(k)] + w[i]
    return wynik

def kod(k):
    d = list(k)
    for i in range(0, len(d), 1):
        (x) = d[i]
        d[i] = (x, i)
    d.sort()
    for i in range(0, len(d), 1):
        (x, y) = d[i]
        d[i] = (y, x, i)
    d.sort()
    for i in range(0, len(d), 1):
        (x, y, z) = d[i]
        d[i] = (z)
    return d

n = nawin(wiadomosc, klucz)
# print(n)
m = kod(klucz)
# print(m)
w = ''
for i in range(0, len(m), 1):
    w = w + n[m[i]]
print(w)