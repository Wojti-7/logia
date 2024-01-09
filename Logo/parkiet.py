from turtle import *

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def czesc_parkietu():
    for i in range(1, 5, 1):
        for j in range(1, 5, 1):
            fillcolor('yellow')
            begin_fill()
            for k in range(1, 3, 1):
                fd(50)
                lt(90)
                fd(10)
                lt(90)
            end_fill()
            przesun(0, -10)
        przesun(60, 10)
        lt(90)
    przesun(40, 10)
    fillcolor('yellow')
    begin_fill()
    for i in range(1, 5, 1):
        fd(10)
        lt(90)
    end_fill()
    przesun(-40, -10)

def parkiet(k, w):
    for i in range(1, w+1, 1):
        for j in range(1, k+1, 1):
            czesc_parkietu()
            przesun(90, 0)
        przesun(-(k*90), -90)


przesun(-400, 262)
tracer(0)
parkiet(10, 7)
update()
done()