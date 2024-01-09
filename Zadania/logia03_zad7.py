def wartosc_litery(l):
    if (l == 'a'):
        return 0
    if (l == 'b'):
        return 1
    if (l == 'c'):
        return 2
    if (l == 'd'):
        return 3
    if (l == 'e'):
        return 4
    if (l == 'f'):
        return 5
    if (l == 'g'):
        return 6
    if (l == 'h'):
        return 7
    if (l == 'i'):
        return 8
    if (l == 'j'):
        return 9
    
def wartosc_cyfry(c):
    if (c == '0'):
        return 'a'
    if (c == '1'):
        return 'b'
    if (c == '2'):
        return 'c'
    if (c == '3'):
        return 'd'
    if (c == '4'):
        return 'e'
    if (c == '5'):
        return 'f'
    if (c == '6'):
        return 'g'
    if (c == '7'):
        return 'h'
    if (c =='8'):
        return 'i'
    if (c == '9'):
        return 'j'

def potegi(x, y):
    wynik = 1
    for i in range(1, y+1, 1):
        wynik = wynik*x
    return wynik

def SUMAS(s1, s2):
    suma1 = 0
    suma2 = 0
    suma = 0
    wynik = ''
    for i in range(0, len(s1), 1):
        f = wartosc_litery(s1[i])* potegi(10, len(s1)-i-1)
        suma1 = suma1 + f 
    for j in range(0, len(s2), 1):
        d = wartosc_litery(s2[j])* potegi(10, len(s2)-j-1)
        suma2 = suma2 + d 
    suma = suma1 + suma2
    k = str(suma)
    for i in range(0, len(k), 1):
        p = wartosc_cyfry(k[i])
        wynik = wynik + p
    return wynik

s1 = input('Podaj s1: ')
s2 = input('Podaj s2: ')
s = SUMAS(s1, s2)
print(s)