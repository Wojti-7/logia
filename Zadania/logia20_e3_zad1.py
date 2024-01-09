s20 = 'abcdefghijklm'
s40 = 'nopqrstuvwxyz'

def d(n):
    s = str(n)
    w = ''
    for i in range(0, len(s)-1, 2):
        a = 10 * int(s[i]) + int(s[i+1])
        if (a > 40):
            b = a % 40 - 1
            w += s40[b]
        else:
            b = a % 20 - 1
            w += s20[b]
    return w

def deszyfr2(t):
    w = []
    for i in range(0, len(t), 1):
        w += [d(t[i])]
    return w

print(deszyfr2([31452122]))
print(deszyfr2([232821473121, 22212252, 30212729]))
print(deszyfr2([332131425021, 4321412925413121]))

