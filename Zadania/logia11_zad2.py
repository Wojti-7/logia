def czy_palindrom(s):
    return s == s[::-1]

def ILEP(s):
    w = 0
    i = len(s)
    j = 1
    while i > 0:
        for k in range(0, i, 1):
            if (czy_palindrom(s[k:k+j])):
                w += 1
        i -= 1
        j += 1
    return w

def ILEP2(s):
    w = 0
    for i in range(0, len(s), 1):
        for j in range(i, len(s), 1):
            if (czy_palindrom(s[i:j+1])):
                w += 1
    return w

print(ILEP('kajak'))
print(ILEP('mama'))

print(ILEP2('kajak'))
print(ILEP2('mama'))