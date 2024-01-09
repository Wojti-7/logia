from turtle import *
from math import sqrt

n = [2, 4, 5, 1, 3, 7, 9, 1]

def kwad():
    fillcolor('green')
    begin_fill()
    for i in range(1, 8, 1):
        fd(50)
        lt(90)
    end_fill()
    rt(270)

def figura1():
    fillcolor('grey')
    begin_fill()
    for i in range(1, 4, 1):
        fd(50)
        lt(120)
    end_fill()

def figura2():
    fillcolor('grey')
    begin_fill()
    fd(50)
    lt(90)
    fd(50)
    lt(150)
    fd(50)
    rt(120)
    fd(50)
    lt(150)
    fd(50)
    lt(90)
    end_fill()

def figura3():
    fillcolor('grey')
    begin_fill()
    fd(50)
    lt(90)
    fd(50)
    lt(135)
    fd(50*sqrt(2))
    lt(135)
    end_fill()
    
def figura4():
    fillcolor('grey')
    begin_fill()
    fd(50)
    lt(135)
    fd(50*sqrt(2))
    lt(135)
    fd(50)
    lt(90)
    end_fill()  

def slupek(a):
    for i in range(1, a+1, 1):
        kwad()

def schemat(n):
    up()
    bk((len(n)*50)/2)
    lt(90)
    bk(200)
    rt(90)
    down()
    for i in range(0, len(n), 1):
        slupek(n[i])
        if (i == 0):
            if (n[i] == n[i+1]):
                figura4()
            if (n[i] > n[i+1]):
                figura1()
            if (n[i] < n[i+1]):
                figura3()
        elif (i == len(n) - 1):
            if (n[i] == n[i-1]):
                figura3()
            if (n[i] > n[i-1]):
                figura1()
            if (n[i] < n[i-1]):
                figura4()
        elif (n[i-1] < n[i] < n[i+1]):
            figura3()
        elif (n[i-1] > n[i] > n[i+1]):
            figura4()
        elif (n[i-1] < n[i] > n[i+1]):
            figura1()
        elif (n[i-1] > n[i] < n[i+1]):
            figura2()
        elif (n[i-1] > n[i] == n[i+1]):
            figura4()
        elif (n[i-1] < n[i] == n[i+1]):
            figura3()
        elif (n[i-1] == n[i] > n[i+1]):
            lt(90)
            rt(90)
        elif (n[i-1] == n[i] < n[i+1]):
            lt(90)
            rt(90)
        lt(90)
        bk(int(n[i])*50)
        rt(90)
        fd(50)
        

tracer(0)
schemat(n)
hideturtle()
update()
done()

