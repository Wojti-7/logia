from turtle import *

def fd2(l):
    fillcolor('black')
    begin_fill()
    for i in range(1, 3, 1):
        fd(10*l)
        lt(90)
        fd(10)
        lt(90)
    end_fill()
    fd(10*l)
    
def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwadrat_rog():
    fd2(7)
    lt(90)
    fd2(9)
    lt(90)
    fd2(9)
    lt(90)
    fd2(7)
    rt(90)
    przesun(-20, 0)
    rt(180)
    for i in range(1, 5, 1):
        fd2(5)
        lt(90)
    przesun(20, 20)
    fd2(1)
    lt(180)
    przesun(50, 10)
    fd2(2)
    przesun(-10, 10)
    rt(90)
    
def czesc_mala():
    przesun(-10, 10)
    rt(90)
    fd2(7)
    lt(90)
    fd2(5)
    lt(90)
    fd2(5)
    przesun(-10, 10)
    rt(90)
    fd2(5)
    przesun(-10, 10)
    rt(90)

def czesc_duza(n):
    fd2(7)
    lt(90)
    fd2(9)
    lt(90)
    fd2(5)
    lt(90)
    fd2(5)
    przesun(-10, 10)
    rt(90)
    fd2(5)
    przesun(-10, 10)
    rt(90)
    fd2(n)

def pierwsza_linia():
    for i in range(1, 3, 1):
        czesc_duza(9)
        czesc_mala()
        czesc_duza(7)
        lt(90)
        fd2(5)
        czesc_mala()
        czesc_duza(9)
        czesc_mala()
        kwadrat_rog()

def druga_linia():
    lt(90)
    przesun(30, 10)
    for i in range(1, 3, 1):
        czesc_mala()
        czesc_duza(9)
        czesc_mala()
        kwadrat_rog()
        czesc_duza(9)
        czesc_mala()
        czesc_duza(7)
        lt(90)
        fd2(5)


tracer(0)
przesun(155, 200)
lt(90)
speed(10)
pierwsza_linia()
druga_linia()
hideturtle()
update()
done()

