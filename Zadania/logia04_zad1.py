from turtle import *
from math import sqrt

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def trojkat(a, k):
    fillcolor(k)
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(135)
    fd(a*sqrt(2))
    lt(135)
    end_fill()

def domek0(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k2)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)

def domek1(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k1)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(2*a, 2*a)
    rt(180)
    trojkat(a, k3)
    rt(180)
    przesun(-2*a, -2*a)

def domek2(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k2)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(a, a)
    trojkat(a, k3)
    przesun(-a, -a)

def domek3(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k1)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(2*a, 0)
    lt(90)
    trojkat(a, k3)
    rt(90)
    przesun(-2*a, 0)

def domek4(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k2)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(a, a)
    rt(90)
    trojkat(a, k3)
    lt(90)
    przesun(-a, -a)

def domek5(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k1)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    trojkat(a, k3)

def domek6(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k2)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(a, a)
    lt(180)
    trojkat(a, k3)
    lt(180)
    przesun(-a, -a)

def domek7(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k1)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(0, 2*a)
    rt(90)
    trojkat(a, k3)
    lt(90)
    przesun(0, -2*a)

def domek8(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k2)
    przesun(a, a)
    rt(90)
    trojkat(a, k1)
    lt(90)
    przesun(-a, -3*a)
    przesun(a, a)
    lt(90)
    trojkat(a, k3)
    rt(90)
    przesun(-a, -a)

def domek9(a, k1, k2, k3):
    lt(45)
    fd(2*a*sqrt(2))
    rt(45)
    przesun(-2*a, 0)
    rt(45)
    fd(2*a*sqrt(2))
    lt(45)
    przesun(-2*a, 0)
    lt(90)
    fd(2*a)
    bk(2*a)
    rt(90)
    przesun(2*a, 0)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    lt(90)
    fd(2*a)
    rt(90)
    przesun(-a, -2*a)
    fd(2*a)
    bk(2*a)
    przesun(0, 2*a)
    fd(2*a)
    przesun(-2*a, -a)
    fd(2*a)
    przesun(-2*a, -a)
    przesun(0, 2*a)
    trojkat(a, k1)
    przesun(a, a)
    rt(90)
    trojkat(a, k3)
    lt(90)
    przesun(-a, -3*a)

def DOMKI(l):
    up()
    bk(400)
    down()
    s = str(l)
    k1 = 'white'
    k2 = 'grey'
    k3 = 'black'
    a = 800/(len(s)*2)
    for i in range(0, len(s), 1):
        if (s[i] == '0'):
            domek0(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '1'):
            domek1(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '2'):
            domek2(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '3'):
            domek3(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '4'):
            domek4(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '5'):
            domek5(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '6'):
            domek6(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '7'):
            domek7(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '8'):
            domek8(a, k1, k2, k3)
            przesun(2*a, 0)
        if (s[i] == '9'):
            domek9(a, k1, k2, k3)
            przesun(2*a, 0)

l = 4545
tracer(0)
DOMKI(l)
hideturtle()
update()
done()