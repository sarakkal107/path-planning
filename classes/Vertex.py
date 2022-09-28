import math

class Vertex:

    def __init__(self, parent=None, coords=None):
        self.parent = parent
        self.coords = coords
        self.f = 0
        self.g = 0
        self.h = 0
    
    def setParent(self, parentVer):
        self.parent = parentVer

    def xVal(self):
        return self.coords[1]
    
    def yVal(self):
        return self.coords[0]

    def equals(self, vertex2):
        if self == None:
            return False
        elif vertex2 == None:
            return False
        else:
            return (self.coords[0] == vertex2.coords[0]) and (self.coords[1] == vertex2.coords[1])
    
    def setH(self, xGoal, yGoal):
        xDifference = abs(self.coords[0] - xGoal)
        yDifference = abs(self.coords[1] - yGoal)
        self.h = math.sqrt(2) * float(min(xDifference,yDifference)) + float(max(xDifference,yDifference)) - float(min(xDifference, yDifference))

    def setG(self, g):
        self.g = float(g)
    
    def setF(self):
        self.f = float(self.g) + float(self.h)

    def __hash__(self):
        return hash(str(self.coords))

