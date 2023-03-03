import re

str = input()

new_str = re.findall("[A-Z][^A-Z]*", str)

print(new_str)