def osiedla(d):
    osiedla = []
    biezace_osiedle = [d[0]]
    for i in range(1, len(d), 1):
        if (d[i] - d[i-1] <= 3):
            biezace_osiedle = biezace_osiedle + [d[i]]
        else:
            osiedla = osiedla + [biezace_osiedle]
            biezace_osiedle = [d[i]]
    osiedla = osiedla + [biezace_osiedle]
    # uliczka jest pętlą więc:
    if (1 in osiedla[0]) or (2 in osiedla[0]) or (3 in osiedla[0]):
        # osiedla[0] =  osiedla[len(osiedla)-1] + osiedla[0]
        # osiedla.pop(len(osiedla)-1)
        osiedla[len(osiedla)-1] =  osiedla[len(osiedla)-1] + osiedla[0]
        osiedla.pop(0)
    return osiedla

def maksos(n):
    o = osiedla(n)
    max = 0
    for i in range(1, len(o), 1):
        if (len(o[i]) > len(o[max])):
            max = i
    return len(o[max])

# d = [1, 4, 7, 11, 13, 14, 15, 16, 20]
d = [1, 4, 7, 13, 14, 15, 20]

w = maksos(d)
print(w)
