n = int(input())

def to_zero(n):
    while n >= 0:
        yield n
        n -= 1

for x in to_zero(n):
    print(x, end=' ')