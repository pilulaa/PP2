def gen(n):
    x = 1
    while n > 0:
        yield x * x 
        x += 1
        n -= 1
    
n = int(input())

for x in gen(n):
    print(x, end = ' ')