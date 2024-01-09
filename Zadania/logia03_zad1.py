from turtle import *

sam = 'aeiouy'

cyf = '0123456789'

gor = 'bdfhklt'

dol = 'gjpqy'

def kwad(a, k):
    fillcolor(k)
    begin_fill()
    for i in range(0, 4, 1):
        fd(a)
        lt(90)
    end_fill()

def pros_gora(a, k):
    fillcolor(k)
    begin_fill()
    for i in range(0, 2, 1):
        fd(a)
        lt(90)
        fd(2*a)
        lt(90)
    end_fill()

def pros_dol(a, k):
    fillcolor(k)
    begin_fill()
    for i in range(0, 2, 1):
        fd(a)
        rt(90)
        fd(2*a)
        rt(90)
    end_fill()

def RYSUJ(s):
    up()
    bk(635)
    down()
    a = 1270/len(s)
    for i in range(0, len(s), 1):
        if (s[i] in cyf):
            pros_gora(a, 'green')
            up()
            fd(a)
            down()
        elif (s[i] in gor):
            pros_gora(a, 'yellow')
            up()
            fd(a)
            down()
        elif (s[i] in dol):
            if (s[i] in sam):
                pros_dol(a, 'red')
                up()
                fd(a)
                down()
            else:
                pros_dol(a, 'yellow')
                up()
                fd(a)
                down()
        elif (s[i] in sam):
            kwad(a, 'red')
            up()
            fd(a)
            down()
        else:
            kwad(a, 'yellow')
            up()
            fd(a)
            down()

tracer(0)
RYSUJ('2krokodyle')
hideturtle()
update()
done()




