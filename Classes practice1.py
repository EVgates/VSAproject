class Shape(object):
    def __init__(self,side):
        self.side = side


class Square(Shape):
    def find_area(self):
        return self.side*self.side

class Triangle(Shape):
    def find_area(self, height):
        self.height = height
        self.side= self.side/2
        return self.side*self.height

class Rectangle(Shape):
    def find_volume(self, height, length):
        self.height = height
        self.length = length
        return self.height*self.length*self.side

s = Square(5)
print s.find_area()

t = Triangle(4)
print t.find_area(3)

r = Rectangle(6)
print r.find_volume(2, 3)