# zestaw 1
a = '2345'
b = '4321'

# zestaw 2
# a = '1023'
# b = '1024'

# zestaw 3
# a = '9876'
# b = '6543'

# liczniki
licznikWow = 0
licznikOoo = 0

# printy i tym podobne
# print(a)
# print(b)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])

def porownaj(i, j):
    global licznikOoo
    global licznikWow
    if (a[i] == b[j]):
        if (i == j):
            licznikWow = licznikWow + 1
        if (i != j):
            licznikOoo = licznikOoo + 1

# a[0]

porownaj(0, 0)
porownaj(0, 1)
porownaj(0, 2)
porownaj(0, 3)

# a[1]

porownaj(1, 0)
porownaj(1, 1)
porownaj(1, 2)
porownaj(1, 3)

# a[2]

porownaj(2, 0)
porownaj(2, 1)
porownaj(2, 2)
porownaj(2, 3)

# a[3]

porownaj(3, 0)
porownaj(3, 1)
porownaj(3, 2)
porownaj(3, 3)

print(licznikWow)
print(licznikOoo)