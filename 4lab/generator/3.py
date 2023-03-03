n = int(input())

def three_or_four(n):
    x  = 0
    while n > 0:
        if x % 3 == 0 or x % 4 == 0:
            yield x
        x += 1
        n -= 1

a = three_or_four(n)
for i in a:
    print(i, end=' ')