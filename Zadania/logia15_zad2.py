def redukcja1(n):
    s = str(n)
    # jesli liczba krotsza niz dwie cyfry to koniec rekurencji
    if len(s) < 2:
        return n
    # zostawiam s, zmieniam w, zeby sprawdzic na koniec czy cos sie zmienilo
    w = s
    i = len(w)-2
    while i>=0:
        if w[i] == w[i+1]:
            l = (int(w[i]) + int(w[i+1])) % 10
            w = w[:i] + str(l) + w[i+2:]
            i -= 2
        else:
            i -= 1
    # jesli nic sie nie zmienilo, to koniec rekurencji
    if w == s:
        return n
    else:
        return redukcja2(int(w))

def redukcja2(n):
    n = list(str(n))
    if (len(n) == 1):
        return int(''.join(n))

    z = []
    while z != n:
        z = n
        x = []
        y = []
        k = []
        l = 0
        i = len(n) - 1
        while i > 0:
            if (n[i] == n[i - 1]):
                x = n[0:i-1]
                y = n[i+1:]
                l = (int(n[i]) + int(n[i - 1])) % 10
                k = [str(l)]
                n = x + k + y
                i -= 2
            else:
                i -= 1
    s = ''.join(n)
    s = int(s)

    return s

def redukcja3(n):
    n = str(n)
    if (len(n) == 1):
        return int(n)

    z = ''
    while z != n:
        z = n
        x = ''
        y = ''
        k = ''
        l = 0
        i = len(n) - 1
        while i > 0:
            if (n[i] == n[i - 1]):
                x = n[0:i-1]
                y = n[i+1:]
                l = (int(n[i]) + int(n[i - 1])) % 10
                k = str(l)
                n = x + k + y
                i -= 2
            else:
                i -= 1
    s = int(n)

    return s

print(redukcja1('84211'))
print(redukcja1('426633'))

print(redukcja2('84211'))
print(redukcja2('426633'))

print(redukcja3('84211'))
print(redukcja3('426633'))