from turtle import *
from math import sqrt

def kwad(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok); rt(90)
    end_fill()

def strz():
    bok = 80
    a = bok * sqrt(2) / 4
    kwad(bok, 'white')
    fd(bok/2); rt(45)
    fillcolor('olivedrab')
    begin_fill()
    fd(a); lt(90)
    fd(a); rt(135)
    fd(bok); rt(90)
    fd(bok); rt(135)
    fd(a); lt(90)
    fd(a); rt(90)
    fd(2 * a); rt(45)
    bk(bok/2)
    end_fill()

def jeden():
    kwad(200, 'tomato')
    pu(); fd(80); pd()
    for i in range(4):
        strz()
        pu(); fd(120); rt(90); fd(80); pd()
    pu(); bk(80); pd()

def dywan():
    for i in range(4):
        jeden()
        rt(90)

tracer(0)
# speed(100)
# kwad(100, 'red')
# strz()
# jeden()
dywan()
update()
done()
