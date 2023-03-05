import os

path = '/Users/willki/Documents/PP2/6lab/dir-and-files'

os.mkdir(f'{path}/alphabet')

os.chdir(f'{path}/alphabet')


for i in range (65, 91):
    open(chr(i) + '.txt', 'x')
