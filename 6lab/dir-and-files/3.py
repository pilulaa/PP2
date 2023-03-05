import os 

path = '/Users/willki/Documents/PP2/6lab/dir-and-files'

x = os.path.exists(path)

if x:
    list = os.listdir(path)

for i in list:
    if i == 'test.txt':
        print(i)
        print(os.path.abspath(i))