
class Pt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __add__(self, B):
        return Pt(self.x+B.x, self.y+B.y)

    def __sub__(self, B):
        return Pt(self.x-B.x, self.y-B.y)

    def __mul__(self, a):
        return Pt(a*(self.x), a*(self.y))
