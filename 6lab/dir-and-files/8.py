import os

x = os.path.exists('/Users/willki/Documents/PP2/6lab/dir-and-files/new_test.txt')

if x:
    os.remove('/Users/willki/Documents/PP2/6lab/dir-and-files/new_test.txt')
else:
    print("file doesn't exist")