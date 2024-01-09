from turtle import *

def romb(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 3, 1):
        fd(bok)
        lt(45)
        fd(bok)
        lt(135)
    lt(45)
    end_fill()

def gwiazdka(bok, kolor, kolor2):
    for i in range(1, 5, 1):
        romb(bok, kolor)
        romb(bok, kolor2)

def gwiazdka_srodkowa(kolor, kolor2):
    gwiazdka(60, kolor, kolor2)
    rt(45)
    fd(60)
    for i in range(1, 9, 1):
        fd(15)
        lt(45)
        fd(60 + 15)
        lt(135)
        fd(60 + 15)
        rt(135)
        bk(15)
    bk(60)
    lt(45)

def romb_z_gwiazdkami(kolor, kolor2):
    gwiazdka(15, kolor, kolor2)
    lt(90)
    fd(75)
    rt(90)
    gwiazdka(15, kolor, kolor2)
    lt(90)
    bk(75)
    lt(45)
    fd(75)
    rt(135)
    gwiazdka(15, kolor, kolor2)
    lt(90)
    fd(75)
    rt(90)
    gwiazdka(15, kolor, kolor2)
    rt(45)
    fd(75)
    bk(75)
    lt(45)

def bukiet(kolor, kolor2):
    gwiazdka_srodkowa(kolor2, kolor)
    fd(75)
    rt(45)
    fd(75)
    lt(90)
    fd(75)
    rt(45)
    for i in range(1, 5, 1):
        romb_z_gwiazdkami(kolor, kolor2)
        lt(45)
        romb_z_gwiazdkami(kolor2, kolor)
        lt(45)

tracer(0)
bukiet('red', 'green')
hideturtle()
update()
done()
