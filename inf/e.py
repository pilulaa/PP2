a = list(map(int, input().split()))

for i in range(0, len(a) - 1):
    if a[i] * a[i+1] > 0:
        print(a[i], a[i+1], end=" ")
        exit()