def wow(n, m):
    licznik = 0
    j = 0
    for i in range(0, min(len(n), len(m)), 1):
        if (n[i] == m[j]):
            licznik = licznik + 1
        j = j + 1
    return licznik

def ooo(n, m):
    litery = set(n) & set(m)
    wynik = 0
    for l in litery:
        wynik = wynik + min(n.count(l), m.count(l))
    return wynik
        
n = 'aaabbbcd'
m = 'aabb'

# print(wow(n, m))
# print(ooo(n, m))
print(9*wow(n, m) + ooo(n, m))
