def LC(s):
    w = ''
    for i in range(1, len(s), 2):
        # for j in range(0, int(s[i]), 1):
        #     w += s[i-1]
        w += int(s[i]) * s[i-1]
    return w

a = input()
l = LC(a)
print(l)