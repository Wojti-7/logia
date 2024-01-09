from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def ksztalt():
    up()
    fd(12)
    down()
    lt(120)
    fd(24)
    lt(120)
    fd(24)
    lt(60)
    fd(24)
    lt(120)
    fd(24)
    lt(60)
    fd(24)
    lt(30)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(24)
        lt(90)
    end_fill()
    lt(90)
    fd(24)
    rt(30)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(24)
        lt(90)
    end_fill()
    lt(90)
    fd(24)
    lt(30)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(24)
        lt(90)
    end_fill()
    lt(90)
    fd(24)
    rt(30)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(24)
        lt(90)
    end_fill()
    up()
    lt(90)
    fd(24)
    lt(150)
    fd(24*sqrt(3)/2)
    lt(90)
    down()

def posadzka(n):
    for i in range(1, int((n/2)+2), 1):
        for j in range(1, int(n/2)+1, 1):
            ksztalt()
            przesun(0, -((48*sqrt(3)+48)/2))
        przesun(24+24*sqrt(3), (n/2)*(48*sqrt(3)+48)/2)

ile = int(input("Podaj:"))
speed(10)
przesun(-200, 200)
posadzka(ile)
done()
