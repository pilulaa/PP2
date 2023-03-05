l = list((1, 2, 3, 4, 5))

def mult(l):
    x = 1
    for i in l:
        x = x * i
    return x

print(mult(l))