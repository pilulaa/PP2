a = list(map(int, input().split()))

max = 0
index = -1

for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
        index = i

print(max, index)