import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

#f string fajna rzecz
    def __repr__(self):
        return f'Vector({self.x},{self.y})'

    @property
    def grid_cords(self):
        return (round(self.x), round(self.y))
    #@property
    #def absol(self):

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __mul__ (self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__ (self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

v1 = Vector(3,4)
v2 = Vector(2,3)
v3 = v1 + v2
v4 = 2 * v2
print(v4)
print(v3)
print(v1)
print(abs(v1))