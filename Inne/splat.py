# splat, double-splat, argument unpacking, keyword argument unpacking
#
# https://softwareengineering.stackexchange.com/questions/131403/what-is-the-name-of-in-python
# Iterables are objects that implement the __iter__() method
# and mappings are objects that implement keys() and __getitem__().
# Any object that supports this protocol will be understood by the constructors tuple() and dict(),
# so they can be used for unpacking arguments.

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
