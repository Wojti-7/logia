a = int(input())
b = input()

def tablica(a, b):
    w = []
    for i in range(0, len(b), a):
        w += [b[i:i+a]]
    return w

def dywany(a, b):
    t = tablica(a, b)
    w = 0
    for i in range(0, len(t), 1):
        for j in range(0, a, 1):
            if (i == 0) or (i == len(t)-1) or (j == 0) or (j == a - 1):
                w += 0
            else:
                if(t[i][j] == 'P') and (t[i][i-1] == 'P') and (t[i][i+1] == 'P') and (t[i+1][j] == 'P') and (t[i-1][j] == 'P'):
                    w += 1
    return w

print(dywany(a, b))




