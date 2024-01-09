from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def trojkat_duzy(bok, kolor):
    rt(45)
    fillcolor(kolor)
    begin_fill()
    for j in range(1, 4, 1):
        fd(bok*sqrt(2))
        lt(120)
    end_fill()
    fd(bok*sqrt(2))

def trojkat_maly(bok, kolor2):
    rt(45)
    fillcolor(kolor2)
    begin_fill()
    for j in range(1, 4, 1):
        fd(bok)
        lt(120)
    end_fill()
    fd(bok)
        
def trojkat_duzy2(bok, kolor):
    rt(45)
    fillcolor(kolor)
    begin_fill()
    for j in range(1, 4, 1):
        fd(bok)
        lt(120)
    end_fill()
    fd(bok)

def trojkat_maly2(bok, kolor2):
    rt(45)
    fillcolor(kolor2)
    begin_fill()
    for j in range(1, 4, 1):
        fd(bok/sqrt(2))
        lt(120)
    end_fill()
    fd(bok/sqrt(2))

def gwiazdka_mniejsza_gora(bok, kolor, kolor2):
    przesun(bok/2, (bok/2) + bok)
    for i in range(1, 5, 1):
        trojkat_duzy(bok, kolor)
        trojkat_maly(bok, kolor2)
    przesun(-(bok/2), -((bok/2) + bok))
        
def gwiazdka_wieksza_gora(bok, kolor, kolor2):
    przesun(bok/2, (bok/2) + bok)
    for i in range(1, 5, 1):
        trojkat_maly2(bok, kolor)
        trojkat_duzy2(bok, kolor2)
    przesun(-((bok/sqrt(2))/2), -(((bok/sqrt(2))/2) + (bok/sqrt(2))))



gwiazdka_wieksza_gora(20, 'red', 'green')
done()