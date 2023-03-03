import re

str = input()
pattern = "[A-Z]+[a-z]"

x = re.search(pattern, str)

if x:
    print("yes")
else:
    print("no")