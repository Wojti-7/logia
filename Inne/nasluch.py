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

# a[0]

if (a[0] == b[0]):
    licznikWow = licznikWow + 1

if (a[0] == b[1]):
    licznikOoo = licznikOoo + 1

if (a[0] == b[2]):
    licznikOoo = licznikOoo + 1

if (a[0] == b[3]):
    licznikOoo = licznikOoo + 1    

# a[1]

if (a[1] == b[0]):
    licznikOoo = licznikOoo + 1

if (a[1] == b[1]):
    licznikWow = licznikWow + 1

if (a[1] == b[2]):
    licznikOoo = licznikOoo + 1

if (a[1] == b[3]):
    licznikOoo = licznikOoo + 1    

# a[2]

if (a[2] == b[0]):
    licznikOoo = licznikOoo + 1

if (a[2] == b[1]):
    licznikOoo = licznikOoo + 1

if (a[2] == b[2]):
    licznikWow = licznikWow + 1

if (a[2] == b[3]):
    licznikOoo = licznikOoo + 1    

# a[3]

if (a[3] == b[0]):
    licznikOoo = licznikOoo + 1

if (a[3] == b[1]):
    licznikOoo = licznikOoo + 1

if (a[3] == b[2]):
    licznikOoo = licznikOoo + 1

if (a[3] == b[3]):
    licznikWow = licznikWow + 1    

print(licznikWow)
print(licznikOoo)