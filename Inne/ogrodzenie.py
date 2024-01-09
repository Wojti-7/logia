t = [
    [5, 5, 6, 7, 3, 8, 5, 3, 5, 3],
    [5, 5, 5, 7, 8],
    [7, 5, 5, 5, 8]
]

def koszt(tablica):
    maxi = 0
    maxj = 2
    for i in range(0, len(tablica), 1):
        for j in range(0, len(tablica), 1):
            if not (
                (i==j) or (abs(i-j)==1) or (i==0 and j==len(tablica)-1) or (j==0 and i==len(tablica)-1)
            ):
                if (tablica[i]+tablica[j]) > (tablica[maxi]+tablica[maxj]):
                    maxi = i
                    maxj = j
    wynik = 0
    for k in range(0, len(tablica), 1):
        wynik = wynik + tablica[k]
    wynik = wynik - tablica[maxi] - tablica[maxj]
    return [wynik, maxi, maxj]

for c in range(0, len(t), 1):
    print(c, t[c], koszt(t[c]))
