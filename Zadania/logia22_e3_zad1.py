a = input()
s = str(a)

t0 = '0+'
t1 = '1 '
t2 = '2abc'
t3 = '3def'
t4 = '4ghi'
t5 = '5jkl'
t6 = '6mno'
t7 = '7pqrs'
t8 = '8tuv'
t9 = '9wxyz'

def koduj(s):
    w = ''
    i = 0
    while i < len(s):
        if (s[i] == '*'):
            w += '*'
            i += 2
        elif (s[i] == '#'):
            w += '#'
            i += 2
        elif (s[i] == '0'):
            a = int(s[i+1]) - 1
            w += t0[a]
            i += 3
        elif (s[i] == '1'):
            a = int(s[i+1]) - 1
            w += t1[a]
            i += 3
        elif (s[i] == '2'):
            a = int(s[i+1]) - 1
            w += t2[a]
            i += 3
        elif (s[i] == '3'):
            a = int(s[i+1]) - 1
            w += t3[a]
            i += 3
        elif (s[i] == '4'):
            a = int(s[i+1]) - 1
            w += t4[a]
            i += 3
        elif (s[i] == '5'):
            a = int(s[i+1]) - 1
            w += t5[a]
            i += 3
        elif (s[i] == '6'):
            a = int(s[i+1]) - 1
            w += t6[a]
            i += 3
        elif (s[i] == '7'):
            a = int(s[i+1]) - 1
            w += t7[a]
            i += 3
        elif (s[i] == '8'):
            a = int(s[i+1]) - 1
            w += t8[a]
            i += 3
        elif (s[i] == '9'):
            a = int(s[i+1]) - 1
            w += t9[a]
            i += 3
    return w

print(koduj(s))


