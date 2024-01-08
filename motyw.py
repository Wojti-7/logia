from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()
    
def szesciokat_maly(a, kolor):
    przesun(a/2, -((a * sqrt(3))/2))
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 7, 1):
        lt(60)
        fd(a)
    end_fill()
    przesun(-(a/2), (a * sqrt(3))/2)

def szesciokat_duzy(a):
    lt(30)
    szesciokat_maly(a, '#f1c100')
    lt(30)
    szesciokat_maly((a*sqrt(3))/2, '#ff6600')
    rt(60)

def motyw():
    przesun(0, 180)
    szesciokat_duzy(60)
    przesun(-(1.5*60*sqrt(3)), -((3*60)/2))
    for i in range(1, 5, 1):
        szesciokat_duzy(60)
        przesun(60*sqrt(3), 0)
    przesun(-(3*60*sqrt(3)) - (60*sqrt(3))/2,  -((3*60)/2))
    for i in range(1, 4, 1):
        szesciokat_duzy(60)
        przesun(60*sqrt(3), 0)
    przesun(-(3*60*sqrt(3)) - (60*sqrt(3))/2,  -((3*60)/2))
    for i in range(1, 5, 1):
        szesciokat_duzy(60)
        przesun(60*sqrt(3), 0)
    przesun(-(2*60*sqrt(3)) - (60*sqrt(3))/2,  -((3*60)/2))
    szesciokat_duzy(60)

tracer(0)

motyw()

up()
home()
hideturtle()
update()
done()
