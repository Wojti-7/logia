from turtle import *
from math import sqrt

def srodek():
    rt(30)
    for i in range(1, 7, 1):
        fillcolor('red')
        begin_fill()
        lt(45)
        fd(90/sqrt(2))
        rt(90)
        fd(90/sqrt(2))
        rt(135)
        fd(90)
        end_fill()
        rt(180)
        fd(90)
        lt(60)
    lt(30)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def obrecz():
    lt(30)
    for i in range(1, 7, 1):
        czesc_obreczy()
        fd(90)
        rt(60)
    lt(60)
    przesun(45, (90*sqrt(3))/2)
    lt(75)
    # for i in range(1, 7, 1):
    for i in range(1, 7, 1):
        fillcolor('red')
        begin_fill()
        fd(90/sqrt(2))
        lt(90)
        fd(90/sqrt(2))
        lt(135)
        fd(90)
        end_fill()
        lt(180)
        fd(90)
        lt(15)
        fillcolor('red')
        begin_fill()
        fd(90/sqrt(2))
        lt(90)
        fd(90/sqrt(2))
        lt(135)
        fd(90)
        end_fill()
        lt(180)
        fd(90)
        lt(15)
        fillcolor('red')
        begin_fill()
        fd(90/sqrt(2))
        lt(90)
        fd(90/sqrt(2))
        lt(135)
        fd(90)
        end_fill()
        lt(180)
        fd(90)
        rt(105)

def czesc_obreczy():
    for i in range(1, 7, 1):
        for j in range(1, 4, 1):
            fd(90)
            lt(120)
        lt(60)
        fillcolor('green')
        begin_fill()
        fd(45)
        rt(90)
        fd(90*sqrt(3)/2)
        rt(150)
        fd(90)
        end_fill()
        rt(180)
        fd(90)
        lt(60)
    
def serwetka():
    srodek()
    przesun(0, 90)
    obrecz()









tracer(0)
serwetka()
update()
done()