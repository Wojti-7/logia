def palindrom(a):
    dlugosc = len(a)
    for i in range(0, dlugosc, 1):
        if (a[i] != a[dlugosc-1-i]):
            return False
    return True

def odwroc(a):
    dlugosc = len(a)
    wynik = ''
    for i in range(0, dlugosc, 1):
        wynik = a[i] + wynik
    return wynik

def koduj(k):
    # k = 'alamakota'
    d = list(k)
    for i in range(0, len(d), 1):
        x = d[i]
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

def przyklad1():
    n = 'lkaabnf'
    m = 'aaabbbc'
    nx = set(n)
    mx = set(m)
    print(n.count('b'))
    print(mx & nx)
    print(mx | nx)
    print(n.find('a'))
    print(set(n) - set(m))
    print(set(range(1, 4, 1)))
    print([3] + 9*[1, 4] + [2])

def przyklad2():
    n = int('1111', 2)
    print(n)
    s = format(3, 'b')
    print(s)
    t = format(3, '04b')
    print(t)
    u = palindrom('anna')
    print(u)
    w = odwroc('wanna')
    print(w)
    x = 'wanna'[::-1]
    print(x)
    y = 'alamakota'
    print(y[0])
    print(y[1:3])
    print(y[1:])
    print(y[:3])
    print(y[:-2])
    v=list(y)
    print(v)
    v.pop(0)
    print(v)
    v.remove('l')
    print(v)
    print(v.index('m'))

def przyklad3():
    o = 'oczko'
    o = list(o)
    o.sort(reverse=False)
    print(o)

def przyklad4():
    ints = [1, 2, 3, 4]
    strings = [str(x) for x in ints]
    print(strings)

def przyklad5():
    for i in range(0, 10, 1):
        for j in range(0, i+1, 1):
            print(j, end="")
        print("")

# s = input('Napis z b:')

s = 'alabama'
print(s)
print(s.count('b'))
print(s.index('b'))

l = list(s)
print(l)
print(l.count('b'))
print(l.index('b'))
