str = input().split()

def reverseString(str):
    for i in reversed(range(len(str))):
        print(str[i])

s = reverseString(str)