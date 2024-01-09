from turtle import *
from math import sqrt

def dom():
    fillcolor('red')
    begin_fill()
    for i in range(1, 4, 1):
        fd(150)
        lt(90)
        fd(150)
        lt(90)
    rt(60)
    end_fill()
    fillcolor('orange')
    begin_fill()
    for i in range(1, 3, 1):
        fd(150)
        lt(120)
    end_fill()
    rt(90)
    fd(150)
    lt(90)
    fd(65)
    lt(90)
    fillcolor('black')
    begin_fill()
    for i in range(1, 3, 1):
        fd(50)
        rt(90)
        fd(20)
        rt(90)
    rt(90)
    end_fill()
    fd(85)
    lt(90)
    fd(150)
    lt(90)
    okno()
    fd(150)
    lt(90)
    okno()
    lt(90)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def drzewo():
    fillcolor('brown')
    begin_fill()
    for i in range(1, 4, 1):
        fd(10)
        lt(90)
        fd(100)
        lt(90)
    end_fill()
    fd(2.5)
    rt(180)
    fillcolor('green')
    begin_fill()
    for i in range(1, 21, 1):
        lt(18)
        fd(12)
    end_fill()

def okno():
    fillcolor('blue')
    begin_fill()
    for i in range(1, 5, 1):
        fd(60)
        lt(90)
    end_fill()


speed(10)
przesun(-250, -200)
dom()
przesun(200, -150)
drzewo()
for i in range(1, 6, 1):
    przesun(60, -100)
    drzewo()
done()

