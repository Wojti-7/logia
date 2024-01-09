def MAXX(s):
    w = ''
    k = ''
    for i in range(0, len(s), 1): # range(len(s)-1, -1, -1):
        for j in range(0, len(s), 1):
            if (s[i] == s[j]):
                k = s[i:j+1]
            if (len(k) > len(w)):
                w = k
    # if (w == ''):
    #     return s[0]
    return w

print(MAXX('abcdefghij'))
print(MAXX('bbbaaubueytwyetrywax'))