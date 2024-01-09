from turtle import *

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwad(a, k):
    fillcolor(k)
    begin_fill()
    for i in range(0, 4, 1):
        fd(a)
        lt(90)
    end_fill()

def nwd(x, y):
    if (x == 0):
        return y
    if (y == 0):
        return x
    for i in range(min(x, y), 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i

def POSADZKA(x, y):
    a = nwd(x, y)
    b = int(x/a)
    c = int(y/a)
    for i in range(0, c, 1):
        if (i%2 == 0):
            k1 = 'red'
            k2 = 'green'
        else:
            k1 = 'green'
            k2 = 'red'
        for j in range(0, b, 1):
            if (j%2 == 0):
                kwad(a, k2)
                przesun(a, 0)
            else:
                kwad(a, k1)
                przesun(a, 0)
        przesun(-b*a, -a)

tracer(0)
POSADZKA(150, 250)
hideturtle()
update()
done()



