from turtle import *

def napis(n):
    w = ''
    for i in range(0, len(n), 1):
        if (n[i] == 'A'):
            w += 'aaaaa'
        if (n[i] == 'B'):
            w += 'aaaab'
        if (n[i] == 'C'):
            w += 'aaaba'
        if (n[i] == 'D'):
            w += 'aaabb'
        if (n[i] == 'E'):
            w += 'aabaa'
        if (n[i] == 'F'):
            w += 'aabab'
        if (n[i] == 'G'):
            w += 'aabba'
        if (n[i] == 'H'):
            w += 'aabbb'
        if (n[i] == 'I') or (n[i] == 'J'):
            w += 'abaaa'
        if (n[i] == 'K'):
            w += 'abaab'
        if (n[i] == 'L'):
            w += 'ababa'
        if (n[i] == 'M'):
            w += 'ababb'
        if (n[i] == 'N'):
            w += 'abbaa'
        if (n[i] == 'O'):
            w += 'abbab'
        if (n[i] == 'P'):
            w += 'abbba'
        if (n[i] == 'Q'):
            w += 'abbbb'
        if (n[i] == 'R'):
            w += 'baaaa'
        if (n[i] == 'S'):
            w += 'baaab'
        if (n[i] == 'T'):
            w += 'baaba'
        if (n[i] == 'U') or (n[i] == 'V'):
            w += 'baabb'
        if (n[i] == 'W'):
            w += 'babaa'
        if (n[i] == 'X'):
            w += 'babab'
        if (n[i] == 'Y'):
            w += 'babba'
        if (n[i] == 'Z'):
            w += 'babbb'
    return w

def kwad(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(0, 4, 1):
        fd(bok)
        lt(90)
    end_fill()
    lt(90)
    fd(bok)
    rt(90)

def pasek(w, d):
    for i in range(0, len(d), 1):
        if (d[i] == 'a'):
            kwad(w, 'yellow')
        else:
            kwad(w, 'blue')
    fd(w)
    lt(90)
    bk(w*5)
    rt(90)

def szyfruj(k):
    g = 700/len(k)
    for i in range(0, len(k), 1):
        l = napis(k[i])
        pasek(g, l)

up()
bk(350)
lt(90)
bk(200)
rt(90)
down()
speed(10)
szyfruj("GODZINAKODOWANIA")
done()