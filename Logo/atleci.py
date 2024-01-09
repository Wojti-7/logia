from turtle import *
from math import sqrt
def pol_sztangi():
    fd(24)
    rt(90)
    fd(4)
    bk(8)
    fd(4)
    lt(90)
    fd(4)
    rt(90)
    fd(8)
    bk(16)
    fd(8)
    lt(90)
    fd(4)
    rt(90)
    fd(12)
    bk(24)
    fd(12)
    lt(90)
    bk(32)

def sztanga():
    pol_sztangi()
    rt(180)
    pol_sztangi()
    rt(180)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def atleta_dol():
    rt(180)
    fd(8)
    rt(90)
    for i in range(1, 4, 1):
        fd(16)
        lt(90)
    rt(180)
    fd(8)
    rt(180)
    przesun(24, 32)
    rt(180)
    fillcolor('red')
    begin_fill()
    for i in range(1, 5, 1):
        fd(16)
        lt(90)
    end_fill()
    rt(180)
    fd(8)
    rt(90)
    fd(16)
    fd(-16)
    rt(90)
    fd(32)
    lt(90)
    fd(16)
    fd(-16)
    lt(90)
    fd(12)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(8)
        lt(90)
    end_fill()
    przesun(4, -20)
    sztanga()
    przesun(0, -12)

def atleta_gora():
    rt(180)
    fd(8)
    rt(90)
    for i in range(1, 4, 1):
        fd(16)
        lt(90)
    rt(180)
    fd(8)
    rt(180)
    przesun(24, 32)
    rt(180)
    fillcolor('red')
    begin_fill()
    for i in range(1, 5, 1):
        fd(16)
        lt(90)
    end_fill()
    rt(180)
    fd(8)
    rt(90)
    fd(-16)
    fd(16)
    rt(90)
    fd(32)
    lt(90)
    fd(-16)
    fd(16)
    lt(90)
    fd(12)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(8)
        lt(90)
    end_fill()
    przesun(4, 16)
    sztanga()
    przesun(0, -48)
    
def atleci1(n):
    if (n%2 == 0):
        for i in range(1, int(n/2)+1, 1):
            atleta_dol()
            przesun(160, -12)
        przesun(-(((n/2)*160)-104), 0)
        for i in range(1 ,int(n/2)+1, 1):
            atleta_gora()
            przesun(160, -48)
    else:
        for i in range(1, int(((n+1))/2)+1, 1):
            atleta_dol()
            przesun(160, -12)
        przesun(-(((n-1)*160)-104), 0)
        for i in range(1 ,int(((n-1)/2))+1, 1):
            atleta_gora()
            przesun(160, -48)

def atleci(n):
    for i in range(0, n, 1):
        if (i%2 == 0):
            atleta_dol()
        else:
            atleta_gora()
        przesun(88, 0)

tracer(0)
speed(10)
przesun(-200, 0)
atleci(6)
update()
done()
