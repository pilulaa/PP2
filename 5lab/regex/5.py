import re

str = input()
# pattern = "^a.+b&"

x = re.search("^a.*b$", str)

if x:
    print("yes")
else:
    print("no")