from turtle import *
from random import *
from math import *

def przesun(x, y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()

def kwadrat(x, k):
    fillcolor(k)
    begin_fill()
    for i in range(0, 4, 1):
        fd(x)
        lt(90)
    end_fill()

tracer(0)

kwadrat(100, 'blue')

up()
fd(100)
lt(90)
bk(100)
rt(90)
down()

goto(0, 0)

circle(50)
circle(100, 270)

ht()
st()

update()
done()

# https://docs.python.org/3/library/turtle.html
#######################################
# 'blue', 'red', 'green', 'black', 'yellow', 'white', 'grey'
# pendown() == pd() == down()
# forward() == fd()
# left() == lt()
# backward() == bk() == back()
# right() == rt()
# pendown() == pd() == down()
# goto() == setpos() == setposition()
# goto(0,0) == home()
# hideturtle() == ht()
# showturtle() | st()
#######################################
