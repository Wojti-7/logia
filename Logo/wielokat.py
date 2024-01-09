from turtle import *

print("Program 1")

# krok = 1
# while krok < 5:
#     print(krok)
#     krok = krok + 1

# for krok in [1, 2, 3, 4]:
#     print(krok)

def wielokat(n):
    krok = 1
    while krok <= n:
        forward(100)
        left(180 - (180-360/n))
        krok = krok + 1

wielokat(6)
done()
