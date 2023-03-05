import os 

x = os.path.exists('/Users/willki/Documents/PP2/6lab/dir-and-files/test.txt')
inf = ''
if x:
    with open('/Users/willki/Documents/PP2/6lab/dir-and-files/test.txt', 'r') as file:
        inf = file.read()
    with open('/Users/willki/Documents/PP2/6lab/dir-and-files/new_test.txt', 'w') as file:
        file.write(inf)