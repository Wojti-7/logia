# Unpacking

a, *b, c = range(5)
print(a, b, c)

a, b, *c = range(5)
print(a, b, c)

def f(a, b, c):
    print(a, b, c)
    return

args = (1, 2, 3)  # usually a tuple, always an iterable
f(*args) # f(1, 2, 3)

kwargs = {"b": 2, "c": 3, "a": 1}  # usually a dict, always a mapping
f(**kwargs) # f(b=2, c=3, a=1)
