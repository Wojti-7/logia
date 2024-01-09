def bieg(n):
    licznik = 0
    a = str(n)
    for i in range(0, len(a)-1, 1):
        if (int(a[i]) == int(a[i+1])):
            licznik = licznik + 1
    return licznik



n = int(input("Podaj n: "))
print(bieg(n))