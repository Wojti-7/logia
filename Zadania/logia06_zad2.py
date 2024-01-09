# bez rysowania

def MAXTR(n):
    poprzednia = 0
    nastepna = 1
    i = 2
    while nastepna < n:
        w = nastepna + i
        poprzednia = nastepna
        nastepna = w
        i += 1
    l = nastepna - poprzednia - 1
    return poprzednia, l

print(MAXTR(16))
print(MAXTR(45))
print(MAXTR(8))
print(MAXTR(2))

