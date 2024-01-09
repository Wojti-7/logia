def przebieg2(n):
    b = str(n)
    w = [''] * len(b)
    for i in range(0, len(b), 1):
        w[i] = w[i] + b[i]
    w.sort(reverse=True)
    k = ''
    for i in range(0, len(w), 1):
        k = k + w[i]
    w.sort()
    l = ''
    for i in range(0, len(w), 1):
        l = l + w[i]
    d = int(k) - int(l)
    return(d)

def przebieg(n):
    b = str(n)
    w = list(b)
    w.sort(reverse=True)
    k = ''.join(w)
    w.sort()
    l = ''.join(w)
    d = int(k) - int(l)
    return(d)

def wynik(n):
    licznik = 0
    while True:
        if n == przebieg(n):
            return licznik
        else: 
            n = przebieg(n)
            licznik += 1
    return licznik

print(wynik(2222))