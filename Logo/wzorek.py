from math import sqrt
from turtle import *

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwad(x, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 5, 1):
        fd(x)
        lt(90)
    end_fill()

def troj(x, kolor):
    fillcolor(kolor)
    begin_fill()
    fd(2*x)
    lt(135)
    fd(x*sqrt(2))
    lt(90)
    fd(x*sqrt(2))
    lt(135)
    fd(2*x)
    end_fill()

def pros(x, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 3, 1):
        fd(2*x)
        lt(90)
        fd(x)
        lt(90)
    end_fill()

def wzorek(x):
    przesun(-200, -200)
    for i in range(1, 5, 1):
        kwad(x, 'red')
        przesun(100, 0)
        pros(x, 'green')
        przesun(300, 0)
        lt(90)
    przesun(x, x)
    for i in range(1, 3, 1):
        troj(x, 'yellow')
        lt(90)
        troj(x, 'blue')
        lt(90)
    przesun(2*x, -x)
    lt(180)
    for i in range(1, 3, 1):
        troj(x, 'pink')
        przesun(-3*x, -3*x)
        lt(90)
        troj(x, 'purple')
        przesun(-3*x, -3*x)
        lt(90)
    for i in range(1, 5, 1):
        przesun(2*x, 0)
        troj(x/2, 'orange')
        rt(90)
        troj(x/2, 'black')
    przesun(-x, 0)
    lt(45)
    przesun(-(x*sqrt(2))/2, 0)
    for i in range(1, 5, 1):
        troj(x*sqrt(2)/2, 'brown')
        rt(45)
        przesun(3*x, 0)
        rt(45)

        

    

speed(10)
wzorek(100)
done()

