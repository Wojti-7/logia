from turtle import *

alfabet = 'abcdefghijklmnopqrstuvwxyz'

def indeks(napis, litera):
    for i in range(0, len(napis), 1):
        if (litera == napis[i]):
            return i 
    return -1

def kwad(bok):
    for i in range(1, 8, 1):
        fd(bok)
        lt(90)
    rt(270)

def slupek_pojedynczy1(bok, litera):
    ind = indeks(alfabet, litera)
    for i in range(0, 13, 1):
        if (i == ind):
            fillcolor('red')
        else:
            fillcolor('white')
        begin_fill()
        kwad(bok)
        end_fill()
    lt(90)
    bk(bok*13)
    rt(90)
    fd(bok)

def slupek_pojedynczy2(bok, litera):
    ind = indeks(alfabet, litera)
    for i in range(25, 12, -1):
        if (i == ind):
            fillcolor('red')
        else:
            fillcolor('white')
        begin_fill()
        kwad(bok)
        end_fill()
    lt(90)
    bk(bok*13)
    rt(90)
    fd(bok)

def slupek_podwojny(bok, litera):
    slupek_pojedynczy1(bok, litera)
    slupek_pojedynczy2(bok, litera)

def koduj(napis):
    # bok = 380/len(napis) 
    bok = 100/len(napis) 
    for i in range(0, len(napis), 1):
        slupek_podwojny(bok, napis[i])

napis = "abcdmwxyz"
up()
back(200)
right(90)
forward(200)
left(90)
down()
tracer(0)
koduj(napis)
update()
done()



