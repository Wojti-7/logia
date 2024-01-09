from turtle import *
from math import sqrt

def trojkat1(bok):
    fillcolor('green')
    begin_fill()
    fd(bok)
    rt(90)
    fd(bok)
    rt(135)
    fd(sqrt(bok*bok*2))
    rt(135)
    end_fill()
    fd(bok)

def trojkat2(bok):
    fillcolor('red')
    begin_fill()
    fd(bok)
    lt(90)
    fd(bok)
    lt(135)
    fd(sqrt(bok*bok*2))
    lt(135)
    end_fill()
    fd(bok)

def lopata1():
    fd(100)
    trojkat1(25)
    fd(50)
    rt(180)
    trojkat1(50)
    rt(180)
    fd(50)
    trojkat1(75)
    bk(250)
    rt(60)

def lopata2():
    fd(50)
    trojkat2(12.5)
    fd(25)
    rt(180)
    trojkat2(25)
    rt(180)
    fd(25)
    trojkat2(37.5)
    bk(125)
    rt(60)

def wiatrak():
    lt(90)
    for i in range(1, 7, 1):
        lopata1()
    rt(30)
    for i in range(1, 7, 1):
        lopata2()

speed(10)
wiatrak()
done()