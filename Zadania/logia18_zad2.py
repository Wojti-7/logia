def neon(t):
    najwieksza = 0
    for i in range(0, len(t)-1, 1):
        for j in range(i+1, len(t), 1):
            w = t[i] + t[j] + (2*(j-i))
            if (w > najwieksza):
                najwieksza = w
    return najwieksza

print(neon([10, 4, 5, 7, 1, 4, 1]))