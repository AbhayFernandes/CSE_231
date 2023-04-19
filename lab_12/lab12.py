import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
    
    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        elif type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def magnitude(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)
    
    def unit(self):
        # check if magnitude is 0
        if self.magnitude() == 0:
            raise ValueError("Cannot divide by 0")
        magnitude = self.magnitude()
        self.x = self.x / magnitude
        self.y = self.y / magnitude

def main():
    # a main function that tests the functionality of all methods in the vector class
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector()
    print(v1)
    print(v2)
    print(v3)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(v1 * 2)
    print(2 * v1)
    print(v1 == v2)
    print(v1.magnitude())
    print(v1.unit())
    print(v1)
    print(v3.unit())

if __name__ == "__main__":
    main()