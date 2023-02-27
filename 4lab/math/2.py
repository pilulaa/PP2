import math

def area(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    return area

a = int(input())
b = int(input())
h = int(input())

trapezoid1 = area(a, b, h)
print(trapezoid1)