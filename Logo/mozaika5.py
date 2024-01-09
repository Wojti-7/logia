from turtle import *
from math import sqrt

def x(n):
    return 800 / (n * (n+1))

def k(i):
    if (i%2 == 0):
        return 'yellow'
    else:
        return 'green'

def przesun(poziomo, pionowo):
    up()
    fd(poziomo)
    lt(90)
    fd(pionowo)
    rt(90)
    down()

def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    fd(bok)
    rt(90)
    fd(bok)
    rt(90)
    fd(bok)
    rt(90)
    fd(bok)
    rt(90)
    end_fill()

def kwadratiprzesun(i, b):
    kwadrat(i*b, k(i))
    przesun(i*b/2, -1*i*b/2)

def polprzekatnej(n):
    b = x(n)
    for i in range(1, n+1, 1):
        kwadratiprzesun(i, b)

n = int(input('Podaj n: '))

speed(10)
przesun(-200, 200)
kwadrat(400, 'white')

for j in range(0, 4, 1):
    polprzekatnej(n)
    up(); fd(200); lt(90); fd(200); rt(180); down()

done()
