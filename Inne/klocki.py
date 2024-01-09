def wyczysc(w):
    # for i in range(len(w)-1, 0, -1):
    #     if (len(w[i]) == 0):
    #         w.pop(i)
    # while len(w[len(w)-1]) == 0:
    # w[-1] -- ostatni element w
    while len(w[-1]) == 0:
        w.pop()
    return w

def tablica(n):
    w = [''] * len(n)
    i = 0
    j = 0
    dlugosc_klocka = 1
    while True:
        # wstawiam
        w[j] = w[j] + n[i]
        # przesuwam
        i = i+1
        if (i >= len(n)):
            return wyczysc(w)
        j = j+1
        if (j >= dlugosc_klocka):
            j = 0
            dlugosc_klocka = dlugosc_klocka+1
    return wyczysc(w)

def sprawdz(k):
    if (len(k) == 0):
        return False
    for i in range(1, len(k), 1):
        if (k[0] != k[i]):
            return False
    return True

def kolit(n):
    t = tablica(n)
    wynik = 0
    for i in range(0, len(t), 1):   
        if (sprawdz(t[i]) == True):
            wynik = wynik + 1
    return wynik

k = kolit('alamakraby')
print(k)

l = kolit('alabama')
print(l)
