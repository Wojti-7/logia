from turtle import *
from math import sqrt

def klocek():
    fillcolor('red')
    begin_fill()
    for i in range(1, 5, 1):
        fd(14)
        lt(90)
        fd(7)
        rt(90)
        fd(7)
        rt(90)
        fd(7)
        lt(90)
        fd(14)
        lt(90) 
    end_fill()

def lacznik_poziomy():
    fillcolor('blue')
    begin_fill()
    for i in range(1, 3, 1):
        fd(21)
        lt(90)
        fd(7)
        lt(90)    
    end_fill()

def lacznik_pionowy():
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 3, 1):
        fd(7)
        lt(90)
        fd(21)
        lt(90)
    end_fill()

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def piramida(n):
    klocek()
    przesun(-42, -42)
    for i in range(2, n+1, 1):
        for j in range(1, i+1, 1):
            klocek()
            przesun(42, 0)
        przesun(-((i+1)*42), -42)
    przesun(((n-1)*42)+28, ((n-1)*42)+14)
    for i in range(1, n, 1):
        for j in range(1, i+1, 1):
            lacznik_poziomy()
            przesun(42, 0)
        przesun(-(i+1)*42, -42)
    przesun((n*42)-14, ((n-1)*42)+14)
    for i in range(1, n, 1):
        for j in range(1, i+1, 1):
            lacznik_pionowy()
            przesun(42, 0)
        przesun(-((i+1)*42), -42)

tracer(0)
przesun(50, 100)

piramida(6)

hideturtle()
update()
done()
