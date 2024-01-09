def tablica1():
    max = 100
    min = 1
    t = [min]
    p = 1
    d = 5
    l = 2
    while t[len(t) - 1] < max:
        for i in range(p+d, p+d+l+1, 1):
            t += [i]
        p += d
        d += 8
        l += 2
    return t

def tablica3():
    max = 100
    min = 3
    t = [min]
    p = 3
    d = 9
    l = 2
    while t[len(t) - 1] < max:
        for i in range(p+d, p+d+l+1, 1):
            t += [i]
        p += d
        d += 8
        l += 2
    return t

def tablica4():
    max = 100
    min = 2
    t = [min]
    p = 2
    d = 7
    l = 2
    while t[len(t) - 1] < max:
        for i in range(p+d, p+d+l+1, 1):
            t += [i]
        p += d
        d += 8
        l += 2
    return t

def klocki(n):
    if (n in tablica1()):
        return 'I'
    elif (n in tablica3()):
        return 'III'
    elif (n in tablica4()):
        return 'IV'
    else:
        return 'II'

a = int(input())

print(klocki(a))
