def czy_jest_pierwsza(n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        pierw = int(n**0.5) + 1
        for dzielnik in range(3, pierw, 2):
            if n % dzielnik == 0:
                return False, dzielnik
        return True

def liczby_pierwsze(p, k):
    j = k
    wynik = []
    for i in range(p, k, 1):
        if (czy_jest_pierwsza(i) == True):
            wynik = wynik + [str(i)]
    while True:
        if (czy_jest_pierwsza(j) == True):
            wynik = wynik + [str(j)]
            return wynik
        j = j+1
            
def LLPP(p, k):
    wynik = 0
    liczby_naturalne = []
    for i in range(0, 10001, 1):
        liczby_naturalne = liczby_naturalne + [i]
    l = liczby_pierwsze(p, k)
    for i in range(0, len(l)-1, 1):
        s = int((int(l[i])+int(l[i+1]))/2)
        for j in range(0, len(liczby_naturalne), 1):
            if (liczby_naturalne[j] == s) and (s<k):
                wynik = wynik+1
    return wynik
    
# p = int(input('Podaj poczatek: '))
# k = int(input('Podaj koniec: '))
# l = LLPP(p, k)
# print(l)
p = czy_jest_pierwsza(1199)
print(p)