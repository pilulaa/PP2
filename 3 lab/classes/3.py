class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input("square len: "))
    
    def area(self):
        return self.length ** 2;

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("rectangle len: "))
        self.width = int(input("rectangle wid: "))

    def area(self):
        return self.length * self.width

# square1 = Square()
# print(square1.area())

rec1 = Rectangle()
print(rec1.area())