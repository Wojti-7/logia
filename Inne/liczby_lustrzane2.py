def czy_palin(n):
    return str(n) == str(n)[::-1]

def odwroc(n):
    return int(str(n)[::-1])

def lustro(n, l):
    while l>0:
        w = n + odwroc(n)
        if (czy_palin(w)):
            return w
        else:
            n = w
        l -= 1
    return -1

n, l = input().split()
n = int(n)
l = int(l)

print(lustro(n, l))
