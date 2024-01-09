from turtle import *
from math import sin
from math import radians

def kolor(i):
    if (i%2 == 0):
        return 'green'
    else:
        return 'red'

def kwadrat(bok, kolor):
    color(kolor)
    for i in range(0, 4, 1):
        fd(bok)
        rt(90)

def kwadraty():
    for i in range(1, 100, 3):
        kwadrat(i, kolor(i))

def spirala(n, a):
    for i in range(1, n+1, 1):
        fd(i*a)
        rt(90)

def wielokat(n, bok):
    dopisany = 360 / n
    for i in range(1, n+1, 1):
        fd(bok)
        rt(dopisany)

def wielokat2(n, bok):
    dopisany = 360 / n
    wewnetrzny = 180 - dopisany
    promien = (bok / 2) / sin(radians(180 / n))
    for i in range(1, n+1, 1):
        rt(wewnetrzny / 2)
        fd(promien)
        bk(promien)
        lt(wewnetrzny / 2)
        fd(bok)
        rt(dopisany)

speed(10)
wielokat2(5, 40)
done()
