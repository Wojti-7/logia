from turtle import *

# n = 'YYYYGGYGGGYYGGGYYYYYY'
# n = 'YYGGGGGGGYGGYGGG'
n = 'GGGYGGGYYYYYYYYGGGGGGYGGYGYYGGGGGGYGGGYYGGGGGGGGGYYG'

def wystapienia(t):
    wynik = []
    liczba_wystapien = 1
    biezaca = t[0]
    for i in range(1, len(t), 1):
        if (t[i] == biezaca):
            liczba_wystapien = int(liczba_wystapien) + 1
        if (t[i] != biezaca):
            wynik = wynik + [[biezaca, str(liczba_wystapien)]]
            liczba_wystapien = 1
            biezaca = t[i]
    wynik = wynik + [[biezaca, str(liczba_wystapien)]]
    return wynik

def kwad(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(1, 8, 1):
        fd(400/len(wystapienia(n)))
        lt(90)
    rt(270)
    end_fill()

def slupek(k, kolor):
    for i in range(1, int(k)+1, 1):
        kwad(kolor)
    lt(90)
    bk(400/len(wystapienia(n))*int(k))
    rt(90)
    fd(400/len(wystapienia(n)))
    
def wie(n):
    w = wystapienia(n)
    for i in range(0, len(w), 1):
        if ((w[i][0]) == 'G'):
            kolor = 'green'
        if ((w[i][0]) == 'Y'):
            kolor = 'yellow'
        slupek(int(w[i][1]), kolor)

speed(10)
up()
bk(200)
lt(90)
bk(100)
rt(90)
down()
wie(n)
hideturtle()
done()

