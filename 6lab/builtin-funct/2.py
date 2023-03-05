str = input()

def upper(str):
    cnt_upper = 0
    for i in str:
        if i.isupper():
            cnt_upper += 1
    return cnt_upper 

def lower(str):
    cnt_lower = 0
    for i in str:
        if i.islower():
            cnt_lower += 1
    return cnt_lower

print(upper(str))
print(lower(str))