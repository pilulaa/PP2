# a = int(input())

# for i in range(a):
#     b = int(in)

a = list(map(int, input().split()))

for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")