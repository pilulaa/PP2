import math

def gen(n):
    x = 0

    while x < n:
        yield x
        x = math.sqrt(x)


for x in gen(5):
    print(x)