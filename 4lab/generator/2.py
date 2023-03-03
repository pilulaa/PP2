n = int(input())

def even_num(n):
    x = 0
    while n > 0:
        if x % 2 == 0:
            yield x
        x += 1
        n -=1

a = even_num(n)

for x in a:
    print(x, end=', ')