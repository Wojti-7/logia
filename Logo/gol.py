from turtle import *
from math import sqrt
from math import sin
from math import radians

def pilkarz():
    fd(80)
    lt(210)
    fd(80)
    bk(80)
    lt(150)
    fd(70)
    lt(150)
    fd(50)
    bk(50)
    lt(60)
    fd(50)
    bk(50)
    lt(60)
    fd(3)
    for i in range(1, 20, 1):
        lt(18)
        fd(6)
    fd(3)
    lt(18)

def wielokat():
    dopisany = 360 / 20
    wewnetrzny = 180 - dopisany
    promien = (5 / 2) / sin(radians(180 / 20))
    for i in range(1, 20+1, 1):
        lt(wewnetrzny / 2)
        fd(promien)
        bk(promien)
        rt(wewnetrzny / 2)
        fd(5)
        lt(dopisany)

def bramkarz():
    fd(80)
    lt(210)
    fd(80)
    bk(80)
    lt(150)
    fd(70)
    lt(150)
    fd(50)
    bk(50)
    lt(60)
    fd(50)
    bk(50)
    lt(60)
    fd(3)
    for i in range(1, 20, 1):
        lt(18)
        fd(6)
    fd(3)
    lt(18)

def bramkarzstary():
    fd(90)
    rt(30)
    fd(50)
    bk(50)
    lt(60)
    fd(50)
    bk(50)
    lt(150)
    fd(90)
    rt(50)
    fd(40)
    bk(40)
    lt(100)
    fd(40)
    bk(40)
    rt(45)
    fd(5)
    rt(90)
    fd(2)
    for i in range(1, 20, 1):
        lt(18)
        fd(4)
    fd(2)
    lt(18)

def bramka():
    lt(90)
    fd(120)
    lt(90)
    fd(250)
    lt(90)
    fd(120)
    lt(90)

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def lotpilki():
    for i in range(1, 5, 1):
        lt(18)
        for j in range(1, 7, 1):
            up()
            fd(9)
            down()
            fd(9)
    lt(18)
    for i in range(1, 3, 1):
        up()
        fd(9)
        down()
        fd(9)  
    rt(90)

def murek(ilu):
    for i in range(0, ilu, 1):
        pilkarz()
        przesun(35, -149)
        lt(90)

speed(10)

przesun(200, 100)
bramka()

przesun(-100, -250)
lt(90)
pilkarz()

przesun(30, -135)
lotpilki()

wielokat()

up()
rt(160)
fd(215)
rt(180)
down()

bramkarz()

rt(20)
przesun(200, -200)
rt(180)

murek(5)

done()