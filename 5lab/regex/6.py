import re

str = input()

x = re.sub("[ ,.]", ":", str)

print(x)