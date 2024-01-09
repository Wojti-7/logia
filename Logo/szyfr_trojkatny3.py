from turtle import *

def trojkat(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 4, 1):
        fd(26)
        lt(120)
    end_fill()

def pasek(n):
    a = str(n)
    up()
    bk(((len(a)*52)+13)/2)
    down()
    for i in range(0, len(a), 1):
        f = int(a[i])
        t = format(f, '04b')
        b = str(t)
        for j in range(0, len(b), 1):
            k = int(b[j])
            if (k == 0):
                trojkat('white')
            if (k == 1):
                trojkat('green')
            if (j%2 == 0):
                fd(26)
                lt(60)
            if (j%2 == 1):
                rt(60)

speed(10)
pasek(1203)
done()





































































