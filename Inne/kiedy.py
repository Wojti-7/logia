def kiedy(x, y):
    z = x - y
    m = 0
    k = z*m
    while (k < 1000):
        k = z*m
        m = m + 1
    return m-1

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
print(kiedy(x, y))


