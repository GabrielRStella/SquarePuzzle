class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adj(self):
        ret = []
        ret.append(Point(self.x + 1, self.y))
        ret.append(Point(self.x - 1, self.y))
        ret.append(Point(self.x, self.y + 1))
        ret.append(Point(self.x, self.y - 1))
        return ret

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __lt__(self, other):
        if(self.x < other.x):
            return True
        if(self.x > other.x):
            return False
        return self.y < other.y
    
    def __le__(self, other):
        return self == other or self < other
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not (self == other)
    
    def __gt__(self, other):
        return other <= self
    
    def __ge__(self, other):
        return other < self
    
