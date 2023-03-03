import re

def snake(camel):
    str_list = re.findall("[A-Z]*[^A-Z]*", camel)
    return '_'.join(i.lower() for i in str_list[0:len(str_list) - 1])

camel = input()

print(snake(camel))