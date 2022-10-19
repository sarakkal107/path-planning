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

    def __eq__(self, vertex2):
        if vertex2 == None:
            return False
        elif self == None:
            return False
        if (self.coords == vertex2.coords):
            return True
        else:
            return False
    
    def setH(self, xGoal, yGoal):
        xDifference = abs(self.coords[0] - xGoal)
        yDifference = abs(self.coords[1] - yGoal)
        self.h = math.sqrt(2) * float(min(xDifference,yDifference)) + float(max(xDifference,yDifference)) - float(min(xDifference, yDifference))

    def setHtheta(self, xGoal, yGoal):
        xDifference = abs(self.coords[0] - xGoal)
        yDifference = abs(self.coords[1] - yGoal)
        self.h = math.sqrt(float(xDifference**2) + float(yDifference**2))

    def setG(self, g):
        self.g = float(g)
    
    def setF(self):
        self.f = float(self.g) + float(self.h)

    def __hash__(self):
        return hash(self.coords)

        

