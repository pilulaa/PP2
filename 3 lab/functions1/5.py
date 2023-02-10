import itertools

def perm():
    str = input()
    str1 = [''.join(p) for p in itertools.permutations(str)]
    return str1

s = perm()
print(s)