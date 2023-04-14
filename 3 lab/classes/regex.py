import re

str = 'KBTU'

x = re.search("[A-Z]", str)

if x:
    print("yes")
else:
    print("no")