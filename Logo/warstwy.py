from turtle import *

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwadrat(a):
    for i in range(1, 5, 1):
        fd(a)
        lt(90)
    fd(a)

def warstwy(b, c):
    for i in range(1, b+1, 1):
        a = c/i
        for j in range(1, i+1, 1):
            kwadrat(a)
        przesun(-c, a)

b = int(input("Podaj liczbe wierszy: "))
c = int(input("Podaj szerokosc: "))
przesun(0, -300)
tracer(0)
warstwy(b, c)
update()
done()