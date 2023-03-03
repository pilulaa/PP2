import re

str = input()
new_str = ''

str_list = re.findall("[A-Z][^A-Z]*", str)

new_str = ' '.join(i for i in str_list[0:])

print(new_str)