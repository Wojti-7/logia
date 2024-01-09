import random

print("Hello world!")
random.seed()
losowaliczba = random.randint(0,100)
print("Twoja tajna liczba ktora zgadujesz: ")
print(losowaliczba)

zgadles = False
print("Wartosc zgadles po raz pierwszy:")
print(zgadles)
while (zgadles == False):
    print("Zgadnij liczbe:")
    mojaliczba = int(input())
    if (losowaliczba < mojaliczba):
        print("Nie zgadles - szukana liczba jest mniejsza")
    if (losowaliczba > mojaliczba):
        print("Nie zgadles - szukana liczba jest wieksza")
    if (losowaliczba == mojaliczba):
        print("Zgadles")
        zgadles = True
print("Koniec programu")
print("Wartosc zgadles po raz drugi:")
print(zgadles)
