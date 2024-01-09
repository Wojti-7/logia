def litera(t, k):
    x = ord(t) - ord('A')
    y = ord(k) - ord('A')
    z = (x - y) % 26 + ord('A')
    return chr(z)

def klucz(tt, kk):
    w = ''
    for i in range(0, len(tt), 1):
        w += kk[i % len(kk)]
    return w

def deszyfr(tt, kk):
    w = ''
    for i in range(0, len(tt), 1):
        w += litera(tt[i], kk[i])
    return w

a, b = input().split()

print(deszyfr(a, klucz(a, b)))
