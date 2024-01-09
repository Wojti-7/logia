x = 'alice'

def f():
    x = 'bob'
    print(x)

def g():
    global x
    x = 'celine'
    print(x)

print(x)
f()
print(x)
g()
print(x)
