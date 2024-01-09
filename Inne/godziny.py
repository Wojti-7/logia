n = '27:45:43'
a = n[2:]
b = int(n[0:2])
c = b % 24
n = str(c) + a
n = n.zfill(8)
print(n)
