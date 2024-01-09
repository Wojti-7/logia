def zakoduj(s):
    a = ord(s[0]) - ord('a')
    b = ord(s[1]) - ord('a')
    c = 26 * a + b
    return c

def odkoduj(n):
    w = ''
    for i in range(0, 26, 1):
        if ((n - i) % 26 == 0):
            a = i
            b = int((n-i)/26)
    e = a + ord('a')
    f = b + ord('a')
    c = chr(e)
    d = chr(f)
    w = d + c
    return w

def SZYFR(s, n):
    w = ''
    for i in range(0, len(s)-1, 2):
        c = s[i:i+2]
        d = zakoduj(c)
        e = (d + n) % 676
        f = odkoduj(e)
        w += f
    return w

print(SZYFR('ab', 1))
print(SZYFR('abrakadabraa', 500))
print(SZYFR('dzisiajjestkonkurs', 487))
