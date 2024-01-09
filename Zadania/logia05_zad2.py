def POWIEL(s, l):
    k = str(l)
    w = ''
    for i in range(0, len(s), 1):
        w += s[i] * int(k[i%len(k)])
    return w

print(POWIEL('krokodyl', 123))
print(POWIEL('lis', 2005))

s = input()
l = int(input())
p = POWIEL(s, l)
print(p)