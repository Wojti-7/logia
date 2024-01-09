def ile_wystapien(litera, napis):
    wystapienia = 0
    for i in range(0, len(napis), 1):
        if (napis[i] == litera):
            wystapienia = wystapienia + 1
    return(wystapienia)

def kodowanie(napis):
    alfabet = 'aeiouybcdfghjklmnpqrstvwxz'   
    wynik = ''
    for i in range(0, len(alfabet), 1):
        ile = ile_wystapien(alfabet[i], napis)
        if (ile == 0):
            wynik = wynik
        elif (ile == 1):
            wynik = wynik + alfabet[i]
        elif (ile > 1):
            wynik = wynik + alfabet[i] + str(ile)
    print(wynik)

y = input("Podaj napis: ")
kodowanie(y)
