def spy_game(nums):
    q = False
    l = []
    for i in range(len(nums)):
        if nums[i] == 0:
            l.append(nums[i])
        elif nums[i] == 7:
            l.append(nums[i])
    if len(l) % 3 == 0:
        for i in range(1):
            if l[i] == 0 and l[i+1] == 0 and l[i+2] == 7:
                q = True
    return q

p1 = spy_game([1,2,4,0,0,7,5])
p2 = spy_game([1,0,2,4,0,5,7])
p3 = spy_game([1,7,2,0,4,5,0])

print(p1)
print(p2)
print(p3)