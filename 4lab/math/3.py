import math

def area_polygon(x, y):
    p = y / 2
    area = (x * y * p) / 2
    return area

n = float(input())
l = float(input())

pol1  = area_polygon(n, l)

print(pol1)
