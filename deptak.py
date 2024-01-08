from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def trojkat(a, kolor):
    fillcolor(kolor)
    begin_fill()
    fd(a)
    lt(135)
    fd(a/sqrt(2))
    lt(90)
    fd(a/sqrt(2))
    lt(135)
    end_fill()

def kwad_dol():
    ciemny = 'Navy' # rgb(0, 0, 128)
    jasny = 'LightBlue' # rgb(173, 216, 230)
    przesun(-45, -45)
    for i in range(1, 5, 1):
        fd(90)
        lt(90)
    for i in range(1, 3, 1):
        trojkat(90, ciemny)
        fd(90)
        lt(90)
        trojkat(90, jasny)
        fd(90)
        lt(90)
    for i in range(1, 3, 1):
        fd(30)
        trojkat(30, jasny)
        fd(60)
        lt(90)
        fd(30)
        trojkat(30, ciemny)
        fd(60)
        lt(90)
    przesun(15, 15)
    for i in range(1, 3, 1):
        trojkat(60, jasny)
        fd(60)
        lt(90)
        trojkat(60, ciemny)
        fd(60)
        lt(90)
    przesun(45, 45)
    rt(90)
    trojkat(30, jasny)
    przesun(30, -30)
    lt(180)
    trojkat(30, jasny)
    rt(90)
    przesun(15, 15)

def kwad_gora():
    lt(90)
    kwad_dol()
    rt(90)

def deptak(n):
    przesun(-((n-1)*45), 45)
    for i in range(1, n+1, 1):
        if (i%2 == 1):
            kwad_dol()
            przesun(90, 0)
        else:
            kwad_gora()
            przesun(90, 0)
    przesun(-(n*90), -90)
    for i in range(1, n+1, 1):
        if (i%2 == 1):
            kwad_gora()
            przesun(90, 0)
        else:
            kwad_dol()
            przesun(90, 0)

n = int(input())
tracer(0)

deptak(n)

up()
home()
hideturtle()
update()
done()
