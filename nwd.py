def nwd1(x, y):
    if (x == 0):
        return y
    if (y == 0):
        return x
    for i in range(min(x, y), 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i
        
def nwd2(x, y):
    if (x == 0):
        return y
    if (y == 0):
        return x
    w = 0
    while x != y:
        if (x > y):
            x -= y
        else:
            y -= x
    return x

def nwd3(x, y):
    while y != 0:
        w = x % y
        x = y
        y = w
    return x

f = nwd1

print(f(84, 35))
print(f(45, 63))
print(f(87, 25))
print(f(87, 0))
print(f(0, 25))
print(f(25, 25))
# x = int(input())
# y = int(input())
# print(nwd1(x, y))
