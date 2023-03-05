def isPalindrome(str):
    x = reversed(str)
    if list(str) == list(x):
        return True
    return False

str = input()

if isPalindrome(str):
    print("it's a palindrome")
else:
    print("not a palindrome")