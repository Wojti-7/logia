sam = 'aeiouy'

def szyfr_lit(l, k):
    x = ord(l) - ord('a')
    x += k
    y = x % 26
    y += ord('a')
    return chr(y)

def SZYFR(s, k1, k2):
    w = ''
    for i in range(0, len(s), 1):
        if (s[i] in sam):
            w += szyfr_lit(s[i], k1)
        else:
            w += szyfr_lit(s[i], k2)
    return w

s = input()
k1 = int(input())
k2 = int(input())
l = SZYFR(s, k1, k2)
print(l)
