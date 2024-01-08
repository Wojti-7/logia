def md(m):
    if (m<1) or (m>12):
        return 0
    t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return t[m-1]

def ymd(y, m):
    if ((y % 4) != 0):
        return md(m)
    if ((y % 100) == 0) and ((y % 400) != 0):
        return md(m)
    if (m == 2):
        return md(m)+1
    else:
        return md(m)

def yd(y):
    if ((y % 4) != 0):
        return 365
    if ((y % 100) == 0) and ((y % 400) != 0):
        return 365
    return 366

print(ymd(2020, 2))
print(yd(2020))
