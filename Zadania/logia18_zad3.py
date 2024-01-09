def tablica(t):
    w = [0]
    for i in range(0, len(t), 1):
        if (i % 2 == 0):
            for j in range(1, t[i] + 1, 1):
                if (i == 0):
                    w += [j]
                else:
                    w += [w[len(w)-1] + 1]
        else:
            for j in range(1, t[i] + 1, 1):
                w += [w[len(w)-1] - 1]
    return w

def ilerazy(l, t):
    w = 0
    n = tablica(t)
    for i in range(0, len(n), 1):
        if (n[i] == l):
            w += 1
    return w

print(ilerazy(4, [5, 3, 5, 3, 2, 1]))