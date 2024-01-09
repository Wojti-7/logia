sam = 'aeiouy'

def zamien_spo(s):
    a = s[0]
    b = s[len(s)-1]
    c = a + b
    return c

def zamien_sam(l):
    a = 2 * l
    return a

def KOD(s):
    w = ''
    i = 0
    while i < len(s):
        l = ''
        if (s[i] in sam):
            # print('S',s[i])
            if (i != 0) and (i != len(s)-1):
                w += zamien_sam(s[i])
                i += 1
            else:
                w += s[i]
                i += 1
        else:
            while s[i] not in sam:
                l += s[i]
                i += 1
            # print('P',l)
            if (len(l) == 1):
                w += l
            elif (len(l) == 2):
                w += l
            else:
                w += zamien_spo(l)
    return w

print(KOD('abrakadabra'))
print(KOD('skrzynka'))

# print(zamien_spo('skrz'))
# print(zamien_sam('a'))