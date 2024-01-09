def ile(n):
    predkosc = 1
    for i in range(2, n+1, 1):
        if (i%2 == 0):
            predkosc = predkosc+3
        if (i%2 == 1):
            predkosc = predkosc-1
        if (i%12 == 1):
            predkosc = predkosc-9
    return predkosc

n = int(input("Numer kroku: "))
print(ile(n))
