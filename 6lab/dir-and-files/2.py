import os

x = '/Users/willki/Documents/PP2/6lab/dir-and-files/test.txt'

def access(x):
    list = []

    if os.access(x, os.F_OK):
        list.append("file exists")
    else:
        list.append("file don't exists")

    if os.access(x, os.R_OK):
        list.append("file readable")
    else:
        list.append("file isn't readable")

    if os.access(x, os.W_OK):
        list.append("file writable")
    else:
        list.append("file isn't writable")

    if os.access(x, os.X_OK):
        list.append("file executable")
    else:
        list.append("file isnt't executable")
    return list
    
print(access(x))
print(access('/Users/willki/Documents/PP2/6lab/dir-and-files/test1.txt'))