
def fibonacci(n):
    x = 0
    y = 1
    for i in range(1, n+1, 1):
        z = x+y
        x = y
        y = z
        print(i, ': ', z)

fibonacci(10)