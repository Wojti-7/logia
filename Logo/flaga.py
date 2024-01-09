from turtle import *

def kawalek_flagi(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 3, 1):
        fd(8)
        lt(90)
        fd(8)
        rt(90)
    lt(180)
    fd(8)
    rt(90)
    fd(8)
    rt(90)
    fd(16)
    rt(90)
    fd(16)
    lt(90)
    for i in range(1, 3, 1):
        fd(8)
        lt(90)
        fd(8)
        rt(90)
    lt(180)
    fd(8)
    rt(90)
    fd(8)
    lt(90)
    fd(32)
    lt(90)
    fd(8)
    rt(90)
    fd(8)
    lt(90)
    fd(16)
    lt(90)
    fd(8)
    rt(90)
    fd(8)
    lt(90)
    end_fill()

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def trojkat_zielona_podstawa():
    kawalek_flagi('green')
    przesun(44, 20)
    kawalek_flagi('green')
    przesun(-12, 52)
    lt(180)
    kawalek_flagi('yellow')
    lt(180)
    przesun(-32, -72)

def flaga(n):
    for i in range(1, n+1, 2):
        for j in range(0, n-i, 1):
            trojkat_zielona_podstawa()
            przesun(44, 20)
        przesun(-(44*(n-i)), -(20*(n-i)))
        przesun(0, 64)
    if (n%2 == 1):
        przesun(0, -64)
        kawalek_flagi('green')


n = int(input("Podaj: "))
przesun(-500, -300)
tracer(0)
flaga(n)
update()
done()
