from turtle import *
from math import sqrt

def ziarno(n):
    fillcolor('yellow')
    begin_fill()
    fd(250/(2*n))
    lt(45)
    fd(2*(250/(2*n)))
    lt(45)
    fd(250/(2*n))
    lt(90)
    fd(250/(2*n))
    lt(45)
    fd((2*250/(2*n)))
    lt(45)
    fd(250/(2*n))
    lt(90)
    end_fill()

def kls(n):
    fd(250)
    for i in range(1, n+1, 1):
        ziarno(n)
        rt(90)
        ziarno(n)
        lt(90)
        fd(250/n)
    rt(45)
    ziarno(n)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

speed(10)
przesun(-300, 0)
kls(9)
hideturtle()
done()
