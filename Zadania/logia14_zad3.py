def kosp(s1, s2):
    w1 = 0
    w2 = 0
    for i in range(0, len(s1), 2):
        for j in range(0, len(s2), 2):
            if (s1[i] == s2[j]):
                for k in range(1, i, 2):
                    w1 += int(s1[k])
                for l in range(1, j, 2):
                    w2 += int(s2[l])
                return w1 + w2
    for k in range(1, len(s1), 2):
        w1 += int(s1[k])
    for l in range(1, len(s2), 2):
        w2 += int(s2[l])
    return w1 + w2

print(kosp('D3E5J8', 'H3I2E4J6'))
print(kosp('A3T5U6', 'B4G1Y4'))