w, k = input().split()
 
def klucz(w, k):
    l = ''
    for i in range(0, len(w), 1):
        l += k[i % len(k)]
    return l

def odbij_l(l):
    a = ord(l)
    b = ord('z') - a
    c = b + ord('a')
    return chr(c)

def odbij_s(s):
    l = ''
    for i in range(0, len(s), 1):
        l += odbij_l(s[i])
    return l

def licz_zam(l):
    return ord(l) - ord('a') + 1

def zamien(lw, lk):
    x = licz_zam(lk)
    y = ord(lw)
    z = (x + y)
    if (z < ord('z')):
        return chr(z)
    else:
        z = z % ord('z')
        return chr(z + ord('a') - 1)

def szyfruj(w, k):
    p = ''
    s = odbij_s(w)
    k = klucz(w, k)
    for i in range(0, len(s), 1):
        p += zamien(s[i], k[i])
    return p

print(szyfruj(w, k))
