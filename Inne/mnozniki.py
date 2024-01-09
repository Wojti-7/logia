napis = input("wejscie: ")
n = len(napis)

iloczyn_najwiekszy = 0
for i in range(0, n-2, 1):
    iloczyn_biezacy = int(napis[i]) * int(napis[i+1]) * int(napis[i+2])
    if (iloczyn_biezacy > iloczyn_najwiekszy):
        iloczyn_najwiekszy = iloczyn_biezacy
    # print(i, ': ', napis[i], napis[i+1], napis[i+2], iloczyn_biezacy, iloczyn_najwiekszy)

print("wyjscie:", iloczyn_najwiekszy)