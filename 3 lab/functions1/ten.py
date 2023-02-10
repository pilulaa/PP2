def uniqueNum(nums):
    l = []
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            l.append(nums[i])
    l.append(nums[len(nums) - 1])

    return l

w1 = uniqueNum([1, 4, 5, 4, 3, 9, 5, 9])
w2 = uniqueNum([3, 9, 0, 6, 0, 3, 9, 1])

print(w1)
print(w2)