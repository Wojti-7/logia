from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def figura1():
    fillcolor('blue')
    begin_fill()
    rt(45)
    for i in range(1, 5, 1):
        fd(16*sqrt(2))
        lt(90)
    end_fill()
    fd(16*sqrt(2))
    lt(45)
    fd(16)
    lt(45)
    fd(16*sqrt(2))
    lt(135)
    fd(16)
    rt(180)
    fd(16)
    lt(135)
    fd(16*sqrt(2))
    lt(45)
    fd(16)
    bk(16)
    rt(45)
    bk(16*sqrt(2))
    rt(135)

def figura2():
    lt(45)
    fd(16*sqrt(2))
    rt(45)
    fd(16)
    bk(16)
    lt(45)
    bk(16*sqrt(2))
    rt(45)
    fd(16)
    bk(16)
    rt(45)
    fd(16*sqrt(2))
    lt(45)
    fd(16)
    lt(45)
    fillcolor('blue')
    begin_fill()
    for i in range(1, 5, 1):
        fd(16*sqrt(2))
        lt(90)
    end_fill()
    fd(16*sqrt(2))
    rt(45)

def pasek_waski():
    figura1()
    figura2()

def pasek_szeroki():
    figura1()
    przesun(32, 0)
    figura2()

def filary(x, y):
    for i in range(1, int((y+1)/2)+1, 1):
        for j in range(1, int(x/2)+1, 1):
            pasek_waski()
            przesun(32, 0)
        przesun(-int((x/2)*128), -64)
    przesun(-16, (y*32))
    for i in range(1, int((y-1)/2)+1, 1):
        for j in range(1, int(x/2)+1, 1):
            pasek_szeroki()
        przesun(-int((x/2)*128), -64)


speed(10)
przesun(-250, 250)
filary(12, 11)
hideturtle()
done()