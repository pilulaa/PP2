import math

class Point():
    def __init__(self):
        self.x1 = int(input("first coord: "))
        self.y1 = int(input("second coord: "))

    def show(self):
        print(self.x1, self.y1)

    def move(self):
        self.x2 = int(input("furst new coord: "))
        self.y2 = int(input("second new coord: "))

    def dist(self):
        self.x3 = int(input("x3: "))
        self.y3 = int(input("y3: "))
        self.x4 = int(input("x4: "))
        self.y4 = int(input("y4: "))
        return math.sqrt(pow(abs(self.x3 - self.x4), 2) + pow(abs(self.y3 - self.y4), 2))

p = Point()
print(p.dist())
