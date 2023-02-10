class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input("square len: "))
    
    def area(self):
        return self.length ** 2;

square1 = Square()
print(square1.area())