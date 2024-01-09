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
licznikOoo = 0
licznikWow = 0

# printy i tym podobne
# print(a)
# print(b)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])

def porownaj(i, j):
    global licznikWow
    global licznikOoo
    if (a[i] == b[j]):
        if (i == j):
            licznikWow = licznikWow + 1
        if (i != j):
            licznikOoo = licznikOoo + 1

for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        # print(i, j)
        porownaj(i, j)

print(licznikWow)
print(licznikOoo)