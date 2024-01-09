n = 'ppapadaaaamaaapaappaddmppaapadaaaamppaa'

def papadam(n):
    p = 'papadam'
    licznik = 0
    j = 0
    for i in range(0, len(n), 1):
        if (p[j] == n[i]):
            j = j+1
        if (j == len(p)): 
            licznik = licznik + 1
            j = 0
    return licznik

def papadam2(n):
    p = 'papadam'
    licznik = 0
    j = 0
    i = 0
    while (i < len(n)):
        if (p[j] == n[i]):
            j = j+1
        if (j == len(p)):
            licznik = licznik + 1
            j = 0
        i = i + 1
    return licznik

print(papadam2(n))
