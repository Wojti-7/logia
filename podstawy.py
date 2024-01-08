def system26(n):
    podstawa = 26
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    wynik = ''
    while n>0:
        c = n % podstawa
        wynik = symbol[c] + wynik
        n = int((n - c) / podstawa)
    return wynik

def system16(n):
    podstawa = 16
    symbol = '0123456789abcdef'
    wynik = ''
    while n>0:
        c = n % podstawa
        wynik = symbol[c] + wynik
        n = int((n - c) / podstawa)
    return wynik

def system10(n):
    podstawa = 10
    symbol = '0123456789'
    wynik = ''
    while n>0:
        c = n % podstawa
        wynik = symbol[c] + wynik
        n = int((n - c) / podstawa)
    return wynik

def system2(n):
    podstawa = 2
    symbol = '01'
    wynik = ''
    while n>0:
        c = n % podstawa
        wynik = symbol[c] + wynik
        n = int((n - c) / podstawa)
    return wynik

print(system26(27))
print(system16(21))
print(system10(21))
print(system2(21))
