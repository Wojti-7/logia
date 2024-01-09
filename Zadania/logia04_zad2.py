def KK(g):
    x = 0
    o = 0
    for i in range(0, len(g), 1):
        if (g[i] == 'x'):
            x += 1
        elif (g[i] == 'o'):
            o += 1
    if (max(x, o) - 2 >= min(x, o)):
        return 'fałsz'
    else:
        return 'prawda'
    

print(KK('xwxoxooww'))
print(KK('xxwowowwo'))
print(KK('xxoowooww'))