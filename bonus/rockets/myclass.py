from math import sqrt

class Rocket:
    def __init__(self, x=0, y=0, name=1):
        self.x = x
        self.y = y
        self.name = name
    
    def move(self, x_increment = 0, y_increment = 1):
        self.x += x_increment
        self.y += y_increment
    
    def get_distance(self, other_rocket):
        try:
            x_distance = self.x - other_rocket.x
            y_distance = self.y - other_rocket.y
            # round to 5 decimal places:
            return round(sqrt(x_distance ** 2 + y_distance ** 2), 4)
        except:
            return None
    def __str__(self):
        return f"Rocket {self.name} is at ({self.x},{self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        square1 = self.x ** 2 + self.y ** 2
        square2 = other.x ** 2 + other.y ** 2
        return square1 > square2

    def __lt__(self, other):
        square1 = self.x ** 2 + self.y ** 2
        square2 = other.x ** 2 + other.y ** 2
        return square1 < square2
    


