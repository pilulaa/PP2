import math

def volume(nums):
    return (4/3) * math.pi * pow(nums, 3)

sphere1 = volume(2) 
# 8 * 3,14 * 4/3 = 33,49
sphere2 = volume(3)
# 27 * 3,14 * 4/3 = 113,09
sphere3 = volume(4)
# 64 * 3,14 * 4/3 = 268,08

print(sphere1)
print(sphere2)
print(sphere3)