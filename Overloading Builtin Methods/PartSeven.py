import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = {self.x, self.y}

    def move(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __sub__(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y)

    def __mul__(self, other_point):
        return self.x * other_point.x + self.y * other_point.y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p1 * p2)
print()
print(p5, p6)

print()
print(p1 == p2)
print(p1 >= p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 < p2)

print(dir(__builtins__))