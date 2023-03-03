import re 

a = input()

x = re.search("ab*", a)

if x:
    print("yes")
else:
    print("no")