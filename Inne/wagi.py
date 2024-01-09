def sortuj(t):
    for j in range(0, len(t), 1):
        for i in range(0, len(t)-1, 1):
            if (t[i] > t[i+1]):
                t[i], t[i+1] = t[i+1], t[i]
    return t

def waga(s):
    x = [1 for c in s]
    sam = 'aouiey'
    for i in range(0, len(s), 1):
        if (i < len(x) / 2):
            x[i] = i+1
        else:
            x[i] = len(x) - i
    b = sum(x)
    for i in range(0, len(s), 1):
        if (s[i] in sam):
            b = b-1
        else:
            b = b+1
    return b

def sortuj_waga(t):
    for j in range(0, len(t), 1):
        for i in range(0, len(t)-1, 1):
            if (waga(t[i]) > waga(t[i+1])):
                t[i], t[i+1] = t[i+1], t[i]
            elif (waga(t[i]) == waga(t[i+1])):
                if (t[i] > t[i+1]):
                    t[i], t[i+1] = t[i+1], t[i]
    return t

tab = ['wykonaj', 'zadanie', 'waga', 'slowa']
# print(tab)
# print(sortuj_waga(tab))
print(sortuj_waga(tab))

