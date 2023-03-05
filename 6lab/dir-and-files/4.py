import os 

path = '/Users/willki/Documents/PP2/6lab/dir-and-files/test.txt'

lines_cnt = 0

with open(path, 'r') as file:
    for line in file:
        if line != "\n":
            lines_cnt += 1

print(lines_cnt)