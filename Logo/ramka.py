from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def rog_ramki(a):
    fillcolor('purple')
    begin_fill()
    fd(a/4)
    rt(90)
    fd(a/4)
    rt(135)
    fd((a/4)*sqrt(2))
    rt(45)
    end_fill()

def bok_ramki(a):
    fillcolor('purple')
    begin_fill()
    fd(a/2)
    rt(90)
    fd(a/4)
    rt(135)
    fd((a/4)/sqrt(2))
    lt(90)
    fd((a/4)/sqrt(2))
    rt(45)
    fd(a/4)
    rt(135)
    fd((a/4)/sqrt(2))
    lt(90)
    fd((a/4)/sqrt(2))
    rt(135)
    fd(a/2)
    end_fill()

def rama(a):
    for i in range(1, 5, 1):
        rog_ramki(a)
        bok_ramki(a)

def ramka(n):
    a = 480
    for i in range(1, n+1, 1):
        rama(a)
        a = a/2
        przesun(-(a/4), (a/4))

n = int(input("Podaj n: "))
przesun(-100, -100)
tracer(0)
ramka(n)
update()
done()
