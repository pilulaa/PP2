def has_33(nums):
    q = False
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            q = True
    return q
            

p1 = has_33([1, 3, 3])
p2 = has_33([1, 3, 1, 3])
p3 = has_33([3, 1, 3])

print(p1)
print(p2)
print(p3)