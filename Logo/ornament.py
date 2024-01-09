from turtle import *
from math import sqrt

def rog_liscia(a):
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(30)
    fd(a)
    lt(120)
    fd(a)
    rt(30)
    fd(a)
    rt(60)
    fd(a)
    lt(120)
    fd(a)
    rt(60)
    fd(a)
    lt(120)
    fd(a)
    rt(60)
    fd(a)
    lt(120)
    fd(a)
    rt(60)
    fd(a)
    rt(30)
    fd(a)
    lt(120)
    fd(a)
    lt(30)
    fd(a)
    rt(90)
    fd(a)
    rt(90)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def lisc_nieparzysty(a):
    rt(30)
    up()
    fd((5*(a*sqrt(3)))/3)
    lt(150)
    down()
    fillcolor('green')
    begin_fill()
    for i in range(1, 4, 1):
        fd(2*a)
        rog_liscia(a)
        fd(2*a)
        lt(120)
    rt(120)
    end_fill()
    przesun(-(2.5)*a, (5*(a*sqrt(3)/6)))
    
def lisc_parzysty(a):
    rt(210)
    up()
    fd((5*(a*sqrt(3)))/3)
    lt(150)
    down()
    fillcolor('green')
    begin_fill()
    for i in range(1, 4, 1):
        fd(2*a)
        rog_liscia(a)
        fd(2*a)
        lt(120)
    rt(120)
    end_fill()
    przesun(-(2.5)*a, (5*(a*sqrt(3)/6)))
    lt(180)
    
def ornament(n):
    a = (50/(n-1))
    if (n%2 == 0):
        for i in range(1, int(n/2)+1, 1):
            lisc_nieparzysty(a)
            przesun(20*a, 0)
        przesun((-((20*a)*(n/2))) + (10*a), 0)
        for j in range(1, int(n/2)+1, 1):
            lisc_parzysty(a)
            przesun(20*a, 0)
    else:
        for i in range(1, int((n+1)/2)+1, 1):
            lisc_nieparzysty(a)
            przesun((20*a), 0)
        przesun((-(20*a)*(int(n+1)/2)) + (10*a), 0)
        for j in range(1, int((n-1)/2)+1, 1):
            lisc_parzysty(a)
            przesun(20*a, 0)

n = int(input("Liczba lisci: "))
tracer(0)
przesun(-300, 0)
ornament(n)
update()
done()