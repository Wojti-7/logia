def lucas(n):
    a = 2
    b = 1
    c = 3
    for i in range(0, n-3, 1):
        a = b
        b = c
        c = a + b
    return c % 100

def lucas2(n):
    if (n == 1):
        return 2
    elif (n == 2):
        return 1
    return (lucas2(n-1) + lucas2(n-2)) % 100

print(lucas(9))
print(lucas(35))
print(lucas(45))
print(lucas2(9))
print(lucas2(35))


        


