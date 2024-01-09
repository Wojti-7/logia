from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwadrat(a, kolor):
    lt(45)
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    end_fill()
    rt(45)

def lodyga(n, a):
    fillcolor('brown')
    begin_fill()
    for i in range(1, 4, 1):
        fd(a)
        lt(120)
    end_fill()
    lt(60)
    fd(a)
    rt(60)
    for i in range(1, n+1, 1):
        kwadrat(a, 'brown')
        przesun(0, a*sqrt(2))

def korona(n, a):
    przesun(-(a*sqrt(2)), 0)


lodyga(3, 20)
done()

