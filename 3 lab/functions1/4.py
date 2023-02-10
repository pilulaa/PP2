import math

def filter_prime():
    a = list(map(int, input().split()))
    l = []
    cnt = 0
    for i in a:
        for j in range(1, i):
            if i % j == 0:
                cnt = cnt + 1
        if cnt == 1:
            l.append(i)
            cnt = 0
        else:
            cnt = 0
    return l
        
x = filter_prime()
print(x)