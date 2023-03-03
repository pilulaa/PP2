import re

str = input()

x = re.search("^[a-z]+_+[a-z]+$", str)

if x:
    print("yes")
else:
    print("no")