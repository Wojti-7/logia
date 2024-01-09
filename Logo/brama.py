from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def podstawa():
    fillcolor('grey')
    begin_fill()
    for i in range(1, 3, 1):
        fd(624)
        lt(90)
        fd(24)
        lt(90)
    end_fill()

def strzalka(a):
    fillcolor('orange')
    begin_fill()
    for i in range(1, 3, 1):
        fd(a)
        lt(90)
        fd(5*a)
        lt(90)
    end_fill()
    przesun(-a, 5*a)
    fillcolor('orange')
    begin_fill()
    for i in range(1, 3, 1):
        fd(3*a)
        lt(90)
        fd(a)
        lt(90)
    end_fill()
    przesun(-a, a)
    fillcolor('orange')
    begin_fill()
    fd(5*a)
    lt(135)
    fd((5*a)/sqrt(2))
    lt(90)
    fd((5*a)/sqrt(2))
    lt(135)
    end_fill()
    przesun(2*a, -(6*a))

def podstawa_ze_strzalkami(a):
    przesun(-350, -300) 
    podstawa()
    przesun(a, 24)     
    strzalka(a)
    przesun(7*a, 0)
    strzalka(a)
    przesun((624-(8*a))-(9*a), 0)
    strzalka(a)
    przesun(7*a, 0)
    strzalka(a)
    przesun(-(624-(6*a)), 0)

def wejscie(a):
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 3, 1):
        fd(2*a)
        lt(90)
        fd(12*a)
        lt(90)
    end_fill()
    przesun(624-(10*a), 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 3, 1):
        fd(2*a)
        lt(90)
        fd(12*a)
        lt(90)
    end_fill()
    przesun(-(624-(5*a)), 12*a)
    fillcolor('red')
    begin_fill()
    fd(624 + (2*a))
    lt(135)
    fd(a*sqrt(2))
    lt(45)
    fd(624)
    lt(45)
    fd(a*sqrt(2))
    lt(135)
    end_fill()
    przesun(4*a, a)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    end_fill()
    przesun(a, 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(2*a)
        lt(90)
    end_fill()
    przesun(2*a, 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    end_fill()
    przesun(624-(13*a), 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    end_fill()
    przesun(a, 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(2*a)
        lt(90)
    end_fill()
    przesun(2*a, 0)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    end_fill()
    przesun(6*a, 4*a)
    lt(180)
    fillcolor('red')
    begin_fill()
    fd(624 + (4*a))
    lt(135)
    fd((2*a)*sqrt(2))
    lt(45)
    fd(624)
    lt(45)
    fd((2*a)*sqrt(2))
    lt(135)
    end_fill()
    lt(180)
    przesun(-(624 + (5*a)), 0)
    fillcolor('red')
    begin_fill()
    fd(624 + (6*a))
    lt(135)
    fd(a*sqrt(2))
    lt(45)
    fd(624 + (4*a))
    lt(45)
    fd(a*sqrt(2))
    lt(135)
    end_fill()

def brama():
    podstawa_ze_strzalkami(a)
    wejscie(a)

a = 24
tracer(0)
brama()
hideturtle()
update()
done()  