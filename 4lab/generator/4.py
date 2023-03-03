import math

a = int(input())
b = int(input())

def squares(a, b):
    l = a
    while b >= l:
        yield a*a
        b -= 1
        a += 1

a = squares(a, b)
for x in a:
    if x == math.sqrt(x) * math.sqrt(x):
        print(x, end=' ')