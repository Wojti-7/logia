sam = 'aeiouy'

def ILEZ(s):
    o = -1
    p = -1
    w = 0
    k = len(s) -1
    while w <= len(s)-1:
        if (s[w] in sam):
            o = w
        w += 1
    while k >= 0:
        if (s[k] in sam):
            p = k
        k -= 1
    if (o == -1) and (p == -1):
        return -2
    elif (o == p):
        return -1
    else:
        return o - p - 1
    
print(ILEZ('hokuspokus'))
print(ILEZ('klucz'))
print(ILEZ('xxx'))
