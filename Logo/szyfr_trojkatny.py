from turtle import *

def trojkat(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 4, 1):
        fd(26)
        lt(120)
    end_fill()

def cyfra0(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)

def cyfra1(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)

def cyfra2(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)

def cyfra3(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)

def cyfra4(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)

def cyfra5(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)

def cyfra6(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)

def cyfra7(kolor1, kolor2):
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)

def cyfra8(kolor1, kolor2):
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)

def cyfra9(kolor1, kolor2):
    trojkat(kolor2)
    fd(26)
    lt(60)
    trojkat(kolor1)
    rt(60)
    trojkat(kolor1)
    fd(26)
    lt(60)
    trojkat(kolor2)
    rt(60)

def pasek(n):
    a = str(n)
    up()
    bk(((len(a)*52)+13)/2)
    down()
    for i in range(0, len(a), 1):
        if (a[i] == '0'):
            cyfra0('white', 'green')
        if (a[i] == '1'):
            cyfra1('white', 'green')
        if (a[i] == '2'):
            cyfra2('white', 'green')    
        if (a[i] == '3'):
            cyfra3('white', 'green')
        if (a[i] == '4'):
            cyfra4('white', 'green')
        if (a[i] == '5'):
            cyfra5('white', 'green')
        if (a[i] == '6'):
            cyfra6('white', 'green')
        if (a[i] == '7'):
            cyfra7('white', 'green')
        if (a[i] == '8'):
            cyfra8('white', 'green')
        if (a[i] == '9'):
            cyfra9('white', 'green')

x = int(input("Podaj x: "))
speed(10)
pasek(x)
done()