from turtle import *

def slupek_dol(n, a):
    fd(n*a)
    lt(90)
    fd(a)
    lt(90)
    fd(n*a)

def slupek_gora(n, a):
    fd(n*a)
    rt(90)
    fd(a)
    rt(90)
    fd(n*a)

def GRAFKOD(l):
    
    rt(90)
    s = str(l)
    a = 50
    for i in range(0, len(s), 1):
        if(i%2 == 0):
            slupek_dol(int(s[i]), a)
        else:
            slupek_gora(int(s[i]), a)

tracer(0)
GRAFKOD(4236)
hideturtle()
update()
done()