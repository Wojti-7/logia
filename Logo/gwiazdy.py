from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def gwiazdka_0_4_8(bok):
    fillcolor('green')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok)
        rt(60)
        fd(bok)
        lt(120)
    end_fill()
    przesun(3*bok, 0)

def gwiazdka_1_5_9(bok):
    fillcolor('green')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok)
        rt(60)
        fd(bok)
        lt(120)
    end_fill()
    przesun((1.5)*bok, bok*sqrt(3)/2)
    przesun(-(1.5)*bok/2, -bok*sqrt(3)/4)
    fillcolor('white')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok/2)
        rt(60)
        fd(bok/2)
        lt(120)
    end_fill()
    przesun(-(1.5)*bok, -bok*sqrt(3)/2)
    przesun((1.5)*bok/2, bok*sqrt(3)/4)
    przesun(3*bok, 0)
    
def gwiazdka_2_6(bok):
    fillcolor('red')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok)
        rt(60)
        fd(bok)
        lt(120)
    end_fill()
    przesun(3*bok, 0)
    
def gwiazdka_3_7(bok):
    fillcolor('red')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok)
        rt(60)
        fd(bok)
        lt(120)
    end_fill()
    przesun((1.5)*bok, bok*sqrt(3)/2)
    przesun(-(1.5)*bok/2, -bok*sqrt(3)/4)
    fillcolor('white')
    begin_fill()
    for i in range(1, 7, 1):
        fd(bok/2)
        rt(60)
        fd(bok/2)
        lt(120)
    end_fill()
    przesun(-(1.5)*bok, -bok*sqrt(3)/2)
    przesun((1.5)*bok/2, bok*sqrt(3)/4)
    przesun(3*bok, 0)

def gwiazdka(m, bok):
    if (m == '0') or (m == '4') or (m == '8'):
        gwiazdka_0_4_8(bok)
    if (m == '1') or (m == '5') or (m == '9'):
        gwiazdka_1_5_9(bok)
    if (m == '2') or (m == '6'):
        gwiazdka_2_6(bok)
    if (m == '3') or (m == '7'):
        gwiazdka_3_7(bok)

def gwiazdy(n):
    b = str(n)
    j = (560/len(b))/3
    for i in range(0, len(b), 1):
        k = b[i]
        gwiazdka(k, j)
    przesun(-(3*j*(len(b)-1)), -(2*j*sqrt(3)))
    t = int(b[len(b)-1])
    l = int(b)
    l = int((l - t)/10)
    p = str(l)
    for i in range(0, len(p), 1):
        k = p[i]
        gwiazdka(k, j)
    przesun(-(3*j*(len(p)-1)), -(2*j*sqrt(3)))
    h = int(p[len(p)-1])
    r = int(p)
    r = int((r - h)/10)
    s = str(r)
    for i in range(0, len(s), 1):
        k = s[i]
        gwiazdka(k, j)

   


n = int(input("Podaj n:"))
przesun(-280, 200)
tracer(0)
gwiazdy(n)
update()
done()
