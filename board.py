import point, random

Point = point.Point
Random = random.Random

class Board:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.size = w * h
        self.board = list(range(w * h))
        #list(map(lambda x: list(range(x * h, (x + 1) * h)), [y for y in range(w)]))

    def shuffle(self):
        board = self.board
        r = Random()
        for i in range(self.size):
            j = r.randint(0, self.size - 1)
            self.swap(self.pointOf(i), self.pointOf(j))

    def findEmpty(self):
        x = 0
        for i in range(self.size):
            if self.getAt(self.pointOf(i)) == 0:
                return self.pointOf(x)
            x = x + 1
        return None

    def isValid(self, pt):
        if(pt.x < 0):
            return False
        if(pt.x >= self.width):
            return False
        if(pt.y < 0):
            return False
        if(pt.y >= self.height):
            return False
        return True

    def adj(self, pt):
        return [x for x in pt.adj() if self.isValid(x)]

    def indexOf(self, pt):
        if(not self.isValid(pt)):
            return None
        return pt.x + pt.y * self.width

    def pointOf(self, index):
        return Point(index % self.width, index // self.width)

    def getAt(self, pt):
        return self.board[self.indexOf(pt)]

    def setAt(self, pt, value):
        self.board[self.indexOf(pt)] = value

    def swap(self, pt1, pt2):
        val1 = self.getAt(pt1)
        self.setAt(pt1, self.getAt(pt2))
        self.setAt(pt2, val1)
