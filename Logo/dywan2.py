from turtle import *

def kwadrat():
    fillcolor('green')
    begin_fill()
    for i in range(1, 5, 1):
        fd(400)
        lt(90)
    end_fill()

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def czesc_dywanu(n, a):
    fillcolor('pink')
    begin_fill()
    przesun(0, -a)
    for i in range(1, 5, 1):
        rt(90)
        fd(a)
        lt(90)
        fd(a)
        lt(90)
        fd(2*a)
    end_fill()
    przesun(0, a)

def dywan(n):
    a = 400/((3*n)+1)
    kwadrat()
    przesun(2*a, 2*a)
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            czesc_dywanu(n, a)
            przesun(3*a, 0)
        przesun(-(n*3*a), 3*a)

n = int(input("Podaj n: "))
przesun(-200, -200)
tracer(0)
dywan(n)
hideturtle()
update()
done()
