def czy_sfeniczna(n):
    w = 0
    for i in range(1, n+1, 1):
        if (n % i == 0):
            w += 1
    if (w == 8):
        return True
    else:
        return False
    
def liczby_sfeniczne(n):
    w = ''
    j = n + 1
    p = 0
    while p != 3:
        if (czy_sfeniczna(j)):
            w += str(j) + ' '
            p += 1
        j += 1
    return w

print(liczby_sfeniczne(12))
print(liczby_sfeniczne(40))
print(liczby_sfeniczne(110))



